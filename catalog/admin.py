from django.contrib import admin

# Register your models here.
from .models import Position, Employee, Department

admin.site.register(Position)
admin.site.register(Employee)
admin.site.register(Department)

from .models import Station, StationSequence, Busline

@admin.register(Station)
class StationAdmin(admin.ModelAdmin):
    list_display = ('id', 'sName', 'status', 'latitude', 'longitude')  # 确保这些字段存在于Station模型中
    search_fields = ('sName',)  # 添加搜索功能

@admin.register(Busline)
class BuslineAdmin(admin.ModelAdmin):
    list_display = ('lineNumber', 'startTime','status' ,'endTime', 'Price', 'description')  # 显示Busline的字段
    search_fields = ('lineNumber', 'description')  # 可以搜索的字段

@admin.register(StationSequence)
class StationSequenceAdmin(admin.ModelAdmin):
    list_display = ('id', 'station', 'busline', 'order')  # 显示StationSequence的字段
    search_fields = ('station__sName',)  # 允许通过站点名称搜索




