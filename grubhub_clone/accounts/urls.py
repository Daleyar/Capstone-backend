from django.urls import path
from accounts import views


urlpatterns = [
    path('<int:id>/owners', views.Owners.as_view()),
]