from django.urls import path
from . import views
from scraper.views import BlogPostsList


urlpatterns = [
    path('', BlogPostsList.as_view(), name = "index"),
    path('signup/', views.SignUp.as_view(), name='signup'),
    
]