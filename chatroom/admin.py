from django.contrib import admin
from .models import Room, Message

# Register your models here.

class TaskInline(admin.TabularInline):
    model = Message
    extra = 3

class RoomAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Room",{'fields': ['room_name']}),
    ]
    inlines = [TaskInline]

admin.site.register(Room, RoomAdmin)