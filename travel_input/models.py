from django.db import models
from django.contrib.auth.models import User

class City(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        verbose_name_plural = "Cities"
        ordering = ['order', 'name']
    
    def __str__(self):
        return self.name

class Destination(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class TransportationCategory(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class TransportationMode(models.Model):
    category = models.ForeignKey(TransportationCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.category.name} - {self.name}"

class TravelPurpose(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class TravelStyle(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class ImportantFactor(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class WeatherCategory(models.Model):
    name = models.CharField(max_length=50)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order', 'name']
    
    def __str__(self):
        return self.name

class PreferredWeather(models.Model):
    category = models.ForeignKey(WeatherCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['category__order', 'order', 'name']
    
    def __str__(self):
        return f"{self.category.name} - {self.name}"

class Schedule(models.Model):
    title = models.CharField(max_length=200)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    budget = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    notes = models.TextField(blank=True)
    
    travel_purpose = models.ManyToManyField(TravelPurpose)
    travel_style = models.ManyToManyField(TravelStyle)
    important_factors = models.ManyToManyField(ImportantFactor)
    transportation_mode = models.ManyToManyField(TransportationMode)
    
    age_group = models.CharField(max_length=50, blank=True)
    
    ai_response = models.TextField(blank=True)
    user_feedback = models.TextField(blank=True)
    ai_feedback_response = models.TextField(blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title 