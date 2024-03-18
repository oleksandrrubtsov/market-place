from django.urls import  path,include
from . import views

from django.views.generic.base import TemplateView

app_name = 'core'

urlpatterns = [
    path('',views.index, name='index'),
    
    # authentication forms
    path('register/',views.register, name='register'),

    path('login/',views.login, name='login'),
    path('logout',views.logout, name="logout"),
]