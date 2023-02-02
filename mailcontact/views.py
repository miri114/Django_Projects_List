from django.shortcuts import render
from django.views.generic import FormView, TemplateView
from .forms import MailContactForm
from django.urls import reverse_lazy



# Create your views here.

class MailContactView(FormView):
    template_name = 'mailcontact/mailcontact.html'
    form_class = MailContactForm
    success_url = reverse_lazy('mailcontact:success')

    def form_valid(self, form):
        # It calls the custom send() method we crated in forms.py file
        form.send()
        return super().form_valid(form)


class MailContactSuccessView(TemplateView):
    template_name = 'mailcontact/success.html'

