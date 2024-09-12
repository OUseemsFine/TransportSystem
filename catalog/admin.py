from django.contrib import admin

# Register your models here.
from .models import Position, Employee, Department

admin.site.register(Position)
admin.site.register(Employee)
admin.site.register(Department)

from .models import Station, StationSequence, Busline, Vehicle, VehicleInstance

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
    
@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('id', 'vModel', 'vType', 'manufacturer', 'capacity', 'description')  
    search_fields = ('vModel', 'vType', 'manufacturer')  

@admin.register(VehicleInstance)    
class VehicleInstanceAdmin(admin.ModelAdmin):
    list_display = ('plateNumber', 'vehicle', 'busline', 'last_maintenance_date', 'produce_date', 'status')
    list_filter = ('status', 'busline' ,'vehicle')
    search_fields = ('plateNumber','status', 'busline' ,'vehicle')




