from django.shortcuts import render
from tenten.models import Recommend
from .forms import ReplyCntDataForm
# from django.db.models import Count

# Create your views here.

def index(requests):
    recommends = Recommend.objects.all().order_by("-price")
    return render(requests, "index.html", {"recommends" : recommends})


def dashboard(request):
    data = Recommend.objects.all()
    print(data)
    data = data.order_by('-like_cnt')[:10]
    cal1_data = []
    for datas in data:
        cal1 = datas.like_cnt*0.5 + datas.reply_cnt*0.5
        cal1_data.append(cal1)
        cal1_data.sort()
        print(cal1_data)        
    if request.method == 'POST':
        pass
    else: 
        form = ReplyCntDataForm()
        context = {
            'dataset': data,
            }
    return render(request, 'dashboard.html', context)

