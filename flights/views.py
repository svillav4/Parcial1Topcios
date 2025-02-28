from django.views.generic import TemplateView, ListView, CreateView
from django.urls import reverse
from django.db.models import Avg
from .models import Flight
from .forms import FlightForm

class HomePageView(TemplateView):
    template_name = 'home.html'

class RegisterPageView(CreateView):
    model = Flight
    form_class = FlightForm
    template_name = 'register.html'
    
    def get_success_url(self):
        return reverse('list')

class ListPageView(ListView):
    model = Flight
    template_name = 'list.html'
    context_object_name = 'flights'
    ordering = ['price']

class StatsPageView(TemplateView):
    template_name = 'stats.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_nacionales'] = Flight.objects.filter(typee="Nacional").count()
        context['total_internacionales'] = Flight.objects.filter(typee="Internacional").count()
        context['precio_promedio'] = round(
            Flight.objects.filter(typee="Nacional").aggregate(Avg('price'))['price__avg'] or 0, 2
        )
        return context