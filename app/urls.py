from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('answers/<int:id>/', views.answers_view, name='answers'),
    path('answers/<int:id>/like/,', views.like_view, name='like_view'),
]