from django.db import models
from django.db.models import Model, CharField, ForeignKey, IntegerField, DateField, TextField, DateTimeField, DO_NOTHING


# Create your models here.


class Genre(Model):
    name = CharField(max_length=20)

class Movie(Model):
    title = CharField(max_length=80)
    genre = ForeignKey(Genre, on_delete=DO_NOTHING)
    rating = IntegerField()
    released = DateField()
    description = TextField()
    created = DateTimeField(auto_now_add=True)



