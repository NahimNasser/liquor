import models
from django.db.models import Min


def get_alcoholic_beverages():
    return models.LcboProduct.objects.filter(price_per_liter_of_alcohol_in_cents__gt=0, is_discontinued=False, is_dead=False, alcohol_content__gt=0)


def cheapest_price_per_liter_of_alcohol():
    return get_alcoholic_beverages().aggregate(most_effective_alcohol=Min('price_per_liter_of_alcohol_in_cents'))['most_effective_alcohol']


def get_best_value_alcohol():
    return get_alcoholic_beverages().get(price_per_liter_of_alcohol_in_cents=cheapest_price_per_liter_of_alcohol())


def filter_max_price_min_alcohol(price, alcohol_content):
    alcoholic_beverages = models.LcboProduct.objects.filter(alcohol_content__gte=alcohol_content*100, price_in_cents__lte=price*100, price_per_liter_of_alcohol_in_cents__gt=0, is_discontinued=False, is_dead=False, alcohol_content__gt=0).order_by('-price_in_cents')
    if alcoholic_beverages.count() <= 0:
        print "Nothing found for those parameters."
    else:
        for beverage in alcoholic_beverages:
            print "(%s) %s (%dmL) (%s%% alcohol) for $%s" % (beverage.primary_category, beverage.name, beverage.volume_in_milliliters, beverage.alcohol_content/100, beverage.price_in_cents/100.00)


def print_booze_a_lytics():
    print "===Booze-a-lytics==="
    print "%d beers in the system" % models.LcboProduct.objects.filter(primary_category="Beer").count()
    best_value_alcohol = get_best_value_alcohol()
    print "Most cost effective beverage to get drunk is %s (%s)" % (best_value_alcohol.name, best_value_alcohol.primary_category)
    number_of_bottles = 2500 / best_value_alcohol.price_in_cents
    print "For $25, you should be able to get %d (%s mL bottles) of %s" % (number_of_bottles, best_value_alcohol.volume_in_milliliters, best_value_alcohol.name)
    print "==============="
