=====
Liquor
=====

Liquor is a simple library that will copy the lcbo's products api to your database.
This was created from a workshop assignment for the YMC (www.theymc.com).

The purpose is to avoid creating fake data, when building sample applications,
Using manage.py steal_booze, we can now populate our database with live data,
and build a sample site with accurate information.

http://git.io/NM2urA

Quick start
-----------

1. Add "liquor" to your INSTALLED_APPS setting like this::

      INSTALLED_APPS = (
          ...
          'liquor',
      )

2. Run `python manage.py syncdb` to create the LcboProduct models.

3. Run `python manage.py steal_booze` to get data from the LCBO API, and store it in your models.

4. Run `python manage.py analyze_booze` to get some insights.

Accessing the data
-----------------
1. Run `python manage.py shell` to launch the shell
2. `from liquor import models`
3. `models.LcboProduct.objects.all()`
