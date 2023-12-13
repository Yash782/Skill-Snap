from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import User, Certificate
from .forms import CertificateForm

# Create your views here.

def home(request):
    return render(request, 'home.html')

def dashboard(request):
    user_name = User.objects.all
    certificates = Certificate.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'certificates': certificates})

def delete_certificate(request, certificate_id):
    certificate = get_object_or_404(Certificate, id=certificate_id)

    # Ensure that only the owner can delete the certificate
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