from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from .models import Show

# Define the home view
def home(request):
  return render(request, 'base.html')

def show_index(request):
  shows = Show.objects.all()
  return render(request, 'shows/index.html', {'shows': shows})

def show_detail(request, show_id):
  show= Show.objects.get(id=show_id)
  return render(request, 'shows/detail.html', { 'show': show})

class ShowCreate(CreateView):
  model = Show
  fields= '__all__'

class ShowUpdate(UpdateView):
  model= Show
  fields= '__all__'