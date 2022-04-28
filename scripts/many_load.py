import csv  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load

from unesco.models import Category, State, Iso, Region, Site


def run():
    fhand = open('scripts/whc-sites-2018-clean.csv')
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header

    Category.objects.all().delete()
    State.objects.all().delete()
    Iso.objects.all().delete()
    Region.objects.all().delete()
    Site.objects.all().delete()

    # Format
    # email,role,course
    # jane@tsugi.org,I,Python
    # ed@tsugi.org,L,Python

    for row in reader:
        name = row[0]
        if len(name) == 0:
            name = ''

        description = row[1]
        if len(description) == 0:
            justification = None

        justification = row[2]
        if len(justification) == 0:
            justification = None

        try:
            year = int(row[3])
        except:
            year = None

        try:
            longitude = float(row[4])
        except:
            longitude = None

        try:
            latitude = float(row[5])
        except:
            latitude = None

        try:
            area_hectares = float(row[6])
        except:
            area_hectares = None

        category = row[7]
        if len(category) == 0:
            category = None

        category, status = Category.objects.get_or_create(name=category)

        state = row[8]
        if len(state) == 0:
            state = None

        state, status = State.objects.get_or_create(name=state)

        region = row[9]
        if len(region) == 0:
            region = None

        region, status = Region.objects.get_or_create(name=region)

        iso = row[10]
        if len(iso) == 0:
            iso = ''

        iso, status = Iso.objects.get_or_create(name=iso)
        print(iso)

        site = Site.objects.create(
            name=name,
            year=year,
            latitude=latitude,
            longitude=longitude,
            description=description,
            justification=justification,
            area_hectares=area_hectares,
            category=category,
            region=region,
            iso=iso,
            state=state,
        )
        site.save()

