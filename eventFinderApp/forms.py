from django.forms import ModelForm
from .models import Event

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = [
            'title', 
            'location', 
            'venue', 
            'start_time',
            'end_time',
            'categories'
            ]