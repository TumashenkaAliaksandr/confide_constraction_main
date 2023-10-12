from django.shortcuts import render
from webapp.models import ServicesSlider


def index(request):
    """Main, index constr"""
    return render(request, 'webapp/main/index-2.html')



def services_slider(request):
    """Main, index constr"""
    services_sliders = ServicesSlider.objects.all().prefetch_related('services_sliders')

    context = {
        'servis_sliders': services_sliders,
    }
    return render(request, 'webapp/main/index-2.html', context)
