from django.urls import path
from .views import CarListView, CarDetailView, CarCreateView, CarUpdateView, CarDeleteView

urlpatterns = [
    path('cars/', CarListView.as_view(), name='cars_list'),
    path('<int:pk>/', CarDetailView.as_view(), name='cars_detail'),
    path('create/', CarCreateView.as_view(), name='cars_create'),
    path('<int:pk>/update/', CarUpdateView.as_view(), name='cars_update'),
    path('<int:pk>/delete/', CarDeleteView.as_view(), name='cars_delete'),
]