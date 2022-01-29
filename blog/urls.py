from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.home, name="home"),
    path('detail/<int:pk>/', views.post_detail, name="post_detail"),
    path('edit/<int:pk>/', views.post_edit, name="post_edit"),
]
