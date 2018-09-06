from django import forms
from django.contrib.auth import get_user_model
from .models import SMEProfile, StaffProfile

User = get_user_model()

class SMEForm(forms.ModelForm):
    class Meta:
        model = SMEProfile
        fields = [
            'user',
            'company_name',
            'description',
            'legal_structure',
            'ownership',
            'country',
            'city',
            'year_founded',
            'currency',
            'linkedin_urls',
            'sector',
            'avatar'
        ]

class StaffForm(forms.ModelForm):
    class Meta:
        model = StaffProfile
        fields = [
            'full_name',
            'role'
        ]
