from django.urls import path
from .views import PortfolioCreateView

app_name = "portfolio"

urlpatterns = [
    path('create-portfolio/', PortfolioCreateView.as_view(),
        name='create_portfolio'),

    #path('ajax/load-states/', views.load_states, name='ajax_load_states'),
]
