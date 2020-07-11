from typing import TypedDict, List

class responseIsMutant(TypedDict):
    idMsj: int
    msj: str
    valid: bool

class Mutants:
    @staticmethod
    def isMutant(cadenaAdn):
        ResIsMutant = responseIsMutant
        if not cadenaAdn:
            ResIsMutant.idMsj = 1
            ResIsMutant.msj = 'Matriz Inválida'
            ResIsMutant.valid = False
            return ResIsMutant
        columnas = len(cadenaAdn[0])
        filas = len(cadenaAdn)
        i=0
        while i<filas :
            if columnas != len(cadenaAdn[i]) :
                ResIsMutant.idMsj = 2
                ResIsMutant.msj = 'Logitud Inválida'
                ResIsMutant.valid = False
                return ResIsMutant
            cadenaAdn[i] = cadenaAdn[i].upper()
            i+=1

        MinLenghtArray = 4
        if columnas < MinLenghtArray:
            ResIsMutant.idMsj = 2
            ResIsMutant.msj = 'Columnas menor a 4.'
            ResIsMutant.valid = False
            return ResIsMutant

        countHorizontal = 0
        countVertical = 0
        countDiagLR = 0
        countDiagRL = 0
        i=0
        
        while i < columnas :
            j =0
            hor = 1;vert = 1
            diag11 = 1;diag12 = 1
            diag21 = 1;diag22 = 1
            while j < columnas:
                #Validacion de Caracteres
                if(cadenaAdn[i][j] != 'A' and cadenaAdn[i][j] != 'T' and cadenaAdn[i][j] != 'C' and cadenaAdn[i][j] != 'G'):
                    ResIsMutant.idMsj = 3
                    ResIsMutant.msj = 'caracter no soportado'
                    ResIsMutant.valid = False
                    return ResIsMutant

                #Validacion forma horizontal
                if j+1 < columnas and cadenaAdn[i][j] == cadenaAdn[i][j+1] :
                    hor = hor + 1
                else:
                    if hor >= MinLenghtArray :
                        countHorizontal = countHorizontal + 1
                    hor = 1
                    
                #validacion vertical
                if j+1 < columnas and cadenaAdn[j][i] == cadenaAdn[j+1][i] :
                    vert = vert + 1
                else:
                    if vert >= MinLenghtArray :
                        countVertical = countVertical + 1
                    vert = 1

                #Validacion diagonal izquierda - derecha 
                if j+i+1 < columnas and cadenaAdn[j][j+i] == cadenaAdn[j+1][j+i+1]:
                    diag11 = diag11 + 1
                else:
                    if diag11 >= MinLenghtArray :
                        countDiagLR = countDiagLR + 1
                    diag11 = 1
                if j+i>j and j+i+1 < columnas and cadenaAdn[j+i][j] == cadenaAdn[j+i+1][j+1]:
                    diag12 = diag12 + 1
                else:
                    if diag12 >= MinLenghtArray :
                        countDiagLR = countDiagLR + 1
                    diag12 = 1

                #Validacion diagonal derecha - izquiera
                if columnas-1-j+i < columnas and j+1 < columnas and cadenaAdn[j][columnas-1-j+i] == cadenaAdn[j+1][columnas-1-j+i-1]:
                    diag21 = diag21 + 1
                else:
                    if diag21 >= MinLenghtArray :
                        countDiagRL = countDiagRL + 1
                    diag21 = 1
                if i > 0 and columnas-1-j-i-1 >= 0 and j+1 < columnas and cadenaAdn[j][columnas-1-j-i] == cadenaAdn[j+1][columnas-1-j-i-1]:
                    diag22 = diag22 + 1
                else:
                    if diag22 >= MinLenghtArray :
                        countDiagRL = countDiagRL + 1
                    diag22 = 1
                if countHorizontal+countVertical+countDiagLR+countDiagRL > 1 :
                    ResIsMutant.idMsj = 4
                    ResIsMutant.msj = 'Es Mutante'
                    ResIsMutant.valid = True
                    # print('counth:%s countv:%s countobl1:%s countobl2:%s flag:%s'%(countHorizontal,countVertical,countDiagLR,countDiagRL,ResIsMutant.valid))
                    return ResIsMutant
                j = j + 1
            i = i + 1
        ResIsMutant.idMsj = 5
        ResIsMutant.msj = 'No es mutante'
        ResIsMutant.valid = False
        # print('counth:%s countv:%s countobl1:%s countobl2:%s flag:%s'%(countHorizontal,countVertical,countDiagLR,countDiagRL,ResIsMutant.valid))
        return ResIsMutant