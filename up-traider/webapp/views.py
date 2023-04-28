from django.shortcuts import render
from webapp.models import MenuItem
# Create your views here.
def index(request):
    return render(request, "index.html", {'menu_item': MenuItem.objects.all()})