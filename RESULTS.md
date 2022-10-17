from albums.models import Album
from artists.models import Artist
from datetime import date,datetime

art1=Artist(stage_name="Travis Scott", social_link="www.instagram.com/travisscott/")
art2=Artist(stage_name="Dua Lipa", social_link="www.instagram.com/dualipa/")
art3=Artist(stage_name="Marawan Moussa", social_link="www.instagram.com/marawanmoussaa/")
art4=Artist(stage_name="Amir Eid", social_link="www.instagram.com/amir.eid/")

art1.save()
art2.save()
art3.save()
art4.save()

Artist.objects.all()
<QuerySet [<Artist: Amir Eid>, <Artist: Dua Lipa>, <Artist: Marawan Moussa>, <Artist: Travis Scott>]>

Artist.objects.order_by('stage_name')
<QuerySet [<Artist: Amir Eid>, <Artist: Dua Lipa>, <Artist: Marawan Moussa>, <Artist: Travis Scott>]>

- Artist.objects.filter(stage_name__startswith='A')
<QuerySet [<Artist: Amir Eid>]>

---

trav=Artist.objects.get(stage_name='Travis Scott')
amir=Artist.objects.get(stage_name='Amir Eid')
dua=Artist.objects.get(stage_name='Dua Lipa')
maro=Artist.objects.get(stage_name='Marawan Moussa')

                   

alb1=Album.objects.create(artist=trav,album_name='Astroworld',creation_time=date.today(), release_time=date(2018,8,3),cost=300000)
alb2=Album(artist=dua,album_name='Future Nostalgia',creation_time=date.today(), release_time=date(2023,9,21),cost=2000000)
alb3=maro.album_set.create(album_name='kazakairo',creation_time=date.today(), release_time=date(2016,6,6),cost=32652)

alb4=Album.objects.create(artist=maro,album_name='Floria',creation_time=date.today(), release_time=date(2021,1,2),cost=21345)
alb5=Album.objects.create(artist=amir,album_name='Roma',creation_time=date.today(), release_time=date(2022,9,23),cost=20029)
alb6=Album.objects.create(artist=amir,album_name='A Drop of White',creation_time=date.today(), release_time=date(2017,7,10),cost=13256)
alb7=Album.objects.create(artist=dua,album_name='Fake Album',creation_time=date.today(), release_time=date.today(),cost=132560)
alb8=Album.objects.create(artist=trav,album_name='Utopia',creation_time=date.today(), release_time=date(2023,6,4),cost=4000000)

                    

Album.objects.latest('release_time')
<Album: Future Nostalgia>

                    

Album.objects.filter(release_time__lt=date.today())
<QuerySet [<Album: Astroworld>, <Album: Floria>, <Album: Roma>, <Album: A Drop of White>]>

                    

Album.objects.exclude(release_time__gt=date.today())
<QuerySet [<Album: Astroworld>, <Album: Floria>, <Album: Roma>, <Album: A Drop of White>, <Album: Fake Album>]>

                    

Album.objects.count()
7

                    

Artist.objects.get(stage_name='Travis Scott').album_set.all() 
<QuerySet [<Album: Astroworld>, <Album: Utopia>]>
trav.album_set.all()
<QuerySet [<Album: Astroworld>, <Album: Utopia>]>
Album.objects.all().filter(artist=trav)
<QuerySet [<Album: Astroworld>, <Album: Utopia>]>

                    

Album.objects.order_by('cost','album_name')
<QuerySet [<Album: A Drop of White>, <Album: Roma>, <Album: Floria>, <Album: Fake Album>, <Album: Astroworld>, <Album: Future Nostalgia>, <Album: Utopia>]>
