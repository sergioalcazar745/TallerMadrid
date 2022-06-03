from django.shortcuts import render

# Create your views here.

# Django REST Framework
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Serializers
from cliente.serializers import *

# Models
from cliente.models import Cliente

class ClienteViewSet(viewsets.GenericViewSet):

    #permission_classes=(IsAuthenticated,)
    
    @action(detail=False, methods=['post'])
    def signup(self, request):
        """User sign up."""
        serializer = ClienteSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = ClienteSignUpSerializer(user).data
        return Response(data, status=status.HTTP_201_CREATED)
    
        #Capar para que solo salga si el usuario es admin
    @action(detail=False, methods=['get'])
    def users(self, request):
        users_list=Cliente.objects.all()
        users_list_serializer = ClienteModelSerializer(users_list, many=True)
        return Response(users_list_serializer.data, status=status.HTTP_200_OK)
    
    @action(detail=False, methods=['get'])
    def user(self, request):
        print(request.GET["dni"])
        try:
            cliente = Cliente.objects.filter(dni=request.GET["dni"]).first()
            print(cliente)
            if(cliente is None):
                return Response({'mensaje': "No existe ese cliente con ese dni"}, status=status.HTTP_404_NOT_FOUND)
        except self.model.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        cliente_serializer = ClienteModelSerializer(cliente)
        return Response(cliente_serializer.data, status=status.HTTP_200_OK)
        
    @action(detail=False, methods=['get'])
    def modificar(self, request):
        print(request.GET['dni'])
        queryset=Cliente.objects.filter(dni=request.GET['dni']).first()
        serializer=ClienteModifySerializer(queryset, request.data)
        serializer.is_valid(raise_exception=True)
        objeto=serializer.save()
        data=ClienteModelSerializer(objeto).data
        return Response(data, status=status.HTTP_200_OK)
        
    @action(detail=False, methods=['get'])
    def borrar(self, request):
        queryset=Cliente.objects.filter(dni=request.GET['dni']).first()
        try:
            objeto=queryset.delete()
        except Cliente.DoesNotExist:
            return None
        else:
            data= ClienteModelSerializer(objeto).data   #Asi convierto el objeto que he guardado en serilizer para enviar el json
            return Response("Se ha eliminado correctamente", status=status.HTTP_200_OK)