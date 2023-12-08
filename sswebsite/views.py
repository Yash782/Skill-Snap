from django.shortcuts import render, redirect
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