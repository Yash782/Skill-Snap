
from django import forms
from .models import Certificate, UserProfile

class CertificateForm(forms.ModelForm):
    class Meta:
        model = Certificate
        fields = ['certificate_name', 'file', 'certificate_desc' ]
        
#this is form for edit profile option
class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_photo', 'current_position', 'location', 'phone']
