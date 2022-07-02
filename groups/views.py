from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import ListView
from django.views.generic import UpdateView

from students.models import Student

from .forms import GroupCreateForm
from .models import Group


class ListGroupView(ListView):
    model = Group
    template_name = 'groups/list.html'


class CreateGroupView(LoginRequiredMixin, CreateView):
    model = Group
    form_class = GroupCreateForm
    success_url = reverse_lazy('groups:list')
    template_name = 'groups/create.html'


class UpdateGroupView(LoginRequiredMixin, UpdateView):
    model = Group
    success_url = reverse_lazy('groups:list')
    form_class = GroupCreateForm
    template_name = 'groups/update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['students'] = self.get_object().students.prefetch_related('headman_group')

        return context

    def get_initial(self):
        initial = super().get_initial()
        try:
            initial['headman_field'] = self.object.headman.pk
        except AttributeError:
            pass

        return initial

    def form_valid(self, form):
        response = super().form_valid(form)
        try:
            form.instance.headman = Student.objects.get(pk=form.cleaned_data['headman_field'])
            form.instance.save()
        except ValueError:
            pass

        return response


class DeleteGroupView(LoginRequiredMixin, DeleteView):
    model = Group
    success_url = reverse_lazy('groups:list')
    template_name = 'groups/delete.html'
