#Faça um Programa que peça as 4 notas bimestrais e mostre a média.
Lnota= []
for nota in range(1,5):
	nota = float(input(f"Digite a {nota} nota: "))
	Lnota.append( nota )
	
	
mediaAnual = sum(Lnota)/4

print("A media foi: %.2f" % (mediaAnual ))