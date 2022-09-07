from django.shortcuts import render

# Create your views here.
import datetime
def search(request):
    details = {'name': 'Ramesh', 'li': [1,7,3,9,5],
           'score': 40, 'description': 'he is learning the python and React',
           'village': 'Chagallu', 'datetime': datetime.datetime.now()}

    return render(request, 'a.html', context=details)
