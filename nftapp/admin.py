
from django.contrib import admin
from .models import NFTRelease

@admin.register(NFTRelease)
class NFTReleaseAdmin(admin.ModelAdmin):
	list_display = ("name", "launch_date")
