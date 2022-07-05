from django.shortcuts import render
from django.http import HttpResponseRedirect
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