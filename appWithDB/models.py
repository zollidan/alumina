from django.db import models

class categories(models.Model):

    category_title = models.CharField(max_length=255)
    category_name = models.CharField(max_length=255)

class coatings(models.Model):
    
    coating_category = models.IntegerField()
    coating_name = models.CharField(max_length=128)
    coating_vendor_code = models.CharField(max_length=128)
    coating_ral = models.CharField(max_length=128)
    coating_preview = models.CharField(max_length=255)

class orders(models.Model):
    
    order_user_id = models.IntegerField()
    order_user_name = models.CharField(max_length=128) 
    order_user_phone = models.CharField(max_length=64)
    order_user_email = models.CharField(max_length=128)
    order_price = models.FloatField()

class panel_size(models.Model):
    
    panel_size_category = models.IntegerField()
    panel_size_vendor_code = models.CharField(max_length=128)
    panel_size_size = models.CharField(max_length=128)

class panel_thickness(models.Model):
    
    panel_thickness_category = models.IntegerField()
    panel_thickness_vendor_code = models.CharField(max_length=128)
    panel_thickness_thickness = models.FloatField()

class layer_thickness(models.Model):
    layer_thickness_category = models.IntegerField()
    layer_thickness_vendor_code = models.CharField(max_length=128)
    layer_thickness_thickness = models.FloatField()

