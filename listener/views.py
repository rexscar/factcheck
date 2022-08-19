from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def Listen(request):
    if request.method == 'GET' :

        return Response(request.GET)

    elif request.method == 'POST' :

        return Response(request.POST, status=status.HTTP_201_CREATED)