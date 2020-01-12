
# Register your models here.

from django.contrib import admin
from django import forms

from .models import Product, Service, New

class ProductForm(forms.ModelForm ):
    desc = forms.CharField(widget=forms.Textarea)
 
    class Meta:
        model = Product
        fields = '__all__'
 
class ProductAdmin(admin.ModelAdmin):
    form = ProductForm

class NewForm(forms.ModelForm ):
    details = forms.CharField(widget=forms.Textarea)
 
    class Meta:
        model = New
        fields = '__all__'
 
class NewAdmin(admin.ModelAdmin):
    form = NewForm

admin.site.register(Product, ProductAdmin)
admin.site.register(Service, ProductAdmin)
admin.site.register(New, NewAdmin)
