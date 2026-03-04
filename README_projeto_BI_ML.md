
# Projeto BI + Machine Learning para Previsão de Vendas

## Descrição do Projeto
Este projeto demonstra como utilizar **Python, Business Intelligence (BI) e Machine Learning**
para analisar dados de vendas e gerar previsões de faturamento.

O objetivo é mostrar como dados podem apoiar **tomadas de decisão estratégicas**
através de análise e modelos preditivos.

Este projeto pode ser usado como **portfólio para vagas de Analista de Dados, BI ou Data Science**.

---

# Tecnologias Utilizadas

- Python
- Pandas (análise de dados)
- Scikit-learn (Machine Learning)
- Streamlit (Dashboard interativo)

---

# Estrutura do Projeto

projeto_bi_machine_learning_dashboard_paulo

- dados_vendas.csv → base de dados utilizada no projeto
- automacao_bi.py → análise automática de indicadores
- treinar_modelo.py → treinamento do modelo de Machine Learning
- dashboard_ml.py → dashboard interativo
- modelo_vendas.pkl → modelo treinado
- requirements.txt → dependências do projeto

---

# Etapas do Projeto

## 1. Análise de Dados (BI)

O script **automacao_bi.py** realiza análises importantes:

- faturamento total
- quantidade vendida
- ranking de produtos
- produto com maior venda
- produto com menor venda

Esse tipo de análise é semelhante ao realizado em ferramentas de BI como **Power BI**.

---

## 2. Machine Learning

O script **treinar_modelo.py** cria um modelo de regressão linear usando a biblioteca **Scikit‑learn**.

Variáveis utilizadas no modelo:

- mês da venda
- quantidade vendida

O modelo aprende padrões dos dados históricos e consegue prever
o **valor estimado de faturamento**.

O modelo treinado é salvo no arquivo:

modelo_vendas.pkl

---

## 3. Dashboard Interativo

O arquivo **dashboard_ml.py** cria um dashboard utilizando **Streamlit**.

O dashboard apresenta:

- KPI de faturamento
- KPI de quantidade vendida
- gráfico de vendas por produto
- previsão de faturamento usando Machine Learning

O usuário pode escolher:

- mês
- quantidade esperada

E o sistema calcula automaticamente a **previsão de faturamento**.

---

# Como Executar o Projeto

## 1. Instalar dependências

pip install -r requirements.txt

---

## 2. Treinar o modelo

python treinar_modelo.py

Isso irá gerar o arquivo:

modelo_vendas.pkl

---

## 3. Executar o dashboard

streamlit run dashboard_ml.py

O sistema abrirá automaticamente no navegador:

http://localhost:8501

---

# Insights Possíveis

Com este projeto é possível responder perguntas como:

- Qual produto gera mais faturamento?
- Qual produto tem menor desempenho?
- Qual faturamento esperado para determinado mês?
- Como as vendas podem evoluir no futuro?

Essas informações ajudam empresas a **tomar decisões baseadas em dados**.

---

# Possíveis Evoluções

O projeto pode ser evoluído com:

- previsão com séries temporais
- integração com banco SQL
- automação de ETL
- deploy em cloud
- dashboards mais avançados

---

# Autor

Projeto desenvolvido por **[Paulo Beni](https://www.linkedin.com/in/paulo-beni-da-silva-filho-6b3859bb/)**
