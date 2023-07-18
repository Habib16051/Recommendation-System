from rest_framework import serializers
from .models import Companyinfo, CandidateProfile


class CompanyinfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Companyinfo
        fields = '__all__'


class CandidateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CandidateProfile
        fields = '__all__'
