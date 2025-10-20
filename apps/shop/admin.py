from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Product, ProductImage

admin.site.site_header = "Панель управления магазином"
admin.site.site_title = "Магазин"
admin.site.index_title = "Администрирование магазина"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ["name"]
    ordering = ["name"]


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["image_tag", "name", "price", "available", "category"]
    list_filter = ["available", "category", "brand", "color", "size", "age_group"]
    search_fields = ["name", "description", "brand", "color", "size"]
    list_editable = ["price", "available"]
    ordering = ["name"]

    readonly_fields = ["image_tag"]
    inlines = [ProductImageInline]

    def image_tag(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="50" height="50" style="object-fit: cover; border-radius: 6px;"/>',
                obj.image.url,
            )
        return "-"

    image_tag.short_description = "Изображение"
