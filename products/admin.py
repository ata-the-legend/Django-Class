from django.contrib import admin
from .models import Product, Image, Comment, Answer,\
                    ProductOption, ProductPrice, Category, Question
# Register your models here.


class ImageInline(admin.TabularInline):
    model = Image
    extra = 2
    max_num = 5

class ProductPriceInline(admin.TabularInline):
    model = ProductPrice
    max_num = 1
    min_num = 1

class ProductOptionInline(admin.TabularInline):
    model = ProductOption
    extra = 2


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'en_name', 'name', 'category']
    list_filter = ['category'] # ro gesmatayi bayad gozasht ke mahdudiyat dare
    search_fields = ['en_name', 'name']
    inlines = [
        ImageInline,
        ProductPriceInline,
        ProductOptionInline,
    ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug', 'parent']
    list_filter = ['parent']
    search_fields =['name', 'description']
    fieldsets = (
        ('details', {
            "fields": (
                ('name', 'slug'),
                ('description',),
            )
        }),
        ('images', {
            "fields": (
                ('icon',),
                ('image',),
            )
        }),
        ('parent', {
            "fields": (
                ('parent',),
            )
        }),
    )
    

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    pass

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 1

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass

@admin.register(ProductPrice)
class ProductPriceAdmin(admin.ModelAdmin):
    pass

@admin.register(ProductOption)
class ProductOptionAdmin(admin.ModelAdmin):
    pass
