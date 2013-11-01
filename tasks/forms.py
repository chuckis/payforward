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
        #self.helper.form_tag = False    # testing
        self.helper.form_method = 'POST'
        self.helper.form_id = 'example'
        self.helper.form_class = 'modal form-group'
        #self.helper.template = 'bootstrap/betterform.html'
        #self.helper.form_style = 'width: 300px; height: 300px; margin: auto;'
        self.helper.form_action='create_task/'
        self.helper.layout = Layout(
            Field('title', css_class="input",
            placeholder="заголовок просьбы"),
            Field('description', type="textarea", cols='30', rows='5', placeholder = "о чем просите"),
            FormActions(Submit('submit', "Submit", css_class='btn btn-success btn-sm pull-right'),
            Submit('cancel', "Cancel", css_class='btn btn-sm left'),
              )
            )
        super(CreateTaskForm, self).__init__(*args, **kwargs)
