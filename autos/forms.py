from django.forms import ModelForm

from autos.models import Makes


class MakeForm(ModelForm):
    class Meta:
        model = Makes
        fields = '__all__'
