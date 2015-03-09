from django.db import models
from django.utils.translation import ugettext_lazy as _

from idios.models import ProfileBase


class Profile(ProfileBase):
    name = models.CharField(_("name"), max_length=50, null=True, blank=True)
    organization = models.CharField(_("organization"), max_length=100, null=True, blank=True)
    address = models.TextField(_("address"), null=True, blank=True)
    phone = models.CharField(_("phone"), max_length=50, null=True, blank=True)
    fax = models.CharField(_("fax"), max_length=50, null=True, blank=True)
    email = models.CharField(_("email"), max_length=255, null=True, blank=True)
    website = models.URLField(_("website"), null=True, blank=True, verify_exists=False)
