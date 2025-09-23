a = float(input("Nota do primeiro BI:\n"))
b = float(input("Nota do segundo BI:\n"))
media = (a+b)/2

if media >= 6:
    print("Você foi aprovado, com a média:", media)

elif media < 5.9: 
    print("Você foi reprovado, com a média:", media)

else:
    print("ERRO!")    