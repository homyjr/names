from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import to_language
from .models import Name


def index(request):
    
    if request.method == 'POST':
        name = request.POST.get('entername')
        Name.objects.create(student_name=name)
    names = Name.objects.all()

    return render(request, 'polls/index.html', {'names':names})


