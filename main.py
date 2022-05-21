class Ksiazka:
  def __init__(self, tytul, autor):
    self.tytul=str(tytul)
    self.autor=str(autor)

class Egzemplarz:
  def __init__(self, tytul, autor, rokWydania):  
    self.tytul=str(tytul)
    self.autor=str(autor)
    self.rokWydania=int(rokWydania)

class Biblioteka:
  ksiazki = []
  egzemplarze = []

  def pobierz_dane_ksiazki(self, tytul, autor)-> bool:
    self.tytul=tytul
    self.autor=autor
    ksiazkaTF = False
    for ksiazka in self.ksiazki:
      if ksiazka.tytul == tytul:
        ksiazkaTF = True
    return ksiazkaTF

  def dodaj_egzemplarz_ksiazki(self, tytul, autor, rokWydania):
        ksiazka = self.pobierz_dane_ksiazki(tytul, autor)
        if ksiazka == False:
            ksiazka = Ksiazka(tytul, autor)
            self.ksiazki.append(ksiazka)
  
        self.egzemplarze.append(Egzemplarz(tytul, autor, rokWydania)) 

  def printowanie(self, ksiazki, egzemplarze):

    for i in range(len(self.ksiazki)):
      licznik = 0
      temp = ksiazki[i]
      for i in range(len(self.egzemplarze)):
        eg = egzemplarze[i]
        if temp.tytul == eg.tytul and temp.autor == eg.autor:
          licznik = licznik + 1
      licznik = str(licznik)
      print("('"+temp.tytul+"',","'"+temp.autor+"', "+licznik+")")

biblioteka = Biblioteka()
book = []
n = int(input())
for i in range (0,n):
  bk = input().replace('(', '').replace(')', '').replace(' "', '').replace('"', '').replace('\r', '').replace('\n', '').split(",")
  book.append(bk)
  biblioteka.dodaj_egzemplarz_ksiazki(book[i][0],book[i][1],book[i][2]) 

biblioteka.printowanie(sorted(biblioteka.ksiazki, key=lambda ksiazka: ksiazka.tytul), biblioteka.egzemplarze)