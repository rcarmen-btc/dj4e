from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView
from django.shortcuts import render

from cats.models import Breed, Cat


class BreedList(LoginRequiredMixin, View):

    def get(self, request):

        breed = Breed.objects.all()

        context = {
            'breeds': breed,
        }
        return render(request, 'cats/breed_list.html', context);


class CatList(LoginRequiredMixin, View):

    def get(self, request):

        cats = Cat.objects.all()
        breed_count = Breed.objects.all().count()

        context = {
            'cat': cats,
            'breed_count': breed_count,
        }
        return render(request, 'cats/cat_list.html', context);


class BreedCreate(LoginRequiredMixin, CreateView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:cat_list')


class BreedUpdate(LoginRequiredMixin, UpdateView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:cat_list')


class BreedDelete(LoginRequiredMixin, DeleteView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:cat_list')


class CatCreate(LoginRequiredMixin, CreateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:cat_list')


class CatUpdate(LoginRequiredMixin, UpdateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:cat_list')


class CatDelete(LoginRequiredMixin, DeleteView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:cat_list')
