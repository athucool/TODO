from basic_app.models import Task
from django.forms import ModelForm


class Taskform(ModelForm):
    class Meta():
        model= Task
        fields=("__all__")





