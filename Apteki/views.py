from django.shortcuts import render, get_object_or_404

from .models import Lekarstv
from Dj_Learn_start.forms import OrderForm


# Create your views here.
def list(request):
    lekarstvL = Lekarstv.objects.all()
    return render(request, "lekarstv/lekarstv_list.html", {"lekarstvL": lekarstvL})

def detail(request, lekarstv_id):
    form = OrderForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            name_lekarstvo = form.cleaned_data['name']
            #form.save()


    lekarstvD = get_object_or_404(Lekarstv, id=lekarstv_id)
    return render(request, "lekarstv/lekarstv_detail.html", {
        "lekarstvD": lekarstvD,
        "form": form,
    })
