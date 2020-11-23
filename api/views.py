from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from .models import Movie
from .serializers import MovieSerializer
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser
# Create your views here.

class IndexView(APIView):
    """
    API view for searching Movies
    """
    allowed_methods = ['GET']
    serializer_class = MovieSerializer
    permission_classes = (IsAdminUser,)
    authentication_classes = (TokenAuthentication,)

    def get(self, request):
        queryset = Movie.objects.all()
        # # We can filter our movies by name
        name = request.query_params.get('name', None)
        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
