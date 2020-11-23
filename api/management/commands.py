import json
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from assignment.api.models import Movie,Poster

class Command(BaseCommand):
    """
    store movies data from provided dump
    """
    def handle(self, *args, **options):
        filepath = settings.BASE_DIR + '/imdb.json'
        with open(filepath, 'r') as f:
            raw_data = f.read()
            data = json.loads(raw_data)
            k = {}
            for movie_item in data:
                k['name'] = movie_item.get('name')
                k['popularity'] = movie_item.get('99popularity')
                k['director'] = movie_item.get('director')
                k['imdb_score'] = movie_item.get('imdb_score')
                k['genre'] = movie_item.get('genre')
                movie, created = Movie.objects.get_or_create(**k)
                poster_list = movie_item.get('poster')
                # create genre for each genre in list and attach to current movie
                for poster in poster_list:
                    # poster = poster_list.strip()
                    poster, created = Poster.objects.get_or_create(name=poster)
                    movie.poster.add(poster)
                movie.save()
                print (movie)