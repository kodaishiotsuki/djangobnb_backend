# DjangoのHTTPレスポンスクラスをインポート。`JsonResponse`を使ってレスポンスをJSON形式で返す
from django.http import JsonResponse

# Django REST framework のデコレーター（関数をラップしてAPIとしての振る舞いを定義する）
from rest_framework.decorators import api_view, authentication_classes, permission_classes

# 同じアプリケーション内の `Property` モデルをインポート
from .models import Property

# Propertyモデル用のシリアライザをインポート
from .serializers import PropertiesListSerializer

# `properties_list` 関数をDjango REST framework の API ビューとして定義
@api_view(['GET'])  # HTTP GET リクエストに対してこの関数を実行するよう指定
@authentication_classes([])  # 認証クラスを空にする（認証なしでアクセス可能）
@permission_classes([])  # パーミッション（権限）を空にする（誰でもアクセス可能）
def properties_list(request):
    # 物件（Property）モデルの全データをデータベースから取得
    properties = Property.objects.all()
    
    # `PropertiesListSerializer` を使って、取得したデータをシリアライズ
    # `many=True` を指定して、複数の `Property` オブジェクトをシリアライズする
    serializer = PropertiesListSerializer(properties, many=True)
    
    # シリアライズされたデータをJSON形式でレスポンスとして返す
    return JsonResponse({
        'data': serializer.data  # シリアライズされたデータをレスポンスの `data` フィールドに設定
    })
