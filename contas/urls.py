from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('sigin/', views.signin_view, name='signin'),
    path('logout/', views.logout_view, name='logout'),
]

