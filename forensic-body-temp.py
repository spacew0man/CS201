print("What is the temperature of the body at death?")
temperature_0 = float(input())
temperature_1 = temperature_0 + (27 - temperature_0) * 0.2
temperature_2 = temperature_1 + (27 - temperature_1) * 0.2
temperature_3 = temperature_2 + (27 - temperature_2) * 0.2
temperature_4 = temperature_3 + (27 - temperature_3) * 0.2
print("The temperature of the body one hour after death is " + str(temperature_1) + "C")
print("The temperature of the body two hours after death is " + str(temperature_2) + "C")
print("The temperature of the body three hours after death is " + str(temperature_3) + "C")
print("The temperature of the body four hours after death is " + str(temperature_4) + "C")