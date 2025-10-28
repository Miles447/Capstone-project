from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from.models import Animal, Produce
from django.shortcuts import render
from django.http import HttpResponse


#Create your views here.

#Animal views

def home(request):
    return render(request, 'farm/home.html')

class AnimalListView(ListView):
    model = Animal
    template_name = "farm/animal_list.html"
    context_object_name = "animals"

class AnimalDetailView(DetailView):
    model = Animal
    template_name = "farm/animal_detail.html"
    context_object_name = "animal"

class AnimalCreateView(CreateView):
    model = Animal
    template_name = "farm/animal_form.html"
    fields = ['name', 'species', 'age']
    success_url = reverse_lazy("animal_list")

class AnimalUpdateView(UpdateView):
    model = Animal
    template_name = "farm/animal_form.html"
    fields = ['name', 'species', 'age']
    success_url = reverse_lazy("animal_list")

class AnimalDeleteView(DeleteView):
    model = Animal
    template_name = "farm/animal_confirm_delete.html"
    success_url = reverse_lazy("animal_list")


# Produce Views

class ProduceListView(ListView):
    model = Produce
    template_name = "farm/produce_list.html"
    context_object_name = "produces"

class ProduceDetailView(DetailView):
        model = Produce
        template_name = "farm/produce_detail.html"
        context_object_name = "produce"

class ProduceCreateView(CreateView):
    model = Produce
    template_name = "farm/produce_form.html"
    fields = ['animal', 'produce_type', 'quantity']   # ✅ updated
    success_url = reverse_lazy("produce_list")

class ProduceUpdateView(UpdateView):
    model = Produce
    template_name = "farm/produce_form.html"
    fields = ['animal', 'produce_type', 'quantity']   # ✅ updated
    success_url = reverse_lazy("produce_list")

class ProduceDeleteView(DeleteView):
    model = Produce
    template_name = "farm/produce_confirm_delete.html"
    success_url = reverse_lazy("produce_list")
