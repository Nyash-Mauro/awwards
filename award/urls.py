from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', views.home, name='home'),
    path('newproject/', views.new_project, name='newproject'),
    path('search_results/', views.search_project, name="search_project"),
    path('update/', views.update_profile, name="profileupdate"),
    path('profile/', views.profile_info, name='profile')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
