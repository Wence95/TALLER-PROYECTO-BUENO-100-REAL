from urllib import request
from django.shortcuts import render

from django.http import HttpResponse

def eu(request):
    return HttpResponse("este sitio es de el galpon")