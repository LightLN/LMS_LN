from django.contrib import admin

from groups.models import Group

from students.models import Student

from teachers.models import Teacher


class StudentsInlineTable(admin.TabularInline):
    model = Student
    fields = [
        'first_name',
        'last_name',
        'birthday',
        'phone_number',
    ]
    extra = 0
    readonly_fields = fields

    def has_add_permission(self, request, obj):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class TeachersInlineTable(admin.TabularInline):
    model = Teacher
    fields = [
        'first_name',
        'last_name',
        'speciality',
        'phone_number',
    ]

    extra = 0
    readonly_fields = fields

    def has_add_permission(self, request, obj):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class GroupAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'start_date',
        'number_of_lessons',
        'headman',
        'course',
    ]

    fields = [
        'name',
        ('start_date', 'number_of_lessons'),
        ('headman', 'course')
    ]

    search_fields = [
        'name',
    ]

    list_filter = [
        'course',
    ]

    inlines = [StudentsInlineTable, TeachersInlineTable]

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['headman'].widget.can_add_related = False
        return form


admin.site.register(Group, GroupAdmin)
