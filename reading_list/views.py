from django.shortcuts import render, redirect

from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from reading_list.forms import ReadingListItemForm, ListForm
from reading_list.models import ReadingList, ReadingListItems


# Create your views here.

class ReadingListView(ListView):
    model = ReadingList
    template_name = 'reading_list/list.html'
    context_object_name = 'lists'
    queryset = ReadingList.objects.all().prefetch_related('ítems')

class ReadingListDetailsView(DetailView):
    model = ReadingList
    template_name = 'reading_list/detail.html'
    context_object_name = 'reading_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'item_form' not in context:
            context['item_form'] = ReadingListItemForm(initial = {'reading_list': self.object})
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = ReadingListItemForm(request.POST)

        if form.is_valid():
            item = form.save(commit=False)
            item.save()
            messages.success(request, f"{item.book.title} added to {self.object}!")
            return redirect('reading_list_details', pk = self.object.pk)
        return self.render_to_response(self.get_context_data(form=form))

class ReadingListCreateView(CreateView):
    model = ReadingList
    form_class = ListForm
    template_name = 'reading_list/list_form.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Created new List')
        return response

    def get_success_url(self):
        return reverse('reading_list_detail',kwargs = {'pk': self.object.pk})
