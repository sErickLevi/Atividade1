total = int(input("Digite o valor total das mercadorias compradas: R$ "))

if total > 500:
   
    valor_a_mais = total - 500
 
    imposto = valor_a_mais * 0.5
    print(f"O valor do imposto a ser pago é: R$ {imposto: }")
else:
    print(f"O valor que você vai pagar é: R${total}")
    print("Não há imposto a ser pago.")