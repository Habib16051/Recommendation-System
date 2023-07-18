from django.urls import path
from . import views


# app_name = 'website_api'
urlpatterns = [
    path('', views.CompanyListAPIView.as_view(), name='list_apiview'),
    path('<int:pk>/', views.CompanyRetrieveUpdateDestroyAPIView.as_view(),
         name='CRD_apiview'),

    path('candidate/', views.CandidateProfileListAPIView.as_view(),
         name='candidate_list_apiview'),
    path('candidate/<int:pk>/', views.CandidateProfileRetrieveUpdateDestroyAPIView.as_view(),
         name='candidate_CRD_apiview'),


]
