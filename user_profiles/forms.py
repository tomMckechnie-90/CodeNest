from django import forms
from .models import UserProfile

from django import forms
from .models import UserProfile
from django_summernote.widgets import SummernoteWidget

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'date_of_birth', 'gender', 'bio', 'profile_picture']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'bio': SummernoteWidget(),
        }
