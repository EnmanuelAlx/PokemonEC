from django.db import models

# Create your models here.
class Pokemon(models.Model):
    name  = models.CharField(max_length = 100, null=False)
    height = models.PositiveIntegerField(null=False)
    weight = models.PositiveIntegerField(null=False)
    pokemon_id = models.PositiveIntegerField()
    prevolution = models.ManyToManyField(
        "self", 
        related_name='prevolutions',
        verbose_name='prevolution'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # def __str__(self):
    #     prevolution = self.prevolution if self.prevolution else None
    #     return f'{self.name} - revolution: {self.prevolution}'
    
    # class Meta:
    #     unique_together = (
    #         ("id", "pokemon_id"),
    #     )

class Stat(models.Model):
    
    name  = models.CharField(max_length = 40, null=False, default='')
    base_stat = models.IntegerField(null=False, default=0)
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)