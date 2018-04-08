from django.db import models

import datetime
from django.utils import timezone
# from postgres_copy import CopyManager

class User(models.Model):

    DG_ROLE_CHOICES = (
    ('O', 'Data Owner'),
    ('S', 'Data Steward'),
    )

    username = models.CharField(max_length=25, blank=False, null=False, primary_key=True)
    title = models.CharField(max_length=75, blank=True, null=True)
    first_name = models.CharField(max_length=75, blank=True, null=True)
    last_name = models.CharField(max_length=75, blank=True, null=True)
    dg_role = models.CharField(max_length=1, choices=DG_ROLE_CHOICES)
    contact = models.EmailField()
    # permissions = models.

    def __str__(self):
        return self.username

class Raci(models.Model):
    raci_name = models.CharField(max_length=75, blank=False, null=False, primary_key=True)
    description = models.CharField(max_length=250, blank=True, null=True)
    date_enacted = models.DateTimeField(auto_now_add=True)
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.raci_name

class Domain(models.Model):
    domain_name = models.CharField(max_length=25, blank=False, null=False, primary_key=True)
    owner = models.CharField(max_length=75, blank=True, null=True)
    raci = models.ForeignKey(Raci, on_delete=models.CASCADE)
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.domain_name

class Glossary(models.Model):
    SENSITIVITY_CHOICES = (
    ('TS', 'Top Secret'),
    ('PR', 'Private'),
    ('PU', 'Public'),
    )

    REFRESH_CHOICES = (
    ('B', 'Batch'),
    ('RT', 'Real Time'),
    )

    element_name = models.CharField(max_length=25, blank=False, null=False, primary_key=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    definition = models.CharField(max_length=500, null=True)
    domain_name = models.ForeignKey(Domain, on_delete=models.CASCADE)
    source_system = models.CharField(max_length=50, blank=True, null=True)
    source_detail = models.CharField(max_length=50, blank=True, null=True)
    possible_values = models.CharField(max_length=20, blank=True, null=True)
    data_steward = models.CharField(max_length=50, blank=True, null=True)
    sensitivity = models.CharField(max_length=2, choices=SENSITIVITY_CHOICES)
    conditions = models.CharField(max_length=75, blank=True, null=True)
    stakeholders = models.CharField(max_length=50, blank=True, null=True)
    related_depts = models.CharField(max_length=50, blank=True, null=True)
    availability = models.CharField(max_length=75, blank=True, null=True)
    refresh_rate = models.CharField(max_length=2, choices=REFRESH_CHOICES)
    timeliness = models.CharField(max_length=2, choices=REFRESH_CHOICES)
    retention = models.DateTimeField()
    other_systems = models.CharField(max_length=75, blank=True, null=True)
    usage = models.CharField(max_length=75, blank=True, null=True)
    notes = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        return self.element_name
