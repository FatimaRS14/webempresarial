from django.urls import path
from . import views

urlpatterns = [
    path('<int:page_id>/<slug:page_slug>/', views.page, name="page"),
]
#Se pondra de esta manera para poder acceder rapidamente a la página correspondiente que nos pondra el número 
