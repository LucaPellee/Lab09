import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self.distMin = None

    def handleAnalizza(self,e):
        self.distMin = self._view._txtIn.value
        try:
            distMinFloat = float(self.distMin)
        except ValueError:
            self._view._txt_result.controls.clear()
            self._view._txt_result.controls.append(ft.Text("Please provide a numerical value for distance. "))
            self._view.update_page()
            return

        listaRotte = self._model.creaGrafo(distMinFloat)
        numNodes = self._model.getNumNodes()
        self._view._txt_result.controls.append(ft.Text(f"numero nodi: {numNodes}"))
        self._view.update_page()
        numEdges = self._model.getNumEdges()
        self._view._txt_result.controls.append(ft.Text(f"numero archi: {numEdges}"))
        for r in listaRotte:
            self._view._txt_result.controls.append(ft.Text(f"{r[0]} to {r[1]} con ditanza {r[2]}"))
        self._view.update_page()
