from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View

# Create your views here.

class MySampleView(View):
    def get(self, request):
        return render(request,'sample.html', {})
