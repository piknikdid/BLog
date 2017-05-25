# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import View
from models import Blog_Post
from .forms import RegisterForm

class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'blogPost'


    def get_queryset(self):
        return Blog_Post.objects.all()

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

        return render(request, self.template_name, {'form':form})
