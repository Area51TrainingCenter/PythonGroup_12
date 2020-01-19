from django.contrib import admin
from .models import Lector, Preferencia


class PreferenciaInline(admin.StackedInline):
    model = Preferencia
    max_num = 3
    extra = 0
    verbose_name = 'Prefencias'


class Lector_admin(admin.ModelAdmin):
    list_display = ('name', 'last_name')

    list_filter = ('name',)

    inlines = [PreferenciaInline, ]

    fieldsets = (
        (None, {
            'fields': ('name', 'last_name')
        }
        ),
        ('Extra Data', {
            'fields': ('address', 'email', 'bdate')
        }),
    )


admin.site.register(Lector, Lector_admin)

