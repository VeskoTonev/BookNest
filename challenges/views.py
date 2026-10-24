from django.shortcuts import render

from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from challenges.models import ReadingGoal


# Create your views here.

class GoalListView(ListView):
    model = ReadingGoal
    template_name = 'challenges/goal_list.html'
    context_object_name = 'goals'
    ordering = ['-year']
    