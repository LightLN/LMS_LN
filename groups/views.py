from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from webargs.djangoparser import use_args
from webargs.fields import Int, Str

from .forms import GroupCreateForm
from .models import Group


@use_args(
    {
        'name': Str(required=False),
        'start_date': Int(required=False),
        'number_of_lessons': Int(required=False)
    },
    location='query'
)
def get_groups(request, args):
    gr = Group.objects.all()
    for key, value in args.items():
        gr = gr.filter(**{key: value})

    return render(
        request,
        'groups/list.html',
        {'title': 'List of groups', 'groups': gr}
    )


def create_group(request):
    if request.method == 'GET':
        form = GroupCreateForm()
    else:
        form = GroupCreateForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('groups:list'))

    return render(
        request=request,
        template_name='groups/create.html',
        context={'form': form}
    )


def update_group(request, pk):
    group = get_object_or_404(Group, pk=pk)
    if request.method == 'GET':
        form = GroupCreateForm(instance=group)
    else:
        form = GroupCreateForm(request.POST, instance=group)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('groups:list'))

    return render(request, 'groups/update.html', {'form': form})


def delete_group(request, pk):
    group = get_object_or_404(Group, pk=pk)
    if request.method == 'POST':
        group.delete()
        return HttpResponseRedirect(reverse('groups:list'))

    return render(request, 'groups/delete.html', {'group': group})
