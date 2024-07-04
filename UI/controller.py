import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._provider=None
        self._distanza=None
    def fillDD(self):
        for element in self._model.getProvider():
            self._view.ddProvider.options.append(ft.dropdown.Option(text=f"{element}", on_click=self.read_provider))
    def read_provider(self,e):
        self._provider=e.control.text
    def readDistanza(self,e):
        self._distanza=float(e.control.value)
    def handleGraph(self, e):
        if not self._provider:
            self._view.create_alert("inserisci un provider")
            return
        if not self._distanza:
            self._view.create_alert("inserisci un distanza valida")
            return
        self._model.creaGrafo(self._provider, self._distanza)
        self._view.txt_result.controls.append(ft.Text(f"Grafo creato correttamente"))
        self._view.update_page()

        pass
    def handleAnalizza(self,e):
        self._view.txt_result.controls.append(ft.Text("nodi con piu vicini"))
        lista=self._model.Analizza()
        for element in lista.keys():
            self._view.txt_result.controls.append(ft.Text(f"{element}, #vicini= {lista[element]}"))
        self._view.update_page()
        pass
    def handleCalcolaP(self,e):
        pass