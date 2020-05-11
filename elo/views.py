from django.shortcuts import render
from django.http import HttpResponse
from elo.models import model
import random as rd
from rest_framework.views import APIView
from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

lt = []
cache = {}
len_lt = 0


class eloView(APIView):

    c = 0
    lt = []
    cache = {}
    len_lt = 0

    def __init__(self):
        pass
 #       self.get_all_image()

    def get(self,request):
        pic = {"picone":"google.png","pictwo":"google.png"}
        dict = {"hola":pic}
        return render(request,'elo/index.html',context=dict)


    def elo(ra,rb,iwa,iwb,k):
        if iwa+iwb != 1:
            raise Exception("wrong probabilty inputted")
        ea = 1.0/(1+10**((rb-ra)/400))
        eb = 1.0/(1+10**((ra-rb)/400))
        nra = ra + k*(iwa-ea)
        nrb = rb + k*(iwb-eb)
        return nra,nrb

    def get_all_image():
        obj = model.objects.all()
        for i in obj:
            eloView.lt.append(i.image)
        eloView.len_lt = len(eloView.lt)
    

    def get_pic():
 
        a,b = eloView.get_random()
        while str(a) + ":" + str(b) in eloView.cache:
            a,b = eloView.get_random()

        eloView.cache[str(a) + ":" + str(b)] = 1
    
        return eloView.lt[a],eloView.lt[b]

 
    def get_random():
        a = rd.randrange(eloView.len_lt-1)
        b = rd.randrange(eloView.len_lt-1)
        while(a==b):
            b = rd.randrange(eloView.len_lt-1)

        return a,b
    
class processing(APIView):

    def get_name(self,i):
        return i.split('/')[-1]

    def rate(self,request):
        imga = self.get_name(request.GET.get('picone'))
        imgb = self.get_name(request.GET.get('pictwo'))
        obj1 = model.objects.filter(image=imga)
        obj2 = model.objects.filter(image=imgb)
        ra,rb = -1 ,-1
        lka,lkb=0,0
        expa,expb = 0,0
        for i in obj1:
            ra = i.score
            lka = i.likes
            expa = i.exposure
        for i in obj2:
            rb = i.score
            lkb = i.likes
            expb = i.exposure
   #     ra = obj1.score
    #    rb = obj2.score
        if request.GET.get('id') == "1":
            nra,nrb = eloView.elo(ra,rb,1,0,32)
            lka += 1
        elif request.GET.get('id') == '2':
            nra,nrb = eloView.elo(ra,rb,0,1,32)
            lkb += 1
        expa += 1
        expb += 1
        chk1 = request.GET.get('validone')
        chk2 = request.GET.get('validtwo')
        obj1.update(score=nra,likes=lka,is_valid=chk1,exposure=expa)
        obj2.update(score=nrb,likes=lkb,is_valid=chk2,exposure=expb)


    def get(self,request):

        self.rate(request)
        a,b = eloView.get_pic()
        res = {"data":"thr","src":"google2.png"}
        res = {"picone":a,"pictwo":b}
        return JsonResponse(res)


class Top(APIView):

    def get(self,request):
        obj = model.objects.order_by('-score')
        lt = ["picone","pictwo","picthree","picfour","picfive","picsix","picseven","piceight","picnine","picten","piceleven","pictwelve","picthirteen","picfourteen","picfifteenth","picsixteen","picseventeen","piceighteen","picninteen","pictwenty"]

        c=0
        dic = {}
        path = "/static/images/"
        for i in obj:
            dic[lt[c]]= path + i.image
            c += 1
            if c==20:
                break
        dict = {"hola":"g"}
        return render(request,"elo/index_top.html",context=dic)


