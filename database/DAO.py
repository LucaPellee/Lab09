from database.DB_connect import DBConnect
from model.airport import Airport
from model.rotta import Rotta


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def get_airports():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT * FROM airports"""
            cursor.execute(query)
            for row in cursor:
                result.append(Airport(**row))
            cursor.close()
            cnx.close()
            return result

    @staticmethod
    def getRotte():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """select f.ORIGIN_AIRPORT_ID as a1, f.DESTINATION_AIRPORT_ID as a2, SUM(f.DISTANCE) as sumDist, count(*) as nVoli 
                        from flights f 
                        group by a1, a2"""
            cursor.execute(query)
            for row in cursor:
                result.append(Rotta(row["a1"], row["a2"], row["sumDist"], row["nVoli"]))
            cursor.close()
            cnx.close()
            return result
