  # Author: Francisco Varela
  #10/05/2022
  #CEMES
from chantillon import *
from printdoc import *
test ="Y"
while(test=="Y"):

    if __name__ == '__main__':
        print("")

        print("******* DONNES DU ECHANTILLON *********** ")
        print("Signal Periodique  type :   n pts P% Fc[GS/s] ")
        print("type_signal  : sinus/Square [1/2] : ", end="")
        type_signal = int(input()) # Chosir le type de signal
        # n points  à chaque carreua alors n*2 dans un periode
        if (type_signal==1 or type_signal==2) :
            print("Nombres de points : ", end="")
            n = float(input()) * type_signal

            if type_signal==2:
                print("Pourcentage de Gating [%] : ", end="")
                P = float(input())
            print("Frequence de chantillonnage [GS/s] : ", end="")
            Fc = float(input())
            # P_ech point de echantillon Rechantillon par segundo
            if type_signal==2:
                t,f,t_unit,tg= type_square(Fc,n,P)  # unité en nano ns
            else :
                t, f, t_unit= type_sinus(Fc, n)
                tg=0
            printdoc(n, t, f, tg, t_unit,type_signal)  #ecrire sur un document
            print("********PRESENTATION DES VALEURS  ******* ")
            print("")
            print("{:.1E}pts dans un  Periode de T= {:.1E}s".format(n,t*float(0.000000001)))
            print("Frequence de {:.2}Hz ".format(f*1000000,'.1E'))
            if type_signal == 2:
                print("Temps Gating tg = {:.1E}s ".format(tg*float(0.000000001)))

            print("Il fait  1pt en {:.1E}s \n".format(t_unit * float(0.000000001)))
            print("\n************TABOR FINISHED ************** ")
            print("Nouveau calcul ? [Y/N]: ", end="")
            test = str(input())
        else :
            print("Value NOT evailable")



# See PyCharm help at https://www.jetbrains.com/help/pycharm/

