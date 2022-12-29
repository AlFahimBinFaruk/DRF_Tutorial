from django.urls import path
from . import views

urlpatterns = [
    path("",views.GetAllData.as_view()),
    path("add",views.AddNewData.as_view()),
    path("delete/<str:id>",views.DeleteData.as_view()),
    path("update/<str:id>",views.UpdateData.as_view())
]