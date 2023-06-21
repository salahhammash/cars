from django.contrib import admin
# from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import Car
# from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomCarsAdmin(admin.ModelAdmin):
    
    model = Car
    list_display = ['name', 'price', 'desc', 'purchaser',]
    fieldsets= (
        ('Owner',{
            'fields':('purchaser',
            )}
        ),
        ('Cars info',{
            'fields':('name','desc','price'
            )}
        )
    )
admin.site.register(Car, CustomCarsAdmin)