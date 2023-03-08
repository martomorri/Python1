import datetime

class Persona:
    
    def __init__(self, dni, nom, ape, fechaNac):
        self.dni = dni
        self.nom = nom
        self.ape = ape
        self.fechaNac = fechaNac
    
    def obtenerEdad(fechaNac):
        hoy = datetime.datetime.today()
        edad = hoy.year - fechaNac.year
        if fechaNac.month > hoy.month:
            edad -= 1
        elif fechaNac.month == hoy.month:
            if fechaNac.day > hoy.day:
                edad -= 1
        return edad

persona = Persona(46873102, "Martin", "Morrison", datetime.datetime(2005,6,28))
    
edad = Persona.obtenerEdad(persona.fechaNac)
print(f"\n{persona.nom} {persona.ape} tiene {edad} años\n")