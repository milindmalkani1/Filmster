from django.views.generic.base import TemplateView
from django.shortcuts import render, redirect
from .forms import PortfolioForm

class PortfolioCreateView(TemplateView):
    template_name = 'portfolio/portfolio_form.html'

    def get(self, request):
        form = PortfolioForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = PortfolioForm(request.POST)  # fill the form with the data received using request.POST
        if form.is_valid():
            portfolio = form.save(commit=False)
            portfolio.user = request.user
            portfolio.save()

            form.cleaned_data['portfolio']
        else:                                   #error in the form if the entered input is not valid
            print(form.errors)

        args = {'form': form}
        return render(request, self.template_name, args)

def load_states(request):
    country_id = request.GET.get('country')
    states = State.objects.filter(country_id=country_id).order_by('country_name')
    return render(request, 'portfolio/state_dropdown_list_options.html', {'states': states})
