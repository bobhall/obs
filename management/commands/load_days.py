from django.core.management.base import BaseCommand, CommandError
from myproject.models import Day

import csv
from datetime import datetime

class Command(BaseCommand):

    file_name = "/home/hallr/webapps/obs/myproject/static/commute_data/Commuting-weather/data.txt"

    def handle(self, *args, **kwargs):


        fd = open(self.file_name, 'r')
        reader = csv.reader(fd)

        reader.next()

        for line in reader:

            if len(line) == 0:
                continue

            date = datetime.strptime(line[0], '%m-%d-%Y')
            time_of_day = line[1].strip()
            condition = line[2].strip()

            
            if not date or not time_of_day or not condition:
                print "Skipping: ", line
            else:
                print line
                

            try:
                day = Day.objects.get(date=date)
            except:
                day = Day()
                day.date = date
                
            if time_of_day == 'M':
                day.morning = condition
            elif time_of_day == 'E':
                day.evening = condition
            else:
                raise TypeError("File contains bad values")
            day.save()
                

