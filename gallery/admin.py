from django.contrib import admin
from .models import PhotoItem, PurchaseLog

class PhotoItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'photo_price', 'phone_number', 'phone_price', 'is_active')
    list_editable = ('photo_price', 'phone_number', 'phone_price', 'is_active')
    search_fields = ('title', 'phone_number')

admin.site.register(PhotoItem, PhotoItemAdmin)
admin.site.register(PurchaseLog)