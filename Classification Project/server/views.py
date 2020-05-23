#from django.views.generic import TemplateView  # FIXME ANCHOR TAG

from django.shortcuts import render
import numpy as np
import joblib
with open("server/model/classifier.pkl", 'rb') as file:    # test case in tests.py REVIEW
    model = joblib.load(file)

def IndexView(request):
    return render(request, 'index.html')

def PredictView(request):
    if request.method == "POST":
        slength = request.POST['slength']
        swidth = request.POST['swidth']
        plength = request.POST['plength']
        pwidth = request.POST['pwidth']
        
        data = [slength, swidth, plength, pwidth]
        data = np.array(data).reshape(-1,4)
        result = model.predict(data)
        print(*result)
        context = {'result': result[0]}
        return render(request, 'predict.html', context)


''' TODO 
get the data from html format and create numpy or pandas format and predict
'''