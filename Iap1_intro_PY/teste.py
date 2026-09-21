#print ("hellow word")
#print ('10/0' \)
# nome ="maria"
# Sobrenome = 'Silva'
# valor = 1234.50
# cpf ="12345678900"
# print (cpf[0])
# print (cpf[0:3])
# print (cpf[-1:])
# print (nome, Sobrenome)



# preco_textual = "19,50"
# preco = float(preco_textual)
# idade_textual = "18"
# idade = int (idade_textual)

# print(type(nome))

# print(f'{nome} gastou R${valor:.2f}')


# Nome2 = "    maria SILVA "
# limpo = Nome2.strip().title()
# print(limpo)
# print(limpo.split())
# print(" ".join(limpo.split()))



# valor_txt = "R$ 1.234,56"
# limpo = valor_txt.replace("R$", "").replace(".", "").replace(",", ".").strip()
# valor = float(limpo)
# print(valor)


# precos = [19.90, 45.00, 12.50, 89.90]
# #quantos
# print(len(precos))
# #soma
# print(sum(precos))
# #adicionar valor
# precos.append(30.00)
# #apenas os dois primeiros
# print(precos[:2])

#list compreensão

# precos = [19.90, 45.00, 12.50, 89.90]
# # aplicar 10% a todos
# com_imposto = [p * 1.1 for p in precos]
# print(com_imposto)
# carros = (p for p in precos if p > 40)

#dicionario

# cliente = {
#     "nome": "maria",
#     "idade": 34,
#     "Cidade": "São paulo"
# }

# print(cliente["Cidade"])
# cliente["email"] = "maria@gmail.com"
# for chave, valor in cliente.items():
#     print(chave, "->", valor)


# tabela = [
#     {"nome": "Maria", "saldo": 150},
#     {"nome": "João", "saldo": 250},
#     {"nome": "Anna", "saldo": 350}
# ]

# print(tabela[1]["nome"])


# etsados = ["sp", "rj", "mg", "sp"]
# print(set(etsados))
# print(len(set(etsados)))

#if elif else

# VAlor = 250
# #se for pelo menos 550 alto
# # se for pelo menos 100 medio
# #caso contrario baixpo

# if VAlor >= 500:
#     faixa = "alto"
# elif VAlor >= 100:
#     faixa = "medio"
# else:
#     faixa = "Baixo"

# print(f"cliente de ticket {faixa}")

# uF = "SP"

# Validos = ["SP", "RJ", "MG", "PR", "RS"]
# if uF in Validos:
#     print("UF Reconhecida")
# else:
#     print("Não é uma UF reconhecida")

# preco = [19.90, 45.00, 12.50, 89.90]
# total = 0
# for p in preco:
#     total = total + p
# print(F'Total : R${total:.2f}')


# emaild = ['maria@gmail.com', 'joão@g,ail.com', 'mary@gmail.com', 'pedro@gmail.com']
# # variável contadora
# invalidos = 0
# for email in emaild:
#     if "@" not in email or "," in email:
#         invalidos = invalidos + 1
# print(f"Total de inválidos: {invalidos}")

# nomes = ['maria','joão.''ana']
# for i, nome in enumerate(nomes):
#     print (i, nomes)

# def resumo_vendas(valores, imposto=0.1):
#     total = sum(valores)
#     media = total / len(valores)
#     total_com_imposto = total * (1 + imposto)
#     return total, media, total_com_imposto
# t, m, ti = resumo_vendas([100, 200, 300], o.15)
# print(f"Total: {t} Média: {m:.2f} Com imposto: {ti:.2f}")


# dobro = lambda x : x*2
# print(dobro(5))

# situação=  lambda nota: 'aprovado' if nota >= 70 else "REPROVADO"
# print(situação(85))
# print(situação(11))


# valores = ["100", "abc", "250", " "]
# for v in valores:
#     try:
#         numero = int(v)
#         print(numero * 2)
#     except ValueError:
#         print("Valor inválido")

# valores = ["100", "abc", "250", " "]

# for v in valores:
#     try:
#         numero = int(v)
#         print(f"{numero} * 2 = {2 * numero}")
#     except ValueError:
#         print(f"{v} não é um número")




# nome = 'ana'

# print ("o nome é" + nome )

# print (f'o nome é: {nome}')

# numero = int(input("DIGITE UM NUMERO  "))
# numero3= int(input("DIGITE UM NUMERO  RR"))
# print (f"{numero} + {numero3} = {numero + numero3}")

import pandas as pd
pedidos = pd.DataFrame({
    "id_clientes": [1, 2, 1, 3],
    "valor": [100, 300, 200, 50]
})

clientes = pd.DataFrame({
    "id_clientes": [1, 2, 3],
    "nome": [1, 2, 3],
    "cidade": ["sp", "Rio", "BH"]
})

completo = pedidos.merge(clientes, on="id_clientes")
print(completo)
# df = pd.read_csv(
#     "clientes.csv",
#     sep=",",
#     decimal=".",
#     encoding="utf-8"

# print(df.head(3))
# print(df.shape)
# print(df.dtypes)
# print(df.info)
# print(df.describe)
# print(df['cidade'].value_counts())
# print(df.loc[df["valor"] > 100, "clientes"])
# print(df[df["cidade"].isin(["RF", "CR"])])
# print(df[df["valor"].between(80, 200)])
# print(df[df["clientes"].str.contains("a")])
# print(df[(df["valor"] > 100) & (df["cidade"] == "CR")])

# df["com_frete"] = df["valor"] + 15
# print(df.isnull().sum())
# df["valor"].fillna(0)
# print(df.head)

# serie = pd.Series(["1.234,56", "89,90", "abc"])
# numeros = serie.str.replace(".", "", regex=False)
# numeros = numeros.str.replace(",", ".", regex=False)
# numeros = pd.to_numeric(numeros, errors="coerce")
# print(numeros)

# dados = {

# 'clientes ' : ['maria','joão', 'ana',"bruno"],
# 'cidades' : ['SP','RF', 'CR',"RC"],
# "valor" : [150.0, 89.90,230.5,60.0]
# }

# df = pd.DataFrame(dados)
# print(df)

#  