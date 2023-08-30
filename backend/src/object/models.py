from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import gettext_lazy as _

from config.validators import validate_image_size
from config.settings import MAX_NUMBER_OF_GUESTS 


FEATURES_CHOICES = [
    ('Internet', 'Интернет'),
    ('Wifi', 'Бесплатный Wi-Fi'),
    ('Terrace', 'Терасса'),
    ('Patio', 'Патио'),
    ('Balcony', 'Балкон'),
    ('Dishes', 'Посуда'),
    ('Hair dryer', 'Фен'),
    ('Iron', 'Утюг'),
    ('Washing machine', 'Стиральная машина'),
    ('Gas stove', 'Газовая плита'),
    ('Microwave', 'Микроволновая печь'),
    ('Dishwasher', 'Посудомоечная машина'),
    ('Shower / bath', 'Душ / ванна'),
    ('Furniture for babies', 'Мебель для грудных детей'),
    ('Smoking indoors is prohibited', 'Курение в помещении запрещено'),
    ('Electric stove', 'Электроплита'),
    ('Personal pier', 'Личный пирс'),
    ('Shower', 'Душ'),
    ('Kitchen', 'Кухня'),
    ('TV', 'Телевизор'),
    ('Fridge', 'Холодильник'),
    ('Conditioner', 'Кондиционер'),
    ('Playground', 'Детская площадка'),
    ('Brazier', 'Мангал'),
]

SEX_CHOICES = [
    ('Мужской', 'Мужской'),
    ('Женский', 'Женский'),
]

BEDS = [
    ('sgb', 'Single Bed'),
    ('dbb', 'Double Bed'),
    ('qsb', 'Queen SizeBed'),
    ('ksb', 'King SizeBed'),
    ('exb', 'Extra Bed'),
    ('crb', 'Crib'),
]

ROOMS = [
    ('bedroom', 'Спальня'),
    ('guestroom', 'Гостинная'),
]

PURCHASE_STATUSES = [
    ('New', 'Новая'),
    ('Approved', 'Одобрена'),
    ('Denied', 'Отклонена'),
    ('Closed', 'Завершена'),
]

class Object(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='Название'
    )
    pers_num = models.IntegerField(
        verbose_name='Вместимость',
        validators=[MaxValueValidator(MAX_NUMBER_OF_GUESTS), MinValueValidator(1)],
        blank=True,
        null=True
    )
    description_short = models.TextField(
        max_length=256,
        verbose_name='Короткое описание'
    )
    description_long = models.TextField(
        verbose_name='Подробное описание',
        blank=True,
        null=True
    )
    price_weekday = models.DecimalField(
        decimal_places=2,
        max_digits=6,
        verbose_name='Цена по будням'
    )
    price_holiday = models.DecimalField(
        decimal_places=2,
        max_digits=6,
        verbose_name='Цена по выходным',
        blank=True,
        null=True
    )
    created_date = models.DateField(
        auto_now_add=True, verbose_name='Дата добавления')
    is_reserved = models.BooleanField(default=False, verbose_name='Занят')

    class Meta:
        verbose_name = 'Домик'
        verbose_name_plural = 'Домики'

    class Meta:
        verbose_name = 'Домик'
        verbose_name_plural = 'Домики'

    def __str__(self):
        return self.title
    
    @property
    def has_approved_purchases(self):
        purchases = self.purchases.filter(stat='Approved')
        print(purchases)
        return False if len(purchases) == 0 else True


class PhotoObject(models.Model):
    file = models.ImageField(
        upload_to='photo_object',
        null=True,
        blank=True,
        verbose_name='Файл',
        validators=[validate_image_size]
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
        return f''


class Room(models.Model):
    type = models.CharField(
        max_length=20, choices=ROOMS, verbose_name='Комната')
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

    def save(self, *args, **kwargs):
        features = self.object_id.features.all()
        features_types = [f.type for f in features]
        if self.type in features_types:
            return
        return super().save(*args, **kwargs)


class Purchase(models.Model):
    object = models.ForeignKey(
        to="Object", related_name="purchases", on_delete=models.CASCADE, verbose_name='Домик',
        null=True)
    fio = models.CharField(max_length=300, verbose_name=u'ФИО')
    sex = models.CharField(
        max_length=256, choices=SEX_CHOICES, verbose_name=u'Пол')
    passport_country = models.CharField(
        max_length=256, verbose_name=u'Гражданство')
    address = models.TextField(verbose_name=u'Адрес')
    phone_number = models.CharField(max_length=256, verbose_name=u'Телефон')
    email = models.EmailField(verbose_name=u'Email')
    telegram = models.CharField(
        max_length=256, verbose_name=u'Ник Телеграм', blank=True, null=True)
    desired_arrival = models.DateField(verbose_name=u'Дата заселения')
    desired_departure = models.DateField(verbose_name=u'Дата выселения')

    status = models.BooleanField(default=False, verbose_name=u'Статус') # TODO DELETE THE LOGIC

    stat = models.CharField(
        max_length=20, choices=PURCHASE_STATUSES, default='New',
        verbose_name=u'Статус'
    )
    is_finished = models.BooleanField(default=False, verbose_name=u'Завершена')
    was_object = models.ForeignKey(
        to="Object", related_name="was_purchases", on_delete=models.CASCADE,
        verbose_name='Ранее в заказе', blank=True, null=True)
    count_adult = models.IntegerField('Кол-во взрослых',
                                      validators=[MinValueValidator(0),
                                                  MaxValueValidator(20)])
    count_kids = models.IntegerField('Кол-во детей',
                                     validators=[MinValueValidator(0),
                                                 MaxValueValidator(20)])
    pets = models.TextField('Инфо о животных', blank=True, null=True)
    comment = models.TextField('Комментарий закзачика', blank=True, null=True)

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

    def __str__(self):
        return f'Заявка #{self.pk}'


class Bed(models.Model):
    type = models.CharField(choices=BEDS, max_length=40,
                            verbose_name='Кровать')
    object_id = models.ForeignKey(
        to='Object', related_name='beds', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Кровать'
        verbose_name_plural = 'Кровати'

    def __str__(self):
        return self.type
