from prettytable import PrettyTable

# Cria a tabela
x = PrettyTable(["Nome da cidade", "UF", "População", "IDH-M", "Renda per Capita"])

# Alinha as colunas
x.align["Nome da cidade"] = "l"
x.align["UF"] = "l"
x.align["População"] = "r"
x.align["IDH-M"] = "r"
x.align["Renda per Capita"] = "r"

# Deixa um espaço entre a borda das colunas e o conteúdo (default)
x.padding_width = 1

x.add_row(["São Paulo","SP", 12106920, 0.805, 54358]) 
x.add_row(["Rio de Janeiro","RJ", 6520266, 0.799, 49527]) 
x.add_row(["Belo Horizonte", "MG", 2523794, 0.810, 35187]) 
x.add_row(["Porto Alegre", "RS", 1484941, 0.805, 46122]) 
x.add_row(["Salvador", "BA", 2953986, 0.759, 19812]) 
x.add_row(["Recife", "PE", 1633697, 0.772, 29701]) 
x.add_row(["Brasília", "DF", 3039444, 0.824, 73971])

x.del_row(0)
print(x)