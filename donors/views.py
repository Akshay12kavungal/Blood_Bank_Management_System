from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login,logout
from django.contrib.auth.views import LoginView

from .forms import DonorForm, PatientForm, SignUpForm
from .models import Donor, Patient

# Home view
class HomeView(ListView):
    template_name = 'home.html'
    model = Donor
    context_object_name = 'donors'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['patients'] = Patient.objects.all()
        return context


# Donor views
class DonorListView(LoginRequiredMixin, ListView):
    model = Donor
    template_name = 'donors/donor_list.html'
    context_object_name = 'donors'


class DonorCreateView(LoginRequiredMixin, CreateView):
    model = Donor
    form_class = DonorForm
    template_name = 'donors/donor_form.html'
    success_url = reverse_lazy('donor_list')

    def form_valid(self, form):
        donor_instance = form.save(commit=False)
        donor_instance.save()
        return super().form_valid(form)

class DonorUpdateView(LoginRequiredMixin, UpdateView):
    model = Donor
    form_class = DonorForm
    template_name = 'donors/donor_form.html'
    success_url = reverse_lazy('donor_list')


class DonorDeleteView(LoginRequiredMixin, DeleteView):
    model = Donor
    template_name = 'donors/donor_confirm_delete.html'
    success_url = reverse_lazy('donor_list')


class DonorDetailView(LoginRequiredMixin, DetailView):
    model = Donor
    template_name = 'donors/donor_detail.html'
    context_object_name = 'donor'


# Patient views
class PatientListView(LoginRequiredMixin, ListView):
    model = Patient
    template_name = 'patient/patient_list.html'
    context_object_name = 'patients'


class PatientCreateView(LoginRequiredMixin, CreateView):
    model = Patient
    form_class = PatientForm
    template_name = 'patient/patient_form.html'
    success_url = reverse_lazy('patient_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PatientUpdateView(LoginRequiredMixin, UpdateView):
    model = Patient
    form_class = PatientForm
    template_name = 'patient/patient_form.html'
    success_url = reverse_lazy('patient_list')


class PatientDeleteView(LoginRequiredMixin, DeleteView):
    model = Patient
    template_name = 'patient/patient_confirm_delete.html'
    success_url = reverse_lazy('patient_list')


class PatientDetailView(LoginRequiredMixin, DetailView):
    model = Patient
    template_name = 'patient/patient_detail.html'
    context_object_name = 'patient'


# Registration and login views
class SignUpView(View):
    form_class = SignUpForm
    initial = {'key': 'value'}
    template_name = 'registration/signup.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')

        return render(request, self.template_name, {'form': form})

class LoginView(LoginView):
    template_name = 'registration/login.html'

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return redirect('home')

class CustomLogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect(reverse('login'))