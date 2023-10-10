from django.shortcuts import render
from webapp.models import ServicesSlider


def index(request):
    """Main, index constr"""
    return render(request, 'webapp/main/index-2.html')


def services_slider(request):
    """Main, index constr"""
    servis_slider = ServicesSlider.objects.all()
    main_ser = ServicesSlider.objects.filter(is_main=True).first()

    context = locals()
    return render(request, 'webapp/main/index-2.html', context)
