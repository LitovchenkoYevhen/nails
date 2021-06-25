from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from .models import Category, Cleaning, Visit, VisitAsk
from django.views.generic import ListView, DetailView, CreateView
from services.forms import VisitAskForm, UserRegisterForm, UserLoginForm, ContactForm
# from django.urls import reverse_lazy
from django.db.models import Count
from services.utils import MyMixin
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.core.paginator import Paginator
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def send_message(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            mail = send_mail(form.cleaned_data['subject'], form.cleaned_data['content'], 'krisnails@ukr.net',
                             ['litovchenkoyevhen@gmail.com', ], fail_silently=True)
            if mail:
                messages.success(request, 'Письмо отправлено!')
                return redirect('services:contact')
            else:
                messages.error(request, 'Ошибка отправки')
        else:
            messages.error(request, 'Ошибка ввода')
    else:
        form = ContactForm()
    return render(request, 'services/contact.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('services:login')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('services:home')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'services/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('services:home')
    else:
        form = UserLoginForm()
    return render(request, 'services/login.html', {'form': form})


class HomeServices(ListView):
    model = Visit
    template_name = 'services/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        context['list_of_photos'] = Visit.objects.filter(is_published=True, photo_after__contains='jpg')
        return context


class Prices(MyMixin, ListView):  # для демонстрации работы миксина 42
    model = Category
    template_name = 'services/prices.html'
    mixin_prop = 'hello world'  # для демонстрации работы миксина 42

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mixin_prop'] = self.get_prop()  # для демонстрации работы миксина 42
        context['service_list'] = Category.objects.filter(is_published=True)
        return context


def show_contacts(request):
    return render(request, 'services/contacts.html', {'title': 'Контакты'})


class CleaningList(ListView):
    model = Cleaning
    context_object_name = 'cleaning_list'
    template_name = 'services/cleaning_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = Cleaning.objects.get(step_name='ЗАГОЛОВОК')
        context['title'] = 'Стерилизация'
        return context

    def get_queryset(self):
        return get_list_or_404(Cleaning, is_published=True)


class AllVisits(ListView):
    model = Visit
    context_object_name = 'visits_list'
    template_name = 'services/visits_list.html'
    paginate_by = 6

    def get_queryset(self):
        return Visit.objects.filter(is_published=True, photo_after__contains='jpg', category__is_published=True)


def show_visit(request, visit_pk):
    visit = get_object_or_404(VisitAsk, pk=visit_pk)  # VisitAsk.objects.get(pk=visit_pk)
    return render(request, 'services/show_visit.html', {'visit': visit})


class CreateVisit(CreateView):
    form_class = VisitAskForm
    template_name = 'services/make_appointment.html'
    # success_url = reverse_lazy('services:prices')
    extra_context = {'title': 'Запись на маникюр'}


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
        return Visit.objects.filter(category_id=self.kwargs['category_id'], is_published=True,
                                    photo_after__contains='jpg')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        # context['visits_list'] = Visit.objects.filter(category_id=self.kwargs['category_id'], is_published=True)
        return context


class Statistic(LoginRequiredMixin, ListView):
    model = Category
    context_object_name = 'statistic'
    template_name = 'services/statistic.html'
    raise_exception = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cats'] = Category.objects.annotate(cnt=Count('visit'))
        context['title'] = 'Статистика'
        return context
