from django.contrib import admin
from .models import Category
# Register your models here.
class categoriesAdmin(admin.ModelAdmin):
    search_fields=('title',)
admin.site.register(Category,categoriesAdmin)