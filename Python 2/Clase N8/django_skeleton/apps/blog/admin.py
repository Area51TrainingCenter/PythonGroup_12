from django.contrib import admin
from .models import Category, Post, Footer, FooterSocialNet, Tag


class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)


class CategoryAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'user':
            kwargs['initial'] = request.user.id
        return super(CategoryAdmin, self).formfield_for_foreignkey(db_field,
                                                             request,
                                                             **kwargs)

    list_display = ('name', 'user', 'created', 'mod')


class PostAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'user':
            kwargs['initial'] = request.user.id
        return super(PostAdmin, self).formfield_for_foreignkey(db_field,
                                                               request,
                                                               **kwargs)
    list_display = ('name', 'user', 'created', 'mod', 'category')


class FooterSocialNetinline(admin.StackedInline):
    model = FooterSocialNet
    #form = ContactForm
    extra = 0
    max_num = 5


class FooterAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

    inlines = [FooterSocialNetinline]


admin.site.register(Tag, TagAdmin)
admin.site.register(Footer, FooterAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
