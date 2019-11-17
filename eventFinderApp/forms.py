from django.forms import ModelForm
from django.contrib.admin import widgets
from .models import Event, Category
from django.forms import ModelForm, SplitDateTimeField

class EventForm(ModelForm):
    start_time = SplitDateTimeField(widget=widgets.AdminSplitDateTime())
    end_time = SplitDateTimeField(widget=widgets.AdminSplitDateTime())


    class Meta:
        model = Event
        fields = ["title", "location", "venue", "start_time", "end_time", "categories"]
