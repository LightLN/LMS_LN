from django import forms

from groups.models import Group


class GroupCreateForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = [
            'name',
            'start_date',
            'number_of_lessons'
        ]

        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'})
        }
