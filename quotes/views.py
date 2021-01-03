from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.urls import reverse , reverse_lazy
from .models import Stock
from .forms import StockForm
from django.views.generic.edit import DeleteView
from django.contrib import messages

# Create your views here.
# pk_36114405301146b5812f93985fe4983d

def home(request):
    import requests
    import json
    if request.method =="POST":
        ticker = request.POST['ticker']
        api_request = requests.get("https://cloud.iexapis.com/stable/stock/"+ticker+"/quote?token=pk_36114405301146b5812f93985fe4983d")
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api="Error..."
        return render(request,'quotes/home.html',context={'api':api})

    else:
        return render(request,'quotes/home.html',context={'ticker':"enter ticker "})


def about(request):
    return render(request,'quotes/about.html',context={})


def add_stock(request):
    import requests
    import json
    form = StockForm()
    if request.method == 'POST':
        form = StockForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Stock Has been added!!")
            return HttpResponseRedirect(reverse('quotes:add_stock'))
    tickers = Stock.objects.all()
    output = []
    for ticker_item in tickers:
        api_request = requests.get("https://cloud.iexapis.com/stable/stock/"+str(ticker_item)+"/quote?token=pk_36114405301146b5812f93985fe4983d")
        try:
            api = json.loads(api_request.content)
            output.append(api)
        except Exception as e:
            aapi="Error..."
    return render(request,'quotes/add_stock.html',context={'tickers':tickers,'form':form,'output':output})



class del_stock(DeleteView):
    model = Stock
    template_name = "quotes/delete.html"

    def get_success_url(self):
        return reverse_lazy('quotes:add_stock')


def delete(request):
    ticker = Stock.objects.all()
    return render(request,'quotes/delete_stock.html',context={'ticker':ticker})
