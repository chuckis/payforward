# -*- coding:utf-8 -*-
from django import forms
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import *
from crispy_forms.bootstrap import *
from models import Task

class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title','description','category','end_date','task_photo')
        
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.form_id = ''
        self.helper.form_class = 'modal-body'
        self.helper.form_action=''
        self.helper.layout = Layout(
            Field('title', css_class="input",
            placeholder="заголовок просьбы"),
            Field('description', type="textarea", placeholder = "о чем просите"),
            FormActions(Submit('submit', "Submit", css_class='btn btn-success'),
            Submit('cancel', "Cancel", css_class='btn'),
              )
            )
        super(CreateTaskForm, self).__init__(*args, **kwargs)
