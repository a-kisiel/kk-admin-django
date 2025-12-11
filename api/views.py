from rest_framework import viewsets
from django.http.response import JsonResponse
from django.shortcuts import render
from api.serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.models import *

from rest_framework_simplejwt.views import TokenObtainPairView

class PieceViewSet(viewsets.ModelViewSet):
    queryset = Piece.objects.all()
    serializer_class = PieceSerializer
    permission_classes = [IsAuthenticated]

    @api_view(('GET',))
    def title_list(request):
        titles = Piece.objects.all().values_list('filename', flat=True)
        return Response(list(titles))

    def get_queryset(self):
        if self.request.query_params.get('is_parent') is not None:
            qs = Piece.objects.filter(parent__isnull=True)
        else:
            qs = Piece.objects.all()
        return qs

class MediaViewSet(viewsets.ModelViewSet):
    queryset = Medium.objects.all()
    serializer_class = MediaSerializer
    permission_classes = [IsAuthenticated]

class CollectionViewSet(viewsets.ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    permission_classes = [IsAuthenticated]