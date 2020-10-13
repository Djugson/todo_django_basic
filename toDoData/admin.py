from django.contrib import admin
from .models import ToDo

class ToDoAdmin(admin.ModelAdmin):
	readonly_field =  ['created_date',]

# Register your models here.
admin.site.register(ToDo, ToDoAdmin)
