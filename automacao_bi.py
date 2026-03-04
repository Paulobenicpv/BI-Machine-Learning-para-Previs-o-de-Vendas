
import pandas as pd

print("Automação BI iniciada")

df = pd.read_csv("dados_vendas.csv")

faturamento = df["valor"].sum()
quantidade = df["quantidade"].sum()

print("Faturamento total:", faturamento)
print("Quantidade vendida:", quantidade)

produto = df.groupby("produto")["valor"].sum().sort_values(ascending=False)

print("\nRanking de Produtos")
print(produto)

print("\nProduto mais vendido:", produto.idxmax())
print("Produto com menor venda:", produto.idxmin())
