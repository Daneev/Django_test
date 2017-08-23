from django.shortcuts import render, get_object_or_404
from Apteki.models import Lekarstv

# Create your views here.
def list(request):
    lekarstvL = Lekarstv.objects.all()
    return render(request, "lekarstv/lekarstv_list.html", {"lekarstvL": lekarstvL})

def detail(request, lekarstv_id):
    lekarstvD = get_object_or_404(Lekarstv, id=lekarstv_id)
    return render(request, "lekarstv/lekarstv_detail.html", {"lekarstvD": lekarstvD})
