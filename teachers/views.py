from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from faker import Faker

from webargs.djangoparser import use_args
from webargs.fields import Str

from .forms import TeacherCreateForm
from .models import Teacher


def generate_teachers(request):
    cnt = int(request.GET.get("cnt", 10))
    fk = Faker()
    for _ in range(cnt):
        teach = Teacher(
            first_name=fk.first_name(),
            last_name=fk.last_name(),
            speciality=fk.job(),
            phone_number=fk.phone_number(),
        )
        teach.save()
    return HttpResponse('')


@use_args(
    {
        'first_name': Str(required=False),
        'last_name': Str(required=False),
        'speciality': Str(required=False)
    },
    location='query'
)
def get_teachers(request, args):
    t = Teacher.objects.all()
    for key, value in args.items():
        t = t.filter(**{key: value})

    return render(
        request,
        'teachers/list.html',
        {'title': 'List of teachers', 'teachers': t}
    )


def create_teacher(request):
    if request.method == 'GET':
        form = TeacherCreateForm()
    else:
        form = TeacherCreateForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('teachers:list'))

    return render(
        request=request,
        template_name='teachers/create.html',
        context={'form': form}
    )


def update_teacher(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'GET':
        form = TeacherCreateForm(instance=teacher)
    else:
        form = TeacherCreateForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('teachers:list'))

    return render(request, 'teachers/update.html', {'form': form})


def delete_teacher(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        teacher.delete()
        return HttpResponseRedirect(reverse('teachers:list'))

    return render(request, 'teachers/delete.html', {'teacher': teacher})
