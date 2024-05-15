from django.contrib import admin
from .models import Usermanage, UserEducation,UserLog,Books,PrintShop
# Register your models here.

admin.site.register(Usermanage)
admin.site.register(UserEducation)
admin.site.register(Books)
admin.site.register(PrintShop)