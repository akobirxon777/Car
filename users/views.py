from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import logout

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


   