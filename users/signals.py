from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User

from users.models import Profile


@receiver(post_save, sender=Profile)
def profileUpdated(sender, instance, created, **kwargs):
    print('Profile saved!')
    print('Instance:', instance)
    print('Created:', created)


def createProfile(sender, instance, created, **kwargs):
    print('Profile signal triggered!')
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user, 
            username=user.username,
            email=user.email,
            name=user.first_name + ' ' + user.last_name,
        )


@receiver(post_delete, sender=Profile)
def profileDeleted(sender, instance, **kwargs):
    print('Profile deleted!')
    print('Instance:', instance)


def deleteUser(sender, instance, **kwargs):
    user = instance.user
    user.delete()


post_save.connect(createProfile, sender=User)
post_delete.connect(deleteUser, sender=Profile)