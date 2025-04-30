# **Subnetting de IPv4 clase C en Python**
Este programa permite realizar subnetting a las direcciones IP de clase C. Imprime en la terminal las direcciones IP de las subredes válidas y los nodos válidos para cada subred.

## Características del programa

- Calcula las subredes válidas a partir de una dirección IP de clase C.
- Imprime la primera y última dirección IP en cada subred.
- Muestra la dirección de broadcast y la máscara de subred.
- Verifica la validez de las direcciones de nodos.

## **Requisitos**
- Python 3.6+.
- No requiere ninguna librería externa.

## **Instrucciones de instalación**

1. Asegúrate de tener Python 3.6 o superior instalado en tu sistema. Lo puedes verificar así:
```bash
   python --version
```
2. Clona este repositorio o descarga el archivo `main.py` a tu máquina.
3. Ejecuta el archivo y proporciona la dirección IP
4. Después proporciona cuantos bits quieres "robar" y si quieres formato binario.
5. Se imprimirán las direcciones de las subredes válidas, y de sus hosts válidos, también las direcciones de broadcast.

## Ejemplo de salida
```bash
$ python main.py
Introduce la dirección IP para hacer Subnetting: 192.168.45.87
Máscara: 255.255.255.0 (192.168.45.87/24)
¿Cuántos bits quieres robar? (2-6): 5
¿Quieres formato binario? Si/No: No
Subredes útiles posibles: 30
Hosts por subred: 6
Nueva máscara: 255.255.255.248
1º Subred útil: 192.168.45.0
1º Subred útil (1º nodo válido): 192.168.45.1
1º Subred útil (2º nodo válido): 192.168.45.2
1º Subred útil (3º nodo válido): 192.168.45.3
1º Subred útil (4º nodo válido): 192.168.45.4
1º Subred útil (5º nodo válido): 192.168.45.5
1º Subred útil (6º nodo válido): 192.168.45.6
1º Subred útil (Dirección de broadcast): 192.168.45.7
2º Subred útil: 192.168.45.8
2º Subred útil (1º nodo válido): 192.168.45.9
2º Subred útil (2º nodo válido): 192.168.45.10
```

## Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.