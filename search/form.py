from django import forms



class FilterForm(forms.Form):

    min_price =  forms.Decimal('min_price')
    max_price =  Decimal(request.POST.get('max_price'))
   # <input value="-2000" min="-2000" max="2020" step="20" type="range" name="min_year">
    min_year = RangeSliderField(minimum=30,maximum=300,step=20,value=-2000,name="min_year")
    max_year = RangeSliderField(minimum=30,maximum=300,step=20,value=2020,name="min_year")
    
    artifact_origin = request.POST.get('artifact_origin')
    
    credit_card_number = forms.CharField(label='Credit card number', required=False)
    cvv = forms.CharField(label='Security code (CVV)', required=False)
    expiry_month = forms.ChoiceField(label='Month', choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(label='Year', choices=YEAR_CHOICES, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = (
            'full_name', 'phone_number', 'country', 'postcode',
            'town_or_city', 'street_address1', 'street_address2'
        )