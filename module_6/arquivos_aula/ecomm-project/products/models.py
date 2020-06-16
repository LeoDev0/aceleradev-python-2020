from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField('Nome', max_length=50)
    description = models.TextField('Descrição')

    def __str__(self):
        return f'{self.name} - {self.products.count()}'

    class Meta:
        verbose_name_plural = 'Categories'


class Product(models.Model):
    name = models.CharField('Nome', max_length=100)
    description = models.TextField('Descrição')
    price = models.DecimalField('Preço', max_digits=8, decimal_places=2)
    category = models.ForeignKey(
        Category,
        on_delete=models.deletion.DO_NOTHING,
        related_name='products'
    )

    def __str__(self):
        return self.name


class Order(models.Model):
    name = models.CharField('Nome do Cliente', max_length=100)
    payment = models.CharField('Meio Pagamento', max_length=50)
    products = models.ManyToManyField(Product)

    @property
    def total_amount(self):
        return sum([product.price for product in self.products.all()])

    def __str__(self):
        return f'{self.name} - {self.total_amount}'
