from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.home, name="home"),
    path('<int:id>/detail/', views.post_detail, name="post_detail"),
]
