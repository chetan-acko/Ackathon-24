from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

from .models import ConfigurableDataTable

class ProviderForm(forms.ModelForm):
    class Meta:
        model = ConfigurableDataTable
        fields = '__all__'

    # Define validators for the 'interest_rate' field
    intrest_rate = forms.DecimalField(
        validators=[MinValueValidator(5.0), MaxValueValidator(10.0)]
    )
