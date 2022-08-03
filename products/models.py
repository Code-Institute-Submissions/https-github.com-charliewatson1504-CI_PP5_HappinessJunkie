# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.db import models
from django.contrib.auth.models import User


# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Category(models.Model):
    """
    Class for the category model
    """
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(verbose_name=('Name'), max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        """
        Method returns the category name string

        Returns:
            Category name string
        """
        return self.name

    def get_friendly_name(self):
        """
        Method returns friendly name string

        Returns:
            Category friendly name string
        """
        return self.friendly_name


class Product(models.Model):
    """
    Class for the product model
    """
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    has_zodiac_style = models.BooleanField(
        default=False, null=True, blank=True)
    has_foil_print_color = models.BooleanField(
        default=False, null=True, blank=True)
    star_rating = models.DecimalField(
        verbose_name=('Star Rating'),
        max_digits=6,
        decimal_places=2,
        default=0,
        null=True,
        blank=True
    )
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    """
    Class for review model
    """
    class Meta:
        ordering = ['-created_on']

    STAR_CHOICES = [
        (1, '*'),
        (2, '**'),
        (3, '***'),
        (4, '****'),
        (5, '*****')
    ]

    user = models.ForeignKey(
        User,
        null=True,
        on_delete=models.SET_NULL
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    star_rating = models.IntegerField(
        choices=STAR_CHOICES,
        default=5
    )

    review_text = models.TextField(
        verbose_name=_('Review Text'),
        max_length=255,
        null=False,
        blank=False
    )

    created_on = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        """
        Returns review text

        Returns:
            Review text
        """
        return self.review_text
