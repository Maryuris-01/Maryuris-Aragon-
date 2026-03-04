import time

# 🌈 Colores ANSI
ROSADO = "\033[95m"
AZUL = "\033[94m"
GREEN = "\033[92m"
AMARILLO = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"

from colorama import init, Fore, Back

init(autoreset=True)



# Calculadora 

print("╔══════════════════╗")
print(" 🌸 CALCULADORA 🌸 ")
print("╚══════════════════╝")
print(Fore.MAGENTA + "Iniciando programa...")

for i in range(5, 0, -1):
    print(f"⏳ {i}... ")
    time.sleep(1)

print(Fore.LIGHTYELLOW_EX+ "🌷 ¡Comenzamos! 🌷")
print(Fore.LIGHTMAGENTA_EX + "¿Qué quieres hacer hoy?")
print(Fore.RED + "1. Suma")
print(Fore.RED + "2. Resta")
print(Fore.RED + "3. Multiplicacion")
print(Fore.RED + "4. Division")
print(Fore.RED + "5. Salir")


Opcion = int(input(f"{ROSADO}Escoja una opción:\n {RESET}"))


if Opcion == 1:
    Numero1 = float(input(f"{AMARILLO}Ingrese el primer numero: \n {RESET}"))
    Numero2 = float(input(f"{AMARILLO}Ingrese el segundo numero: \n{RESET}"))
    Resultado = Numero1 + Numero2
    print(Back.LIGHTYELLOW_EX+ Fore.BLACK+"El resultado de la suma es:", Resultado)
    
elif Opcion == 2:
    Numero1 = float(input(f"{AMARILLO} Ingrese el primer número \n {RESET}"))
    Numero2 = float(input(f"{AMARILLO}Ingrese el segundo número \n {RESET}"))
    Resultado = Numero1 - Numero2
    print(Back.LIGHTYELLOW_EX + Fore.WHITE + "El resultado de la resta es:", Resultado)
    
elif Opcion == 3:
    Numero1 = float(input(f"{AMARILLO}Ingrese el primer número \n{RESET}"))
    Numero2 = float(input(f"{AMARILLO}Ingrese el segundo número \n{RESET}"))
    Resultado = Numero1 * Numero2
    print(Back.LIGHTYELLOW_EX + Fore.BLACK + "El resultado de la multiplicación es de:", Resultado)
    
elif Opcion == 4:
    Numero1 = float(input(f"{AMARILLO}Ingrese el primer número \n{RESET}"))
    NUmero2 = float(input(f"{AMARILLO}Ingrese el segundo número \n{RESET}"))
    Resultado = Numero1 / NUmero2
    print(Back.LIGHTYELLOW_EX + Fore.WHITE + "El resultado de la división es de:" , Resultado)
    
else:
    Opcion == 5
    print(f"{ROSADO}🌷 Gracias por usar la calculadora. ¡Adiós! 💕{RESET}")
    
    
    
    