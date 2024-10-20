from django.contrib import admin
from .models import Product
from django.utils.html import format_html


class MemberAdmin(admin.ModelAdmin):
    list_display = ("name", 'image_tag',)
    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(obj.image.url))


admin.site.register(Product, MemberAdmin)