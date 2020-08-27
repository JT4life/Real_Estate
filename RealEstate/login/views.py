from django.contrib.auth.models import auth, User
from django.shortcuts import render, redirect
from django.contrib import messages


# Create your views here.



def signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        uname = request.POST['uname']
        fname=request.POST['fname']
        lname=request.POST['lname']

        pass1 = request.POST['password']
        pass2 = request.POST['cpassword']
        #user1=users.objects.get(username=uname)
        if User.objects.filter(username=uname).exists():
            messages.info(request, 'user already exist')
            return redirect('signup')

        elif pass1 != pass2:
            messages.info(request, 'password and confirm password should be same')
            return redirect('signup')
        elif uname == pass1:
            messages.info(request, 'username and password should not be same')
            return redirect('signup')

        else:
            user = User.objects.create_user(username=uname, first_name=fname, last_name=lname, email=email,
                                            password=pass2)
            user.save()
            messages.info(request, 'your are registered now try to login')
            return redirect('login')

    return render(request,'signup.html')



def login(request):
    if request.method == 'POST':
        uname=request.POST['username']
        password=request.POST['password']
        user = auth.authenticate(username=uname, password=password)
        if user:


            #request.session['logedUser'] = uname
            auth.login(request,user)
            #data ={ 'username':request.session.get('logedUser')}
            return redirect("index")
        else:
            messages.info(request, 'Invalid User')
            return redirect('login')
    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    #messages.info(request, 'Sorry you need to register or login')
    return redirect("index")