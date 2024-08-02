import os

def main():
	nombre = os.getenv("USERNAME")
	lenguaje = os.getenv("LANGUAGE")
	print('Triggers')
	print(f"¡Hola, {nombre} desde Github!, tu lenguaje seleccionado es: {lenguaje}")

if __name__ == '__main__':
	main()
