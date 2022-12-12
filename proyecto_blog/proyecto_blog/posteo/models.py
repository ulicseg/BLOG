from django.db import models

class posteo(models.Model):
     autor = models.Charfield(max_lenght=255)
     titulo= models.Charfield(max_length=255)
     text= models.TextField()
     fecha_publicacion=models.DateTimeField(blank=True, null=True)

     def __str__(self):
        return self.titulo
  

