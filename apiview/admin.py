from django.contrib import admin
from apiview.models import Mobile

# Register your models here.
class MobileAdmin(admin.ModelAdmin):
	list_display = ['id','brand','model_no', 'ram', 'rom', 
				    'screen', 'front_camera', 'rear_camera',]

admin.site.register(Mobile, MobileAdmin)