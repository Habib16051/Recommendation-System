from django.db import models


# Create your models here.
class Companyinfo(models.Model):
    company_name = models.CharField(max_length=100)
    company_email = models.CharField(max_length=100)
    company_website = models.CharField(max_length=100)
    company_about = models.CharField(max_length=100)

    def __str__(self):
        return self.company_name


class CandidateProfile(models.Model):
    degree_level = models.CharField(max_length=100)
    degree_name = models.CharField(max_length=100)
    degree_cgpa = models.DecimalField(max_digits=5, decimal_places=2)
    degree_institution = models.CharField(max_length=100)
    employment_status = models.CharField(max_length=50)
    employment_type = models.CharField(max_length=100)
    areas_of_work = models.CharField(max_length=100)
    total_experience = models.IntegerField()
    target_degree_year = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)

    def __str__(self):
        return self.degree_level
