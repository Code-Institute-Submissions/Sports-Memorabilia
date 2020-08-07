from django.contrib import admin

from .models import League, Team, Merchandise

# Register your models here.


class MerchandiseAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'team',
        'league',
        'year',
        'price',
        'description',
        'image',
    )

    ordering = ('sku',)


class LeagueAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


class TeamAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'league',
        'nickname',
        'image'
    )

admin.site.register(Merchandise, MerchandiseAdmin)
admin.site.register(League, LeagueAdmin)
admin.site.register(Team, TeamAdmin)