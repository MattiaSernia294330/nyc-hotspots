import networkx as nx
from geopy.distance import geodesic
from database.DAO import DAO
class Model:
    def __init__(self):
        self._grafo=nx.Graph()
        self._dizionarioNodi={}
        self._lista={}
        pass
    def getProvider(self):
        return DAO.getProvider()
    def creaGrafo(self,provider, distanza):
        self._grafo.clear()
        self._dizionarioNodi={}
        for element in DAO.getLocation(provider):
            self._grafo.add_node(element)
            self._dizionarioNodi[element.Location]=element
        for key in self._dizionarioNodi.keys():
            for key2 in self._dizionarioNodi.keys():
                if key!=key2 and geodesic((self._dizionarioNodi[key].Latitude/self._dizionarioNodi[key].numero,self._dizionarioNodi[key].Longitude/self._dizionarioNodi[key].numero), (self._dizionarioNodi[key2].Latitude/self._dizionarioNodi[key2].numero,self._dizionarioNodi[key2].Longitude/self._dizionarioNodi[key2].numero)).kilometers <= distanza:
                    self._grafo.add_edge(self._dizionarioNodi[key], self._dizionarioNodi[key2], weight=geodesic((self._dizionarioNodi[key].Latitude/self._dizionarioNodi[key].numero,self._dizionarioNodi[key].Longitude/self._dizionarioNodi[key].numero), (self._dizionarioNodi[key2].Latitude/self._dizionarioNodi[key2].numero,self._dizionarioNodi[key2].Longitude/self._dizionarioNodi[key2].numero)).kilometers)
    def Analizza(self):
        self._lista={}
        listanon={}
        for element in self._grafo.nodes():
            listanon[element]=len(list(nx.neighbors(self._grafo, element)))
        listanon=dict(sorted(listanon.items(), key=lambda item: item[1], reverse=True))
        max=0
        for key in listanon.keys():
            if max<=listanon[key]:
                self._lista[key]=listanon[key]
                max=listanon[key]
            else:
                break
        return self._lista



