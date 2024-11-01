#Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.
medida = float(input('Digite uma distancia em metros: '))
cm = medida*100
mm = medida*1000

print('a media de {}, corresponde a {:.0f}cm e {:.0f}mm'.format(medida,cm,mm))
 
