from PyQt5 import QtWidgets

import sys
import Tri
import Functions as fn
import matplotlib.animation as animation
import matplotlib.pyplot as plt


class designWindow(QtWidgets.QMainWindow,Tri.Ui_MainWindow):
    def __init__(self):
        super(designWindow, self).__init__()
        self.setupUi(self)
        self.animerBtn.setDisabled(True)
        self.decroissantBtn.setDisabled(True)
        self.croissantBtn.setDisabled(True)
        self.resZone.setDisabled(True)
        self.etatZone.setText("Entrer une liste d'entiers")
        self.RaiseError = True
        self.textZone.textChanged.connect(self.Tri)
        radio = [self.decroissantBtn, self.croissantBtn]
        self.group = QtWidgets.QButtonGroup()
        for btn in radio:
            self.group.addButton(btn)
        self.animerBtn.clicked.connect(self.showAnim)
        self.group.buttonClicked.connect(self.Tri)
        self.sortCombo.currentTextChanged.connect(self.Tri)
        self.sortCombo.currentTextChanged.connect(self.showalg)
        self.algZone.setStyleSheet("font-size: 25px;font-weight:bold;")
        self.resZone.setStyleSheet("font-size: 25px;font-weight:bold;")
        self.etatZone.setStyleSheet("font-size: 25px; font-weight:bold;")
        self.textZone.setStyleSheet("font-size: 25px; font-weight:bold;")
        self.textZone.setPlaceholderText("Entrer une séquence d'entiers séparés par des espaces")
        self.algZone.setText("""Procedure tri_rapide (tableau [1:n], gauche, droit )
        DEBUT
          (* mur marque la separation entre les elements plus petits et ceux plus grands que pivot*)
          mur ← gauche;
          (* On prend comme pivot l element le plus a droite *)
          pivot ← tableau[droit];  
          placer a gauche de mur tout les elements plus petits
          placer a droite de mur tout les element plus grands
          (* On place correctement le pivot *)
          placer le pivot a la place de mur
          (* On poursuit par recursivite *)
          SI (gauche<mur-1) ALORS tri_rapide(tableau,gauche,mur-1);
          SI (mur+1<droit) ALORS tri_rapide(tableau,mur,droit);
        FIN;""")
    def Tri(self):
        Errortext="Liste non valide ❌"
        EnteredList = self.textZone.text()

        try:
            if (len(EnteredList)>0):
                self.splitList = list(map(int, EnteredList.split()))
                self.splitListcopy1=self.splitList.copy()
                self.textZone.setStyleSheet("font-size: 25px; font-weight:bold ; color:green;")
                self.etatZone.setStyleSheet("color: green; font-size:25px; font-weight:bold;")
                self.resZone.setStyleSheet("color: black; font-size:25px; font-weight:bold;")
                sortalg = self.sortCombo.currentText()
                if (len(self.splitList)>=2):
                    self.etatZone.setText("Vous avez entré une liste valide ✓")
                    self.animerBtn.setDisabled(False)
                    self.decroissantBtn.setDisabled(False)
                    self.croissantBtn.setDisabled(False)
                    self.resZone.setDisabled(False)
                    if (self.group.checkedButton().text()=="Croissante"):
                        if sortalg == "Tri à bulles":
                            self.resZone.setText("La liste triée en utilisant {} de façon {} est ".format(sortalg,self.group.checkedButton().text())+str(fn.bubbleSortNG(self.splitListcopy1)))
                        elif sortalg == "Tri par insertion":
                            self.resZone.setText("La liste triée en utilisant {} de façon {} est ".format(sortalg,self.group.checkedButton().text())+str(fn.insertion_sortNG(self.splitListcopy1)))
                        elif sortalg == "Tri par fusion":
                            self.resZone.setText("La liste triée en utilisant {} de façon {} est ".format(sortalg,self.group.checkedButton().text())+str(fn.merge_sortNG(self.splitListcopy1)))
                        elif sortalg == "Tri rapide":
                            self.resZone.setText("La liste triée en utilisant {} de façon {} est ".format(sortalg,self.group.checkedButton().text())+str(fn.quick_sortNG(self.splitListcopy1, 0, len(self.splitListcopy1) - 1)))
                        else:
                            self.resZone.setText("La liste triée en utilisant {} de façon {} est ".format(sortalg,self.group.checkedButton().text())+str(fn.selection_sortNG(self.splitListcopy1)))
                    else:
                        if sortalg == "Tri à bulles":
                            self.resZone.setText("La liste triée en utilisant {} de façon {} est ".format(sortalg,self.group.checkedButton().text())+str(fn.bubbleSortNG(self.splitListcopy1)[::-1]))
                        elif sortalg == "Tri par insertion":
                            self.resZone.setText("La liste triée en utilisant {} de façon {} est ".format(sortalg,self.group.checkedButton().text())+str(fn.insertion_sortNG(self.splitListcopy1)[::-1]))
                        elif sortalg == "Tri par fusion":
                            self.resZone.setText("La liste triée en utilisant {} de façon {} est ".format(sortalg,self.group.checkedButton().text())+str(fn.merge_sortNG(self.splitListcopy1)[::-1]))

                        elif sortalg == "Tri rapide":
                            self.resZone.setText("La liste triée en utilisant {} de façon {} est ".format(sortalg,self.group.checkedButton().text())+str(fn.quick_sortNG(self.splitListcopy1, 0, len(self.splitListcopy1) - 1)[::-1]))
                        else:
                            self.resZone.setText("La liste triée en utilisant {} de façon {} est ".format(sortalg,self.group.checkedButton().text())+str(fn.selection_sortNG(self.splitListcopy1)[::-1]))
                else:
                    self.textZone.setStyleSheet("color: black; font-size:25px; font-weight:bold;")
                    self.etatZone.setText("Entrer une liste d'entiers")
                    self.etatZone.setStyleSheet("color: black; font-size:25px; font-weight:bold;")
                    self.resZone.clear()
                    self.animerBtn.setDisabled(True)
                    self.decroissantBtn.setDisabled(True)
                    self.croissantBtn.setDisabled(True)
                    self.resZone.setDisabled(True)
            else:
                self.etatZone.setText("Entrer une liste d'entiers")
                self.etatZone.setStyleSheet("color: black; font-size:25px; font-weight:bold;")
                self.resZone.clear()
                self.textZone.setStyleSheet("color: black; font-size:25px; font-weight:bold;")

        except:
            self.textZone.setStyleSheet("font-size: 25px; font-weight:bold;color:red;")
            self.animerBtn.setDisabled(True)
            self.decroissantBtn.setDisabled(True)
            self.croissantBtn.setDisabled(True)
            self.resZone.setDisabled(True)
            self.etatZone.setText(Errortext)
            self.etatZone.setStyleSheet("color: red; font-size:25px; font-weight:bold;")
            self.resZone.setText(Errortext)
            self.resZone.setStyleSheet("color: red; font-size:25px; font-weight:bold;")
    def showalg(self):
        self.algZone.setStyleSheet("font-size: 25px;")
        sortalg = self.sortCombo.currentText()
        if sortalg == "Tri à bulles":
            self.algZone.setText("""PROCEDURE tri_bulle ( TABLEAU a[1:n])
passage ← 0
REPETER
    permut ← FAUX
    POUR i VARIANT DE 1 A n - 1 - passage FAIRE
        SI a[i] > a[i+1] ALORS
            echanger a[i] ET a[i+1]
            permut ← VRAI
        FIN SI
    FIN POUR
    passage ← passage + 1
TANT QUE permut = VRAI;""")
        elif sortalg == "Tri par insertion":
            self.algZone.setText("""PROCEDURE tri_Insertion ( Tableau a[1:n])
    POUR i VARIANT DE 2 A n FAIRE
        INSERER a[i] à sa place dans a[1:i-1];
FIN PROCEDURE;""")
        elif sortalg == "Tri par fusion":
            self.algZone.setText("""PROCEDURE tri_fusion ( TABLEAU a[1:n])
FAIRE
    SI TABLEAU EST VIDE RENVOYER TABLEAU
    gauche = partie_gauche de TABLEAU
    droite = partie_droite de TABLEAU
    gauche = tri_fusion gauche
    droite = tri_fusion droite
    renvoyer fusion gauche droite
    POUR i VARIANT DE 1 A n - 1 - passage FAIRE
        SI a[i] > a[i+1] ALORS
            echanger a[i] ET a[i+1]
            permut ← VRAI
        FIN SI
    FIN POUR
    passage ← passage + 1
FIN PROCEDURE;""")
        elif sortalg == "Tri rapide":
            self.algZone.setText("""Procedure tri_rapide (tableau [1:n], gauche, droit )
DEBUT
  (* mur marque la separation entre les elements plus petits et ceux plus grands que pivot*)
  mur ← gauche;
  (* On prend comme pivot l element le plus a droite *)
  pivot ← tableau[droit];  
  placer a gauche de mur tout les elements plus petits
  placer a droite de mur tout les element plus grands
  (* On place correctement le pivot *)
  placer le pivot a la place de mur
  (* On poursuit par recursivite *)
  SI (gauche<mur-1) ALORS tri_rapide(tableau,gauche,mur-1);
  SI (mur+1<droit) ALORS tri_rapide(tableau,mur,droit);
FIN;""")
        else:
            self.algZone.setText("""PROCEDURE tri_Selection ( Tableau a[1:n])
    POUR i VARIANT DE 1 A n - 1 FAIRE
        TROUVER [j] LE PLUS PETIT ELEMENT DE [i + 1:n];
        ECHANGER [j] ET [i];
FIN PROCEDURE;""")
    def showAnim(self):
        self.splitListcopy2=self.splitList.copy()
        sortalg = self.sortCombo.currentText()
        if sortalg == "Tri à bulles":
            generator = fn.bubblesort(self.splitListcopy2)
        elif sortalg == "Tri par insertion":
            generator = fn.insertionsort(self.splitListcopy2)
        elif sortalg == "Tri par fusion":
            generator = fn.mergesort(self.splitListcopy2, 0, len(self.splitListcopy2)- 1)
        elif sortalg == "Tri rapide":
            generator = fn.quicksort(self.splitListcopy2, 0, len(self.splitListcopy2) - 1)
        else:
            generator = fn.selectionsort(self.splitListcopy2)
        title = sortalg
        fig, ax = plt.subplots()
        ax.set_title(title)
        bar_rects = ax.bar(range(len(self.splitListcopy2)), self.splitListcopy2, align="center")
        text = ax.text(0.02, 0.95, "", transform=ax.transAxes)
        iteration = [0]
        def update_fig(A, rects, iteration):
            for rect, val in zip(rects, A):
                rect.set_height(val)
                rect.set_color("green")
            iteration[0] += 1
            text.set_text(" Nombre d'opérations effectué : {}".format(iteration[0]))

        anim = animation.FuncAnimation(fig, func=update_fig,
                                       fargs=(bar_rects, iteration), frames=generator, interval=1,
                                       repeat=False)
        plt.show()
def main():
    app = QtWidgets.QApplication(sys.argv)
    form = designWindow()
    form.show()
    app.exec_()
if __name__ == "__main__":
    main()