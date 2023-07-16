import os

from django.db.models.signals import post_delete, pre_save, post_init
from django.dispatch import receiver, Signal

from pages.models import PhotoMainPage, BackPhoto
from config.settings import DEFAULT_IMAGES, MEDIA_ROOT


@receiver(signal=post_delete, sender=PhotoMainPage, dispatch_uid='delete_main_page_photo')
def delete_main_page_photo(sender, instance, **kwargs):
    if os.path.isfile(instance.file.path):
        os.remove(instance.file.path)


@receiver(signal=post_delete, sender=BackPhoto, dispatch_uid='delete_background_photo')
def delete_background_photo(sender, instance, **kwargs):
    if instance.photo_m.path != os.path.join(MEDIA_ROOT, *DEFAULT_IMAGES.get('main')):
        if os.path.isfile(instance.photo_m.path):
            os.remove(instance.photo_m.path)
    if instance.photo_h.path != os.path.join(MEDIA_ROOT, *DEFAULT_IMAGES.get('houses')):
        if os.path.isfile(instance.photo_h.path):
            os.remove(instance.photo_h.path)
    if instance.photo_k.path != os.path.join(MEDIA_ROOT, *DEFAULT_IMAGES.get('kitchen')):
        if os.path.isfile(instance.photo_k.path):
            os.remove(instance.photo_k.path)
    if instance.photo_e.path != os.path.join(MEDIA_ROOT, *DEFAULT_IMAGES.get('entertainment')):
        if os.path.isfile(instance.photo_e.path):
            os.remove(instance.photo_e.path)


@receiver(signal=post_init, sender=BackPhoto, dispatch_uid='create_origainal_backphotos')
def create_origainal_backphotos(sender, instance, **kwargs):
    if instance.photo_m:
        instance.original_photo_m = instance.photo_m
    if instance.photo_h:
        instance.original_photo_h = instance.photo_h
    if instance.photo_k:
        instance.original_photo_k = instance.photo_k
    if instance.photo_e:
        instance.original_photo_e = instance.photo_e


@receiver(signal=pre_save, sender=BackPhoto, dispatch_uid='delete_background_photo')
def delete_background_photo(sender, instance, **kwargs):
    if (hasattr(instance, 'original_photo_m') and instance.original_photo_m and instance.original_photo_m.path != instance.photo_m.path and
        instance.original_photo_m.path != os.path.join(MEDIA_ROOT, *DEFAULT_IMAGES.get('main')) and
        os.path.isfile(instance.original_photo_m.path)):
            os.remove(instance.original_photo_m.path)
    if (hasattr(instance, 'original_photo_h') and instance.original_photo_h and instance.original_photo_h.path != instance.photo_h.path and            
        instance.original_photo_h.path != os.path.join(MEDIA_ROOT, *DEFAULT_IMAGES.get('houses')) and
        os.path.isfile(instance.original_photo_h.path)):
            os.remove(instance.original_photo_h.path)
    if (hasattr(instance, 'original_photo_k') and instance.original_photo_k and instance.original_photo_k.path != instance.photo_k.path and           
        instance.original_photo_k.path != os.path.join(MEDIA_ROOT, *DEFAULT_IMAGES.get('kitchen')) and
        os.path.isfile(instance.original_photo_k.path)):
            os.remove(instance.original_photo_k.path)
    if (hasattr(instance, 'original_photo_e') and instance.original_photo_e and instance.original_photo_e.path != instance.photo_e.path and        
        instance.original_photo_e.path != os.path.join(MEDIA_ROOT, *DEFAULT_IMAGES.get('entertainment')) and
        os.path.isfile(instance.original_photo_e.path)):
            os.remove(instance.original_photo_e.path)