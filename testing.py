import random

# Lista de numeros de bala usadas
used_shot = []

# Numero de recamaras
bullet_chamber = 6

# Recamara con munición
bullet = random.randint(1, bullet_chamber)

print("🎯 Bienvenido a la ruleta rusa 😃")
print(f"La pistola 🔫 tiene {bullet_chamber} recamaras...")
print(f"Ingresa un numero del 1 al 6 para escoger la recamara. Si lo dejas vacio se escogera una aleatoriamente 💀")

while True:
    # Funcion donde se gana el juego
    if len(used_shot) == bullet_chamber - 1:
        print("¡Has ganado, tienes suerte!, ¿Me subes la nota? 🥺🎉")
        break

    # Pide numero de recamara
    user_chamber = input("Seleccione una recamara (1-6): ")

    # Condicion de numero vacio escoger camara aleatoriamente
    if user_chamber == "":
        choose = [n for n in range(1, bullet_chamber + 1) if n not in used_shot]
        shot = random.choice(choose)
        print(f"Numero vacio se ha elegido automaticamente la recamara ¡¡numero {shot}!!")
    else:
         # Validamos que sea número
        if not user_chamber.isdigit():
            print("Solo se permiten números enteros")
            continue
        shot = int(user_chamber)

    # Validamos rango
    if shot < 1 or shot > bullet_chamber:
        print(f"❌ El número debe estar entre 1 y {bullet_chamber}.")
        continue

    # Comprobamos que el numero no se haya usado
    if shot in used_shot:
        print("⚠️ Recamara ya usada, usa otra ☠️")
        continue

    # Guarda numeros usados
    used_shot.append(shot)

    # Verificamos si es la bala cargada
    if shot == bullet:
        print("¡BANG! Has perdido... Te voy a borrar System32")
        break
    else:
        print("💨 Click... sigues vivo.")
