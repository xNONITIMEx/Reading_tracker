from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import FormView
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
# from django.utils.decorators import

from .tokens import account_activation_token
from .forms import ReaderCreationForm
from .email_server import send

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


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('/')


# @user_not_authenticated
def sign_up(request):
    if request.method == 'POST':
        form = ReaderCreationForm(request.POST)
        if form.is_valid():
            reader = form.save(commit=False)
            reader.is_active = False
            reader.save()

            current_site = get_current_site(request)
            mail_subject = 'Activate your account.'
            message = render_to_string('user/activate_account.html', {
                'user': reader.email,
                'domain': get_current_site(request).domain,
                'uid': urlsafe_base64_encode(force_bytes(reader.pk)),
                'token': account_activation_token.make_token(reader),
                'protocol': 'https' if request.is_secure() else 'http'
            })
            print(message)
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to=[to_email])
            print("EmailMessage:", email)
            if email.send():
                print('Good')

            messages.success(request, f'Account for {email} was created!')
            # activate_email(request, reader, form.cleaned_data.get('email'))
            return redirect('/')
        else:
            return render(request, 'user/sign_up.html', {'form': form})
    else:
        print('Method GET')
        form = ReaderCreationForm()
        return render(request, 'user/sign_up.html', {'form': form})


def activate_email(request, user, to_email):
    mail_subject = 'Activate your account.'
    message = render_to_string('user/activate_account.html', {
        'user': user.email,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        'protocol': 'https' if request.is_secure() else 'http'
    })
    # email = EmailMessage(mail_subject, message, to=[to_email])
    send(mail_subject, message, [to_email])
    # if email.send():
    messages.success(request, f'Dear <b>{to_email.split("@")[0]}</b, please go to your email <b>{to_email}</b> inbox and verify your account.'
                              f' <b>Note:</b> Check your spam folder.')
    # else:
    #     messages.error(request, f'Problem sending confirmation email to {to_email}, check if you typed it correctly.')


def activate(request, uidb64, token):
    return redirect('home')
