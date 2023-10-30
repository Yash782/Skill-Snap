from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                userTaken = messages.info(request, "Username Taken")
                return redirect('register')
                
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email Already Exists")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, first_name=first_name, last_name=last_name, password=password1)
                user.save()
                print("User created")
        else:
            messages.info(request, "Password does not match")
            return redirect('register')

        return redirect('/signin')
    else:
        return render(request, 'register.html')
    

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password = password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        
        else:
            messages.info(request, "Invaild credentials ")
            return redirect('/signin')


    else:
        return render(request, 'login.html')
    

def signout(request):
    auth.logout(request)
    return redirect('signin')