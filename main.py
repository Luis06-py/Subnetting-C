import re

def preguntar():
	patron = r'^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
	ip = input("Introduce la dirección IP para hacer Subnetting: ")
	print (f"Máscara: 255.255.255.0 ({ip}/24)")
	if bool(re.match(patron, ip)):
		return ip
	else:
		return False
	
def subnetting(ip, bits, binary):
	ceros = 8-bits
	subredes = 2**bits-2
	hosts = 2**ceros-2
	print ("Subredes útiles posibles: "+str(subredes))
	print ("Hosts por subred: "+str(hosts))

	octetos = ip.split(".")
	ip_base = ".".join(octetos[:3]) + "."
	octetoL = int('1' * bits + '0' * ceros, 2)
	print (f"Nueva máscara: 255.255.255.{octetoL}")

	for i in range(subredes): # De 0 a SubRedes - 1
		dirSubred = str(bin(i)[2:].zfill(bits))
		binario = dirSubred+str(bin(0)[2:].zfill(ceros))
		if binary == False:
			print (f"{i+1}º Subred útil: "+ip_base+(str(int(binario, 2))))
		else:
			print (f"{i+1}º Subred útil: "+ip_base+binario)
		for j in range(1, hosts+2): # 1 - hosts, la última es de broadcast
			if j == hosts+1:
				txt = "Dirección de broadcast"
			else:
				txt = f"{j}º nodo válido"
			binario2 = dirSubred+str(bin(j)[2:].zfill(ceros))
			if binary == False:
				print(f"{i+1}º Subred útil ({txt}): "+ip_base+(str(int(binario2, 2))))
			else:
				print(f"{i+1}º Subred útil ({txt}): "+ip_base+binario2)

	
	
if __name__ == '__main__':
	ip = preguntar()
	if ip:
		bits = input("¿Cuántos bits quieres robar? (2-6): ")
		bits = int(bits)
		if bits >= 2 and bits <= 6:
			x = input("¿Quieres formato binario? Si/No: ")
			if x == "Si":
				subnetting(ip, bits, True)
			else:
				subnetting(ip, bits, False)