# João tem uma bicicletaria e gostaria de resgistar as vendas de suas bicicletas.
# Crie um programa onde joão informe: Cor, mdelo, ano e valor da bicicleta vendida. 
# Uma bicicleta pode: buzinar, parar e correr. Adione esse comportamentos! 

class Bicicleta:
    # Inicializando as caracteristicas
    def __init__(self, cor, modelo, ano, valor):  # Self = referencia para o  objeto/ atributos da classe
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        

    def buzinar(self):
        print("Plim plim plim")
    
    def parar(self):
        print("Parando bicicleta")
        print("Bicicleta Parada")

    def correr(self):
        print("Vrummmmmm...")

    # def __str__(self):
        #return f"Bicicleta: cor={self.cor}, modelo={self.modelo}, ano={self.ano}, valor={self.valor} " 

    # Codigo util para fazer representação de classe
    def __str__(self): 
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
    
#Instanciando a Bici
b1 = Bicicleta("Vermelha", "Caloi", 2022, 600)
b1.buzinar()
b1.correr()
b1.parar()

# Pedindo para exibir os atributos da classe 
print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = Bicicleta("Verde", "monark", 2000, 189)
b2.buzinar() # Bicileta.buzinar(b2)

print(b2)
