from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=7,decimal_places=2)
    text = models.TextField(max_length=255)
    image = models.ImageField(null=True,blank=True)


    def __str__(self):
        return self.title

    @property
    def imageURL(self):
        try:
            url = self.image.url 
        except:
            url = ''
        return url
