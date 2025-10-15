from django import forms
from .models import Application

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ["company", "role", "location", "source", "status", "salary", "notes", "next_action_date"]

