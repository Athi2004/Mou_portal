from django import forms
from .models import MOU

class MOUForm(forms.ModelForm):
    class Meta:
        model = MOU
        fields = ['name', 'category', 'sub_department', 'start_date', 'end_date', 'document']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }

    CATEGORY_CHOICES = [
        ('Department', 'Department'),
        ('College', 'College'),
        ('Industry', 'Industry'),
    ]

    SUB_DEPARTMENT_CHOICES = {
        'Department': [
            ('N/A', 'Not Applicable'),
            ('BM', 'Biomedical Engineering'),
            ('CE', 'Civil Engineering'),
            ('CSD', 'Computer Science & Design'),
            ('CSE', 'Computer Science & Engineering'),
            ('EEE', 'Electrical & Electronics Engineering'),
            ('ECE', 'Electronics & Communication Engineering'),
            ('EIE', 'Electronics & Instrumentation Engineering'),
            ('ISE', 'Information Science & Engineering'),
            ('ME', 'Mechanical Engineering'),
            ('MC', 'Mechatronics Engineering'),
            ('AG', 'Agricultural Engineering'),
            ('AIDS', 'Artificial Intelligence and Data Science'),
            ('AIML', 'Artificial Intelligence and Machine Learning'),
            ('BT', 'Biotechnology'),
            ('CSBS', 'Computer Science & Business Systems'),
            ('CT', 'Computer Technology'),
            ('FT', 'Food Technology'),
            ('FT', 'Fashion Technology'),
            ('IT', 'Information Technology'),
            ('TT', 'Textile Technology'),
        ],
        'College': [
            ('N/A', 'Not Applicable'),
        ],
        'Industry': [
            ('N/A', 'Not Applicable'),
        ],
    }

    category = forms.ChoiceField(choices=CATEGORY_CHOICES)
    sub_department = forms.ChoiceField(choices=SUB_DEPARTMENT_CHOICES['Department'])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].widget.attrs.update({'onchange': 'updateSubDepartmentOptions()'})

    def clean_sub_department(self):
        sub_department = self.cleaned_data.get('sub_department')
        if not sub_department:
            return 'N/A'
        return sub_department