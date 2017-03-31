from __future__ import unicode_literals

from django.db import models

from category.models import CategoryData
from city.models import CityData


class ShopData(models.Model):
    city_id = models.ForeignKey(CityData, db_column="CityData.id")
    category_id = models.ForeignKey(CategoryData, db_column="CategoryData.id")
    name = models.CharField(max_length=255, unique=True, blank=True, null=True)
    image = models.ImageField(upload_to='shop/', default="/media/shop/default.png")
    address = models.CharField(max_length=120, blank=True, null=True)
    description = models.CharField(max_length=120, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    password = models.CharField(max_length=55, blank=False, null=False, default=0)

    def __unicode__(self):
        return str(self.name)
        #
        # def save(self, *args, **kwargs):
        #     self.city_id = self.city_name.id
        #     self.category_id = self.category_name.id
        #     super(ShopData, self).save(*args, **kwargs)
