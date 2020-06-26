print("====simple calculation===")
min_wight_BMI = 17
max_wight_BMI = 25

name = "ratna"
heiht_M = 1.56
weigh_kg = 50

Bmi = weigh_kg / (heiht_M ** 2)
print("BMI : ")
print(Bmi)
if Bmi <= min_wight_BMI:
    print(name)
    print("less ideal body weight")
elif Bmi >= max_wight_BMI:
    print(name)
    print("more than ideal body weight")
elif Bmi > max_wight_BMI + 15:
    print(name)
    print("Obesity")
else:
    print(name)
    print("Good!!! maintayour body weight")
