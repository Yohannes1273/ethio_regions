from django.db import models

# Create your models here.
class RegionalInfo(models.Model):
    region_number=models.PositiveSmallIntegerField()
    name=models.CharField(max_length=64)
    population_size=models.PositiveBigIntegerField()
    area_in_square=models.FloatField()
    capital_city=models.CharField(max_length=100)
    flag=models.ImageField( upload_to='flag' )
    email_address=models.EmailField()
    map=models.ImageField(upload_to='map')
    website=models.URLField()
    def __str__(self):
      return self.name
