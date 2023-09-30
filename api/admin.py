from django.contrib import admin
from .models import Banklist, Branch, Bank

# Register your models here.
@admin.register(Banklist)
class BankListAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'Branch_List']

@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ['id', 'ifsc', 'branch', 'address', 'city', 'district', 'state', 'bank_name']