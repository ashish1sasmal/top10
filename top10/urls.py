
from django.urls import path
from top10 import views

app_name='top10'

urlpatterns = [
    path('login/',views.user_login,name='user_login'),
    path('register/',views.register,name='register')
]