from django.contrib import admin
from .models import User

@admin.register(User)
class useradmin(admin.ModelAdmin):
    list_display=('id','name','email','password')





# Register your models here.
