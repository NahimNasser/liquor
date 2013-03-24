from django.core.management.base import BaseCommand
from liquor import liquor_horse


class Command(BaseCommand):
    help = 'Copies data from the LCBO Api to the database'

    def handle(self, *args, **options):
        print "Begin stealing booze..."
        liquor_horse.store_all_lcbo_products()
        print "Booze successfully stolen."
