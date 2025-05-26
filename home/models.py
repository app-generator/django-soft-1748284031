# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Projects(models.Model):

    #__Projects_FIELDS__
    project_code = models.CharField(max_length=255, null=True, blank=True)
    project_name = models.TextField(max_length=255, null=True, blank=True)
    project_description = models.TextField(max_length=255, null=True, blank=True)
    project_start = models.DateTimeField(blank=True, null=True, default=timezone.now)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)

    #__Projects_FIELDS__END

    class Meta:
        verbose_name        = _("Projects")
        verbose_name_plural = _("Projects")


class Customer(models.Model):

    #__Customer_FIELDS__
    customer_domain = models.TextField(max_length=255, null=True, blank=True)
    customer_email = models.TextField(max_length=255, null=True, blank=True)
    customer_id = models.CharField(max_length=255, null=True, blank=True)

    #__Customer_FIELDS__END

    class Meta:
        verbose_name        = _("Customer")
        verbose_name_plural = _("Customer")



#__MODELS__END
