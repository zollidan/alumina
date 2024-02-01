from django.db import models

# class Categorie(models.Model):
#     category_title = models.CharField(max_length=255)
#     category_name = models.CharField(max_length=255)

class categories(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_title = models.CharField(max_length=255)
    category_name = models.CharField(max_length=255)

class coatings(models.Model):
    coating_id = models.AutoField(primary_key=True)
    coating_category = models.IntegerField()
    coating_name = models.CharField(max_length=128)
    coating_vendor_code = models.CharField(max_length=128)
    coating_ral = models.CharField(max_length=128)
    coating_preview = models.CharField(max_length=255)
