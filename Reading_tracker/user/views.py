from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import FormView
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm



class Login(FormView):
    form_class = AuthenticationForm
    success_url = '/'
    template_name = 'user/login.html'

    def form_valid(self, form):
        self.reader = form.get_user()
        login(self.request, self.reader)
        return super(Login, self).form_valid(form)

    def form_invalid(self, form):
        return super(Login, self).form_invalid(form)


class LogOut(View):
    def get(self, request):
        logout(request)
        return redirect('/')


def sign_up(request):
    if request.method == 'POST':
        form = ReaderCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            messages.success(request, f'Account for {email} was created!')
            print('Success')
            return redirect('/')
        print('Failed')
    else:
        print('Method GET')
        form = ReaderCreationForm()
        return render(request, 'user/sign_up.html', {'form': form})
