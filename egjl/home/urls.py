from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path('', views.Index.as_view(), name="index"),
    path('masita/', views.About.as_view(), name="masita"),
    path('masita/detail/<int:pk>/', views.DetailUser.as_view(), name="detail"),
]
