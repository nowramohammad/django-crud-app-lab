from django.db import models

# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name
class Review(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name='reviews')
    comment = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return f"Review for {self.food.name}"

class Tag(models.Model):
    name = models.CharField(max_length=50)
    foods = models.ManyToManyField(Food, related_name='tags')

    def __str__(self):
        return self.name   