from django.shortcuts import render
from .forms import EmailForm
from models import calculate, calculateAmortization
from chartit import DataPool, Chart
from django.views.decorators.csrf import ensure_csrf_cookie

def home(request):
        form = EmailForm(request.POST or None)
        valores = 0
        print request.POST
        print "Form is valid: " + str(form.is_valid())
        if form.is_valid():
            interest = float(request.POST['interest'])
            principal = float(request.POST['principal'])
            valores = calculate(interest,principal)
            print(interest)
            print(principal)
        else:
            interest = ""
            principal = ""
        context = {'valor': valores, 'valid': form.is_valid(),'interest' : interest,'principal' : principal}
        template = "home.html"
        return render(request, template, context)
 
def Amortization(request):
        if request.method == "GET":
            years = int(request.GET['years'])
            interest = float(request.GET['interest'])
            principal = float(request.GET['principal'])
            cuota = int(float(request.GET['monthly']))
            validForm = True
            amTable = calculateAmortization(years,interest,principal)
        else:
            validForm = False
            amTable = ''
            cuota = ''
            years = ''
        print "Ajax is valid: " + str(validForm)
        context = {'amTable' : amTable, 'cuota' : cuota,'years' : years,'validForm' : validForm, }
        template = 'ajax_adjustment.html'
        return render(request, template, context)
