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


    """def trovaArchi(self,min):
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
        return listRotte"""


    def getNumNodes(self):
        return len(self.grafo.nodes)

    def getNumEdges(self):
        return len(self.grafo.edges)

    def trovaArchi(self, min):
        rotte = DAO.getRotte()
        listRotte = []
        route_map = {}

        # Crea una mappatura delle rotte per evitare il ciclo annidato
        for r in rotte:
            key = (r.a1_id, r.a2_id)
            if key not in route_map:
                route_map[key] = r

        # Ora itera attraverso il dizionario
        for (a1_id, a2_id), r in route_map.items():
            peso = r.sumDist / r.nVoli
            if peso > min:
                airp1 = self.airportMap[a1_id]
                airp2 = self.airportMap[a2_id]
                self.grafo.add_edge(airp1, airp2, weight=peso)
                listRotte.append((airp1, airp2, peso))

            # Controlla anche per le rotte inverse
            reverse_key = (a2_id, a1_id)
            if reverse_key in route_map:
                r2 = route_map[reverse_key]
                sum = r.sumDist + r2.sumDist
                numVoli = r.nVoli + r2.nVoli
                peso = sum / numVoli
                if peso > min:
                    airp1 = self.airportMap[a1_id]
                    airp2 = self.airportMap[a2_id]
                    self.grafo.add_edge(airp1, airp2, weight=peso)
                    listRotte.append((airp1, airp2, peso))

        return listRotte