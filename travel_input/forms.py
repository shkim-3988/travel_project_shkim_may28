from django import forms
from .models import (
    Schedule, Destination, TravelPurpose, TravelStyle,
    ImportantFactor, TransportationMode
)

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = [
            'title', 'destination', 'start_date', 'end_date',
            'budget', 'notes', 'travel_purpose', 'travel_style',
            'important_factors', 'transportation_mode', 'age_group'
        ]
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'notes': forms.Textarea(attrs={'rows': 4}),
            'budget': forms.NumberInput(attrs={'min': 0}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 모든 필드에 Bootstrap 클래스 추가
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            
        # ManyToMany 필드에 대한 위젯 스타일 조정
        for field_name in ['travel_purpose', 'travel_style', 'important_factors', 'transportation_mode']:
            self.fields[field_name].widget.attrs['class'] = 'form-select'
            self.fields[field_name].widget.attrs['multiple'] = 'multiple' 