# 🗄️ Database - DataLivros

Estrutura e operações do banco SQLite3.

## 📊 Três Tabelas Principais

```
livros ←── emprestimos ──→ leitores
```

## 📚 Tabela: livros

### Schema SQL

```sql
CREATE TABLE livros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    autores TEXT,
    isbn TEXT UNIQUE,
    editora TEXT,
    ano_publicacao INTEGER,
    descricao TEXT,
    categorias TEXT,
    thumbnail TEXT,
    data_adicao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## 👥 Tabela: leitores

```sql
CREATE TABLE leitores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT UNIQUE,
    telefone TEXT,
    endereco TEXT,
    data_inscricao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ativo BOOLEAN DEFAULT 1
);
```

## 📤 Tabela: emprestimos

Registro de todas as transações de empréstimo.

### Estrutura

```sql
CREATE TABLE emprestimos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    livro_id INTEGER NOT NULL,
    leitor_id INTEGER NOT NULL,
    data_emprestimo TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_devolucao_prevista TIMESTAMP,
    data_devolucao_real TIMESTAMP,
    renovacoes INTEGER DEFAULT 0,
    status TEXT DEFAULT 'ativo',
    observacoes TEXT,
    FOREIGN KEY (livro_id) REFERENCES livros(id) ON DELETE CASCADE,
    FOREIGN KEY (leitor_id) REFERENCES leitores(id) ON DELETE CASCADE
);
```

### Campos

| Campo | Tipo | Constraints | Descrição |
|-------|------|-------------|-----------|
| `id` | INTEGER | PRIMARY KEY, AUTOINCREMENT | Identificador único |
| `livro_id` | INTEGER | NOT NULL, FK → livros | Qual livro |
| `leitor_id` | INTEGER | NOT NULL, FK → leitores | Quem pegou |
| `data_emprestimo` | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Data do empréstimo |
| `data_devolucao_prevista` | TIMESTAMP | - | Quando deve devolver |
| `data_devolucao_real` | TIMESTAMP | - | Quando devolveu (NULL se ativo) |
| `renovacoes` | INTEGER | DEFAULT 0 | Quantas vezes renovou |
| `status` | TEXT | DEFAULT 'ativo' | 'ativo' ou 'finalizado' |
| `observacoes` | TEXT | - | Notas sobre o empréstimo |

### Exemplo de Dados

```sql
INSERT INTO emprestimos VALUES (
    1,
    1,                    -- livro_id (O Cortiço)
    1,                    -- leitor_id (João Silva)
    '2026-03-03 10:00:00',
    '2026-03-17 10:00:00',
    NULL,                 -- Ainda não devolveu
    0,                    -- Sem renovações
    'ativo',
    'Empréstimo inicial'
);
```

### Índices

```python
# Criados automaticamente
PRIMARY KEY (id)
FOREIGN KEY (livro_id)
FOREIGN KEY (leitor_id)

# Recomendados
CREATE INDEX idx_leitor_ativo ON emprestimos(leitor_id, status);
CREATE INDEX idx_data_devolucao ON emprestimos(data_devolucao_prevista);
CREATE INDEX idx_status ON emprestimos(status);
```

### Status Values

| Status | Significado |
|--------|-------------|
| `ativo` | Empréstimo em aberto |
| `finalizado` | Livro devolvido |

### Consultas Comuns

```python
# Empréstimos ativos
SELECT * FROM emprestimos WHERE status = 'ativo' ORDER BY data_emprestimo DESC;

# Empréstimos de um leitor
SELECT * FROM emprestimos WHERE leitor_id = 1 AND status = 'ativo';

# Livros em atraso (hoje > data_devolucao_prevista)
SELECT e.*, l.titulo, l2.nome FROM emprestimos e
JOIN livros l ON e.livro_id = l.id
JOIN leitores l2 ON e.leitor_id = l2.id
WHERE e.status = 'ativo' AND e.data_devolucao_prevista < date('now');

# Histórico de um leitor
SELECT e.*, l.titulo FROM emprestimos e
JOIN livros l ON e.livro_id = l.id
WHERE e.leitor_id = 1
ORDER BY e.data_emprestimo DESC;



## 📤 Tabela: emprestimos

```sql
CREATE TABLE emprestimos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    livro_id INTEGER NOT NULL,
    leitor_id INTEGER NOT NULL,
    data_emprestimo TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_devolucao_prevista TIMESTAMP NOT NULL,
    data_devolucao_real TIMESTAMP,
    renovacoes INTEGER DEFAULT 0,
    status TEXT DEFAULT 'ativo',
    observacoes TEXT,
    FOREIGN KEY(livro_id) REFERENCES livros(id),
    FOREIGN KEY(leitor_id) REFERENCES leitores(id)
);
```

## 🔗 Relacionamentos

- **Livro → Empréstimos (1:N)** - Um livro pode ter múltiplos empréstimos
- **Leitor → Empréstimos (1:N)** - Um leitor pode ter múltiplos empréstimos
- **Livro ↔ Leitor (N:M via Empréstimos)** - Relacionamento indireto

## ✅ Constraints

- `PRIMARY KEY` - Identificadores únicos
- `UNIQUE (isbn)` - ISBN não se repete
- `UNIQUE (email)` - Email não se repete
- `FOREIGN KEY` - Integridade referencial
- `NOT NULL` - Campos obrigatórios

## 🚀 Operações CRUD

Classe `DatabaseGerenciador` em `database.py`:

**Livros:** adicionar, buscar, atualizar, deletar, listar
**Leitores:** adicionar, buscar, atualizar, deletar, listar  
**Empréstimos:** registrar, renovar, devolver, listar ativos

---

Para detalhes técnicos, veja [ARQUITETURA.md](ARQUITETURA.md).

