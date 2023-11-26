from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CertificateForm
# Create your views here.

def home(request):
    return render(request, 'home.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def upload_certificate(request):
    if request.method == 'POST':
        form = CertificateForm(request.POST, request.FILES)
        if form.is_valid():
            # Create a Certificate object but don't save it to the database yet
            certificate = form.save(commit=False)

            # Associate the certificate with the currently logged-in user
            certificate.user = request.user

            # Save the certificate to the database
            certificate.save()

            # Get the uploaded file and move it to the desired location
            uploaded_file = request.FILES['file']
            handle_uploaded_file(uploaded_file, certificate.id)
            return redirect('dashboard')  # Redirect to the user's dashboard
    else:
        form = CertificateForm()
    return render(request, 'userInfo.html', {'form': form})


def handle_uploaded_file(uploaded_file, certificate_id):
    # Define the target directory
    target_directory = 'media/user_uploads/'

    # Create a unique filename using the certificate id and the original filename
    target_filename = f'{certificate_id}_{uploaded_file.name}'

    # Write the uploaded file to the target directory
    with open(target_directory + target_filename, 'wb+') as destination:
        for chunk in uploaded_file.chunks():
            destination.write(chunk)



