from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from django.contrib.auth.admin import UserAdmin
from authorization.models import Account

class AccountAdmin(UserAdmin):
    list_display = ('email', 'date_joined', 'last_login')
    search_fields = ('email',)
    readonly_fields = ('id', 'date_joined')
    
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Account, AccountAdmin)
