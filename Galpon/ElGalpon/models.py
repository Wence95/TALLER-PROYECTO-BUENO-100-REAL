from unittest.util import _MAX_LENGTH
from django.db import models

class Tazones(models.Model):
    NombreT = models.CharField(max_length=35)
    TamañoT = models.CharField(max_length=10)
    ColorT = models.CharField(max_length=20)

    def tazon(self):
        cadena = "{0} {1} {2}"
        return  cadena.format(self.NombreT,self.TamañoT,self.ColorT)

    def __str__(self):
        return self.tazon()

class Relojes(models.Model):
    NombreR = models.CharField(max_length=35)
    ModeloR = models.CharField(max_length=35)

    def reloj(self):
        cadena = "{0} {1}"
        return  cadena.format(self.NombreR,self.ModeloR)

    def __str__(self):
        return self.reloj()

class Imanes(models.Model):
    NombreI = models.CharField(max_length=35)

    def iman(self):
         cadena = "{0}"
         return  cadena.format(self.NombreI)

    def __str__(self):
        return self.iman()

class Llaveros(models.Model):    
    NombreL = models.CharField(max_length=35)

    def llavero(self):
         cadena = "{0}"
         return  cadena.format(self.NombreL)

    def __str__(self):
        return self.llavero()
    
class Portavasos(models.Model):    
    NombreP = models.CharField(max_length=35)
    ColorP = models.CharField(max_length=35)
    TamañoP = models.CharField(max_length=20)

    def portavaso(self):
         cadena = "{0} {1} {2}"
         return  cadena.format(self.NombreP, self.ColorP, self.TamañoP)

    def __str__(self):
        return self.portavaso()

class Jardineria(models.Model):    
    TipoJ = models.CharField(max_length=35)
    NombreJ= models.CharField(max_length=35)

    def jardineria(self):
         cadena = "{0} {1}"
         return  cadena.format(self.TipoJ, self.NombreJ)

    def __str__(self):
        return self.jardineria()

class Cuadros(models.Model):    
    NombreC = models.CharField(max_length=35)

    def cuadro(self):
         cadena = "{0}"
         return  cadena.format(self.NombreC)

    def __str__(self):
        return self.cuadro()

class Cocina(models.Model):    
    TipoC = models.CharField(max_length=35)
    NombreC= models.CharField(max_length=35)

    def cocina(self):
         cadena = "{0} {1}"
         return  cadena.format(self.TipoC, self.NombreC)

    def __str__(self):
        return self.cocina()

class Choperos(models.Model):    
    NombreCh = models.CharField(max_length=35)
    TamañoCh = models.CharField(max_length=10)

    def chopero(self):
         cadena = "{0} {1}"
         return  cadena.format(self.NombreCh, self.TamañoCh)

    def __str__(self):
        return self.chopero()
