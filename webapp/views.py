from django.shortcuts import render

def index(request):
    """Main, index constr"""
    return render(request, 'webapp/main/index-2.html')
