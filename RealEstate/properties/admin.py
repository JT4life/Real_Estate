from django.contrib import admin
from .models import properties, agent, user_request, saved


# Register your models here.

class showproperties(admin.ModelAdmin):
    list_display = ['id','type','purpose','images','address','city','state','zipCode','agent_name','area','price','available','created']
    search_fields = ['type','purpose','city','state','zipCode','price','available']
    list_filter = ['type','purpose','city','state','zipCode','price','available']

admin.site.register(properties,showproperties)

class showagent(admin.ModelAdmin):
    list_display = ['id','name','phone','email','image','office_address']
    search_fields = ['name']
    list_filter = ['name']

admin.site.register(agent,showagent)

class showuser_request(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'email', 'message','agent_name','property_id']
    search_fields = ['full_name']
    list_filter = ['full_name']


admin.site.register(user_request,showuser_request)

class showSaved(admin.ModelAdmin):
    list_display = ['user_name','property_id']

admin.site.register(saved,showSaved)
