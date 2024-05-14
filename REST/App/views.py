from django.shortcuts import render
from django.http import HttpRequest, JsonResponse
# Create your views here.



def index(request:HttpRequest):
    response={"message, Hello world"}
    return JsonResponse(data=response)