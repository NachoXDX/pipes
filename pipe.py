import sys
import os
from tabulate import tabulate
from pipe_static import accesorios
from pipe_classes import PipeLine
from pipe_core_functions import generate_pipe_file, pipe_to_py_parser, check_pipe_file

def main():
    if len(sys.argv) == 1:
        print("Uso: ")
        print("-n archivo  | Nuevo archivo con wizard")
        print("-b archivo  | Nuevo archivo vacio")
        print("-c archivo  | Calculo del archivo")
        print("-i archivo  | Calculo iterativo del archivo")
        print("-t carpeta  | Calculo de todos los archivos de la carpeta")
        print("-v archivo  | Validar archivo")
        print("-r archivo  | Calcular archivo cambiando v y dp")
        sys.exit()
    if sys.argv[1] == "-n":

        newFile(sys.argv[2])

    if sys.argv[1] == "-c":
        
        pipe1 = instanceatePipeObjFromFile(sys.argv[2])
        print(tabulate([pipe1.getAdvancedData()],pipe1.getAdvancedDataKeys()))

        sys.exit()
    if sys.argv[1] == "-b":

        newBlankFile(sys.argv[2])
        sys.exit()

    if sys.argv[1] == "-i":
        results = iteration(sys.argv[2]) 
        print(tabulate(results,PipeLine.getDataKeys(""),tablefmt="grid"))
    
    if sys.argv[1] == "-t":

        results = calculateProject(sys.argv[2])

        print(tabulate(results,PipeLine.getDataKeys(""),tablefmt="grid"))
        sys.exit()

    if sys.argv[1] == "-v":
        try:
            check_pipe_file(sys.argv[2])
        except:
            print("Invalid!")
            sys.exit()
        else:
            print("Valid!")
            sys.exit()
    if sys.argv[1] == "-r":

        results = recalculate(sys.argv[2])
        print(tabulate(results,PipeLine.getDataKeys(""),tablefmt="grid"))

def newFile(fileName):
        name = input("Nombre = ") 
        v = input("Velocidad (m/s) = ")
        l = input("Longitud (m) = ")
        p = input("Presion (bar) = ")
        dp = input("Caida de presion (x%) = ")
        t = input("Temperatura (C) = ")
        q = input("Caudal [l/m] = ")
        curva90 = input("Curva 90 = ") 
        codo90 = input("Codo 90 = ") 
        reduccion = input("Reduccion = ") 
        tDivergente =  input("T Divergente = ")
        tDirecta = input("T Directa = ") 
        valvulaBola = input("Valvula de Bola = ") 
        llavePaso = input("Llave de Paso = ")
        generate_pipe_file(fileName,v,l,p,dp,t,q,curva90,codo90,reduccion,tDivergente,tDirecta,valvulaBola,llavePaso,name)
        sys.exit()

def newBlankFile(fileName):
        generate_pipe_file(fileName)
        
def iteration(fileName):
        
        pipeObj = instanceatePipeObjFromFile(fileName)
        results = []

        
        vmin = float(input("v min: "))
        vmx = float(input("v mx: "))
        iterv = int(input("Iteraciones: "))-1 
        stepv = (vmx - vmin)/iterv
        
        dpmin = float(input("dp min: "))
        dpmx = float(input("dp mx: "))
        iterdp = int(input("Iteraciones: "))-1 
        stepdp = (dpmx - dpmin)/iterdp
        
        
        for i in range(iterv+1):
            pipeObj.v = vmin + i*stepv    
            for j in range(iterdp+1):
                pipeObj.dp = dpmin + j*stepdp
                pipeObj.reCalculate()
                results.append(pipeObj.getData())

        return results

def instanceatePipeObjFromFile(fileName):
        try:
            check_pipe_file(fileName)
        except:
            sys.exit("Invalid file")
        else:
            with open(fileName) as file:
                fileLines = []
                for line in file:
                    fileLines.append(line.strip("\n"))
            pipeObj = PipeLine(pipe_to_py_parser(fileLines))
            return pipeObj

def calculateProject(projectPath):
    results = []
    
    for project in os.listdir(projectPath):
        tmpObj = instanceatePipeObjFromFile(projectPath+"/"+project)
        results.append(tmpObj.getData())

    return results 

def recalculate(fileName):
    pipeObj = instanceatePipeObjFromFile(fileName)
    v = float(input("Velocidad (m/s): "))
    dp = float(input("Delta P: "))
    pipeObj.v = v
    pipeObj.dp = dp
    pipeObj.reCalculate()
    return [pipeObj.getData()]
    
if __name__ == "__main__":
    main()