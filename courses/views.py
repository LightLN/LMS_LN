from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from webargs.djangoparser import use_args
from webargs.fields import Int, Str

from .forms import CourseCreateForm
from .models import Course


@use_args(
    {
        'name': Str(required=False),
        'educational_direction': Str(required=False),
        'count_disciplines': Int(required=False)
    },
    location='query'
)
def get_courses(request, args):
    cr = Course.objects.all()
    for key, value in args.items():
        cr = cr.filter(**{key: value})

    return render(
        request,
        'courses/list.html',
        {'title': 'List of courses', 'courses': cr}
    )


def create_course(request):
    if request.method == 'GET':
        form = CourseCreateForm()
    else:
        form = CourseCreateForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('courses:list'))

    return render(
        request=request,
        template_name='courses/create.html',
        context={'form': form}
    )


def update_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'GET':
        form = CourseCreateForm(instance=course)
    else:
        form = CourseCreateForm(request.POST, instance=course)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('courses:list'))

    return render(request, 'courses/update.html', {'form': form})


def delete_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        course.delete()
        return HttpResponseRedirect(reverse('courses:list'))

    return render(request, 'courses/delete.html', {'course': course})
