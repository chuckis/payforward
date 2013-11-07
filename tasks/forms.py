# -*- coding:utf-8 -*-
#from django import forms
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import *
from crispy_forms.bootstrap import *
from models import Task, User

class CreateTaskForm(ModelForm):
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
        
        
# custom class for handling crispy forms in registration form
#class CustomUserCreationForm(UserCreationForm):
    #class Meta:
        #model = User
        #fields = ("username",)
    #def __init__(self, *args, **kwargs):
        #self.helper = FormHelper()
        #self.helper.form_method = 'POST'
        #self.helper.form_id = 'example'
        #self.helper.form_class = 'modal form-group'
        #self.helper.form_action = 'registration'
        #self.helper.layout = Layout(
                #Fieldset(
        #'Sign up',
        #'username',
        ##'password',
        ##'confirm_password'
    #),
    #FormActions(
        #Submit('submit', 'Signup', css_class="btn-large")
    #)
#)
        ##self.helper.layout = Layout(
            ##Field('username', css_class="input",
            ##placeholder="юзернэйм"),
            ###Field('password', css_class="input",
            ###placeholder="пароль"),
            ##FormActions(Submit('submit', "Submit", css_class='btn btn-success btn-sm pull-right'),
            ##Submit('cancel', "Cancel", css_class='btn btn-sm left'),
            ##)
        ##)
        #super(CustomUserCreationForm, self).__init__(*args, **kwargs)









