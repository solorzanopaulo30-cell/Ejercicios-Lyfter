

hotel = {
    "name": "Hotel Python",
    "number_of_start" : 5,
    "rooms": [
        {
            "number": 101,
            "floor": 10,
            "price_per_night": 150.0
        },
        {
            "number": 106,
            "floor": 11,
            "price_per_night": 160.0
        },
        {
            "number": 8,
            "floor": 3,
            "price_per_night": 120.0
        }
    ]
}

print(f"Nombre del hotel: {hotel['name']}")
print(f"Número de estrellas: {hotel['number_of_start']}")

for i in hotel["rooms"]:
    print(i)