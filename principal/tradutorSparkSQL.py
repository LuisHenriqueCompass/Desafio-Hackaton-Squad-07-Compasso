def gerar_spark_sql(consulta):
    """Gera código SparkSQL."""
    sql = "SELECT " + ', '.join(consulta['select']) + "\n"
    sql += "FROM " + consulta['from'] + "\n"

    for join in consulta['joins']:
        sql += f"{join['type']} JOIN {join['table']} ON {join['condition']}\n"

    if consulta['where']:
        sql += "WHERE " + consulta['where'] + "\n"

    if consulta['group_by']:
        sql += "GROUP BY " + ', '.join(consulta['group_by']) + "\n"

    if consulta['having']:
        sql += "HAVING " + consulta['having'] + "\n"

    if consulta['order_by']:
        sql += f"ORDER BY {consulta['order_by']['column']} {consulta['order_by']['direction']}\n"

    return f'spark.sql("""\n {sql.strip()}\n""")'
