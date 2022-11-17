def generate_pipe_file(fileName,v=0,l=0,p=0,dp=0,t=0,q=0,curva90=0,codo90=0,reduccion=0,TDiv=0,TDir=0,valvBola=0,llavePaso=0,name=""):
    if not fileName.endswith(".pipe"):
        raise ValueError

    with open(fileName,"w") as file:
        file.write("<pipe>\n")
        file.write(f"name : {name} \n")
        file.write(f"v : {v} \n")
        file.write(f"l : {l} \n")
        file.write(f"p : {p} \n")
        file.write(f"dp : {dp} \n")
        file.write(f"t : {t} \n")
        file.write(f"q : {q} \n")
        file.write(f"curva 90 : {curva90} \n")
        file.write(f"codo 90 : {codo90} \n")
        file.write(f"reduccion : {reduccion} \n")
        file.write(f"t divergente : {TDiv} \n")
        file.write(f"t directa : {TDir} \n")
        file.write(f"valvula bola : {valvBola} \n")
        file.write(f"llave paso : {llavePaso} \n")
        file.write("<\pipe>")

def check_pipe_file(fileName):

    if not fileName.endswith(".pipe"):
        raise ValueError            
    fileLines = []
    keys = ["v","l","p","dp","t","q","curva 90","codo 90","reduccion","t divergente","t directa","valvula bola","llave paso","name"]
    with open(fileName) as file:
        for  line in file:
            fileLines.append(line.strip("\n"))
    if not len(fileLines) ==  16:
        raise ValueError
    try:
        for line in fileLines[1:-1]:
            key, value = line.split(" : ")
            if not key in keys:
                raise ValueError
            if not key == "name":
                value = float(value)
    except:
        raise ValueError
    if not fileLines[0] == "<pipe>":     
        raise ValueError
    if not fileLines[15] == "<\pipe>":
        raise ValueError
    return True

def pipe_to_py_parser(fileLines):
    d = {}
    for line in fileLines[1:-1]:
        k,v = line.split(" : ")
        if k == "name":
            d[k] = v
        else:
            d[k] = float(v)
    return d