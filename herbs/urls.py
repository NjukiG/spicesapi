from django.urls import path
from .views import HerbsList, HerbsDetail

urlpatterns = [
path("<int:pk>/", HerbsDetail.as_view(), name="herbs_detail"),
path("", HerbsList.as_view(), name="herbs_list"),
]