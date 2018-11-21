from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
    path('mentors/', views.mentors, name='mentors'),
    path('mentees/', views.mentees, name='mentees'),
    path('user_profile/', views.user_profile, name='user profile'),
    path('workspace/', views.workspace, name='workspace'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
