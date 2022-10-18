from unittest.util import _MAX_LENGTH
from django.db import models

class Tazones(models.Model):
    Nombre = models.CharField(max_length=35)
    Tamaño = models.CharField(max_length=10)
    Color = models.CharField(max_length=20)
    Stock = models.CharField(max_length=35)

    def tazon(self):
        cadena = "{0} {1} {2}"
        return  cadena.format(self.Nombre,self.Tamaño,self.Color)

    def __str__(self):
        return self.tazon()

class Relojes(models.Model):
    Nombre = models.CharField(max_length=35)
    Modelo = models.CharField(max_length=35)
    Stock = models.CharField(max_length=35)

    def reloj(self):
        cadena = "{0} {1}"
        return  cadena.format(self.Nombre,self.Modelo)

    def __str__(self):
        return self.reloj()

class Imanes(models.Model):
    Nombre = models.CharField(max_length=35)
    Stock = models.CharField(max_length=35)

    def iman(self):
         cadena = "{0}"
         return  cadena.format(self.Nombre)

    def __str__(self):
        return self.iman()

class Llaveros(models.Model):    
    Nombre = models.CharField(max_length=35)
    Stock = models.CharField(max_length=35)

    def llavero(self):
         cadena = "{0}"
         return  cadena.format(self.Nombre)

    def __str__(self):
        return self.llavero()
    
class Portavasos(models.Model):    
    Nombre = models.CharField(max_length=35)
    Color = models.CharField(max_length=35)
    Tamaño = models.CharField(max_length=20)
    Stock = models.CharField(max_length=35)

    def portavaso(self):
         cadena = "{0} {1} {2}"
         return  cadena.format(self.Nombre, self.Color, self.Tamaño)

    def __str__(self):
        return self.portavaso()

class Jardineria(models.Model):    
    Tipo = models.CharField(max_length=35)
    Nombre= models.CharField(max_length=35)
    Stock = models.CharField(max_length=35)

    def jardineria(self):
         cadena = "{0} {1}"
         return  cadena.format(self.Tipo, self.Nombre)

    def __str__(self):
        return self.jardineria()

class Cuadros(models.Model):    
    Nombre = models.CharField(max_length=35)
    Stock = models.CharField(max_length=35)

    def cuadro(self):
         cadena = "{0}"
         return  cadena.format(self.Nombre)

    def __str__(self):
        return self.cuadro()

class Cocina(models.Model):    
    Tipo = models.CharField(max_length=35)
    Nombre = models.CharField(max_length=35)
    Stock = models.CharField(max_length=35)

    def cocina(self):
         cadena = "{0} {1}"
         return  cadena.format(self.Tipo, self.Nombre)

    def __str__(self):
        return self.cocina()

class Choperos(models.Model):    
    Nombre = models.CharField(max_length=35)
    Tamaño = models.CharField(max_length=10)
    Stock = models.CharField(max_length=35)

    def chopero(self):
         cadena = "{0} {1}"
         return  cadena.format(self.Nombre, self.Tamaño)

    def __str__(self):
        return self.chopero()
class TiposDePrecio(models.Model):
    Precio = models.CharField(max_length=35)

    def precio(self):
         cadena = "{0}"
         return  cadena.format(self.Precio)

    def __str__(self):
        return self.precio()

TiposDeProductos = ['Tazones', 'Relojes', 'Imanes', 'Llaveros', 'Portavasos', 'Jardineria', 'Cuadros', 'Cocina', 'Choperos']


class Producto(models.Model):
    Producto = models.ForeignKey(Tazones, Relojes, Imanes, Llaveros, Portavasos, Jardineria, Cuadros, Cocina, Choperos, null=False, blank=False, on_delete=models.CASCADE)
    Precio = models.ForeignKey(TiposDePrecio, null=False, blank=False, on_delete=models.CASCADE)
    Tipo = models.ForeignKey(TiposDeProductos, null=False, blank=False, on_delete=models.CASCADE)
    fechaIngreso = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        cadena = "{0} => {1}"
        return cadena.format(self.Alumno, self.Curso)