from django.urls import path
from . import views


urlpatterns = [
    path('',views.main),
    path('edit/',views.editpost),
    path('create/', views.createpost),
    path('detail', views.detail)
]