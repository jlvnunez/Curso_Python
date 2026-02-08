#Dissecando uma variavel

a = input('Digite algo: ')
print('O tipo primitivo desse valor é :',type (a))
print('So tem espaços?',a.isspace())
print('É Numerico?',a.isnumeric())
print('É Alfabetico?',a.isalpha())
print('É Alfanumerico?',a.isalnum())
print('É Maiusculo?',a.isupper())
print('É Minusculo?',a.islower())
print('Está Capitalizada?',a.istitle())