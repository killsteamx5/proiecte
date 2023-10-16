import math


def paint_calc(inaltime, latime, suprafata):
    area = inaltime*latime
    nr_can = math.ceil(area / suprafata)
    print(f"Ai nevoie de {nr_can} canistre vopsea pentru dimensiunile introduse.")


h = int(input("Inaltime perete: "))
w = int(input("Latime perete: "))
coverage = 5
paint_calc(inaltime=h, latime=w, suprafata=coverage)
