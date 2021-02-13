from django import forms
from django.forms import ModelForm

from . import models

class TaskForm(forms.ModelForm):
    task= forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Add new task...'}))
    class Meta:
        model = models.List
        fields = "__all__"
        exclude = ['user']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)