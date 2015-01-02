from django.contrib import admin

# Register your models here.
from .models import Todo, TodoArticulo
admin.site.register(Todo)
admin.site.register(TodoArticulo) 
