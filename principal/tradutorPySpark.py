def gerar_pyspark_code(consulta):
    """Gera código PySpark DataFrame."""
    codigo = f"{consulta['from'].split()[0]}_df"

    for join in consulta['joins']:
        join_df = f"{join['table'].split()[0]}_df"
        tipo_join = join['type'].lower()
        codigo += f".join({join_df}, \"{join['condition']}\", \"{tipo_join}\")"

    if consulta['where']:
        codigo += f".filter(\\\"{consulta['where']}\\\")"

    if consulta['group_by']:
        group_cols = ', '.join([f'\\\"{col}\\\"' for col in consulta['group_by']])
        codigo += f".groupBy({group_cols})"

    if consulta['select']:
        select_cols = ', '.join([f'\\\"{col}\\\"' for col in consulta['select']])
        codigo += f".select({select_cols})"

    if consulta['having']:
        codigo += f".filter(\\\"{consulta['having']}\\\")"

    if consulta['order_by']:
        col = consulta['order_by']['column']
        asc = "False" if consulta['order_by']['direction'] == "DESC" else "True"
        codigo += f".orderBy(\\\"{col}\\\", ascending={asc})"

    return codigo
