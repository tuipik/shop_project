from django.db import models
from datetime import datetime
from django.urls import reverse
from django.utils.text import slugify
from transliterate import translit


def gen_slug(title):
    slug = slugify(translit(title, 'ru', reversed=True))
    return slug


def image_folder(instance, filename):
    filename = instance.slug + '.' + filename.split('.')[1]
    return '{0}/{1}/{2}/{3}'.format(instance.category.slug,
                                    instance.brand.slug,
                                    instance.slug, filename)


class Category(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=130, blank=True, unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'category_slug': self.slug})



class Brand(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=130, blank=True, unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)


class ProductManager(models.Manager):
    def all(self, *args, **kwargs):
        return super(ProductManager, self).get_queryset().filter(available=True)


class Product(models.Model):
    category = models.ForeignKey(Category, db_index=True,
                                 on_delete=models.CASCADE,
                                 blank=True)
    brand = models.ForeignKey(Brand, db_index=True, on_delete=models.CASCADE,
                              blank=True)
    title = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=130, blank=True)
    description = models.TextField(blank=True, db_index=True)
    image = models.ImageField(max_length=None,
                              upload_to=image_folder, blank=True)
    price = models.DecimalField(max_digits=9, decimal_places=2,
                                blank=True)
    available = models.BooleanField(default=True)
    objects = ProductManager()
    for_promo = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = gen_slug(self.title) + '-'\
                    + str(datetime.now().timestamp()).replace('.', '')
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'product_slug': self.slug})



