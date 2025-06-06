# 🚀 SparkMigrator  
**Desafio Hackathon | Squad 07 - Compass UOL**

---

## 📌 Sobre o Projeto

O **SparkMigrator** é uma ferramenta desenvolvida em Python que interpreta queries SQL tradicionais e as converte automaticamente para comandos equivalentes em **PySpark** ou **Spark SQL**. 

Seu principal objetivo é facilitar a migração de sistemas baseados em SQL tradicional para ambientes Apache Spark, agilizando o trabalho de analistas, engenheiros e cientistas de dados que precisam modernizar pipelines e consultas em big data.

---

## 🎯 Objetivo

- Receber queries SQL padrão, incluindo cláusulas como `WITH`, `JOIN`, `GROUP BY`, `HAVING` e outras.
- Analisar a estrutura da query usando a biblioteca `sqlparse`.
- Gerar duas versões equivalentes:
  - Spark SQL, via `spark.sql("...")`.
  - PySpark, utilizando a API DataFrame com encadeamento de métodos (`.filter()`, `.groupBy()`, `.agg()`, etc.).

---

## 🧠 Como Funciona

1. **Entrada:** O usuário fornece uma query SQL, seja diretamente no terminal ou por meio de um arquivo.
2. **Análise:** A query é analisada e seus componentes são extraídos com a biblioteca `sqlparse`.
3. **Tradução:** O conteúdo é processado para montar as consultas equivalentes.
4. **Conversão:** São geradas as versões convertidas em Spark SQL e PySpark.
5. **Saída:** As versões convertidas são exibidas no terminal e podem ser exportadas conforme necessidade.

---

## 📁 Estrutura do Projeto
Principal/
├── main.py # Ponto de entrada da aplicação
├── tradutorPySpark.py # Conversor SQL → PySpark
├── tradutorSparkSQL.py # Conversor SQL → Spark SQL
├── requirements.txt # Dependências do projeto
└── README.md # Documentação do projeto

---

## ▶️ Como Usar

1. Clone o repositório:

git clone https://github.com/joaopierretcompasso/Desafio-Hackaton-Squad-07-Compasso.git
cd sparkMigrator
pip install -r requirements.txt
python main.py

---

4. Após a execução, o terminal exibirá:

- A query SQL original.

- A versão convertida para Spark SQL.

- A versão convertida para PySpark.

---

⚙️ Tecnologias Utilizadas

🐍 Python 3.10+

🔥 Apache PySpark

🧩 sqlparse

☁️ Amazon Q

📊 AI Cockpit 

---

## 🧪 Exemplo de Uso

### Query SQL de entrada

```sql
SELECT cliente_id, SUM(valor_compra) AS total_compras
FROM vendas
WHERE ano = 2024
GROUP BY cliente_id
HAVING total_compras > 1000
ORDER BY total_compras DESC

- Spaark SQL:
spark.sql("""
SELECT cliente_id, SUM(valor_compra) AS total_compras
FROM vendas
WHERE ano = 2024
GROUP BY cliente_id
HAVING total_compras > 1000
ORDER BY total_compras DESC
""")

- PySpark:
vendas_df \
    .filter("ano = 2024") \
    .groupBy("cliente_id") \
    .agg(F.sum("valor_compra").alias("total_compras")) \
    .filter("total_compras > 1000") \
    .orderBy(F.desc("total_compras"))

```
--- 

👥 Autoria
Projeto desenvolvido pela Squad 07 durante o Hackathon promovido pela Compass UOL.
Nosso objetivo foi criar uma solução prática e automatizada para migração de queries SQL tradicionais para Spark, aplicando boas práticas de desenvolvimento e automação.