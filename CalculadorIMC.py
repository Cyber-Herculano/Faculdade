peso = float(input("digite o seu peso(kg)"))
altura = float(input("digite a sua altura(cm)"))
imc = peso / (altura ** 2)
print(f"o seu imc é de {imc:.2f}")

if imc < 18.5:
    print("Você está abaixo do peso normal")
elif 18.5 <= imc < 25:
    print("Parabéns você está no peso ideal")
elif 25 <= imc < 30:
    print("Você está levemente acima do peso")
elif 30 <= imc < 35:
    print("Alerta! Obesidade grau 1")
elif 35 <= imc < 40:
    print("Cuidado!! Obesidade grau 2")
elif imc >= 40:
    print("Procure um médico!! Obesidade mórbida!!!")                        