from django.urls import path
from .views import *

app_name = 'teachers'

urlpatterns = [
    path("", TeamView.as_view(), name="team"),
    path("boglanish/", contact, name="contact"),
    path("boglan/", get_contact, name="con")
]
