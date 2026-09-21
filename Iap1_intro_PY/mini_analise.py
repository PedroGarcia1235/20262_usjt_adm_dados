import matplotlib.pyplot as plt
import pandas as pd

dados = {
    "pedidos": [1, 2, 2, 3, 4],
    "Valor": ["100,00", "250,00", "250,00", "abc", "80"]
}

df = pd.DataFrame(dados)

print(df["Valor"].dtype)


df = df.drop_duplicates(subset="pedidos")

df["Valor"] = df["Valor"].str.replace(",", ".", regex=False)
df["Valor"] = pd.to_numeric(df["Valor"], errors="coerce")

df = df.dropna(subset=["Valor"])

print(f"Pedidos válidos: {len(df)}")
print(f"Ticket médio: R${df['Valor'].mean():.2f}")


df = pd.read_csv(
    "clientes.csv",
    sep=",",
    decimal=".",
    encoding="utf-8"
)


total_cidade = df.groupby("cidade")["valor"].sum()
print(total_cidade)
total_cidade.sort_values().plot(kind="hist")
plt.title("Total vendido por cidade")
plt.xlabel("Valor (R$)")
plt.show()
