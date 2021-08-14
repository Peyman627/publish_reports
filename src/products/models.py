from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to='products', default='no_picture.png')
    price = models.FloatField(help_text='in US dollars $')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        created_date = self.created.strftime('%d/%m/%Y')
        return f'{self.name} --- {created_date}'
