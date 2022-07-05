from django.contrib import admin

from teachers.models import Teacher


class TeacherAdmin(admin.ModelAdmin):
    list_display = [
        'first_name',
        'last_name',
        'speciality',
        'group',
    ]

    list_display_links = list_display
    list_per_page = 15

    search_fields = [
        'first_name',
        'last_name',
    ]

    list_filter = [
        'group',
    ]

    fields = [
        ('first_name', 'last_name'),
        ('phone_number', 'speciality', 'group')
    ]


admin.site.register(Teacher, TeacherAdmin)
