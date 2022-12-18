from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import UserCreationForm
from .models import *

User = get_user_model()

@admin.register(User)
class UserAdmin(UserAdmin):
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2')
        }),
    )

    add_from = UserCreationForm

class WorkspacesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_workspace', 'describe_workspace', 'user_id')
    list_display_links = ('id', 'user_id')
    search_fields = ('id', 'user_id')
    prepopulated_fields = {"slug":("user_id", "name_workspace")}


class ColumnsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_column', 'describe_column', 'user_id', 'id_workspace_id')
    list_display_links = ('id', 'user_id', 'id_workspace_id')
    search_fields = ('id', 'user_id', 'id_workspace_id')


class CardsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_card', 'describe_card', 'date_card', 'isdo_card', 'id_column_id', 'user_id')
    list_display_links = ('id', 'user_id', 'id_column_id')
    search_fields = ('id', 'user_id', 'id_column_id')
    list_editable = ('isdo_card',)

class MembersAdmin(admin.ModelAdmin):
    list_display = ('id', 'access_workspace', 'id_workspace_id', 'user_id')
    list_display_links = ('id', 'user_id', 'id_workspace_id')
    search_fields = ('id', 'user_id', 'id_workspace_id')
    list_editable = ('access_workspace',)


admin.site.register(Workspaces, WorkspacesAdmin)
admin.site.register(Columns, ColumnsAdmin)
admin.site.register(Cards, CardsAdmin)
admin.site.register(Members, MembersAdmin)
