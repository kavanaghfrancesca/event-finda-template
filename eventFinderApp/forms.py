from django.forms import ModelForm
from django.contrib.admin import widgets
from .models import Event, Category

class EventForm(ModelForm):

    class Meta:
        model = Event
        fields = ["title", "location", "venue", "start_time", "end_time", "categories"]
        widgets = {
            'start_time': widgets.AdminSplitDateTime,
            'end_time': widgets.AdminSplitDateTime,
        }