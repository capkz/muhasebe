from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import redirect, get_object_or_404
from .forms import ogrenci_arama
from onkayit.models import ogrenci

def ogrenci_listesi(request):
    if request.method == 'GET':
        query = request.GET.get('q',)
        if query == '':
            return redirect('ogrenci_listesi',)
        ogrenci_detay = get_object_or_404(ogrenci, pk=query)
        return render(request, 'ogrenci/ogrenci_arama.html' ,{'ogrenci': ogrenci_detay})
    return render(request, 'ogrenci/ogrenci_listesi.html')
