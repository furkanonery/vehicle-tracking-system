Yazılım Laboratuvarı-2 dersi 1. proje ödevi olarak
verilen bu çalışmada, temelde birden fazla veri
tabanı kullanılarak bir web uygulaması üzerinden
kullanıcılara araç takip hizmeti sunulması
amaçlanmıştır.

Uygulamayı çalıştırmak için gerekli modüller:
pymongo
pytz
datetime
django.contrib
django.shortcuts

Ayrıca pages_car içinde bulunan araç verilerini bir noSQL sunucusuna yükleyin.

        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client['cars']
        carsNoSQL = db['pages_cars'].find()

templates/pages/araclarim.html ve templates/pages/sonKonumlar.html dosyalarına google api key'inizi girin.

        <script src="https://maps.googleapis.com/maps/api/js?key=<API-KEY>&callback=initMap&libraries=&v=weekly"async></script>

        çalıştırmak için -> python manage.py runserver

**********************************************************************

Software Laboratory-2 course as the 1st project assignment
In this study, which was given, basically more than one data
via a web application using the base
Providing vehicle tracking service to users
intended.

Required modules to run the application:
pymongo
pytz
datetime
django.contrib
django.shortcuts

Also upload the tool data contained in pages_car to a noSQL server.

        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client['cars']
        carsNoSQL = db['pages_cars'].find()

templates/pages/araclarim.html ve templates/pages/sonKonumlar.html enter your google api key in the files.

        <script src="https://maps.googleapis.com/maps/api/js?key=<API-KEY>&callback=initMap&libraries=&v=weekly"async></script>

        running -> python manage.py runserver

