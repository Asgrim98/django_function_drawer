from django.shortcuts import render
from django.http import HttpResponse
import matplotlib.pyplot as plt
import numpy as np

def index(request):
    my_dict = {'insert_me' : "To jest drugi insert :P"}
    return render(request,'djangoapp/index.html', context = my_dict)

def help(request):
    return HttpResponse('Pomocy!!')

def funkcjo(request):

    res_set = request.GET.copy()
    wartosci = list( res_set.values() )

    potegi = np.poly1d( np.array( wartosci, dtype=np.float32 ) )

    x_val = np.linspace(-20,20,100)
    y_val = potegi(x_val)

    plt.clf()
    plt.plot(x_val, y_val, c='r')
    plt.savefig('static/images/wykres.jpg')

    #initial test

    return render(request,'djangoapp/funkcjo.html')
