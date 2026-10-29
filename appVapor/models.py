from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Dev(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Sale_event(models.Model):
    name = models.CharField(max_length=50)
    min_discount = models.PositiveSmallIntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    tag = models.ForeignKey(Tag, models.PROTECT, null=True) 

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=50)
    sort_description = models.CharField(max_length=300)
    price = models.PositiveSmallIntegerField()
    tags = models.ManyToManyField(Tag)
    realese_date = models.DateField()
    dev = models.ForeignKey(Dev, models.PROTECT) #Los devis no pueden ser eliminados si tienen algun juego subido
    discount = models.PositiveSmallIntegerField()
    sale_event = models.ForeignKey(Sale_event, models.PROTECT, null=True)

    def __str__(self):
        return self.title

