from django.db import models

class Category(models.Model):
    name = models.CharField("Название категории", max_length=255)
    slug = models.SlugField("URL", unique=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        Category, verbose_name="Категория", on_delete=models.CASCADE, related_name="products"
    )
    name = models.CharField("Название товара", max_length=255)
    description = models.TextField("Описание", blank=True)
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    available = models.BooleanField("В наличии", default=True)
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)
    updated_at = models.DateTimeField("Дата обновления", auto_now=True)

    age_group = models.CharField(
        "Возраст", max_length=50, blank=True, help_text="Например: 0-3 года, 4-6 лет"
    )
    size = models.CharField("Размер", max_length=50, blank=True)  # например: 86, 92, M, L
    color = models.CharField("Цвет", max_length=50, blank=True)
    brand = models.CharField("Бренд", max_length=100, blank=True)

    image = models.ImageField("Главное изображение", upload_to="products/", blank=True, null=True)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, verbose_name="Товар", on_delete=models.CASCADE, related_name="images"
    )
    image = models.ImageField("Изображение", upload_to="products/")
    alt_text = models.CharField("Описание изображения", max_length=255, blank=True)

    class Meta:
        verbose_name = "Изображение товара"
        verbose_name_plural = "Изображения товаров"

    def __str__(self):
        return f"{self.product.name} - {self.id}"
