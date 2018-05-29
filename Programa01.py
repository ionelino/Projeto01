# Exercício 3/1190
    
Lc = float(input('Digite o comprimento do cabo em m:'))
D = float(input('Digite a distância em linha reta de AD em m:'))
BC = float(input('Digite o comprimento BC em m: '))
P1 = float(input('Digite o peso do semáforo 1 em N: '))
P2 = float(input('Digite o pedo do semáforo 2 em N: '))
 
Eq = print ('As equações são: ')
Eq1 = print ('AB +', BC, '+ CD =', Lc)
Eq2 = print ('ABcosα +', BC, '+ CDcosγ  = 10.5')
Eq3 = print ('ABsenα = CDSsenγ')
Eq4 = print ('-TABcosα + TBC = 0')
Eq5 = print ('TABsenα -', P1, '= 0')
Eq6 = print ('-TBC + TCDcosγ = 0')
Eq7 = print ('TCDsenγ -', P2, '= 0')