from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.request_list, name='request_list'),
    path('request/<int:pk>/', views.request_detail, name='request_detail'),
    path('submit/', views.submit_request, name='submit_request'),
    path('signup/', views.signup, name='signup'),
    path('download/<str:filename>/', views.download_file, name='download_file'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)