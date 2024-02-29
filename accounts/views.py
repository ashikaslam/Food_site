from django.shortcuts import render,redirect
from .forms import RegistrationForm
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import User_profile_update
from order.models import Order
# Create your views here.



def sign_up(request):
    if request.method=="POST":
         form = RegistrationForm(request.POST) 
         print('hello')
         if form.is_valid():
             user = form.save()
             login(request,user)
             return redirect('user_profile')
         
             
        
    else:
        form = RegistrationForm()    


    return render (request,'register.html',{'form':form})


def log_in(request):
   if request.method=='POST':
       username = request.POST['username']
       password = request.POST['password']
       user = authenticate(username= username, password= password)
       if user is not None:
           login(request,user)
           return redirect('user_profile')

   return render(request,'login.html')

def log_out(request):
    logout(request)
    return redirect('login')

def user_profile(request):
    return render(request,'profile.html')


@login_required
def profileUP(request):
    if request.method == 'POST':
        user_form = User_profile_update(request.POST, instance=request.user)

        if user_form.is_valid():
            user_form.save()
         
            messages.success(request, 'Your profile is updated successfully')
            return redirect('user_profile')
    else:
        user_form = User_profile_update(instance=request.user)
       
    return render(request, 'profile_p.html', {'form': user_form})



def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user) 
            messages.success(request, 'Your password was successfully updated!')
            return redirect('user_profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'pass.html', {
        'form': form
    })




def see_user_ordr_history(request):
    my_orders = Order.objects.filter(user=request.user).order_by('-created_at')

    return render(request,'hostory.html',{'my_orders':my_orders})