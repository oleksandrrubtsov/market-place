from django.contrib import admin
from django.urls import path,include
from django.views.generic.base import TemplateView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('author/', include('author.urls',namespace= 'author')),
    path('books/', include('book.urls',namespace= 'books')),
    
    
    
    path('admin/', admin.site.urls),
    path('core/',include('django.contrib.auth.urls')),
    path('core/',include('core.urls',namespace= 'core')),
    path('',TemplateView.as_view(template_name = "core/home.html"), name="home"),
   
    
    
]
