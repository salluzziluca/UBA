########################## Apareo de Archivos #############################
# Genera un maestro actualizado, en base al archivo maestro original y las
# novedades que vienen informadas en el archivo de novedades.
# Se controla que el tipo de operación a realizar Alta, Baja o Modificacion
# sea consistente con la logica de comparacion de claves
# La funcion leerMaeNov utiliza el parametro "devolver", para en caso del
# archivo Maestro devolver 3 vacios, y en el caso del archivo Novedades,
# devolver 4 vacios
def leerMaeNov(archivo,devolver):
    linea = archivo.readline()
    linea = linea.rstrip('\n')
    return linea.split(',') if linea else devolver.split(",")

def grabar_MaeActualizado(archivo, legajo, nomApe, sueldo):
    archivo.write(legajo + ',' + nomApe + ',' + sueldo + '\n')

def grabar_error(archivo, legajo, nomApe, sueldo, tipo):
    archivo.write(legajo + ',' + nomApe + ',' + sueldo + ',' + tipo + '\n')

def aparearArchivos(arMaestro, arNovedades, arMaeActualizado, arLogErrores):
    # Tener en cuenta que en esta funcion estamos recibiendo los archivos
    # abiertos, si no estuvieramos seguros que nos encontramos al principio
    # de los archivos, antes de hacer la primer lectura, deberíamos aplicar
    # un seek(0), a arSuc1 y arSuc2, para asegurar que procesaremos los datos
    # desde el principio al final de cada archivo

    legajo_mae, nombre_mae, sueldo_mae = leerMaeNov(arMaestro,",,")
    legajo_nov, nombre_nov, sueldo_nov, tipo = leerMaeNov(arNovedades,",,,")
    
    while (legajo_mae and legajo_nov):
        if (legajo_mae < legajo_nov):
            # Va directo al nuevo archivo
            grabar_MaeActualizado(arMaeActualizado, legajo_mae, nombre_mae, sueldo_mae)
            # Vuelvo a leer Maestro
            legajo_mae, nombre_mae, sueldo_mae = leerMaeNov(arMaestro,",,")
        
        elif (legajo_mae > legajo_nov):
            # Deberia ser un alta
            if (tipo == 'A'): # si es alta la graba
                grabar_MaeActualizado(arMaeActualizado, legajo_nov, nombre_nov, sueldo_nov)
            else: # si no es alta graba en Log de Errores
                grabar_error(arLogErrores, legajo_nov, nombre_nov, sueldo_nov, tipo)
            
            # Se vuelve a leer novedades
            legajo_nov, nombre_nov, sueldo_nov, tipo = leerMaeNov(arNovedades,",,,")
        
        else: # son iguales. Deberia ser una modificacion o una baja
            if (tipo == 'M'): # actualizo
                grabar_MaeActualizado(arMaeActualizado, legajo_nov, nombre_nov, sueldo_nov)
            elif (tipo == 'A'): # va al Log de Errores
                grabar_error(arLogErrores, legajo_nov, nombre_nov, sueldo_nov, tipo)
                # En este caso, el que estaba en el Maestro, lo dejo igual
                grabar_MaeActualizado(arMaeActualizado,legajo_mae, nombre_mae, sueldo_mae)
                # Si fuese una "B" (baja), no hacemos nada
                pass
            # Leo los dos
            legajo_mae, nombre_mae, sueldo_mae = leerMaeNov(arMaestro,",,")
            legajo_nov, nombre_nov, sueldo_nov, tipo = leerMaeNov(arNovedades,",,,")

    # Del while puedo estar saliendo porque encontre el final de ambos archivos
    # o porque encontre el de solo uno. Por lo tanto, puede haber registros a
    # a procesar y debo hacerlo
    while legajo_mae:
        grabar_MaeActualizado(arMaeActualizado,legajo_mae, nombre_mae, sueldo_mae)
        legajo_mae, nombre_mae, sueldo_mae = leerMaeNov(arMaestro,",,")

    while legajo_nov:
        if (tipo == "A"):
            grabar_MaeActualizado(arMaeActualizado, legajo_nov, nombre_nov, sueldo_nov)
        else:
            grabar_error(arLogErrores, legajo_nov, nombre_nov, sueldo_nov, tipo)
        legajo_nov, nombre_nov, sueldo_nov, tipo = leerMaeNov(arNovedades,",,,")

#########################################################################

arMaestro = open("maestro.csv","r")
arNovedades = open("novedades.csv","r")
arMaeActualizado = open('maestro_actual.csv','w')
arLogErrores = open('logErrores.txt','w')

aparearArchivos(arMaestro, arNovedades, arMaeActualizado, arLogErrores)

arMaestro.close()
arNovedades.close()
arMaeActualizado.close()
arLogErrores.close()