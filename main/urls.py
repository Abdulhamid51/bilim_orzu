from django.urls import path
from .views import *

app_name = 'main'

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("elonlar/", ReportsView.as_view(), name="report"),
    path("elon/<pk>", report_detail, name="report_detail"),
    path("yangiliklar/", NewsView.as_view(), name="news"),
    path("yangilik/<pk>", news_detail, name="news_detail"),
    path("comment/", comment, name="comment"),
]
