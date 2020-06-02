from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
# from froala_editor.fields import FroalaField
from django.utils.safestring import mark_safe
from tinymce.models import HTMLField

# Create your models here.
from store.validators import ASCIIUsernameValidator

CAR_LISTING_TYPE = (
    ('For Sale', 'For Sale'),
    ('For Hire', 'For Hire'),
    ('Classified', 'Classified'),
)

CAR_STATUS = (
    ('New', 'New'),
    ('Used', 'Used'),
)


class User(AbstractUser):
    is_agent = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)
    portfolio_site = models.URLField(blank=True)
    phone = models.CharField(max_length=60, blank=True, null=True)
    country = models.CharField('Country', max_length=60, blank=True, null=True)
    city = models.CharField('City', max_length=60, blank=True, null=True)
    postal_code = models.CharField('Postal Code', max_length=60, blank=True, null=True)
    address = models.CharField(max_length=60, blank=True, null=True)
    picture = models.ImageField(upload_to="users/pictures/%Y/%m/%d'", blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    # password settings
    # password_type = models.CharField('Password Type', default='Expirable', max_length=200, choices=PASSWORD_TYPES)
    # days_for_password_expiry = models.ForeignKey(PasswordConfigurations, on_delete=models.CASCADE, null=True, blank=True)
    # last_password_reset_date = models.DateField('Reset On', auto_now=True)
    # password_expiry_date = models.DateField(editable=False, null=True, blank=True)
    # is_password_expired = models.BooleanField(default=False,)

    username_validator = ASCIIUsernameValidator()

    def get_picture(self):
        no_picture = settings.STATIC_URL + 'img/img_avatar.png'
        try:
            return self.picture.url
        except:
            return no_picture

    def get_full_name(self):
        full_name = self.username
        if self.first_name and self.last_name:
            full_name = self.first_name + " " + self.last_name
        return full_name

    def __str__(self):
        return self.get_full_name()


class Category(models.Model):
    category_name = models.CharField('Category Name', max_length=200)
    slug = models.SlugField(max_length=150, unique=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('category_name',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category_name

    def get_absolute_url(self):
        return reverse('product_list_by_category', args=[self.slug])


class Location(models.Model):
    location_name = models.CharField('Name Of Location', max_length=1000, )

    def __str__(self):
        return self.location_name


class Product(models.Model):
    is_vehicle_model = models.BooleanField(default=True)
    user = models.ForeignKey(User, verbose_name='Agent Name', null=True, default='', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, null=True, related_name='products', default='', on_delete=models.CASCADE)
    brand = models.CharField(max_length=200, verbose_name='Brand', null=True, blank=True)
    title = models.CharField('Product Title', max_length=200, help_text='Name of product')
    # description = models.TextField(null=True, blank=True)
    stock = models.IntegerField(null=True, blank=True, default=1)
    sold = models.IntegerField(null=True, blank=True, default=0)
    description = HTMLField()
    price = models.DecimalField(decimal_places=2, max_digits=100, default=0.00)
    sale_price = models.DecimalField(decimal_places=2, null=True, blank=True, max_digits=100, default=0.00)
    slug = models.SlugField(unique=True)
    listing_type = models.CharField(max_length=200, verbose_name='Listing Type', default='', choices=CAR_LISTING_TYPE)
    vehicle_status = models.CharField(max_length=200, verbose_name='Vehicle Status', default='', choices=CAR_STATUS)
    mileage = models.CharField('Mileage', max_length=200, default=0, )
    year = models.CharField('Year', max_length=200, default=0, help_text='Year of Manufacture')
    location = models.ForeignKey(Location, null=True, related_name='location', default='', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Vehicles'
        verbose_name = 'Vehicle'
        index_together = ('id', 'slug')
        unique_together = ('title', 'slug')

    def __str__(self):
        return self.title + ', Seller Name: ' + self.user.username + ', Seller No.: ' + self.user.phone

    def get_price(self):
        return self.price

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.slug, ])


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/images/%Y/%m/%d', null=True)
    # featured = models.BooleanField(default=False)
    # thumbnail = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.title

    def image_tag(self):
        if self.image:
            return mark_safe('<img src="%s" style="width: 50px; height: 50px;"/>' % self.image.url)
        else:
            return 'No image found!'
    image_tag.short_description = 'Image'

    class Meta:
        verbose_name_plural = 'Vehicle Images'
        verbose_name = 'Vehicle Images'


class ProductVariationManager(models.Manager):
    def all(self):
        return super(ProductVariationManager, self).filter(active='True')

    def sizes(self):
        return self.all().filter(category='size')

    def colors(self):
        return self.all().filter(category='color')


class ProductVariation(models.Model):
    VARIATIONS_CATEGORIES = (
        ('size', 'size'),
        ('color', 'color'),
        ('package', 'package'),
    )

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    category = models.CharField(max_length=200, choices=VARIATIONS_CATEGORIES, default='')
    title = models.CharField(max_length=200, )
    image = models.ForeignKey(ProductImage, null=True, blank=True, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=100, decimal_places=2, default=0.00, null=True, blank=True)
    active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ProductVariationManager()

    def __str__(self):
        return self.title


class EventType(models.Model):
    event_type_name = models.CharField('Event Type Name', max_length=200)
    slug = models.SlugField(max_length=150, unique=True, db_index=True)

    def __str__(self):
        return self.event_type_name

    def get_absolute_url(self):
        return reverse('event_types', args=[self.slug])


class Event(models.Model):
    is_event_model = models.BooleanField(default=True)
    event_type = models.ForeignKey(EventType, on_delete=models.CASCADE)
    event_name = models.CharField('Event Name', max_length=200)
    slug = models.SlugField(max_length=150, unique=True, db_index=True)
    event_description = HTMLField()
    event_date = models.DateTimeField('Date Of Event')
    posted_on = models.DateTimeField(auto_now=True)
    venue = models.CharField('Venue', max_length=200, default='')

    def __str__(self):
        return self.event_name

    def get_absolute_url(self):
        return reverse('event_detail', args=[self.slug])


class QuickLinks(models.Model):
    is_quicklinks_model = models.BooleanField(default=True)
    link_name = models.CharField('Link Name', max_length=200)
    link = models.URLField('Url', default='', help_text='(e.g) www.necor.co.zm')

    def __str__(self):
        return self.link_name


RATINGS = (
    ('0', '0'),
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
)


class ProductReview(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.CharField('Rating', max_length=200, choices=RATINGS, default=0)
    description = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)
    name = models.CharField('Name', max_length=200, default='Unknown', help_text='Optional')

    def __str__(self):
        return self.description







