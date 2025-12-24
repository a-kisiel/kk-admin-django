from rest_framework import viewsets
from django.http.response import JsonResponse
from django.shortcuts import render
from api.serializers import *
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from api.models import *

from rest_framework_simplejwt.views import TokenObtainPairView

class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

@api_view(('GET',))
@permission_classes([ReadOnly])
def get_everything(request):
    data = {
        'pieces': [],
        'media': [],
        'collections': []
    }

    for piece in Piece.objects.all():
        data['pieces'].append(PieceSerializer(piece).data)
    for medium in Medium.objects.all():
        data['media'].append(MediaSerializer(medium).data)
    for collection in Collection.objects.all():
        data['collections'].append(CollectionSerializer(collection).data)

    return JsonResponse(data)

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