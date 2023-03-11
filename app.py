# Inițializăm o listă de locuri de parcare, care conține tipul de mașină sau valoarea None, dacă locul este liber
p = ["Mercedes", None, "BMW", None, None, "Toyota", "BMW"]

# Inițializăm un dicționar pentru a număra fiecare tip de mașină
car_counts = {}

# Obținem de la utilizator tipul de mașină și indexul locului de parcare
user_car_brand = input("Name your brand car: ")
user_park_index = int(input("What place: "))

# Verificăm dacă indexul locului de parcare introdus de utilizator este valid (între 1 și numărul total de locuri de parcare)
if user_park_index > 0 and user_park_index <= len(p):
    # Verificăm dacă locul de parcare este liber
    if p[user_park_index-1] == None:
        print("Ok, you can park there!!!")
        # Parcăm mașina la locul specificat de utilizator
        p[user_park_index-1] = user_car_brand
    else:
        # Dacă locul de parcare este ocupat, afișăm un mesaj corespunzător
        print("This place is occupied!!!")
else:
    # Dacă indexul locului de parcare nu este valid, afișăm un mesaj corespunzător
    print("There is no such index!!!")

# Loop prin fiecare mașină parcată și numărăm fiecare tip de mașină
for i in range(len(p)):
    car = p[i]
    if car is not None:
        if car not in car_counts:
            car_counts[car] = 1
        else:
            car_counts[car] += 1

# Calculăm și afișăm numărul total de locuri de parcare și locurile de parcare libere
total = len(p)
free = p.count(None)
print("Parking (free/total):", free, "/", total, "places")

# Afișăm numărul de mașini pentru fiecare tip de mașină
for car, count in car_counts.items():
    print(f"{car:10} - {count}")