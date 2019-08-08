from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('user.urls')),
    path('items/', include('item.urls.item_urls')),
    path('categorys/', include('item.urls.cate_urls')),
    path('media/uploads/item_images/<str:file_name>', views.image_view),
]