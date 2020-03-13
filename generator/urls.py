from django.contrib import admin
from django.urls import path
from django.urls import path
from . import views
 



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name="homepage" ),
    path('password/', views.password, name='password'),
    path('about/', views.about, name='aboutpage')


]
