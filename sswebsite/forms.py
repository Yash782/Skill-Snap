
from django import forms
from .models import Certificate, UserProfile, Links

class CertificateForm(forms.ModelForm):
    class Meta:
        model = Certificate
        fields = ['certificate_name', 'file', 'certificate_desc' ]
        
#this is form for edit profile option
class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_photo', 'current_position', 'location', 'phone']

#this form deals with social links
        
class LinksForm(forms.ModelForm):
    class Meta:
        model = Links
        fields = ['gitLink', 'linkedInLink', 'portfolioLink', 'otherLink']
