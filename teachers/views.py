from django.http import HttpResponse
from faker import Faker

from teachers.models import Teacher


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
