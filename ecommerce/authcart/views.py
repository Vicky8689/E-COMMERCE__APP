from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def signup(request):
  if request.method == "POST":
    email = request.POST['email']
    password = request.POST['pass1']
    confirm_password = request.POST['pass2']
    
    if password != confirm_password:
        messages.warning(request,"Password Not Match")
        return render(request,'signup.html')
        # return HttpResponse("Password not match")

    try:
        if User.objects.get(username=email):
            messages.warning(request,"Alredy a user")
            # return HttpResponse("Email already exists")
            return render(request,'signup.html')

    except User.DoesNotExist:
        pass

    user = User.objects.create_user(email, email, password)
    user.save()
    messages.warning(request,"User Created")
    # return HttpResponse("User created")
    return render(request,'login.html')
    


  return render(request,"signup.html")



def handlelogin(request):
  
  if request.method == "POST":
     
     
     username=request.POST['email']
     userpassword = request.POST['pass1']
     myuser=authenticate(username=username,password = userpassword ) #if username or password any one is wrong than myuser give none

     if myuser is not None:
        
        login(request,myuser)
        messages.success(request,"Login Suuccesfull")
        return redirect('/')
     else:
        
        messages.error(request,"Invalid Credentials")
        return redirect('/auth/login') 
        
  


  return render(request,"login.html")




def handlelogout(request):
  logout(request)
  messages.info(request,"Logout Success")


  return redirect('/auth/login')