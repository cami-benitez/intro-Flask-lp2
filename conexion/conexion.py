import psycopg2 
class Conexion:
    """Metodo constructor de tu perro
    """
    def __init__(self):
        self.con = psycopg2.connect("dbname=Vseterinaria-db user=postgres host=localhost password=6740362")
        """getConexion 
        self
        retorno la instalacion de la base de datos 
        """
    def getConexion(self):
        return self.con