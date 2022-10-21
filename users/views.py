from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from .forms import LoginForm
from django.views.generic import View
from django import forms


class LoginPageView(View):
    template_name = 'login_user.html'
    form_class = LoginForm
    
    
    def get(self, request):

        form = self.form_class()
        return render(request, self.template_name, context={'form': form})
        
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('/artists/create')
        
        return redirect('/artists')

# def login_user(request):
#     if request.method == "POST":
       
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('/artists/create')
#         else:
#             return redirect('artists')
#             # Return an 'invalid login' error message.
#     else:
#         return render(request , 'login_user.html',{})
