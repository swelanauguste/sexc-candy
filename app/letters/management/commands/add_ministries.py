import csv

from django.core.management.base import BaseCommand

from ...models import Correspondence

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        
        with open(f"static/ministries.csv", "r") as file:
            reader = csv.reader(file)
            next(reader)
            for i, row in enumerate(reader):
                name = row[0].replace("\n", "")
                Correspondence.objects.get_or_create(
                    name=name,
                )
                self.stdout.write(self.style.SUCCESS(f"{name} added"))
                
            