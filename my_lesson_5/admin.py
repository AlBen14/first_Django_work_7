from django.contrib import admin
from .models import Advertisment

# Register your models here.

class AdvertismentAdmin(admin.ModelAdmin):
    list_display=["id","title","description","price","author","created_date","updated_date","action","photo_img"]
    list_filter=["action"]
    actions=["forbid_the_auction"]
    # fieldsets=(
    # ('Общее',{
    # 'fields':('title','description'),
    # 'classes':["collapse"]
    # }),
    # )
    # в list_display надо написать только то что есть здесь(но не факт)

    @admin.action(description="убрать возможность торга")
    def forbid_the_auction(self,request,queryset):
        queryset.update(action=False)

admin.site.register(Advertisment,AdvertismentAdmin)