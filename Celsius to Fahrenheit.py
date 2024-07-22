print("Celsius to Fahrenheit Converter") 
C = int(input("Celsius Value>"))
def calcFahrenheit(C):
    F=9/5*C+32
    return F
answer = calcFahrenheit(C)
print(answer)
