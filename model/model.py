from database.DAO import DAO
import networkx as nx

class Model:
    def __init__(self):
        self.airportList = DAO.get_airports()
        self.airportMap = {}
        for a in self.airportList:
            self.airportMap[a.ID] = a
        self.grafo = nx.Graph()

    def creaGrafo(self, min):
        self.grafo.clear()
        self.grafo.add_nodes_from(self.airportList)
        listaRotte = self.trovaArchi(min)
        return listaRotte


    def trovaArchi(self,min):
        rotte = DAO.getRotte()
        listRotte = []
        for r in rotte:
            for r2 in rotte:
                if r.a1_id == r2.a2_id and r.a2_id == r2.a1_id:
                    sum = r.sumDist + r2.sumDist
                    numVoli = r.nVoli + r2.nVoli
                    peso = sum / numVoli
                    if peso > min:
                        airp1 = self.airportMap[r.a1_id]
                        airp2 = self.airportMap[r.a2_id]
                        self.grafo.add_edge(airp1, airp2, weight=peso)
                        listRotte.append((airp1, airp2, peso))
                else:
                    if (r.sumDist / r.nVoli) > min:
                        airp1 = self.airportMap[r.a1_id]
                        airp2 = self.airportMap[r.a2_id]
                        peso = (r.sumDist / r.nVoli)
                        self.grafo.add_edge(airp1, airp2, weight=peso)
                        listRotte.append((airp1, airp2, peso))
        return listRotte


    def getNumNodes(self):
        return len(self.grafo.nodes)

    def getNumEdges(self):
        return len(self.grafo.edges)