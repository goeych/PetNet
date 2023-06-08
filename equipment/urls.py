from django.urls import path

from . import views

urlpatterns = [
    path('',views.equipmentPage, name='equipmentPage'),
    path('weeklymonitor/',views.weeklymonitor, name='weeklymonitor'),
    path('ListCalibrationRecord/',views.ListCalibrationRecord,name='ListCalibrationRecord'),
    path('AddCalibrationRecord/',views.AddCalibrationRecord,name='AddCalibrationRecord'),
    path('UpdateCalibrationRecord/<str:pk>/',views.UpdateCalibrationRecord,name='UpdateCalibrationRecord'),
    path('DeleteCalibrationRecord/<str:pk>/',views.DeleteCalibrationRecord,name='DeleteCalibrationRecord'),
         ]
