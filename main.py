Menu = '''
          ###Menu###
          1-Depósito
          2--Saque---
          3-Extrato--
          4---Saír---
      '''
op = 0
limite = 3
extrato = []
conta = 0
while op != 4:
  print(Menu)
  op = int(input("Digite a Opção desejada"))
  print(op)
  if(op > 4 or op <= 0):
    print("Valor ínvalido")
    continue
  match op:
    case 1:
      print("Digite o quanto pretende depositar")
      x=float(input(""))
      conta = conta + x
      x = "Depósito: R${deposito:.2f}".format(deposito = x)
      extrato.append(x)
    
    case 2:
      print("Você selecionou a opção de saque lembre-se do limite de 3 saques diarios")
      print("Digite a quantidade que pretende sacar")
      x = float(input(""))
      if(x > conta or x > 500):
        print("Não é possível sacar esse valor")
        continue
      if(limite == 0):
        print("Limites diários esgotados")
        continue
      limite= limite - 1
      conta = conta - x
      x = "Saque: R${saque:.2f}".format(saque = x)
      extrato.append(x)
    case 3:
      x = "Valor total: R${valor_total:.2f}".format(valor_total = conta)
      extrato.append(x)
      print(extrato)
    case 4:
      break
    
  