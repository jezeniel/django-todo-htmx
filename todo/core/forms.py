from django import forms

from crispy_forms.helper import FormHelper


class AddTodoForm(forms.Form):
    description = forms.CharField(max_length=255)
