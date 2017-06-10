# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, models, logout
from django.views import generic
from django.views.generic import View
from models import Blog_Post
from .forms import RegisterForm, LoginForm

class IndexView(generic.base.TemplateView):
    template_name = 'blog/index.html'

    def get(self,request):
        if request.user.is_authenticated :
            return render(request, self.template_name, {'blogPost':Blog_Post.objects.all()[:5]})
        else:
            return redirect('blog:register')

        return render(request, self.template_name, {'blogPost':Blog_Post.objects.all()[:5]})


class UserFormView(View):
    form_class = RegisterForm
    template_name = 'blog/form_register.html'

    def get(self,request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password= password)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('blog:index')
                else: return redirect('blog:index')

        return render(request, self.template_name, {'form':form})

class LoginFormView(generic.UpdateView):
    form_class = LoginForm
    template_name = 'blog/form_login.html'

    def get(self,request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)

        if  form.is_valid():
            user = form

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password= password)
            login(request, user)
            return redirect('blog:index')
        return render(request, self.template_name, {'form':form})




def logoutView(request):
    logout(request)
    return redirect('/')
