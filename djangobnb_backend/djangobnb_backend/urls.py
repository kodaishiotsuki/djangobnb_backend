from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

# URLパターンのリストを定義
urlpatterns = [
    # 管理画面へのアクセスURLを定義 ('admin/' でアクセス可能)
    path('admin/', admin.site.urls),
    
    # 'api/properties/' にアクセスした際に、propertyアプリのurls.pyに定義されたURLパターンを含める
    path('api/properties/', include('property.urls')),

    # 'api/auth/' にアクセスした際に、useraccountアプリのurls.pyに定義されたURLパターンを含める
    path('api/auth/', include('useraccount.urls')),
]

# 開発環境でメディアファイル（画像など）にアクセスできるようにする設定
# settings.py の MEDIA_URL に対応するURLパスから、MEDIA_ROOT に保存されたファイルにアクセス可能にする
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
