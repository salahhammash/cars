
# Create your views here.
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Car


class CarListView(ListView):
    template_name = "cars/cars-list.html"
    model = Car
    context_object_name = "Car"


class CarDetailView(DetailView):
    template_name = "cars/cars-detail.html"
    model = Car


class CarCreateView(CreateView):
    template_name = "cars/cars-create.html"
    model = Car
    fields = '__all__'


class CarUpdateView(UpdateView):
    template_name = "cars/cars-update.html"
    model = Car
    fields = '__all__'


class CarDeleteView(DeleteView):
    template_name = "cars/cars-delete.html"
    model = Car
    success_url = reverse_lazy("cars_list")