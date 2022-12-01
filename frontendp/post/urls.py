from django.urls import path
from . import views


urlpatterns = [
    path('',views.main, name="home"),
    path('edit/',views.editpost),
    path('create/', views.createpost),
    path('detail', views.detail)
]