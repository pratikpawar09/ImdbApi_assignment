from rest_framework import serializers
from .models import Movie, Poster

class PosterSerializer(serializers.ModelSerializer):
    """
    Serializer for Poster model
    """
    poster_url = serializers.SerializerMethodField()
    class Meta:

        model = Poster
        fields = ('id','poster','poster_url')

    def get_poster_url(self, car):
        request = self.context.get('request')
        poster_url = car.poster.url
        return request.build_absolute_uri(poster_url)

class MovieSerializer(serializers.ModelSerializer):
    """
    Serializer for Movie model
    """
    poster = PosterSerializer(many=True)
    class Meta:

        model = Movie
        fields = ('name', 'imdb_score', 'popularity', 'director', 'genre','poster') 