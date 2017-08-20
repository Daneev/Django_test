from django.shortcuts import render, get_object_or_404
from Lekarstvo.models import Lekarstvo

# Create your views here.
def lekarstva_list(request):
    lekarstva = Lekarstvo.objects.all()
    return render(request, "lekarstva/lekarstva_list.html", {"lekarstva": lekarstva})

def lekarstvo(request, lekarstvo_id):
    lekarstvo = get_object_or_404(Lekarstvo, id=lekarstvo_id)
    return render(request, "lekarstva/lekarstvo.html", {"lekarstvo": lekarstvo})
