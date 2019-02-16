from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('updateprofile/<int:pk>', views.UpdateProfile.as_view(), name='updateprofile'),
    path('newpet/', views.PetCreate.as_view(), name='newpet'),
    path('updatepet/<int:pk>', views.PetUpdate.as_view(), name='updatepet'),
    path('delpet/<int:pk>', views.PetDelete.as_view(), name='delpet'),

]
