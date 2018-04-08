from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from .models import Glossary, User, Domain, Raci

def glossary(request):
    names = Glossary.objects.order_by('-date_created')[:100]
    context = {'names': names}
    return render(request, 'glossary/index.html', context)

def element_detail(request, element_name):
    names = get_object_or_404(Glossary)
    context = {'names': names}
    return render(request, 'glossary/element_detail.html', context)
