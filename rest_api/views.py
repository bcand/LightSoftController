from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view,  permission_classes
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response

# Create your views here.
def home(request):
    # album = Album.objects.get(pk=1)
    # ser = AlbumSerializer(album)
    return render(request, "rest_api/home.html", {"greeting":"hello"})




# @api_view(['GET', 'POST'])
# # @permission_classes((permissions.AllowAny,))
# def rest_album(request):
#     """get or post a new project"""
#     if request.method=='GET':
#         albums=Album.objects.all()
#         serialiser =AlbumSerializer(albums, many=True)
#         return Response(serialiser.data)
#
#     elif request.method=='POST':
#         serialiser = AlbumSerializer(data = request.data)
#         if serialiser.is_valid():
#             serialiser.save()
#             return Response(serialiser.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serialiser.errors, status=status.HTTP_400_BAD_REQUEST)