from django.db import models

# Create your models here.

class Poster(models.Model):
    """
    Genre model : Table for movie Genres
    """
    poster = models.ImageField(upload_to='posters/')

    def __str__(self):
        return '{}'.format(self.poster)

class Movie(models.Model):
    """
    Movie model : model for Movies
    """
    GENRE_CHOICES = (('horror', 'Horror'),
                     ('family', 'Family'),
                     ('fantasy', 'Fantasy'),
                     ('musical', 'Musical'),
                     ('sci-Fi', 'Sci-Fi'),
                     ('drama', 'Drama'),
                     ('war', 'War'),
                     ('animation', 'Animation'),
                     ('romance', 'Romance'),
                     ('mystery', 'Mystery'),)
    name = models.CharField(max_length=500)
    imdb_score = models.FloatField()
    popularity = models.FloatField()
    director = models.CharField(max_length=500)
    genre = models.CharField(choices=GENRE_CHOICES,max_length=8,default=None)
    poster = models.ForeignKey(Poster,on_delete=models.CASCADE,default=None)

    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movies"

    def __str__(self):
        return self.name
