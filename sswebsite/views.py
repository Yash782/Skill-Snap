from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import User, Certificate
from .forms import CertificateForm

# Create your views here.

def home(request):
    # Checking if user is authenticated.
    if request.user.is_authenticated:
        certificates = Certificate.objects.filter(user=request.user)
        user_name = User.objects.all
    else:
        certificates = []  # Or handle the case when the user is not authenticated

    return render(request, 'home.html', {'certificates': certificates})

def dashboard(request):
    user_name = User.objects.all
    certificates = Certificate.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'certificates': certificates})

def delete_certificate(request, certificate_id):
    certificate = get_object_or_404(Certificate, id=certificate_id)

    # To ensure that only user can delte the certificate
    if request.user == certificate.user:
        certificate.delete()

    return redirect('dashboard')

def upload_certificate(request):
    if request.method == 'POST':
        form = CertificateForm(request.POST, request.FILES)
        if form.is_valid():
            certificate = form.save(commit=False)
            certificate.user = request.user
            certificate.save()
            return redirect('dashboard')
        else:
            print("Form errors:", form.errors)
            print("Form data:", form.data)
    else:
        form = CertificateForm()
    return render(request, 'userInfo.html', {'form': form})