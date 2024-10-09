# Djangoの管理サイトに関連するモジュールをインポート
from django.contrib import admin

# 同じアプリケーション内のPropertyモデルをインポート
from .models import Property

# PropertyモデルをDjango管理サイトに登録します
admin.site.register(Property)
