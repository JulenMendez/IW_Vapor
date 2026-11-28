from django.db import models
import math, os

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.name

    def get_image_name(self) -> str:
        low:str = self.name.lower()
        return "".join(low.split(" "))

    def get_url_name(self) -> str:
        low:str = self.name.lower()
        return "-".join(low.split(" "))

    @staticmethod
    def name_from_url(tag_url:str) -> str:
        return " ".join(tag_url.split("-"))

    
class Dev(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.name
    
    def get_image_name(self) -> str:
        low:str = self.name.lower()
        return "".join(low.split(" "))

    def get_url_name(self) -> str:
        low:str = self.name.lower()
        return "-".join(low.split(" "))

    @staticmethod
    def name_from_url(dev_url:str) -> str:
        return " ".join(dev_url.split("-"))


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
    short_description = models.CharField(max_length=300)
    price = models.PositiveSmallIntegerField()
    tags = models.ManyToManyField(Tag)
    realese_date = models.DateField()
    dev = models.ForeignKey(Dev, models.PROTECT) #Los devis no pueden ser eliminados si tienen algun juego subido
    discount = models.PositiveSmallIntegerField()
    sale_event = models.ForeignKey(Sale_event, models.PROTECT, null=True)

    def __str__(self):
        return self.title

    def get_image_name(self) -> str:
        low:str = self.title.lower()
        return "".join(low.split(" "))

    def get_url_name(self) -> str:
        low:str = self.title.lower()
        return "-".join(low.split(" "))

    @staticmethod
    def name_from_url(game_url:str) -> str:
        return " ".join(game_url.split("-"))

    def get_current_price(self) -> int:
        price_dicount:int = int(self.price * ((100 - self.discount)/100))
        return price_dicount
        
    def get_carousel_names(self) -> list[str]:
        image_dir:str = self.get_image_name()
        carousel_path:str = os.path.join("appVapor", "static", "images", "Carrusel")
        result:list[str] = []

        exist:bool = True
        i:int = 0
        while(exist):
            image_name:str = f"{image_dir}{i}"
            exist = os.path.exists(os.path.join(carousel_path, image_dir, f"{image_name}.jpg"))

            if (exist):
                result.append(image_name)

            i += 1

        return result


