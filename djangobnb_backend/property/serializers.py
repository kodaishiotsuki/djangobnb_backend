from rest_framework import serializers  # Django REST framework のシリアライザをインポート
from .models import Property  # 同じアプリケーション内の Property  モデルをインポート

# 物件リスト用のシリアライザ
class PropertiesListSerializer(serializers.ModelSerializer):
    # Metaクラスで、どのモデルを使うかと、シリアライズするフィールドを定義しています
    class Meta:
        model = Property  # Propertyモデルを使います
        fields = (
            'id',  # 物件ID
            'title',  # 物件タイトル
            'price_per_night',  # 1泊あたりの価格
            'image_url',  # 物件の画像URL
        )


# # 物件詳細用のシリアライザ
# class PropertiesDetailSerializer(serializers.ModelSerializer):
#     # UserDetailSerializerを使用して、物件オーナー（landlord）の詳細情報を取得します
#     landlord = UserDetailSerializer(read_only=True, many=False)

#     # Metaクラスで、シリアライズするフィールドを定義
#     class Meta:
#         model = Property  # Propertyモデルを使います
#         fields = (
#             'id',  # 物件ID
#             'title',  # 物件タイトル
#             'description',  # 物件の詳細説明
#             'price_per_night',  # 1泊あたりの価格
#             'image_url',  # 物件の画像URL
#             'bedrooms',  # ベッドルームの数
#             'bathrooms',  # バスルームの数
#             'guests',  # 収容可能なゲストの数
#             'landlord',  # 物件オーナーの詳細情報
#         )


# # 予約リスト用のシリアライザ
# class ReservationsListSerializer(serializers.ModelSerializer):
#     # Propertyリストの情報を含めてシリアライズするために、PropertiesListSerializerを使用
#     property = PropertiesListSerializer(read_only=True, many=False)

#     # Metaクラスで、シリアライズするフィールドを定義
#     class Meta:
#         model = Reservation  # Reservationモデルを使います
#         fields = (
#             'id',  # 予約ID
#             'start_date',  # 予約開始日
#             'end_date',  # 予約終了日
#             'number_of_nights',  # 宿泊日数
#             'total_price',  # 総額
#             'property',  # 物件情報（リスト形式）
#         )
