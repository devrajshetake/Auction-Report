from django.forms import ModelForm
from .models import *

class PlayerForm(ModelForm):
    
    class Meta:
        model = Player
        fields = ("selling_price", "team")
