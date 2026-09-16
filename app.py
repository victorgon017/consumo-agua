#Perfil dos consumidores 
#entrada de dados
propiedade = input("Digite o tipo da sua propiedade entre: comercial, casa e apartamento: ")
consumo_mensal = float(input("Digite o seu consumo mensal em metros cúbicos (m³): "))
#processamento e saída
if propiedade == "comercial": 
    print("Tarifa comercial aplicada, consulte o plano corporativo.")
elif propiedade == "apartamento" and consumo_mensal < 10:
    print("Consumo econômico, excelente controle de água!")
elif (propiedade == "apartamento" or propiedade == "casa") and consumo_mensal <= 25:
    print("Consumo moderado, dentro do padrão residencial.")
else:
    print("Consumo excessivo, adote medidas de economia e verifique vazamentos.")
