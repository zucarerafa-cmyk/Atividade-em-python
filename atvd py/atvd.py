filmesNormais = "Forrest Gump, Toy Story, O Rei Leão, Jurassic Park, Titanic, Harry Potter e a Pedra Filosofal, De Volta para o Futuro."
filmesPrataOuro = "Matrix, Gladiador, Os Vingadores"
filmesOuro = "Interestelar, Clube da Luta, A Origem"
filmesTerror = "O Exorcista, It — A Coisa"

nome = input ("Digite seu nome: ")
cpf = int (input("Digite seu CPF: "))
idade = int(input("Digite sua idade: "))
plano = input("Digite seu plano: ").upper()

if plano == "BRONZE":
 print(filmesNormais)

elif plano == "PRATA":
 if idade >= 18:
  print (filmesNormais + filmesPrataOuro + filmesTerror)
 else:
  print (filmesNormais + filmesPrataOuro) 

elif plano == "OURO":
 if idade >=18:
  print(filmesNormais + filmesOuro + filmesPrataOuro + filmesTerror)
 else:
  print (filmesNormais + filmesOuro + filmesPrataOuro)

 