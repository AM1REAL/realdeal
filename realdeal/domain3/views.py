from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import mixins, status, viewsets, serializers
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from .models import *
from .serializers import *

class ObjectPViewSet(viewsets.ModelViewSet):
    queryset = ObjectP.objects.all()
    serializer_class = ObjectPSerializer

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class ObjectPList(ListAPIView):
    queryset = ObjectP.objects.all()
    serializer_class = ObjectPSerializer

class AuthEmailObjectPAPI(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = ObjectP.objects.all()
    serializer_class = AuthEmailObjectPSerializer

@api_view(['POST'])
def submit_data(request):
    serializer = ObjectPSerializer(data=request.image)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def get_data(request, pk):
    try:
        objectp = ObjectP.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return Response(status=404)

    serializer = ObjectPSerializer(objectp)
    return Response(serializer.data)

@api_view(['PATCH'])
def update_data(request, pk):
    try:
        objectp = ObjectP.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return Response({'state': 0, 'message': 'Такого перевала не существует'}, status=status.HTTP_404_NOT_FOUND)

    if objectp.status != 'new':
        return Response({'state': 0, 'message': 'Статус перевала не "новый"'}, status=status.HTTP_400_BAD_REQUEST)

    serializer = ObjectPSerializer(objectp, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({'state': 1}, status=status.HTTP_200_OK)
    return Response({'state': 0, 'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

def get_email(self, request, *args, **kwargs):
    email = kwargs.get('email', None)
    if ObjectP.objects.filter(user__email=email).is_exist:
        responsedata = AuthEmailObjectPSerializer(ObjectP.objects.filter(user__email=email), many=True).data
    else:
        responsedata = {'message': f'Записей от email {email} не существует'}

    return Response(responsedata, status=200)
