from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Show
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Define the home view
class Home(LoginView):
  template_name = 'home.html'

def show_index(request):
  shows = Show.objects.filter(user=request.user)
  return render(request, 'shows/index.html', {'shows': shows})

def show_detail(request, show_id):
  show= Show.objects.get(id=show_id)
  return render(request, 'shows/detail.html', { 'show': show})

class ShowCreate(CreateView):
  model = Show
  fields= ['name', 'genre', 'seasons', 'notes', 'rating', 'stillWatching']
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class ShowUpdate(UpdateView):
  model= Show
  fields= '__all__'

class ShowDelete(DeleteView):
  model= Show
  success_url= '/shows/'

class Home(LoginView):
  template_name = 'home.html'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('show-index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)
