from django.contrib import admin
from .models import Companyinfo, CandidateProfile

# Register your models here.


@admin.register(Companyinfo)
class CompanyinfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'company_name', 'company_email',
                    'company_website', 'company_about']


@admin.register(CandidateProfile)
class CandidateProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'degree_level', 'degree_name',
                    'degree_cgpa', 'degree_institution', 'employment_status', 'employment_type', 'areas_of_work', 'total_experience', 'target_degree_year', 'subject']
