from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import logout,authenticate, login

def user_register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():

            chek = checkbox_value = request.POST.get('checkbox')
            print(chek)

            if User.objects.filter(username=form.cleaned_data['username']).exists():
                return render(request, 'registration.html', {
                    'form': form,
                    'error_message': 'Bunday foydalanuvchi mavjud'
                })
            elif form.cleaned_data['password'] != form.cleaned_data['password_repeat']:
                return render(request, 'registration.html', {
                    'form': form,
                    'error_message': 'Parollar bir-biriga mos kelmadi'
                })
                  
            else:
                user = User.objects.create_user(
                    username=form.cleaned_data['username'],
                    password=form.cleaned_data['password']
                )
                user.first_name = form.cleaned_data['first_name']
                user.save()

                return redirect('car')
    else:
        form = RegistrationForm()

    return render(request, 'registration.html', {'form': form})



def logout_(request):
   logout(request)
   return redirect('car')


def user_login(request):
   if request.method == 'POST':
      username = request.POST['username']
      password = request.POST['password']
      
      user = authenticate(username=username, password=password)
      
      if user is not None:
         login(request, user)
         return redirect('car')
      else:
         return render(request, 'login.html', 
                  {'error_message': 'Bunday foydalanuvchi mavjud'})
   else:
      return render(request, 'login.html')   