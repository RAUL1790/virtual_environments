from django.contrib import admin
from todo.models import Todo, TodoArticulo
# Register your models here.
class TodoArticuloAdmin(admin.TabularInline):
	model = TodoArticulo
	extra = 1

class TodoAdmin(admin.ModelAdmin):
	inlines = [TodoArticuloAdmin]	

admin.site.register(Todo,TodoAdmin)
admin.site.register(TodoArticulo)