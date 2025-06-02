import sqlparse
from sqlparse.sql import IdentifierList, Identifier, Where, Function
from sqlparse.tokens import DML

def parse_query(sql):
    """Analisa uma consulta SQL SELECT e extrai seus componentes."""
    parsed = sqlparse.parse(sql)[0]
    tokens = [token for token in parsed.tokens if not token.is_whitespace]

    consulta = {
        'select': [],
        'from': None,
        'where': None,
        'order_by': None,
        'group_by': None,
        'having': None,
        'joins': [],
    }

    i = 0
    while i < len(tokens):
        token = tokens[i]
        val = token.value.upper()

        if token.ttype is DML and val == 'SELECT':
            i += 1
            select_token = tokens[i]
            consulta['select'] = extrair_colunas(select_token)
        elif val == 'FROM':
            i += 1
            from_token = tokens[i]
            consulta['from'] = extrair_tabela(from_token)
        elif isinstance(token, Where):
            consulta['where'] = token.value.strip()[6:].strip()
        elif val == 'ORDER BY':
            i += 1
            order_token = tokens[i]
            consulta['order_by'] = extrair_order_by(order_token)
        elif val == 'GROUP BY':
            i += 1
            group_token = tokens[i]
            consulta['group_by'] = extrair_group_by(group_token)
        elif val == 'HAVING':
            i += 1
            having_token = tokens[i]
            consulta['having'] = having_token.value.strip()
        elif 'JOIN' in val:
            join = extrair_join(tokens, i)
            consulta['joins'].append(join)
            i = join['next_index']
            continue
        i += 1

    return consulta

# ---------------- Funções auxiliares ------------------

def extrair_colunas(token):
    """Extrai colunas do SELECT, suportando aliases e funções."""
    colunas = []
    if isinstance(token, IdentifierList):
        for sub in token.get_identifiers():
            colunas.append(str(sub).strip())
    elif isinstance(token, Identifier) or isinstance(token, Function):
        colunas.append(str(token).strip())
    else:
        colunas.append(token.value.strip())
    return colunas

def extrair_tabela(token):
    """Extrai nome da tabela, considerando alias."""
    if isinstance(token, Identifier):
        return str(token).strip()
    else:
        return token.value.strip()

def extrair_order_by(token):
    """Extrai coluna e direção do ORDER BY."""
    partes = token.value.strip().split()
    nome_coluna = partes[0]
    direcao = partes[1].upper() if len(partes) > 1 else 'ASC'
    return {'column': nome_coluna, 'direction': direcao}

def extrair_group_by(token):
    """Extrai colunas do GROUP BY."""
    if isinstance(token, IdentifierList):
        return [str(t).strip() for t in token.get_identifiers()]
    else:
        return [token.value.strip()]

def extrair_join(tokens, index):
    """Extrai cláusula JOIN."""
    tipo_join = tokens[index].value.strip().split()[0].upper()
    tabela_token = tokens[index + 1]
    on_token = tokens[index + 3]
    condicao = on_token.value.strip()
    return {
        'type': tipo_join,
        'table': str(tabela_token).strip(),
        'condition': condicao,
        'next_index': index + 4
    }
