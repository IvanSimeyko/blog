# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect, render
from django.contrib import auth
from django.core.context_processors import csrf
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def login(request):
    context = {}
    context.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Hello %s' % username)
            return redirect('home')
        else:
            context['login_error'] = 'Пользователь не найден'
            return render(request, 'login.html', context)
    else:
        return render(request, 'login.html', context)


def logout(request):
    auth.logout(request)
    return redirect('home')


class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)
    subscribe = forms.BooleanField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None


def register(request):
    args = {}
    args.update(csrf(request))
    args['form'] = UserCreateForm()
    if request.POST:
        new_user_form = UserCreateForm(request.POST)
        if new_user_form.is_valid():
            new_user_form.save()
            new_user = auth.authenticate(username=new_user_form.cleaned_data['username'], password=new_user_form.cleaned_data['password2'])
            auth.login(request, new_user)
            messages.success(request, 'Hello %s' % new_user.username)
            return redirect('home')
        else:
            args['form'] = new_user_form
    return render_to_response('user_form.html', args)



