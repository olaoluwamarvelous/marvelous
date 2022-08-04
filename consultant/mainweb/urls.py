"""
from . import views
from django.urls import path
#from .views import views


urlpatterns =[
    path('main', views.main, name='main'),
    path('blog', views.blog, name='blog'),
    path('recentpost', views.recentpost, name='recentpost'),

    path('<slug:slug>/', views.blogdetail, name='blogdetail'),
    path('contact', views.contact, name='contact'),
    path('', views.index, name='index'),
    path('service', views.service, name='service'),
    path('team', views.team, name='team'),
    path('about', views.about, name='about'),
    path('testimony', views.testimony, name='testimony'),
]
"""

from . import views
from django.urls import path

#from .views import views


urlpatterns = [
    path('contact', views.contact, name='contact'),


    path('service', views.service, name='service'),
    path('about', views.about, name='about'),

    path('<slug:slug>/', views.blogdetail, name='blogdetail'),


    path('main', views.main, name='main'),
    path('', views.index, name='index'),
    #generic ones
    path('testimony', views.TestimonyView.as_view(), name='testimony'),


    path('team', views.TeamView.as_view(), name='team'),
    path('blog',  views.BlogView.as_view(), name='blog'),
    path('recentpost', views.RecentpostView.as_view(), name='recentpost'),
    
]
