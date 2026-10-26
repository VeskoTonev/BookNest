from django.shortcuts import render, redirect

from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from reading_list.forms import ReadingListItemForm, ListForm, ReadingListItemFormSet
from reading_list.models import ReadingList, ReadingListItems


# Create your views here.

class ReadingListView(ListView):
    model = ReadingList
    template_name = 'reading_list/list.html'
    context_object_name = 'lists'
    queryset = ReadingList.objects.all().prefetch_related('items')

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

        data = request.POST.copy()
        data['reading_list'] = self.object.pk
        form = ReadingListItemForm(data)

        if form.is_valid():
            item = form.save(commit=False)
            item.reading_list = self.object
            item.save()
            messages.success(request, f"{item.book.title} added to {self.object}!")
            return redirect('reading_list:detail', pk = self.object.pk)
        return self.render_to_response(self.get_context_data(item_form=form))

class ReadingListCreateView(CreateView):
    model = ReadingList
    form_class = ListForm
    template_name = 'reading_list/list_form.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Created new List')
        return response

    def get_success_url(self):
        return reverse('reading_list:create')


class ReadingListUpdateView(UpdateView):
    model = ReadingList
    form_class = ReadingListItemForm
    template_name = 'reading_list/list_update.html'
    success_message = 'Reading list updated successfully!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context["item_formset"] = ReadingListItemFormSet(
                self.request.POST, instance = self.object
            )
        else:
            context["item_formset"] = ReadingListItemFormSet(
                 instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        item_formset = context['item_formset']

        if item_formset.is_valid():
            self.object = form.save()
            item_formset.instance = self.object
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form = form))

    def get_success_url(self):
        return reverse('reading_list:detail', kwargs = {'pk': self.object.pk})




class ReadingListDeleteView(DeleteView):
    model = ReadingList
    template_name = 'reading_list/confirm_delete.html'
    context_object_name ='reading_list'
    success_url = reverse_lazy('reading_list:list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Reading list deleted successfully!')
        return super().delete(request, *args, **kwargs)


class ReadingItemListDeleteView(DeleteView):
    model = ReadingListItems
    template_name = 'reading_list/item_confirm_delete.html'
    context_object_name ='item'

    def get_success_url(self):
        return reverse('reading_list:detail', kwargs = {'pk': self.object.pk})

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, f'{obj.book.title} deleted successfully!')
        return super().delete(request, *args, **kwargs)
