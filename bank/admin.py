from django.contrib import admin

from bank.models import Account

class AccountAdmin(admin.ModelAdmin):
    list_display = [
            'holder',
            'balance'
    ]

admin.site.register(Account, AccountAdmin)
