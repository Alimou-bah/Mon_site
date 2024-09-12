from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Article(models.Model):
    title = models.CharField(_("Titre"), max_length=60)
    sumary = models.CharField(_("Sommaire"), max_length=60, null=True )
    content = models.TextField(_("Contenue"), max_length= 100)
    image = models.ImageField(_("Images"), upload_to='images')
    date_pub = models.DateField(_("Date de publication"), null=True)
    


    def __str__(self):
        return self.title