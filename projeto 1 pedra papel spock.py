n=0
ncpu=0
njog=0
while (ncpu<3 and njog<3):
  import random  
  cpu=random.randint(1,5)
  n=n+1
  print("jogada: %d " % n)
  jog=int(input("digite 1-pedra 2-papel 3-tesoura 4-spock 5-lagarto : "))
  print ("Jogador= %d" % jog)
  print ("Computador= %d" % cpu)
  if jog==1:
      if cpu==1:
          print("empate")
      elif cpu==2:
          print("ganha computador")
          ncpu=ncpu+1
      elif cpu==3:
          print("ganha jogador")
          njog=njog+1
      elif cpu==4:
          print("ganha computador")
          ncpu=ncpu+1
      elif cpu==5:
          print("ganha jogador")
          njog=njog+1
      else:
          print("entrada invalida, jog dif 1")
  elif jog==2:
      if cpu==1:
          print("ganha jogador")
          njog=njog+1
      elif cpu==2:
          print("empate")
      elif cpu==3:
          print("ganha computador")
          ncpu=ncpu+1
      elif cpu==4:
          print("ganha jogador")
          njog=njog+1
      elif cpu==5:
          print("ganha computador")
          ncpu=ncpu+1
      else:
          print("entrada invalida, jog dif 2")
  elif jog==3:
      if cpu==1:
          print("ganha computador")
          ncpu=ncpu+1
      elif cpu==2:
          print("ganha jogador")
          njog=njog+1
      elif cpu==3:
          print("empate")
      elif cpu==4:
          print("ganha computador")
          ncpu=ncpu+1
      elif cpu==5:
          print("ganha jogador")
          njog=njog+1
      else:
          print("entrada invalida, jog dif 3")
  elif jog==4:
      if cpu==1:
          print("ganha jogador")
          njog=njog+1
      elif cpu==2:
          print("ganha computador")
          ncpu=ncpu+1
      elif cpu==3:
          print("ganha jogador")
          njog=njog+1
      elif cpu==4:
          print("empate")
      elif cpu==5:
          print("ganha computador")
          ncpu=ncpu+1
      else:
          print("entrada invalida, jog dif 4")
  elif jog==5:
      if cpu==1:
          print("ganha computador")
          ncpu=ncpu+1
      elif cpu==2:
          print("ganha jogador")
          njog=njog+1
      elif cpu==3:
          print("ganha computador")
          ncpu=ncpu+1
      elif cpu==4:
          print("ganha jogador")
          njog=njog+1
      elif cpu==5:
          print("empate")
      else:
          print("entrada invalida, jog dif 5")
  else:
      print("entrada invalida")
print("")  
print("resultado final")
if njog>=3:
    print("ganha jogador")
else:
    if ncpu>=3:
        print("ganha computador")
    else:
        print("fim sem resultado")
