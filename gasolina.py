# código de geração do gráfico
import seaborn as sns
import pandas as pd

data = pd.read_csv('gasolina.csv')
data.head()


dados = data[["dia", "venda"]].groupby(["dia","venda"]).agg("sum").reset_index()
dados.head()


import matplotlib.pyplot as plt 

with sns.axes_style('whitegrid'):

  grafico = sns.lineplot(data=dados, x="dia", y="venda", palette="rocket")
  grafico.set(title= 'Preço diário da gasolina', xlabel= 'Dia', ylabel='Venda');
  plt.savefig("gasolina.png")