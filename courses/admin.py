from courses.models import Course

from django.contrib import admin


class CourseAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'educational_direction',
        'count_disciplines',
        'group'
    ]
    list_display_links = list_display

    list_per_page = 15

    search_fields = [
        'name',
    ]

    fields = [
        ('name', 'educational_direction'),
        ('count_disciplines', 'group')
    ]

    readonly_fields = ['group']

    def group(self, instance):
        return instance.group


admin.site.register(Course, CourseAdmin)
