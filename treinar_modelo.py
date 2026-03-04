
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

print("Treinando modelo de previsão de vendas...")

df = pd.read_csv("dados_vendas.csv")

df["data"] = pd.to_datetime(df["data"])
df["mes"] = df["data"].dt.month
df["ano"] = df["data"].dt.year

X = df[["mes","quantidade"]]
y = df["valor"]

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

modelo = LinearRegression()
modelo.fit(X_train,y_train)

score = modelo.score(X_test,y_test)

print("Precisão do modelo:", score)

with open("modelo_vendas.pkl","wb") as f:
    pickle.dump(modelo,f)

print("Modelo salvo como modelo_vendas.pkl")
