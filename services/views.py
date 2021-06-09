from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from .models import Category, Cleaning, Visit, VisitAsk
from django.views.generic import ListView, DetailView, CreateView
from services.forms import VisitAskForm
from django.urls import reverse_lazy


class HomeServices(ListView):
    model = Visit
    template_name = 'services/index.html'
    context_object_name = 'photos_list'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):
        return Visit.objects.filter(is_published=True)


class Prices(ListView):
    model = Category
    template_name = 'services/prices.html'
    context_object_name = 'service_list'

    def get_queryset(self):
        return Category.objects.filter(is_published=True)


def show_contacts(request):
    return render(request, 'services/contacts.html')


class CleaningList(ListView):
    model = Cleaning
    context_object_name = 'cleaning_list'
    template_name = 'services/cleaning_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = Cleaning.objects.get(step_name='ЗАГОЛОВОК')
        return context

    def get_queryset(self):
        return get_list_or_404(Cleaning, is_published=True)


class AllVisits(ListView):
    model = Visit
    context_object_name = 'visits_list'
    template_name = 'services/visits_list.html'

    def get_queryset(self):
        return Visit.objects.filter(is_published=True)


def show_visit(request, visit_pk):
    visit = get_object_or_404(VisitAsk, pk=visit_pk)  # VisitAsk.objects.get(pk=visit_pk)
    return render(request, 'services/show_visit.html', {'visit': visit})


class CreateVisit(CreateView):
    form_class = VisitAskForm
    template_name = 'services/make_appointment.html'
    success_url = reverse_lazy('services:prices')


# def make_appointment(request):
#     if request.method == 'POST':
#         form = VisitAskForm(request.POST)
#         if form.is_valid():
#             visit_ask = form.save()
#             return redirect(visit_ask)
#     else:
#         form = VisitAskForm()
#     return render(request, 'services/make_appointment.html', {'form': form})


# def show_work(request, work_pk):
#     work = Visit.objects.get(pk=work_pk)
#     return render(request, 'services/show_work.html', {'work': work})

# class ShowWork(ListView):
#     model = Visit
#
#     template_name = 'services/show_work.html'
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['work'] = Visit.objects.get(pk=self.kwargs['work_pk'])
#         return context

class ShowWork(DetailView):
    model = Visit
    # pk_url_kwarg = 'work_pk'
    template_name = 'services/show_work.html'


class WorksByCategory(ListView):
    model = Visit
    context_object_name = 'visits_list'
    template_name = 'services/show_works_by_category.html'

    def get_queryset(self):
        return Visit.objects.filter(category_id=self.kwargs['category_id'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        # context['visits_list'] = Visit.objects.filter(category_id=self.kwargs['category_id'], is_published=True)
        return context
