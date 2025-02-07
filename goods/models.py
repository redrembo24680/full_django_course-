from tabnanny import verbose
from django.db import models
from django.forms import CharField


class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Назва")
    slag = models.SlugField(
        max_length=200,
        unique=True,
        blank=True,
        null=True,
        verbose_name="Посилання(URL)",
    )

    class Meta:
        db_table = "Category"
        verbose_name = "Категорію"
        verbose_name_plural = "Категорії"

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Назва")
    slag = models.SlugField(
        max_length=200,
        unique=True,
        blank=True,
        null=True,
        verbose_name="Посилання(URL)",
    )
    description = models.TextField(blank=True, null=True, verbose_name="Опис")
    image = models.ImageField(
        upload_to="goods_images", blank=True, null=True, verbose_name="Зображення"
    )
    price = models.DecimalField(
        default=0.00, max_digits=7, decimal_places=2, verbose_name="Ціна"
    )
    discount = models.DecimalField(
        default=0.00, max_digits=7, decimal_places=2, verbose_name="Знижка в процентах"
    )
    quantity = models.PositiveIntegerField(default=0, verbose_name="Кількість")
    category = models.ForeignKey(
        to=Categories, on_delete=models.CASCADE, verbose_name="Катигорія"
    )

    class Meta:
        db_table: "product"
        verbose_name = "Продукт"
        verbose_name_plural = "Продукти"

    def __str__(self):
        return self.name
