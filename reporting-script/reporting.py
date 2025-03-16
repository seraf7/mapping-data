import argparse
import os 
from os.path import abspath, join, getsize

# Ejemplo de ejecucion
# python3 reporting.py /home/seraf/Documentos/

def obten_archivos(path):
    reporte = {}
    for top_dir, directorios, archivos in os.walk(path):
        for arch in archivos:
            # Obtiene ruta completa del archivo
            ruta = abspath(join(top_dir, arch))
            # Obtiene tamanio de archivo
            tam = os.path.getsize(ruta)
            reporte[ruta] = tam
    return reporte

def imprime_completo(reporte):
    for archivo in reporte.keys():
        print(archivo)

def imprime_top(reporte):
    i = 0
    for archivo in reporte.keys():
        print("PATH: {0}, SIZE: {1}".format(archivo, reporte[archivo]))
        i += 1
        if i > 10:
            break

def imprime_size(reporte, size):
    for archivo in reporte.keys():
        if reporte[archivo] >= size:
            print("SIZE: {1} | PATH: {0}".format(archivo, reporte[archivo]))

# Impresion de reporte completo
# Impresion de reporte con cantidad especifica
# Impresion de reporte para tamanio especifico

def main():
    # Instancia del parser de argumentos
    parser = argparse.ArgumentParser()

    # Agregamos argumentos para procesar
    parser.add_argument('path', help='Ruta requerida para analizar')

    parser.add_argument('-t', '--top', action='count', default=0)

    parser.add_argument('-s', '--size', type=int, nargs=1)

    # Procesa argumentos
    args = parser.parse_args()

    # Valida ruta
    if args.path != "":
        #print("Ruta: ", args.path)
        #print("Top:", args.top)
        #print("Size: ", args.size)
        reporte = obten_archivos(args.path)

        if args.top:
            imprime_top(reporte)
        elif args.size and args.size[0] > 0:
            imprime_size(reporte, args.size[0])
        else:
            imprime_completo(reporte)
    else:
        parser.error("Se debe especificar ruta de analisis")

if __name__ == "__main__":
    main()

