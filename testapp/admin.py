from django.contrib import admin
from testapp.models import hydjobs, blorejobs, chennaijobs, punejobs, noidajobs, indorejobs

# Register your models here.


class hydjobsAdmin(admin.ModelAdmin):
    list_display = ['date', 'company', 'title',
                    'eligibility', 'address', 'email', 'phonenumber']


class blorejobsAdmin(admin.ModelAdmin):
    list_display = ['date', 'company', 'title',
                    'eligibility', 'address', 'email', 'phonenumber']


class chennaijobsAdmin(admin.ModelAdmin):
    list_display = ['date', 'company', 'title',
                    'eligibility', 'address', 'email', 'phonenumber']


class punejobsAdmin(admin.ModelAdmin):
    list_display = ['date', 'company', 'title',
                    'eligibility', 'address', 'email', 'phonenumber']


class noidajobsAdmin(admin.ModelAdmin):
    list_display = ['date', 'company', 'title',
                    'eligibility', 'address', 'email', 'phonenumber']

class indorejobsAdmin(admin.ModelAdmin):
    list_display = ['date', 'company', 'title',
                    'eligibility', 'address', 'email', 'phonenumber']


admin.site.register(hydjobs, hydjobsAdmin)
admin.site.register(chennaijobs, chennaijobsAdmin)
admin.site.register(blorejobs, blorejobsAdmin)
admin.site.register(punejobs, punejobsAdmin)
admin.site.register(noidajobs, noidajobsAdmin)
admin.site.register(indorejobs, indorejobsAdmin)
