from django.shortcuts import render
# from django.views.generic.edit import CreateView
from .models import Show

# Define the home view
def home(request):
  return render(request, 'base.html')

def show_index(request):
  shows = Show.objects.all()
  return render(request, 'shows/index.html', {'shows': shows})

# class ShowCreate(CreateView):
#   model = Show
#   fields= '__all__'