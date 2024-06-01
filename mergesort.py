# Funktion zum Zuweisen von Werten von einer Liste zu einer anderen an bestimmten Indizes
def ASSIGNMENT(new_list, i, old_list, j):
    new_list[i] = old_list[j]

# Funktion zur Implementierung des Merge-Sort-Algorithmus
def mergeSort(liste_zum_sortieren):
    # Überprüfen, ob die Liste mehr als ein Element hat
    if len(liste_zum_sortieren) > 1:
        # Finden des mittleren Index der Liste
        mitte = len(liste_zum_sortieren) // 2
        
        # Die Liste in zwei Hälften aufteilen
        links = liste_zum_sortieren[:mitte]
        rechts = liste_zum_sortieren[mitte:]

        # Rekursiver Aufruf von mergeSort für die linke und rechte Hälfte
        mergeSort(links)
        mergeSort(rechts)

        # Zusammenführen der sortierten Hälften
        l = 0
        r = 0
        i = 0
        
        # Zusammenführen der beiden Hälften unter Beibehaltung der sortierten Reihenfolge
        while l < len(links) and r < len(rechts):
            if links[l] <= rechts[r]:
                ASSIGNMENT(new_list=liste_zum_sortieren, i=i, old_list=links, j=l)
                l += 1
            else:
                ASSIGNMENT(new_list=liste_zum_sortieren, i=i, old_list=rechts, j=r)
                r += 1
            i += 1

        # Hinzufügen der verbleibenden Elemente aus der linken Hälfte
        while l < len(links):
            liste_zum_sortieren[i] = links[l]
            l += 1
            i += 1

        # Hinzufügen der verbleibenden Elemente aus der rechten Hälfte
        while r < len(rechts):
            liste_zum_sortieren[i] = rechts[r]
            r += 1
            i += 1

# Importieren der matplotlib-Bibliothek für das Plotten
import matplotlib.pyplot as plt

# Definition der unsortierten Liste
meine_liste = [54, 26, 93, 17, 77, 31, 44, 55, 20]

# Plotten der unsortierten Liste
x = range(len(meine_liste))
plt.plot(x, meine_liste)
plt.title('Unsortierte Liste')
plt.xlabel('Index')
plt.ylabel('Wert')
plt.show()

# Sortieren der Liste mit Merge-Sort
mergeSort(meine_liste)

# Plotten der sortierten Liste
x = range(len(meine_liste))
plt.plot(x, meine_liste)
plt.title('Sortierte Liste')
plt.xlabel('Index')
plt.ylabel('Wert')
plt.show()
