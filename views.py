
from django.http import HttpResponse
import datetime
from django.shortcuts import render_to_response

from models import Day

#    now = datetime.datetime.now()
#    html = "<html><body><h2>It is now %s.</h2></body></html>" % now

def home(request):

    chance_of_evening_given_morning = float(Day.objects.chance_of_rain_in_evening_given_rain_in_morning()) * 100
    chance_of_evening_given_morning = "%.2f%%" % chance_of_evening_given_morning

    chance_of_rain = float(Day.objects.chance_of_rain()) * 100
    chance_of_rain = "%.2f%%" % chance_of_rain

    chance_of_dry = float(Day.objects.chance_of_dry()) * 100
    chance_of_dry = "%.2f%%" % chance_of_dry

    
    return render_to_response('home.html', {'name': 'Bob',
                                            'wet_rides': Day.objects.num_wet_commutes(),
                                            'dry_rides': Day.objects.num_dry_commutes(),
                                            'chance_of_evening_given_morning': chance_of_evening_given_morning,
                                            'chance_of_rain': chance_of_rain,
                                            'chance_of_dry': chance_of_dry})


