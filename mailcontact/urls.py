from django.urls import path, include
from .views import MailContactView, MailContactSuccessView

app_name = 'mailcontact'

urlpatterns = [
    path('', MailContactView.as_view(), name="mailcontact"),
    path('success/', MailContactSuccessView.as_view(), name="success"),
]