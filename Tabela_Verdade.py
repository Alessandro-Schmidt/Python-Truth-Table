from tabulate import tabulate

opcoes = [['Investimento:', 'Porcentagem:'], ['Ações', '50%'], ['FIIS', '20%'],['Fundos de Investimento', '20%'] ,['Tesouro Direto', '10%']] 
print(tabulate(opcoes, headers='firstrow', tablefmt='grid'))