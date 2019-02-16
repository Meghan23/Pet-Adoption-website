# Create your views here.
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render
from .models import Pet, CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.views import redirect_to_login


def index(request):
    return render(request, 'index.html')


def search(request):
    Breed = request.GET['p']
    Sex = request.GET['q']
    Color = request.GET['r']
    try:
        Needs = request.GET['u']
    except:
        Needs = False
    try:
        Bonded = request.GET['v']
    except:
        Bonded = False
    results = Pet.objects.filter(breed=Breed, sex=Sex, color=Color, needs=Needs, bonded=Bonded)

    return render(request, 'results.html', {'results': results})


def allposts(request, pid):
    a = Pet.objects.get(id=pid)
    us = a.uid
    return render(request, 'allposts.html', {'us': us})


def dashboard(request):
    return render(request, 'home.html')


class SignUp(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class UpdateProfile(UpdateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    success_url = reverse_lazy('dashboard')
    template_name = 'signup.html'


class PetCreate(CreateView):
    model = Pet
    fields = ['photo', 'name', 'breed', 'sex', 'age', 'color', 'needs', 'bonded']

    def form_valid(self, form):
        form.instance.uid = self.request.user
        return super(PetCreate, self).form_valid(form)


class PetUpdate(UpdateView):
    model = Pet
    fields = ['photo', 'name', 'breed', 'sex', 'age', 'color', 'needs', 'bonded']

    def form_valid(self, form):
        form.instance.uid = self.request.user
        return super(PetUpdate, self).form_valid(form)


class PetDelete(DeleteView):
    model = Pet
    success_url = reverse_lazy(dashboard)
