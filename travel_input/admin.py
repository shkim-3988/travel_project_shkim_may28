from django.contrib import admin
from .models import (
    Schedule, Destination,
    TravelPurpose, TravelStyle, ImportantFactor,
    TransportationMode, TransportationCategory,
    PreferredWeather, WeatherCategory,
    Destination, Activity
)

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active', 'order']
    list_filter = ['is_active']
    search_fields = ['name']
    ordering = ['order', 'name']

@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ['name', 'city', 'is_active', 'order']
    list_filter = ['city', 'is_active']
    search_fields = ['name', 'city__name']
    ordering = ['city', 'order', 'name']

@admin.register(TransportationCategory)
class TransportationCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'order']
    search_fields = ['name']
    ordering = ['order', 'name']

@admin.register(TransportationMode)
class TransportationModeAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'order']
    list_filter = ['category']
    search_fields = ['name', 'category__name']
    ordering = ['category', 'order', 'name']

@admin.register(TravelPurpose)
class TravelPurposeAdmin(admin.ModelAdmin):
    list_display = ['name', 'order']
    search_fields = ['name']
    ordering = ['order', 'name']

@admin.register(TravelStyle)
class TravelStyleAdmin(admin.ModelAdmin):
    list_display = ['name', 'order']
    search_fields = ['name']
    ordering = ['order', 'name']

@admin.register(ImportantFactor)
class ImportantFactorAdmin(admin.ModelAdmin):
    list_display = ['name', 'order']
    search_fields = ['name']
    ordering = ['order', 'name']

@admin.register(WeatherCategory)
class WeatherCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'order']
    search_fields = ['name']
    ordering = ['order', 'name']

@admin.register(PreferredWeather)
class PreferredWeatherAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'order']
    list_filter = ['category']
    search_fields = ['name', 'category__name']
    ordering = ['category', 'order', 'name']

@admin.register(TransportationCategory)
class TransportationCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(TransportationMode)
class TransportationModeAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']
    list_filter = ['category']
    search_fields = ['name', 'category__name']
    fields = ['category', 'name']

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
<<<<<<< HEAD
    list_display = ('title', 'destination', 'start_date', 'end_date', 'display_transportation_mode', 'created_at')
    list_filter = ('start_date', 'end_date')
    search_fields = ('title', 'destination__name')
    filter_horizontal = ('travel_purpose', 'travel_style', 'important_factors', 'transportation_mode')

    fieldsets = (
        ('기본 정보', {
            'fields': ('title', 'destination', 'start_date', 'end_date', 'budget', 'notes')
        }),
        ('카테고리', {
            'fields': ('travel_purpose', 'travel_style', 'important_factors', 'transportation_mode')
        }),
        ('기타 정보', {
            'fields': ('age_group',)
        }),
        ('AI 관련', {
            'fields': ('ai_response', 'user_feedback', 'ai_feedback_response')
        }),
    )

    def display_transportation_mode(self, obj):
        return ", ".join([mode.name for mode in obj.transportation_mode.all()])
    display_transportation_mode.short_description = "선호 교통수단"

admin.site.register(TravelPurpose)
admin.site.register(TravelStyle)
admin.site.register(ImportantFactor)

@admin.register(WeatherCategory)
class WeatherCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    list_editable = ('order',)
    search_fields = ('name',)
    ordering = ('order', 'name')

@admin.register(PreferredWeather)
class PreferredWeatherAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'order')
    list_editable = ('order',)
    list_filter = ('category',)
    search_fields = ('name', 'category__name')
    ordering = ('category__order', 'order', 'name')
    fields = ('category', 'name', 'order')
=======
    list_display = ['title', 'user', 'city', 'start_date', 'end_date', 'created_at']
    list_filter = ['city', 'start_date', 'end_date']
    search_fields = ['title', 'user__username', 'city__name']
    date_hierarchy = 'start_date'
    ordering = ['-created_at']
    filter_horizontal = ('travel_purpose', 'travel_style', 'destinations', 'activities', 'important_factors', 'transportation_mode')

admin.site.register(Destination)
admin.site.register(Activity)
>>>>>>> c894644 (허재 설문 폼 개선)
