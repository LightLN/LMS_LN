from django import forms
from teachers.models import Teacher


class TeacherCreateForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = [
            'first_name',
            'last_name',
            'speciality',
            'phone_number'
        ]

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        result = ''.join([char for char in phone_number if char.isdigit()])
        return result
