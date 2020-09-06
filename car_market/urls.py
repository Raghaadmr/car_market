
from django.contrib import admin
from django.urls import path
from cars import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cars/', views.car_list, name='car-list'),
    path('cars/<int:car_id>/', views.car_detail, name='car-detail'),

    path('cars/create', views.create, name='car-create'),
    path('cars/<int:car_id>/update/', views.update, name='car-update'),
    path('cars/<int:car_id>/delete/', views.delete, name='car-delete'),
]
urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
