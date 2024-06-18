# pip install prettytable
from prettytable import PrettyTable

tabela = PrettyTable(['Nome', 'Idade', 'CPF'])
tabela.add_row(['Andrew', '32', '012.345.678-90'])
tabela.add_row(['Ana', '66', '098.765.432-10'])
tabela.add_row(['Regis', '62', '246.802.468-02'])

print(tabela)
input('Aperte ENTER para sair...')