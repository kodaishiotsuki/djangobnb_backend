import uuid

from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.db import models

# カスタムユーザーのマネージャークラス
class CustomUserManager(UserManager):
    # ユーザー作成のための内部メソッド
    def _create_user(self, name, email, password, **extra_fields):
        # メールアドレスが指定されていない場合、エラーを発生させる
        if not email:
            raise ValueError("You have not specified a valid e-mail address")
        
        # メールアドレスを正規化（小文字にするなどの処理）
        email = self.normalize_email(email)
        # ユーザーモデルを作成し、パスワードを設定する
        user = self.model(email=email, name=name, **extra_fields)
        user.set_password(password)
        # データベースに保存
        user.save(using=self.db)

        return user

    # 一般ユーザーを作成するメソッド
    def create_user(self, name=None, email=None, password=None, **extra_fields):
        # 一般ユーザーは管理者ではない
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(name, email, password, **extra_fields)
    
    # スーパーユーザー（管理者）を作成するメソッド
    def create_superuser(self, name=None, email=None, password=None, **extra_fields):
        # スーパーユーザーは管理者権限を持つ
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(name, email, password, **extra_fields)

# カスタムユーザーモデルクラス
class User(AbstractBaseUser, PermissionsMixin):
    # ユーザーIDをUUIDで生成し、デフォルトでユニークなIDを設定
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # メールアドレスを一意に設定
    email = models.EmailField(unique=True)
    # ユーザー名（名前）は空白でもOK
    name = models.CharField(max_length=255, blank=True, null=True)
    # アバター画像をアップロードするためのフィールド
    avatar = models.ImageField(upload_to='uploads/avatars')

    # ユーザーがアクティブかどうか
    is_active = models.BooleanField(default=True)
    # スーパーユーザー（管理者）かどうか
    is_superuser = models.BooleanField(default=False)
    # スタッフ（管理画面にアクセスできるか）かどうか
    is_staff = models.BooleanField(default=False)

    # ユーザーの作成日時
    date_joined = models.DateTimeField(auto_now_add=True)
    # 最後にログインした日時
    last_login = models.DateTimeField(blank=True, null=True)

    # カスタムマネージャーを使用
    objects = CustomUserManager()

    # ユーザーログインに使うフィールドはメールアドレス
    USERNAME_FIELD = 'email'
    # メールフィールドの指定
    EMAIL_FIELD = 'email'
    # 必須フィールド（スーパーユーザーを作成するときに必要）
    REQUIRED_FIELDS = ['name',]

    # アバター画像のURLを取得するメソッド
    def avatar_url(self):
        # アバター画像が設定されている場合、そのURLを返す
        if self.avatar:
            return f'{settings.WEBSITE_URL}{self.avatar.url}'
        else:
            # 画像がない場合は空文字列を返す
            return ''
