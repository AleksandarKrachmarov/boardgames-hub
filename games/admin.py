from django.contrib import admin

from games.models import BoardGame


# Register your models here.
@admin.register(BoardGame)
class BoardGameAdmin(admin.ModelAdmin):
    pass