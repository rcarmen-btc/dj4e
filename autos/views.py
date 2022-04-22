from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin

from autos.models import Makes, Autos
from autos.forms import MakeForm

class AutosList(LoginRequiredMixin, View):

    def get(self, request):

        autos = Autos.objects.all()
        makes_count = Makes.objects.all().count()

        context = {
            'autos': autos,
            'makes_count': makes_count,
        }
        return render(request, 'autos_list.html', context);
        



class MakesList(LoginRequiredMixin, View):

    def get(self, request):

        makes = Makes.objects.all()

        context = {
            'makes': makes,
        }
        return render(request, 'makes_list.html', context);
        

class MakesCreate(LoginRequiredMixin, View):

    def get(self, request):
        form = MakeForm()
        context = {
                'form': form,
        }
        return render(request, 'autos/make_form.html', context)

    def post(self, request):
        form = MakeForm(request.POST)
        if not form.is_valid():
            ctx = {'form': form}
            return render(request, 'autos/make_form.html', ctx)
        make = form.save()
        return redirect(reverse_lazy('autos:autos_list'))



class MakesUpdate(LoginRequiredMixin, View):

    def get(self, request, pk):
        data = get_object_or_404(Makes, pk=pk)
        form = MakeForm(instance=data)
        context = {
                'form': form,
        }
        return render(request, 'autos/make_form.html', context)

    def post(self, request, pk):
        data = get_object_or_404(Makes, pk=pk)
        form = MakeForm(request.POST, instance=data)
        if not form.is_valid():
            ctx = {'form': form}
            return render(request, 'autos/make_form.html', ctx)
        make = form.save()
        return redirect(reverse_lazy('autos:autos_list'))

class MakesDelete(LoginRequiredMixin, View):

    def get(self, request, pk):
        data = get_object_or_404(Makes, pk=pk)
        form = MakeForm(instance=data)
        context = {
                'form': form,
        }
        return render(request, 'autos/makes_delete_submition.html', context)

    def post(self, request, pk):
        data = get_object_or_404(Makes, pk=pk)
        data.delete()
        return redirect(reverse_lazy('autos:autos_list'))


class AutoCreate(LoginRequiredMixin, CreateView):
        model = Autos
        fields = '__all__'
        success_url = reverse_lazy('autos:autos_list')


class AutoUpdate(LoginRequiredMixin, UpdateView):
        model = Autos
        fields = '__all__'
        success_url = reverse_lazy('autos:autos_list')

class AutoDelete(LoginRequiredMixin, DeleteView):
        model = Autos
        fields = '__all__'
        success_url = reverse_lazy('autos:autos_list')


