from django.db import models
from django.db.models import Q

class DayManager(models.Manager):
    def num_wet_commutes(self):
        return sum([d.num_wets() for d in self.filter()])
#        return self.filter(morning='W').count() + self.filter(evening='W').count()

    def num_dry_commutes(self):
        return self.filter(morning='D').count() + self.filter(evening='D').count()

    def chance_of_rain_in_evening_given_rain_in_morning(self):
        double_wets =  self.filter(Q(morning='W') & Q(evening='W'))
        morning_wets = self.filter(Q(morning='W') & Q(evening='D'))
        return float(double_wets.count()) / (double_wets.count() + morning_wets.count())

    def chance_of_rain(self):
        wet_rides = sum([day.num_wets() for day in self.all()])
        total_rides = self.all().count() * 2
        return float(wet_rides) / total_rides

    def chance_of_dry(self):        
        return 1.0 - self.chance_of_rain()

class Day(models.Model):

    date = models.DateField(auto_now=False,auto_now_add=False)

    morning = models.CharField(max_length=1)
    evening = models.CharField(max_length=1)

    def __str__(self):
        return "%s Morning: %s, Evening: %s" % (self.date.strftime("%Y/%m/%d"),self.morning, self.evening)

    def num_wets(self):
        return {'': 0, 'W': 1,'D': 0}[self.morning] + {'': 0, 'W': 1,'D': 0}[self.evening]


    objects = DayManager()
    
