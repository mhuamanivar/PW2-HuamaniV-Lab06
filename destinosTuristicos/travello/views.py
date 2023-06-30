from django.shortcuts import render
from .models import Destination

# Create your views here.

def index(request):

    dest1 = Destination()
    dest1.name = "Arequipa"
    dest1.desc = "La ciudad blanca"
    dest1.img = "destination_1.jpg"
    dest1.price = 50
    dest1.offer = False

    dest2 = Destination()
    dest2.name = "Tacna"
    dest2.desc = "La ciudad heroica"
    dest2.img = "destination_2.jpg"
    dest2.price = 70
    dest2.offer = True

    dest3 = Destination()
    dest3.name = "Piura"
    dest3.desc = "Hermosas playas"
    dest3.img = "destination_3.jpg"
    dest3.price = 90
    dest3.offer = False

    dests = [dest1, dest2, dest3]

    return render(request, 'index.html', {'dests': dests})