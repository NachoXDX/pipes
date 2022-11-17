from pipe_static import accesorios,diametrosComerciales
from pipe_interpolator import createInterpolator

class PipeLine:    

    def __init__(self,dict):
        self.name = dict["name"]
        self.v = dict["v"]
        self.l = dict["l"]
        self.p = dict["p"]*0.986923
        self.dp = dict["dp"]
        self.t = dict["t"] + 273
        self.q = dict["q"]
        self.curva_90 = dict["curva 90"]
        self.codo_90 = dict["codo 90"]
        self.reduccion = dict["reduccion"]
        self.t_divergente = dict["t divergente"]
        self.t_directa = dict["t directa"]
        self.valvula_bola = dict["valvula bola"]
        self.llave_paso = dict["llave paso"]
        self.b = self.getB()
        self.fd = self.convertToComercial(self.calculateDiameter(self.l))
        self.le = self.calculateEquivalentLength()
        self.d = self.convertToComercial(self.calculateDiameter(self.le))

    def getB(self):
        f = createInterpolator()
        return f((self.q*0.078))

    def calculateDiameter(self,leng):
        return ((self.b*(self.v**2)*(leng)*self.p)/((29.27)*(self.t)*(self.p * (self.dp/100))))/(25.4)
    
    def convertToComercial(self,diam):
        delta = 100
        for diams in diametrosComerciales:
            tmpdelta = diametrosComerciales[diams] - diam
            if tmpdelta > 0 and tmpdelta < delta:
                delta = tmpdelta
                tmpkey = diams
        try:
            return tmpkey
        except:
            raise ValueError
    
    def calculateEquivalentLength(self):
        le = self.l
        le += self.curva_90 * accesorios[self.fd]["curva 90"]
        le += self.codo_90 * accesorios[self.fd]["codo 90"]
        le += self.reduccion * accesorios[self.fd]["reduccion"]
        le += self.t_divergente * accesorios[self.fd]["t divergente"]
        le += self.t_directa * accesorios[self.fd]["t directa"]
        le += self.valvula_bola * accesorios[self.fd]["valvula bola"]
        le += self.llave_paso * accesorios[self.fd]["llave paso"]
        return le

    def reCalculate(self):
        self.fd = self.convertToComercial(self.calculateDiameter(self.l))
        self.le = self.calculateEquivalentLength()
        self.d = self.convertToComercial(self.calculateDiameter(self.le))

    def getData(self):
        return [self.name,self.v,self.l,self.le,self.p,self.dp,self.t,self.q,self.b,self.fd,self.d]

    def getDataKeys(self):
        return ["Tramo","V [m/s]","L [m]","Le [m]","P [atm]","dP [%]","T [K]","Q [l/m]","B","D1 [in]","Df [in]"]

    def getAdvancedData(self):
        return [self.name,self.v,self.l,self.le,self.p,self.dp,self.t,self.q,self.b,self.fd,self.d,self.calculateDiameter(self.l),self.calculateDiameter(self.le)]

    def getAdvancedDataKeys(self):
        return ["Tramo","V [m/s]","L [m]","Le [m]","P [bar]","dP [%]","T [K]","Q [l/m]","B","D1 [in]","Df [in]","D1 no normalizado [in]","Df no normalizado [in]"]
        # def convertToComercial(self,diam):
    #     if diam < 3/8:
    #         return "3/8"
    #     elif diam < 1/2:
    #         return "1/2"
    #     elif diam < 3/4:
    #         return "3/4"
    #     elif diam < 1:
    #         return "1"
    #     elif diam < 1.25:
    #         return "1 1/4"
    #     elif diam < 1.5:
    #         return "1 1/2"
    #     elif diam < 2:
    #         return "2"
    #     elif diam < 2.5:
    #         return "2 1/2"
    #     elif diam < 3:
    #         return "3"
    #     elif diam < 4:
    #         return "4"
    #     else:
    #         raise ValueError