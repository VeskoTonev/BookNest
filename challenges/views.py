from django.shortcuts import render

from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from challenges.forms import ReadingGoalsForm
from challenges.models import ReadingGoal


# Create your views here.

class GoalListView(ListView):
    model = ReadingGoal
    template_name = 'challenges/goal_list.html'
    context_object_name = 'goals'
    ordering = ['-year']

class GoalDetailView(DetailView):
    model = ReadingGoal
    template_name = 'challenges/goal_detail.html'
    context_object_name = 'goal'


class GoalCreateView(SuccessMessageMixin, CreateView):
    model = ReadingGoal
    form_class = ReadingGoalsForm
    template_name = 'challenges/goal_form.html'
    success_message = 'Reading goal created successfully!'

    def get_success_url(self):
        return reverse('challenges:goal_list')

class GoalUpdateView(SuccessMessageMixin, UpdateView):
    model = ReadingGoal
    form_class = ReadingGoalsForm
    template_name ='challenges/goal_form.html'
    success_message = 'Reading goal updated successfully!'

    def get_success_url(self):
        return reverse('challenges:goal_list')



class GoalDeleteView(DeleteView):
    model = ReadingGoal
    template_name = 'challenges/goal_confirm_delete.html'
    context_object_name = 'goal'
    success_url = reverse_lazy('challenges:goal_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Reading goal deleted successfully!')
        return super().delete(request, *args, **kwargs)
