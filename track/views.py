from django.shortcuts import render
from django.contrib.auth.models import User
from datetime import datetime,timedelta
import pymongo
import pytz
from track.models import Car
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)



def sonKonumlar(request):

    context = { }

    # client = pymongo.MongoClient("mongodb://localhost:27017/")
    # db = client['cars']
    # carsNoSQL = db['pages_cars'].find({"$and": [{"UserID": request.user.id},{"VehicleID": int(aracid)},{"tarihSaat": {'$gte': a0,'$lt': b0}}]})
    # carsNoSQL = carsNoSQL.sort('tarihSaat', +1)

    if(User.is_authenticated):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client['cars']
        carsNoSQL = db['pages_cars'].find({"UserID": request.user.id})
        aracIDs = []
        for aracID in carsNoSQL:
            if not aracID['VehicleID'] in aracIDs:
                aracIDs.append(aracID['VehicleID'])
        cars2NoSQL = db['pages_cars'].find({"$and": [{'UserID':request.user.id},{'VehicleID':aracIDs[0]}]}).sort('tarihSaat', -1)
        cars3NoSQL = db['pages_cars'].find({"$and": [{'UserID':request.user.id},{'VehicleID':aracIDs[1]}]}).sort('tarihSaat', -1)

        t1=list(cars2NoSQL)[0]['tarihSaat']-timedelta(minutes=30)
        cars2NoSQL.rewind()
        t2=list(cars2NoSQL)[0]['tarihSaat']
        #print(t1,t2)
        t3=list(cars3NoSQL)[0]['tarihSaat']-timedelta(minutes=30)
        cars3NoSQL.rewind()
        t4=list(cars3NoSQL)[0]['tarihSaat']

        cars4NoSQL = db['pages_cars'].find({"$and": [{"tarihSaat": {'$gte': t1,'$lt': t2+timedelta(minutes=1)}},{'UserID':request.user.id},{'VehicleID':aracIDs[0]}]}).limit(25)
        cars5NoSQL = db['pages_cars'].find({"$and": [{"tarihSaat": {'$gte': t3,'$lt': t4+timedelta(minutes=1)}},{'UserID':request.user.id},{'VehicleID':aracIDs[1]}]}).limit(25)

        cars4NoSQL.rewind()
        cars5NoSQL.rewind()

        dateTime1=[]
        dateTime2=[]
        for car in cars4NoSQL:
            dateTime1.append(car['tarihSaat']+timedelta(hours=3))
        for car in cars5NoSQL:
            dateTime2.append(car['tarihSaat']+timedelta(hours=3))

        cars4NoSQL.rewind()
        cars5NoSQL.rewind()

        # cars4carsNoSQL = db['pages_cars'].find({"$and":[]})
        # carscarsNoSQL = Car.objects.filter(tarihSaat__range=[cars3SQLite[0].tarihSaat-timedelta(minutes=30),cars3SQLite[0].tarihSaat],UserID=request.user.id,VehicleID=aracIDs[1])[:25]


        carsSQLite = Car.objects.filter(UserID=request.user.id)
        aracIDs = []
        for aracID in carsSQLite:
            if not aracID.VehicleID in aracIDs:
                aracIDs.append(aracID.VehicleID)
        cars2SQLite = Car.objects.filter(UserID=request.user.id,VehicleID=aracIDs[0]).order_by('-tarihSaat')
        cars3SQLite = Car.objects.filter(UserID=request.user.id,VehicleID=aracIDs[1]).order_by('-tarihSaat')

        #print(cars2SQLite[0].tarihSaat-timedelta(minutes=30),cars2SQLite[0].tarihSaat)

        cars4SQLite = Car.objects.filter(tarihSaat__range=[cars2SQLite[0].tarihSaat-timedelta(minutes=30),cars2SQLite[0].tarihSaat],UserID=request.user.id,VehicleID=aracIDs[0])[:25]
        cars5SQLite = Car.objects.filter(tarihSaat__range=[cars3SQLite[0].tarihSaat-timedelta(minutes=30),cars3SQLite[0].tarihSaat],UserID=request.user.id,VehicleID=aracIDs[1])[:25]

        #print(cars2[0].tarihSaat-timedelta(minutes=30),cars2[0].tarihSaat)
        dateTime1=sorted(dateTime1,reverse=True)
        dateTime2=sorted(dateTime2,reverse=True)
        context = {
            'aracIDs' :aracIDs,
            'cars2' :list(cars4NoSQL),
            'cars3' :list(cars5NoSQL),
            'dateTime1':dateTime1,
            'dateTime2':dateTime2,
        }

    return render(request, 'pages/sonKonumlar.html',context)


def about(request):
    return render(request, 'pages/about.html')

def index(request):
    return render(request, 'pages/index.html')

def aracsec(request):
    if(User.is_authenticated):
            if request.method == 'POST':
                aracID = request.POST['aracid']

    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client['cars']
    cars2NoSQL = list(db['pages_cars'].find({"$and": [{"UserID": request.user.id},{"VehicleID": int(aracID)}]}))
    cars3NoSQL = list(db['pages_cars'].find({"$and": [{"UserID": request.user.id},{"VehicleID": int(aracID)}]}).sort('tarihSaat', -1))

    cars2SQLite = Car.objects.filter(UserID=request.user.id,VehicleID=aracID)
    cars3SQLite = Car.objects.filter(UserID=request.user.id,VehicleID=aracID).order_by('-tarihSaat')

    time1 = cars2NoSQL[0]['tarihSaat']+timedelta(hours=3)
    time1 = time1.strftime("%Y-%m-%dT%H:%M:%S")

    time2 = cars3NoSQL[0]['tarihSaat']+timedelta(hours=3,minutes=1)
    time2=time2.strftime("%Y-%m-%dT%H:%M:%S")

    time3 = list(cars3NoSQL)[0]['tarihSaat']+timedelta(hours=2)
    time3=time3.strftime("%Y-%m-%dT%H:%M:%S")



    # print(time1)
    # print(time2)
    # print(time1.isoformat())
    # print(time2.isoformat())

    context = {
        'aracID':aracID,
        'time1':time1,
        'time2':time2,
        'time3':time3,
    }
    return render(request, 'pages/aracsec.html',context)


def araclarim(request):
    context =  {}
    if(User.is_authenticated):
        if request.method == 'POST':
            aracid = request.POST['aracid']
            start = request.POST['starttime']
            #start = start + "+00:00"
            end = request.POST['endtime']

            #print(start)

            startDate = start.split('T')[0]
            startTime = start.split('T')[1]
            startDateYear = startDate.split('-')[0]
            startDateMonth = startDate.split('-')[1]
            startDateDay = startDate.split('-')[2]

            startTimeHour = startTime.split(':')[0]
            startDateMinute = startTime.split(':')[1]
            endDate = end.split('T')[0]
            endTime = end.split('T')[1]
            a = datetime(int(startDateYear), int(startDateMonth), int(startDateDay), int(startTimeHour), int(startDateMinute))

            endDate = end.split('T')[0]
            endTime = end.split('T')[1]
            endDateYear = endDate.split('-')[0]
            endDateMonth = endDate.split('-')[1]
            endDateDay = endDate.split('-')[2]

            endTimeHour = endTime.split(':')[0]
            endDateMinute = endTime.split(':')[1]
            b = datetime(int(endDateYear), int(endDateMonth), int(endDateDay), int(endTimeHour), int(endDateMinute))

            # print(type(a))
            # print(a)
            # print(b)
            # print(aracid)
            # x = datetime.datetime.now()
            # print(x)
            # tarihSaat=[startDate,startTime],
            
            carsSQLite = Car.objects.filter(tarihSaat__range=[a,b],UserID=request.user.id,VehicleID=int(aracid)).order_by('tarihSaat')
            #cars = Car.objects.all()
            utc = pytz.timezone('Europe/Istanbul')
            a0 = utc.localize(a)
            b0 = utc.localize(b)
            client = pymongo.MongoClient("mongodb://localhost:27017/")
            db = client['cars']
            carsNoSQL = db['pages_cars'].find({"$and": [{"UserID": request.user.id},{"VehicleID": int(aracid)},{"tarihSaat": {'$gte': a0,'$lt': b0}}]})
            carsNoSQL = carsNoSQL.sort('tarihSaat', +1)
            
            

            
            dateTime1=[]
            dateTime2=[]
            for car in carsNoSQL:
                dateTime1.append(car['tarihSaat']+timedelta(hours=3))
                dateTime2.append(car['tarihSaat']+timedelta(hours=3))
            
            carsNoSQL.rewind()
            a=sorted(dateTime1,reverse=True)
            b=sorted(dateTime2,reverse=True)
            # # for car in cars:
            # #     f = car.tarihSaat
            # #     print(f)
            # #     break
            context =  {
                'carsNoSQL': list(carsNoSQL),
                'carsSQLite':list(carsSQLite),
                'dateTime1':a,
                'dateTime2':b}
    return render(request, 'pages/araclarim.html',context)
