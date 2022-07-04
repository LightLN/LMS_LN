from django import forms

from groups.models import Group


class GroupCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['headman_field'] = forms.ChoiceField(
            choices=[
                (student.pk, f'{student.first_name} {student.last_name}') for student in self.instance.students.all()
            ],
            label='Headman',
            required=False
        )

    class Meta:
        model = Group
        fields = '__all__'

        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'})
        }

        exclude = ['headman']
