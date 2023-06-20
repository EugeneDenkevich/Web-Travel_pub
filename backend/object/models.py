from django.db import models


FEATURES_CHOICES = [
    ('Internet', 'Интернет'),
    ('Shower', 'Душ'),
    ('Kitchen', 'Кухня'),
    ('TV', 'Телевизор'),
    ('Fridge', 'Холодильник'),
]
SEX_CHOICES = [
    ('m', 'Мужской'),
    ('w', 'Женский'),
]
BEDS = [
    ('Single Bed', 'Односпальная кровать'),
    ('Double Bed', 'Двухместная кровать'),
    ('Queen SizeBed', 'Двухместная кровать широкая'),
    ('King SizeBed', 'Большая двухместная кровать'),
    ('Extra Bed', 'Дополнительная кровать'),
    ('Crib', 'Детская кровать'),
]
ROOMS = [
    ('bedroom', 'Спальня'),
    ('guestroom', 'Гостинная'),
]


class Object(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='Название'
    )
    pers_num = models.IntegerField(
        verbose_name='Вместимость'
    )
    description_short = models.TextField(
        max_length=256,
        verbose_name='Короткое описание'
    )
    description_long = models.TextField(
        verbose_name='Подробное описание'
    )
    price_weekday = models.DecimalField(
        decimal_places=2,
        max_digits=6,
        verbose_name='Цена по будням'
    )
    price_holiday = models.DecimalField(
        decimal_places=2,
        max_digits=6,
        verbose_name='Цена по выходным'
    )
    created_date = models.DateField(
        auto_now_add=True, verbose_name='Дата добавления')
    is_reserved = models.BooleanField(default=False, verbose_name='Занят')

    class Meta:
        verbose_name = 'Домик'
        verbose_name_plural = 'Домики'

    def __str__(self):
        return self.title


class PhotoObject(models.Model):
    file = models.ImageField(
        upload_to='photo_object',
        null=True,
        blank=True,
        verbose_name='Файл'
    )
    object_id = models.ForeignKey(
        to="Object",
        on_delete=models.CASCADE,
        related_name='photos'
    )

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'

    def __str__(self):
        return f'ID - {self.id}'


class Room(models.Model):
    type = models.CharField(max_length=20, choices=ROOMS, verbose_name='Комната')
    object_id = models.ForeignKey(
        to="Object",
        on_delete=models.CASCADE,
        related_name='rooms'
    )

    class Meta:

        verbose_name = 'Objects room'
        verbose_name_plural = 'Комнаты'

    def __str__(self):
        return self.type.capitalize()


class Feature(models.Model):
    type = models.CharField(
        max_length=256,
        choices=FEATURES_CHOICES
    )

    class Meta:
        verbose_name = 'Feature'
        verbose_name_plural = 'Features'

    def __str__(self):
        return self.type


class ObjectFeature(models.Model):
    type = models.CharField(
        max_length=256,
        choices=FEATURES_CHOICES,
        verbose_name='Тип услуги'
    )

    object_id = models.ForeignKey(
        to='Object',
        on_delete=models.CASCADE,
        related_name='features',
        verbose_name='Object'
    )

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return self.type

    def save(self, *args, **kwargs) :
        obj = self.object_id
        typ = self.type
        features = self.object_id.features.all()
        features_types = [f.type for f in features]
        if self.type in features_types:
            pass
        return super().save(*args, **kwargs)


class Purchase(models.Model):
    object = models.ForeignKey(
        to="Object", related_name="purchases", on_delete=models.CASCADE, verbose_name='Домик',
        blank=True, null=True)
    fio = models.CharField(max_length=300, verbose_name = u'ФИО')
    sex = models.CharField(max_length=256, choices=SEX_CHOICES, verbose_name = u'Пол')
    passport_country = models.CharField(max_length=256, verbose_name = u'Гражданство')
    address = models.TextField(verbose_name = u'Адресс')
    phone_number = models.CharField(max_length=256, verbose_name = u'Телефон')
    email = models.EmailField(verbose_name = u'Email')
    telegram = models.CharField(max_length=256, verbose_name = u'Ник телеграм')
    desired_arrival = models.DateField(verbose_name = u'Дата заселения')
    desired_departure = models.DateField(verbose_name = u'Дата выселения')
    status = models.BooleanField(default=False, verbose_name=u'Одобрена')
    is_finished = models.BooleanField(default=False, verbose_name=u'Завершена')
    was_object = models.ForeignKey(
        to="Object", related_name="was_purchases", on_delete=models.CASCADE, verbose_name='Ранее в заказе',
        blank=True, null=True)

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

    def __str__(self):
        return f'Заявка #{self.pk}'
 

class Bed(models.Model):
    type = models.CharField(choices=BEDS, max_length=40, verbose_name = 'Кровать')
    object_id = models.ForeignKey(
        to='Object', related_name='beds', on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Кровать'
        verbose_name_plural = 'Кровати'

    def __str__(self):
        return self.type
