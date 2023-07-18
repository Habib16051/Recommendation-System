from django.shortcuts import render
from rest_framework import generics
from .models import Companyinfo, CandidateProfile
from .serializers import CompanyinfoSerializer, CandidateProfileSerializer

# Create your views here.


# For displaying all the list of companyinfo
class CompanyListAPIView(generics.ListCreateAPIView):
    queryset = Companyinfo.objects.all()
    serializer_class = CompanyinfoSerializer


# For Read, Update and delete specific info from the companyinfo list
class CompanyRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Companyinfo.objects.all()
    serializer_class = CompanyinfoSerializer


# For displaying all the list of CandidateProfile List
class CandidateProfileListAPIView(generics.ListCreateAPIView):
    queryset = CandidateProfile.objects.all()
    serializer_class = CandidateProfileSerializer


# For Read, Update and delete specific info from the CandidateProfile
class CandidateProfileRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CandidateProfile.objects.all()
    serializer_class = CandidateProfileSerializer
