class Automobile:
    def __init__(self, codice, marca, modello, anno, posti, disponibile=True):
        self.codice = codice
        self._marca = marca
        self._modello = modello
        self._anno = int(anno)
        self.posti = int(posti)
        self.disponibile = disponibile

    @property
    def marca(self):
        return self._marca
    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @property
    def modello(self):
        return self._modello
    @modello.setter
    def modello(self, modello):
        self._modello = modello

    @property
    def anno(self):
        return self._anno
    @anno.setter
    def anno(self, anno):
        self._anno = anno



    def __str__(self):
        stato = "Disponibile" if self.disponibile else "Noleggiata"
        return f"{self.codice} | {self.marca} {self.modello} ({self.anno}) | {self.posti} posti | {stato}"

    def __repr__(self):
        stato = "Disponibile" if self.disponibile else "Noleggiata"
        return f"{self.codice} | {self.marca} {self.modello} ({self.anno}) | {self.posti} posti | {stato}"
