from django.contrib import admin
from .models import Department, Course, Purpose, Material


# Register your models here.
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Department, DepartmentAdmin)


class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug','top']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Course, CourseAdmin)


class PurposeAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Purpose, PurposeAdmin)


class MaterialAdmin(admin.ModelAdmin):
    list_display = ['slug', 'name', 'price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Material, MaterialAdmin)
