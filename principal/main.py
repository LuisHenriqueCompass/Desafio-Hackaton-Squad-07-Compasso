from parser import parse_query
from tradutorPySpark import gerar_pyspark_code
from tradutorSparkSQL import gerar_spark_sql

sql = """
SELECT nome, salario 
FROM funcionarios 
WHERE salario > 5000 
ORDER BY salario DESC;
"""

consulta = parse_query(sql)

spark_sql_code = gerar_spark_sql(consulta)
pyspark_code = gerar_pyspark_code(consulta)

print("SparkSQL:\n", spark_sql_code)
print("\nPySpark:\n", pyspark_code)
