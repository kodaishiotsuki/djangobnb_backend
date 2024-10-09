import os
from datetime import timedelta
from pathlib import Path

# BASE_DIR はプロジェクトの基本ディレクトリを指すパスです。これを使って他のファイルパスを簡単に取得できます。
BASE_DIR = Path(__file__).resolve().parent.parent

# 環境変数から機密情報を取得しています。SECRET_KEYはDjangoアプリケーションのセキュリティ上非常に重要なキーです。
SECRET_KEY = os.environ.get("SECRET_KEY")

# デバッグモードの設定。デバッグモードは開発時に有効にし、運用時には無効にする必要があります。
DEBUG = bool(os.environ.get("DEBUG", default=0))

# 許可するホスト名のリスト。環境変数からスペースで区切られたリストを取得しています。
ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")

# Djangoでカスタムユーザーモデルを使用する場合、そのモデルを指定します。
AUTH_USER_MODEL = 'useraccount.User'

# サイトのID。この設定はDjangoのサイトフレームワークを使用する場合に必要です。
SITE_ID = 1

# サイトのURLを定義しています。デフォルトではローカルホスト。
WEBSITE_URL = 'http://localhost:8000'

# JWT (JSON Web Token) の設定。アクセストークンやリフレッシュトークンの有効期間や、トークン署名に使用するアルゴリズムを指定します。
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
    "ROTATE_REFRESH_TOKEN": False,
    "BLACKLIST_AFTER_ROTATION": False,
    "UPDATE_LAST_LOGIN": True,
    "SIGNING_KEY": "acomplexkey",  # 署名に使用するキー（セキュアにする必要あり）
    "ALOGRIGTHM": "HS512",  # 使用するアルゴリズム（HS512が指定されている）
}

# アカウント作成時の設定。ユーザー名を使用せず、メールアドレスで認証を行う設定になっています。
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = None  # メールアドレスの確認を無効にする

# Django REST frameworkの設定。JWT認証と、デフォルトで認証が必要な設定になっています。
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',  # JWT認証を使用
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',  # 認証済みのユーザーのみ許可
    )
}

# CORS設定。特定のドメインからのリクエストのみ許可する設定。ローカルホストからのアクセスを許可しています。
CORS_ALLOWED_ORIGINS = [
    'http://127.0.0.1:8000',
    'http://127.0.0.1:3000',
]

# RESTフレームワークの設定。JWTを使用する設定が有効です。
REST_AUTH = {
    "USE_JWT": True,
    "JWT_AUTH_HTTPONLY": False
}

# アプリケーション定義。Djangoに組み込むアプリケーションやサードパーティのライブラリが指定されています。
INSTALLED_APPS = [
    'django.contrib.admin',  # 管理画面のアプリ
    'django.contrib.auth',  # 認証機能
    'django.contrib.contenttypes',  # コンテンツタイプフレームワーク
    'django.contrib.sessions',  # セッション管理
    'django.contrib.messages',  # メッセージフレームワーク
    'django.contrib.staticfiles',  # 静的ファイル管理

    'rest_framework',  # Django REST framework
    'rest_framework.authtoken',  # 認証トークン管理
    'rest_framework_simplejwt',  # JWT認証

    'allauth',  # ソーシャルログインなどの機能を提供するパッケージ
    'allauth.account',  # ユーザー管理の機能
    'dj_rest_auth',  # Django REST Auth
    'dj_rest_auth.registration',  # ユーザー登録機能

    'corsheaders',  # CORSヘッダー対応

    'useraccount',  # カスタムユーザーアカウントアプリ
    'property',  # 物件管理アプリ
]

# ミドルウェアの定義。Djangoのリクエスト処理パイプラインで実行される各種ミドルウェアが設定されています。
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',  # セキュリティ関連
    'django.contrib.sessions.middleware.SessionMiddleware',  # セッション管理
    'corsheaders.middleware.CorsMiddleware',  # CORS対応
    'django.middleware.common.CommonMiddleware',  # 基本的なリクエストとレスポンスの処理
    'django.middleware.csrf.CsrfViewMiddleware',  # CSRF攻撃対策
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # 認証
    'django.contrib.messages.middleware.MessageMiddleware',  # メッセージ処理
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # クリックジャッキング対策
]

# URL設定ファイルを指定
ROOT_URLCONF = 'djangobnb_backend.urls'

# テンプレート設定。HTMLテンプレートをどのように処理するかが定義されています。
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',  # Djangoテンプレートエンジンを使用
        'DIRS': [],  # テンプレートディレクトリのリスト（空の場合はデフォルトディレクトリ）
        'APP_DIRS': True,  # アプリ内のテンプレートディレクトリを使用
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',  # デバッグ用のコンテキストプロセッサ
                'django.template.context_processors.request',  # リクエストデータのコンテキストプロセッサ
                'django.contrib.auth.context_processors.auth',  # 認証データのコンテキストプロセッサ
                'django.contrib.messages.context_processors.messages',  # メッセージデータのコンテキストプロセッサ
            ],
        },
    },
]

# WSGIアプリケーション。Djangoのデプロイ時に使用します。
WSGI_APPLICATION = 'djangobnb_backend.wsgi.application'

# データベースの設定。環境変数からデータベース接続情報を取得しています。
DATABASES = {
    'default': {
        'ENGINE': os.environ.get("SQL_ENGINE"),  # 使用するデータベースエンジン（例：django.db.backends.postgresql）
        'NAME': os.environ.get("SQL_DATABASE"),  # データベース名
        'USER': os.environ.get("SQL_USER"),  # データベースユーザー
        'PASSWORD': os.environ.get("SQL_PASSWORD"),  # データベースパスワード
        'HOST': os.environ.get("SQL_HOST"),  # データベースホスト
        'PORT': os.environ.get("SQL_PORT"),  # データベースポート
    }
}

# パスワードバリデーションの設定。Djangoが提供する標準的なパスワードの強度をチェックするための設定。
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',  # ユーザー属性の類似性チェック
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',  # 最小文字数のチェック
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',  # よくあるパスワードを禁止
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',  # 数字のみのパスワードを禁止
    },
]

# 国際化の設定
LANGUAGE_CODE = 'en-us'  # 言語コード
TIME_ZONE = 'UTC'  # タイムゾーン
USE_I18N = True  # 国際化対応を有効化
USE_TZ = True  # タイムゾーンを有効化

# 静的ファイルの設定（CSSやJavaScriptなど）
STATIC_URL = 'static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# プライマリキーのデフォルト設定
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
