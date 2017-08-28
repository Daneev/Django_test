from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from .models import Lekarstv
from Dj_Learn_start.forms import OrderForm


# Create your views here.
def list(request):
    lekarstvL = Lekarstv.objects.all()
    return render(request, "lekarstv/lekarstv_list.html", {"lekarstvL": lekarstvL})

def detail(request, lekarstv_id):
    form = OrderForm(request.POST or None)
    lekarstvD = get_object_or_404(Lekarstv, id=lekarstv_id)
    if request.method == "POST":
        if form.is_valid():
            name_lekarstvo = form.cleaned_data['name']
            #form.save()
            return HttpResponseRedirect('{}?sent=True'.format(reverse("detail", kwargs={'lekarstv_id': lekarstvD.id})))

    return render(request, "lekarstv/lekarstv_detail.html", {
        "lekarstvD": lekarstvD,
        "form": form,
        "sent": request.GET.get('sent', False)
    })
