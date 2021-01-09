from django import forms
from portfolio.models import Portfolio, State

class PortfolioForm(forms.ModelForm):
    # country = forms.CharField(
    #                 widget=forms.Select(
    #                         attrs={
    #                                 "id": "country"
    #                         }
    #                     )
    #                 )
    # state = forms.CharField(
    #                 widget=forms.Select(
    #                         attrs={
    #                                 "id": "state"
    #                         }
    #                     )
    #                 )
    # city = forms.CharField(
    #                 widget=forms.Select(
    #                         attrs={
    #                                 "id": "city"
    #                         }
    #                     )
    #                 )
    # phone = forms.CharField()

    class Meta:
        model = Portfolio
        fields = ('country', 'state', 'phone',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['state'].queryset = State.objects.none()
