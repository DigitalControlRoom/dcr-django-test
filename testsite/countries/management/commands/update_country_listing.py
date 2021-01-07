import json
import os

from django.conf import settings
from django.core.management.base import BaseCommand

from countries.models import Country, Region


class Command(BaseCommand):
    help = "Loads country data from a JSON file."

    IMPORT_FILE = os.path.join(settings.BASE_DIR, "..", "data", "countries.json")

    def get_data(self):
        with open(self.IMPORT_FILE) as f:
            data = json.load(f)
        return data

    def handle(self, *args, **options):
        data = self.get_data()
        for row in data:
            region, region_created = Region.objects.get_or_create(name=row["region"])
            if region_created:
                self.stdout.write(
                    self.style.SUCCESS("Region: {} - Created".format(region))
                )
            country, country_created = Country.objects.get_or_create(
                name=row["name"],
                defaults={
                    "alpha2Code": row["alpha2Code"],
                    "alpha3Code": row["alpha3Code"],
                    "population": row["population"],
                    "region": region,
                },
            )

            self.stdout.write(
                self.style.SUCCESS(
                    "{} - {}".format(
                        country, "Created" if country_created else "Updated"
                    )
                )
            )
