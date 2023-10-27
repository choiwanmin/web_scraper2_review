from django.forms import ModelForm
from .models import Recommend

class ReplyCntDataForm(ModelForm):
    class Meta:
        model = Recommend
        fields = '__all__'