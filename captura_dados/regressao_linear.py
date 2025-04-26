import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

# regressao linear com os anos coletados
df = pd.read_csv('anos_publicacao.csv')

contagem_anos = df['Ano'].value_counts().sort_index()

X = contagem_anos.index.values.reshape(-1, 1)
y = contagem_anos.values 

modelo = LinearRegression()
modelo.fit(X, y)

y_pred = modelo.predict(X)

plt.figure(figsize=(12,6))
plt.scatter(X, y, color='blue', label='Publicações reais')
plt.plot(X, y_pred, color='red', linewidth=2, label='Regressão Linear')
plt.title('Evolução das Publicações com Regressão Linear', fontsize=16)
plt.xlabel('Ano', fontsize=14)
plt.ylabel('Quantidade de Publicações', fontsize=14)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

print(f"Coeficiente Angular (inclinação): {modelo.coef_[0]:.2f}")
print(f"Coeficiente Linear (intercepto): {modelo.intercept_:.2f}")