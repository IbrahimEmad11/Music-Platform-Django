from time import sleep
from django.core.mail import send_mail
from celery import shared_task
from artists.models import Artist
from users.models import User
import datetime


@shared_task()
def send_email_task(email_address, artist,album):  
    sleep(4)  
    send_mail(
        "Congratulations!",
        f"Congrats {artist} on your new album with title: {album}. Good Job!",
        "yarbfokeldee2a@gmail.com",
        [email_address],
        fail_silently=False,
    )

@shared_task
def check_30days():
    all_users = User.objects.all()
    today = datetime.datetime.now().date()
    for user in all_users:
        latest_album =user.artist.related_artist.all().first()
        date=getattr(latest_album,'creation_time')
        if (date.day - today >30):
            send_email_task(user)

    # artists = Artist.objects.all()
    # latest_albums = Album.objects.all().order_by('-creation_time')
    # for artist in artists:
    #     x=  latest_albums.filter(artist = artist).get(pk=1)['creation_time']
    #     if (x - current_date >30):
    #         send_email_task(artist.user.email,Album.artist , Album.album_name)



