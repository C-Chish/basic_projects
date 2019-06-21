user_weight = (input("What is your weight? "))
try:
    float(user_weight)
except ValueError:
    print("That's not a weight, please enter weight in Kgs or Lbs")
    exit()
try:
    kgs_or_lbs = input("Please pick (K) to convert to Kilos or (L) for pounds: ")
    if kgs_or_lbs == str('k'):
        print(f'you are {float(user_weight)*0.45}kgs!')
    elif kgs_or_lbs == str('l'):
        print(f'you are {float(user_weight)*2.205} pounds!')
    else:
        print("That's not a valid answer, please enter pick (K) for kgs and (L) for pounds")
except ValueError:
    print("That's not a valid answer, please enter pick (K) for kgs and (L) for pounds")