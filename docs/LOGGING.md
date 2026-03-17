# Guia de Logging - DataLivros v1.1.2

## 📋 Visão Geral

DataLivros agora inclui um **sistema profissional de logging** que registra todas as operações críticas em arquivo, com suporte especial para:

- **Erros de API** (autenticação, cota, servidor)
- **Erros de Conexão** (timeout, DNS, internet)
- **Buscas Bem-sucedidas** (rastreamento de uso)
- **Operações de Banco de Dados** (auditoria)

## 🎯 Objetivos do Sistema

1. **Rastreabilidade**: Manter histórico de todas as operações
2. **Debugging**: Facilitar diagnóstico de problemas
3. **Auditoria**: Registrar quem fez o quê e quando
4. **Acessibilidade**: Fornecer feedback de erro via NVDA com diálogos

## 📁 Estrutura de Arquivos de Log

```
dataLivros/
├── logs/
│   ├── datalibros_20260306.log    # Log atual (diário)
│   ├── datalibros_20260305.log    # Log anterior
│   └── ...
├── logger_config.py               # Módulo de configuração
└── main.py                        # Integração com UI
```

### Nome do Arquivo de Log

- **Padrão**: `logs/datalibros_YYYYMMDD.log`
- **Exemplo**: `logs/datalibros_20260306.log`
- **Rotação**: Um arquivo por dia
- **Retenção**: Máximo 5 MB por arquivo com backup de 5 versões

## 📊 Formato de Log

Cada entrada no arquivo de log segue este padrão:

```
TIMESTAMP - LOGGER - LEVEL - FUNÇÃO:LINHA - MENSAGEM
```

### Exemplo Real

```
2026-03-06 14:17:38 - DataLivros - ERROR - log_error_api:57 - ERRO DE AUTENTICAÇÃO (401): API key inválida ou expirada. Chave da API inválida ou expirada. Chave no .env não foi reconhecida
2026-03-06 14:17:38 - DataLivros - INFO - log_busca_livro:87 - Busca executada: "1984 George Orwell" - 5 resultado(s) encontrado(s)
```

### Componentes

| Campo | Descrição | Exemplo |
|-------|-----------|---------|
| **TIMESTAMP** | Data e hora exata | `2026-03-06 14:17:38` |
| **LOGGER** | Nome do logger | `DataLivros` |
| **LEVEL** | Nível de severidade | `ERROR`, `WARNING`, `INFO`, `DEBUG` |
| **FUNÇÃO:LINHA** | Onde foi registrado | `log_error_api:57` |
| **MENSAGEM** | Conteúdo do log | `ERRO DE AUTENTICAÇÃO (401)...` |

## 🔍 Níveis de Log

| Nível | Cor | Uso | Arquivo | Console |
|-------|-----|-----|---------|---------|
| **DEBUG** | Cinza | Detalhes técnicos | ✅ Registrado | ❌ Não |
| **INFO** | Azul | Informação geral | ✅ Registrado | ❌ Não |
| **WARNING** | Amarelo | Aviso (não é erro) | ✅ Registrado | ✅ Exibido |
| **ERROR** | Vermelho | Erro crítico | ✅ Registrado | ✅ Exibido |

## 📝 Funções de Logging

### 1. `log_error_api(status_code, error_message, details)`

Registra erros específicos de API com tratamento de diferentes status codes.

**Uso**:
```python
from logger_config import log_error_api

# Erro 401 - Autenticação
log_error_api(401, 'Chave da API inválida', 'Verifique arquivo .env')

# Erro 403 - Cota excedida
log_error_api(403, 'Limite diário atingido', 'Tente novamente amanhã')

# Erro 404 - Não encontrado
log_error_api(404, 'Livro não encontrado', f'Query: {query}')
```

**Status Codes Suportados**:
- `401` → Erro de Autenticação
- `403` → Limite de Cota
- `404` → Livro Não Encontrado
- `500` → Erro do Servidor
- `503` → Serviço Indisponível
- Outros → Erro do Servidor (genérico)

### 2. `log_connection_error(error_type, error_message)`

Registra erros de conexão e rede.

**Uso**:
```python
from logger_config import log_connection_error

# Timeout
log_connection_error('Timeout', 'Requisição excedeu 10 segundos')

# Erro de conexão
log_connection_error('ConnectionError', 'Servidor não respondeu')

# Erro de DNS
log_connection_error('DNSError', 'Não foi possível resolver hostname')
```

**Tipos de Erro Comuns**:
- `Timeout` - Requisição levou muito tempo
- `ConnectionError` - Servidor não respondeu
- `ConnectionRefused` - Conexão recusada
- `DNSError` - Problema com resolução de domínio
- `URLError` - URL inválida ou inacessível

### 3. `log_busca_livro(query, total_resultados)`

Registra buscas bem-sucedidas para análise de uso.

**Uso**:
```python
from logger_config import log_busca_livro

# Busca com múltiplos resultados
log_busca_livro("1984 George Orwell", 5)

# Busca com um resultado
log_busca_livro("ISBN_UNICO", 1)

# Busca sem resultados
log_busca_livro("Livro Inexistente", 0)
```

### 4. `log_acesso_banco(operacao, status)`

Registra operações de banco de dados para auditoria.

**Uso**:
```python
from logger_config import log_acesso_banco

# Operação bem-sucedida
log_acesso_banco('inserir_livro', 'sucesso')

# Operação com erro
log_acesso_banco('atualizar_livro', 'erro')

# Operação de consulta
log_acesso_banco('buscar_livro_por_id', 'sucesso')
```

## 🛡️ Mensagens de Erro em Português

O sistema usa mensagens de erro amigáveis em português para cada tipo de falha:

```python
MENSAGENS_ERRO = {
    401: "Erro de Autenticação: Chave da API inválida ou expirada. Verifique o arquivo .env.",
    403: "Limite de Cota Atingido: Você atingiu o limite diário de requisições. Tente novamente amanhã.",
    404: "Livro não encontrado. Tente buscar com outro título ou ISBN.",
    500: "Erro no servidor do Google Books. Tente novamente em alguns minutos.",
    503: "Serviço indisponível. O Google Books está em manutenção. Tente novamente mais tarde.",
    'timeout': "Tempo limite excedido. Verifique sua conexão de internet.",
    'conexao': "Erro de conexão. Verifique se está conectado à internet.",
    'desconhecido': "Erro desconhecido ao buscar livro. Tente novamente."
}
```

## 🎨 Integração com NVDA

Quando um erro ocorre:

1. **Status Bar Update** (antes do diálogo)
   - NVDA anuncia o erro imediatamente
   - Exemplo: "Erro na Busca de Livro: Chave da API inválida"

2. **Diálogo de Erro** (bloqueante)
   - Mostra mensagem amigável em português
   - Usuário clica OK para fechar

3. **Status Bar Update** (após fechar)
   - NVDA re-anuncia que o diálogo foi fechado
   - Exemplo: "Diálogo fechado. Erro na Busca de Livro."

4. **Log de Erro** (em background)
   - Erro registrado no arquivo de log com detalhes técnicos

## 📖 Exemplos Práticos

### Cenário 1: Chave da API Inválida

**O que Acontece**:
1. Usuário busca um livro
2. API retorna `401 Unauthorized`
3. Sistema registra: `ERRO DE AUTENTICAÇÃO (401)...`
4. Diálogo mostra: "Erro de Autenticação: Chave da API inválida..."
5. NVDA anuncia o erro
6. Usuário é instruído a verificar `.env`

**Log**:
```
2026-03-06 14:17:38 - DataLivros - ERROR - log_error_api:57 - ERRO DE AUTENTICAÇÃO (401): API key inválida ou expirada...
```

### Cenário 2: Cota Diária Excedida

**O que Acontece**:
1. Usuário busca muitos livros
2. API retorna `403 Forbidden`
3. Sistema registra: `ERRO DE COTA (403)...`
4. Diálogo mostra: "Limite de Cota Atingido: Você atingiu o limite diário..."
5. NVDA anuncia
6. Usuário sabe tentar novamente amanhã

**Log**:
```
2026-03-06 14:17:38 - DataLivros - ERROR - log_error_api:59 - ERRO DE COTA (403): Limite diário atingido...
```

### Cenário 3: Problema de Conexão

**O que Acontece**:
1. Internet desconectada
2. Requisição faz timeout após 10 segundos
3. Sistema registra: `ERRO DE CONEXÃO (Timeout)...`
4. Diálogo mostra: "Tempo limite excedido. Verifique sua conexão..."
5. NVDA anuncia
6. Usuário reconecta internet

**Log**:
```
2026-03-06 14:17:38 - DataLivros - ERROR - log_connection_error:76 - ERRO DE CONEXÃO (Timeout): Requisição excedeu 10 segundos
```

## 🔧 Configuração

### Arquivo: `logger_config.py`

```python
# Localização do arquivo de log
LOGS_DIR = 'logs'
LOG_FILENAME = os.path.join(LOGS_DIR, f'datalibros_{datetime.now().strftime("%Y%m%d")}.log')

# Tamanho máximo do arquivo (5 MB)
file_handler = logging.handlers.RotatingFileHandler(
    LOG_FILENAME,
    maxBytes=5 * 1024 * 1024,  # 5 MB
    backupCount=5,  # Mantém 5 versões antigas
    encoding='utf-8'
)

# Nível de detalhe
file_handler.setLevel(logging.DEBUG)      # Tudo no arquivo
console_handler.setLevel(logging.WARNING) # Apenas warnings no console
```

### Modificação de Configuração

Para alterar o comportamento de logging, edite `logger_config.py`:

**Para aumentar tamanho do arquivo**:
```python
maxBytes=10 * 1024 * 1024  # 10 MB em vez de 5 MB
```

**Para incluir INFO no console**:
```python
console_handler.setLevel(logging.INFO)  # Mostra INFO + WARNING + ERROR
```

**Para desabilitar rotação de arquivo**:
```python
# Comentar as linhas de RotatingFileHandler e usar:
file_handler = logging.FileHandler(LOG_FILENAME, encoding='utf-8')
```

## 📊 Análise de Logs

### Ver Últimas Linhas
```bash
powershell
Get-Content logs/datalibros_20260306.log -Tail 10
```

### Filtrar por Tipo de Erro
```bash
Select-String "ERROR" logs/datalibros_*.log
```

### Contar Erros
```bash
(Select-String "ERROR" logs/datalibros_*.log).Count
```

## 🧪 Teste do Sistema

Execute o script de teste para validar logging:

```bash
python test_error_handling.py
```

**O que testa**:
- ✅ Logging básico (info, warning, error)
- ✅ Erros de API (401, 403, 404, 500, 503)
- ✅ Erros de conexão (timeout, ConnectionError, DNS)
- ✅ Buscas bem-sucedidas
- ✅ Operações de banco de dados
- ✅ Criação de arquivo de log
- ✅ Mensagens de erro em português

## 🚨 Troubleshooting

### Problema: Arquivo de log não é criado

**Solução**:
1. Verifique se o diretório `logs/` existe
2. Verifique permissões de escrita no diretório
3. Execute: `mkdir logs` se não existir

### Problema: Erros não aparecem no arquivo

**Solução**:
1. Verifique se o nível de logging está correto
2. Certifique-se de que `logger_config.py` está sendo importado
3. Verifique sintaxe em `api_service.py`

### Problema: Muitos arquivos de log

**Solução**:
1. Aumente `backupCount` em `logger_config.py`
2. Ou limpe manualmente: `Remove-Item logs/datalibros_*.log`

## 📚 Referências Relacionadas

- **Implementação de API**: `api_service.py`
- **Integração com UI**: `main.py` (método `_exibir_erro_dialog`)
- **Teste Completo**: `test_error_handling.py`
- **Configuração de Ambiente**: `.env` e `.env.example`

## ✅ Checklist de Implementação

- [x] Módulo `logger_config.py` criado
- [x] Arquivo de log criado com rotação
- [x] Funções especializadas de logging
- [x] Mensagens de erro em português
- [x] Integração com `api_service.py`
- [x] Método `_exibir_erro_dialog()` em `main.py`
- [x] Teste completo do sistema
- [x] Documentação de logging
- [ ] Teste em produção com NVDA (pendente)
- [ ] Análise de logs após uso real (pendente)

## 📞 Suporte

Para questões sobre logging:
1. Verifique `logs/datalibros_YYYYMMDD.log`
2. Execute `test_error_handling.py`
3. Revise a seção apropriada acima
4. Consulte comentários no código-fonte
