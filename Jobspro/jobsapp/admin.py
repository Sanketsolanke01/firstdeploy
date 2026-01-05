from django.contrib import admin
from .models import Bangjobs,Punejobs,Biharjobs

# Register your models here.

class BangAdmin(admin.ModelAdmin):
    list_display=['date','company','title','address','salary','email','phone']
    
admin.site.register(Bangjobs,BangAdmin)


class PuneAdmin(admin.ModelAdmin):
    list_display=['date','company','title','address','salary','email','phone']
    
admin.site.register(Punejobs,PuneAdmin)


class BiharAdmin(admin.ModelAdmin):
    list_display=['date','company','title','address','salary','email','phone']
    
admin.site.register(Biharjobs,BiharAdmin)
    
    