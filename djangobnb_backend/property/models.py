import uuid
from django.conf import settings
from django.db import models
from useraccount.models import User  # Userモデルをインポート

# Property（物件）モデル
class Property(models.Model):
    # UUIDFieldを使って、プライマリキー（主キー）として自動生成される一意のIDを設定
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    # 物件のタイトルを保存するCharField（最大255文字）
    title = models.CharField(max_length=255)
    
    # 物件の詳細説明を保存するTextField（テキストの長さに制限なし）
    description = models.TextField()
    
    # 1泊あたりの料金（整数）
    price_per_night = models.IntegerField()
    
    # ベッドルームの数（整数）
    bedrooms = models.IntegerField()
    
    # バスルームの数（整数）
    bathrooms = models.IntegerField()
    
    # 収容できるゲストの数（整数）
    guests = models.IntegerField()
    
    # 物件の所在国
    country = models.CharField(max_length=255)
    
    # 国のコード（最大10文字）
    country_code = models.CharField(max_length=10)
    
    # 物件のカテゴリー（例: アパート, ホテル, 別荘など）
    category = models.CharField(max_length=255)
    
    # 多対多の関係を定義。ユーザーが物件を「お気に入り」に追加する機能
    # favorited = models.ManyToManyField(User, related_name='favorites', blank=True)
    
    # 物件の画像をアップロードするフィールド
    image = models.ImageField(upload_to='uploads/properties')
    
    # 物件のオーナー（ユーザー）を指定。物件が削除されたときに関連するデータも削除される
    landlord = models.ForeignKey(User, related_name='properties', on_delete=models.CASCADE)
    
    # 物件が作成された日付と時刻を自動的に保存
    created_at = models.DateTimeField(auto_now_add=True)

    # 物件画像のURLを返すメソッド。Djangoの設定からWEBSITE_URLを使用して完全なURLを返す
    def image_url(self):
        return f'{settings.WEBSITE_URL}{self.image.url}'


# # Reservation（予約）モデル
# class Reservation(models.Model):
#     # UUIDFieldを使って、プライマリキーとして自動生成される一意のIDを設定
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
#     # 外部キーでProperty（物件）を参照。物件が削除されると予約も削除される
#     property = models.ForeignKey(Property, related_name='reservations', on_delete=models.CASCADE)
    
#     # 予約の開始日
#     start_date = models.DateField()
    
#     # 予約の終了日
#     end_date = models.DateField()
    
#     # 宿泊日数（整数）
#     number_of_nights = models.IntegerField()
    
#     # 予約に含まれるゲストの数（整数）
#     guests = models.IntegerField()
    
#     # 合計金額（浮動小数点数）
#     total_price = models.FloatField()
    
#     # 予約を作成したユーザーを指定
#     created_by = models.ForeignKey(User, related_name='reservations', on_delete=models.CASCADE)
    
#     # 予約が作成された日付と時刻を自動的に保存
#     created_at = models.DateTimeField(auto_now_add=True)
