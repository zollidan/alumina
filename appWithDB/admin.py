from django.contrib import admin
from .models import *

#добавить новый не могу значит обновить надо через api через скрипт

admin.site.register(categories)
admin.site.register(coatings)
admin.site.register(panel_thickness)
admin.site.register(panel_size)
admin.site.register(orders)

admin.site.site_header = 'LeFort Designs and Tech Inc.'

