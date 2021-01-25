 # LORENZO E' PASSATO DI QUI

n = int(input("inserisci il numero di quante lettere vuoi che cambi: "))
array = "ciao"
codice = ""
n = n%26
for i in array:
	if (n>26):
		n-26	
	x = ord(i)+n
	x = chr(x)
	codice = codice+x
print(codice)