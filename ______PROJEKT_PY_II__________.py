import random

raha = 10000

investeeringud = [
    ("NVDA",               -0.10,  0.20,   1,   "tavaline"),
    ("Kuld",               -0.05,  0.08,   1,   "tavaline"),
    ("Krüpto",             -0.30,  0.30,   1,   "tavaline"),
    ("NVDA 3x",            -0.10,  0.20,   3,   "tavaline"),
    ("NVDA CALL (100x)",   -0.10,  0.20,   100, "call"),
    ("NVDA PUT  (100x)",   -0.10,  0.20,   100, "put"),
    ("Kuld CALL (100x)",   -0.05,  0.08,   100, "call"),
    ("Kuld PUT  (100x)",   -0.05,  0.08,   100, "put"),
]

sundmused = [
    (" Globaalne majanduskriis!",        0.5),
    (" Börsid kukuvad paanika tõttu.",   0.6),
    (" Tavaline päev turul.",             1.0),
    (" Tavaline päev turul.",             1.0),
    (" Tavaline päev turul.",             1.0),
    (" Investorite optimism kasvab.",     1.3),
    (" Turud plahvatavad positiivselt!",  1.6),
]

def lopphinde(raha):
    if raha >= 20000: return "LEGEND "
    elif raha >= 15000: return "Investor "
    elif raha >= 10000: return "Stabiilne "
    elif raha >= 7000:  return "Mcdonalds kutsub tööle "
    else:               return "See kuu süüa ei saa "

print("INVESTEERIMISE MÄNG")
print("Alustad $10 000-ga\n")

for paev in range(1, 6):
    tekst, multiplier = random.choice(sundmused)

    print(f"\nPäev {paev} | Raha: ${raha:.2f}")
    print(f" {tekst}")
    if multiplier != 1.0:
        print(f"   Tootluse kordaja täna: x{multiplier}")

    print("Vali investeering:")
    for i, (nimi, min_t, max_t, kordaja, tyup) in enumerate(investeeringud):
        print(f"  {i+1}. {nimi}  ({min_t*100:.0f}% kuni {max_t*100:.0f}%)")

    valik = int(input("Sisesta number: ")) - 1
    nimi, min_t, max_t, kordaja, tyup = investeeringud[valik]

    raw  = random.uniform(min_t, max_t)  
    baas = raw * multiplier              

    if tyup == "call":
        if raw > 0:                          
            tootlus = baas * kordaja
        else:                                
            tootlus = -random.uniform(0.60, 0.90)

    elif tyup == "put":
        if raw < 0:                          
            tootlus = -baas * kordaja
        else:                                
            tootlus = -random.uniform(0.60, 0.90)

    else:
        tootlus = baas * kordaja

    raha += raha * tootlus

    nool = "📈" if tootlus > 0 else "📉"
    print(f"{nool} {nimi}: {tootlus*100:+.1f}% → ${raha:.2f}")

kasum = raha - 10000
print(f"\nMäng läbi!")
print(f"Lõppraha: ${raha:.2f}  ({kasum:+.2f}$)")
print(f"Hinne: {lopphinde(raha)}")