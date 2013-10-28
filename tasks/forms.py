from django import forms
from models import Task
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import FormActions

class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title','description','category','end_date','task_photo')
