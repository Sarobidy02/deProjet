from django.shortcuts import render
from django.views import View
# Create your views here.
class EvaluationView(View):
    def get(self, request):
        #load a trained model
        #load test data
        #make prediction and generate score
        context = {'precision': 82.56, 'recall': 87.03, 'accuracy': 84.89, 'fone': 84.74}
        return render(request, 'evaluation/evaluation.html', context = context)
