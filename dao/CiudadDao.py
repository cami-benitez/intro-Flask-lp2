#Data access objeto - Dao 
from conexion.conexion import conexion
class CiudadDao: 

    def getCiudades(self):
        ciudadSQL = """
        SELECT id, descripcion 
        FROM ciudades 
        """
        # objeto conexion 
        conexion = conexion()
        con = conexion.getConexion()
        try:
            pass
        except:
            pass
        finally:
            pass
