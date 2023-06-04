from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('shows/', views.show_index, name='show-index'),
  path('shows/<int:show_id>/', views.show_detail, name='show-detail'),
  # path('shows/create/', views.ShowCreate.as_view(), name='show-create'),
]