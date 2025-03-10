from django import urls
from django.http.request import validate_host
from django.urls import path


from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_login_view, name='register_login'),
    path('dashboard/about', views.dashboard_about, name='dashboard_about'),
    path('dashboard/article', views.dashboar_article, name='dashboard_article'),
    path('dashboard/certificate', views.dashboard_sertificate, name='dashboard_certificate'),
    path('dashboard/password-change', views.dashboard_pasword_change, name='password_change'), 

    path('documents/', views.documents, name='documents'),
    path('help-handbook/', views.help_handbook, name='help_handbook')
]
