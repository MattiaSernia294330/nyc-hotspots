from database.DB_connect import DBConnect
from model.Location import Location

class DAO():
    def __init__(self):
        pass
    @staticmethod
    def getProvider():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct provider
                from nyc_wifi_hotspot_locations nwhl 
                order by nwhl.Provider Asc
                """

        cursor.execute(query)

        for row in cursor:
            result.append(row["provider"])

        cursor.close()
        conn.close()
        return result
    @staticmethod
    def getLocation(provider):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select Location,  count(*) as numero, SUM(Latitude) as Latitude  , SUM(Longitude) as Longitude 
from nyc_wifi_hotspot_locations nwhl 
where nwhl.Provider = %s 
group by Location 
"""

        cursor.execute(query,(provider,))

        for row in cursor:
            result.append(Location(row["Location"], row["Latitude"], row["Longitude"], row["numero"]))

        cursor.close()
        conn.close()
        return result