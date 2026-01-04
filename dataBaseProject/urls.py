
from django.contrib import admin
from django.urls import path
from postgresApp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.signup),
    path('show/', views.alll),
    path('writefile/', views.writefile),

]