from django.shortcuts import render, redirect

from .forms import TrainingForm
from .models import *

# Create your views here.
def index(request):
    trainings = Training.objects.all()
    return render(request, 'index.html', {"trainings": trainings})

def add_training(request):
    if request.method == "POST":
        form = TrainingForm(request.POST, request.FILES)
        if form.is_valid():
            flight = form.save(commit=False)
            flight.user = request.user
            flight.save()
            return redirect('index')
    form = TrainingForm()
    return render(request, 'add_training.html', {"form":form})
