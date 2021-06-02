from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from .models import Category, Cleaning, Visit, VisitAsk
from django.views.generic import ListView
from services.forms import VisitAskForm


class HomeServices(ListView):
    model = Visit
    template_name = 'services/home_services_list.html'
    context_object_name = 'photos_list'


# def index(request):
#     photos_list = Visit.objects.all()
#     context = {'photos_list': photos_list}
#     return render(request, 'services/index.html', context)


def show_prices(request):
    services = Category.objects.order_by('-price')
    context = {'service_list': services}
    return render(request, 'services/prices.html', context)


def show_contacts(request):
    return render(request, 'services/contacts.html')


def show_cleaning(request):
    header = get_object_or_404(Cleaning, step_name='ЗАГОЛОВОК') # Cleaning.objects.get(step_name='ЗАГОЛОВОК') #get_list_or_404(Cleaning, step_name='ЗАГОЛОВОК')
    cleaning_list = get_list_or_404(Cleaning)
    context = {'cleaning_list': cleaning_list, 'header': header}
    return render(request, 'services/cleaning_list.html', context)


def show_works(request):
    works_list = Visit.objects.filter(is_published=True)
    context = {'works_list': works_list}
    return render(request, 'services/works_list.html', context)


def show_visit(request, visit_pk):
    visit = get_object_or_404(VisitAsk, pk=visit_pk) # VisitAsk.objects.get(pk=visit_pk)
    return render(request, 'services/show_visit.html', {'visit': visit})


def make_appointment(request):
    if request.method == 'POST':
        form = VisitAskForm(request.POST)
        if form.is_valid():
            visit_ask = VisitAsk.objects.create(**form.cleaned_data)
            return redirect(visit_ask)
    else:
        form = VisitAskForm()
    return render(request, 'services/make_appointment.html', {'form': form})

def show_work(request, work_pk):
    work = Visit.objects.get(pk=work_pk)
    return render(request, 'services/show_work.html', {'work': work})