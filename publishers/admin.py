from django.contrib import admin

from publishers.models import Publisher


# Register your models here.
@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    pass