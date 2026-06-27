from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views import View
from administration.forms import RegisterForm


class RegisterView(View):
    def get(self, request):
        form=RegisterForm()
        return render(request, 'register.html', { 'form':form })
    
    def post(self, request):
        form_input=RegisterForm(data=request.data)
        if form_input.is_valid():
            fname=form_input.cleaned_data['first_name']
            lname=form_input.cleaned_data['last_name']
            name=form_input.cleaned_data['username']
            email=form_input.cleaned_data['email']
            role=form_input.cleaned_data['role']
            password1=form_input.cleaned_data['password']
            password2=form_input.cleaned_data['rep_password']

            if password1==password2:
                if User.objects.filter(username=name).exists():
                    return render(request, 'register.html', { 'user_err':'user already exists' })
                
                else:
                    User.objects.create_user(first_name=fname, last_name=lname, username=name, email=email, role=role, password=password1)
                    return redirect('register')




