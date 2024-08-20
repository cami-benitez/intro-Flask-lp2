#Data access objeto - Dao 
from conexion.Conexion import Conexion
class CiudadDao:

    def getCiudades(self):
        

    def getCiudades(self):
        ciudadSQL = """
        SELECT id, descripcion 
        FROM ciudades 
        """
        # objeto conexion 
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(ciudadSQL)
            # trae datos de la red
            lista_ciudades = cur.fetchall()
            # retorno de datos
            return lista_ciudades
        except con.Error as e:
            print(e)
        finally:
            cur.close()
            con.close()

    def guardarCiudad(self, descripcion):

        insertCiudadSQL = """
        INSERT INTO ciudades(descripcion) VALUES(%s)
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ecjecucion exitosa 
        try:
            cur.execute(insertCiudadSQL, (descripcion,))
            con.commit()
            return True
        except con.Error as e:
             print(e)

        # Siempre se va ejecutar
        finally:
            cur.close()
            con.close()

        return False
        
