# -- coding: utf-8 --
"""
Created on Thu Mar  2 22:13:39 2023

@author: NATGF
"""

estado = ['SP','RJ', 'MG', 'ES', 'OUTROS']
faturamento = [67836.43,36678.66, 29229.88,27165.48,19849.53]


totalFat=0          
for i in range(len(faturamento)):
    totalFat = totalFat  + faturamento[i]

print( 'Total de faturamento',totalFat)
    
for i in range(len(faturamento)):
    x = (faturamento[i] * 100)/ totalFat;
    print(estado[i], 'equivale a ',x, '%')