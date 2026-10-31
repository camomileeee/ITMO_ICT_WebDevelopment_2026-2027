from django.shortcuts import render, get_object_or_404
from .models import CarOwner

def owner_detail(request, owner_id):
    owner = get_object_or_404(CarOwner, pk=owner_id)
    return render(request, 'owner.html', {'owner': owner})