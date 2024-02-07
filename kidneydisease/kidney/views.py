from django.shortcuts import render
from django.http import HttpResponse
from joblib import load

log_classifier = load('./savedModels/log_classifier.joblib')


def predictor(request):
    if request.method == 'POST':
        param1 = float(request.POST.get('param1'))
        param2 = float(request.POST.get('param2'))
        param3 = float(request.POST.get('param3'))
        param4 = float(request.POST.get('param4'))
        param5 = float(request.POST.get('param5'))
        param6 = float(request.POST.get('param6'))

        y_pred = log_classifier.predict([[param1, param2, param3, param4, param5, param6]])
        print(y_pred[0])
        if(y_pred[0] == 0):
            result = "Not having Urinal Kidney disease"
        elif(y_pred[0] == 1):
            result = "Having urinal kidney disease"
        #result1 = Blood_test_result[pred[0]]
        #result2 = Genetic_Disorder[pred[1]]
        #result3 = Disorder_Subclass[pred[2]]

        return render(request, 'main.html', {'result': result})

    return render(request, 'main.html')
