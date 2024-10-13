from django.contrib import admin, messages
from django.utils.html import format_html
from .models import Company, Product


@admin.action(description="Обнуление задолженности")
def reset_debt(modeladmin, request, queryset):
    """Очищает задолженность у выбранных объектов"""
    queryset.update(debt_to_supplier=0)


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'level',
        'debt_to_supplier',
        'city',
        'created_at',
        'supplier_link',
    )
    list_filter = ('city',)
    actions = [reset_debt]

    def supplier_link(self, obj):
        if obj.supplier:
            url = f"/admin/elsalnet/company/{obj.supplier.id}/change/"
            return format_html(f'<a href="{url}">{obj.supplier.title}</a>')
        return "-"
    supplier_link.short_description = 'Поставщик'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'model', 'release_date')
    list_filter = ('title',)


