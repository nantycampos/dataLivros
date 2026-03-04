# 🏗️ Arquitetura - DataLivros

## 🎯 Padrão MVC

DataLivros segue o padrão **Model-View-Controller**:

```
View (view.py)
    ↓ (eventos)
Controller (main.py)
    ↓ (chamadas)
Model (database.py) + API (api_service.py)
```

## 📦 Componentes Principais

### View: `view.py`
- **MainFrame** - Janela principal com StatusBar
- **CirculacaoPanel** - Aba 1: Empréstimos/devoluções
- **CadastroPanel** - Aba 2: Adicionar livros via API
- **LeitoresPanel** - Aba 3: Gerenciar usuários

**Princípio:** View é "burra" - apenas apresenta dados, sem lógica de negócio.

### Controller: `main.py`
Classe **DataLivrosController** orquestra:
- Eventos de usuário (cliques, digitação)
- Validações de entrada
- Chamadas a Model e API
- Feedback via StatusBar
- Navegação entre abas

**Padrão:** Evento → Validação → Model/API → Atualizar View → Feedback

### Model: `database.py`
Classe **DatabaseGerenciador** gerencia:
- Persistência SQLite3
- Operações CRUD (livros, leitores, empréstimos)
- Relacionamentos e integridade referencial
- Transações

### API: `api_service.py`
Função **buscar_livro_google_books()**:
- Consulta Google Books API
- Retorna até 10 resultados
- Extrai dados relevantes (título, autores, ISBN, etc.)
- Trata erros de rede
    
    # CRUD Livros
    # CRUD Livros, Leitores e Empréstimos
```

Ver [DATABASE.md](DATABASE.md) para lista completa de métodos e schema SQL.

### 4️⃣ Camada de Serviços (API)
**Arquivo:** `api_service.py`

**Responsabilidades:**
- Integração com Google Books API
- Tratamento de erros de rede
- Parsing de respostas JSON
- Caching (futuro)

**Função Principal:**

```python
def buscar_livro_google_books(isbn_ou_titulo: str) -> Dict
    
    Parâmetros:
        isbn_ou_titulo: String (ISBN ou título)
    
    Retorna:
        {
            'sucesso': bool,
            'titulo': str,
            'autores': list,
            'isbn': str,
            'editora': str,
            'ano_publicacao': int,
            'descricao': str,
            'categorias': list,
            'thumbnail': str,
            'erro': str
        }
    
    Tratamentos:
        - Timeout (10s)
        - Connection Error
        - HTTP Error
        - JSON Parse Error
```

## 🔄 Fluxos Principais

### Fluxo 1: Registrar Empréstimo
1. Usuário digita ISBN/título
2. Controller busca livro localmente (Model)
3. Usuário seleciona leitor
4. Controller valida e calcula data de devolução
5. Model registra no banco
6. StatusBar fornece feedback

### Fluxo 2: Cadastrar Livro via API
1. Usuário digita ISBN/título
2. Controller valida entrada
3. API Service consulta Google Books
4. Controller injeta dados nos campos
5. Usuário revisa e salva
6. Model persiste no banco
7. StatusBar confirma

### Fluxo 3: Navegação com Atalhos
- `Ctrl+1/2/3` → AcceleratorTable → Controller → View atualiza
- NVDA anuncia mudança via StatusBar

## ✅ Validações

**View:** Controller valida entrada antes de processar
**Model:** Banco enforce constraints (UNIQUE, FK, NOT NULL)
**API:** Trata timeouts, erros de conexão e parsing

## � Próximos Passos

- Leia [DATABASE.md](DATABASE.md) para entender o schema e operações CRUD
- Leia [API.md](API.md) para integração com Google Books
- Leia [ACESSIBILIDADE.md](ACESSIBILIDADE.md) para padrões WCAG 2.1

### Empréstimo
```python
{
    'id': int,
    'livro_id': int (FK),
    'leitor_id': int (FK),
    'data_emprestimo': datetime,
    'data_devolucao_prevista': datetime,
    'data_devolucao_real': datetime (null se ativo),
    'renovacoes': int,
    'status': str ('ativo' | 'finalizado'),
    'observacoes': str
}
```

## 🔗 Dependências Entre Módulos

```
main.py (orquestrador)
  ├── importa view.py
  ├── importa database.py
  ├── importa api_service.py
  │   └── requests (externo)
  └── cria instância MainFrame

view.py (interface)
  └── import wx

database.py (persistência)
  └── import sqlite3

api_service.py (integração)
  ├── import requests
  ├── import typing
  └── (sem dependência de view ou database)
```

**Importante:** API Service é **desacoplada** - pode ser testada isoladamente.

## 🧪 Testeabilidade

### Testes Unitários (Futuro)

```python
# Test Model (database.py)
def test_adicionar_livro():
    db = DatabaseGerenciador(':memory:')
    livro_id = db.adicionar_livro('Test Book')
    assert livro_id > 0

# Test API (api_service.py)
def test_buscar_livro_valido():

## 🚀 Extensibilidade

### Adicionar Novo Campo a Livro
1. Alterar schema em `database.py`
2. Atualizar métodos CRUD
3. Adicionar campo UI em `view.py`
4. Adicionar handler em `main.py`

### Integrar Novo Serviço
1. Criar `novo_service.py`
2. Importar e chamar em `main.py`
3. Atualizar UI com resultados

---

**DataLivros segue padrões SOLID para facilitar manutenção e crescimento.**

