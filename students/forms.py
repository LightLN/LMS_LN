from django import forms

from django_filters import FilterSet

from .models import Student


class StudentCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(StudentCreateForm, self).__init__(*args, **kwargs)
        self.fields['group'].required = False

    class Meta:
        model = Student
        fields = [
            'first_name',
            'last_name',
            'phone_number',
            'birthday',
            'group'
        ]

        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }

    def clean_first_name(self):
        fn = self.cleaned_data['first_name']
        return fn.title()

    def clean_last_name(self):
        ln = self.cleaned_data['last_name']
        return ln.title()

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        result = ''.join([char for char in phone_number if char.isdigit()])
        return result


class StudentFilterForm(FilterSet):
    class Meta:
        model = Student
        fields = {
            'first_name': ['exact', 'icontains'],
            'last_name': ['exact', 'startswith'],
        }
