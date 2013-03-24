from django.core.management.base import BaseCommand
from liquor import liquor_analysis


class Command(BaseCommand):
    help = 'Analyze data from the LCBO Api'

    def handle(self, *args, **options):
        liquor_analysis.print_booze_a_lytics()
        maximum_price = int(input("Maximum amount of money to spend (Dollars):"))
        alcohol_content = int(input("Minimum alcohol percentage (Percent):"))
        liquor_analysis.filter_max_price_min_alcohol(maximum_price, alcohol_content)
