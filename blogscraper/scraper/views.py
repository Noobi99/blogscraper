from django.shortcuts import render, HttpResponse
from django.views.generic.list import ListView

from .models import Blog, BlogPost

# Create your views here.
def index(request):
    return HttpResponse("It works")


class BlogPostsList(ListView):
    model = BlogPost
    paginate_by = 100
    template = "scraper/blogpost_list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
