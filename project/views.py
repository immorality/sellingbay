from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
import csv

# Create your views here.
from project.models import Item


def index(request):
    rows = Item.objects.all()
    return render(request, 'project/index.html', {'new': rows})

def update(request):
    from django.db import connection
    cursor = connection.cursor()

    if request.method == 'POST' and request.FILES['filecsv']:
        myfile = request.FILES['filecsv']


        filereader = csv.reader(myfile)

        for n in filereader:
            cursor.execute("SELECT add_new('%s','%s',%d,%f)" % (n[0],n[1],int(n[2]),float(n[3])))

        return HttpResponseRedirect(reverse('project:index'))

def logs(request):
    from django.db import connection
    cursor = connection.cursor()


    cursor.execute("SELECT * FROM logs_item")
    logs = cursor.fetchall()

    return render(request, 'project/logs.html', {'logs': logs})