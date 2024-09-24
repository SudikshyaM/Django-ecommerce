from django.contrib import admin
from .models import *
# Register your models here.

class ChaiReviewInline(admin.TabularInline):
    model=ChaiReview
    extra=2

class ChaiAdmin(admin.ModelAdmin):
    list_display=('name','types','date')
    inlines=[ChaiReviewInline]

class StoreAdmin(admin.ModelAdmin):
    list_display=('name','location')
    filter_horizontal=('chai_varieties',)

class ChaiCertificateAdmin(admin.ModelAdmin):
    list_display=('chai','certificate_number')

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Chai,ChaiAdmin)
# admin.site.register(ChaiReview,ChaiReviewInline)
admin.site.register(Store,StoreAdmin)
admin.site.register(Cerificate,ChaiCertificateAdmin)