from django.shortcuts import render


def index(request):
    return render(request,'mainapp/index.html',{'test':'test'})

def result(request):
    return render(request,'mainapp/result.html',{'lines':[[[116.288200,39.835730],[116.288190,39.835810],[116.288190,39.835810],[116.288190,39.835810],[116.286470,39.835560],[116.286210,39.835390]],]})



