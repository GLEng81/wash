from django.contrib import admin
from colector.models import Station, Error, OnlineStations, NewConfig, Emails

# Register your models here.


class StationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class ErrorAdmin(admin.ModelAdmin):
    list_display = ('station', 'msg', 'time', 'is_sent')


class OnlineStationsAdmin(admin.ModelAdmin):
    list_display = ('station', 'last_request', 'new_config', 'info')


class NewConfigAdmin(admin.ModelAdmin):
    list_display = ('station', 'is_get', 'out1', 'out2', 'out3', 'status')


class EmailsAdmin(admin.ModelAdmin):
    list_display = ('station', 'email')

admin.site.register(Station, StationAdmin)
admin.site.register(Error, ErrorAdmin)
admin.site.register(OnlineStations, OnlineStationsAdmin)
admin.site.register(NewConfig, NewConfigAdmin)
admin.site.register(Emails, EmailsAdmin)

