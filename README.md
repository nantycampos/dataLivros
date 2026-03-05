# DataLivros 📚

Sistema de gestão de sala de leitura com interface 100% acessível para **NVDA** e compatível com **WCAG 2.1**.

[![Python 3.8+](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![wxPython 4.2+](https://img.shields.io/badge/wxPython-4.2+-green.svg)](https://wxpython.org/)

## 🎯 Visão Geral

DataLivros é uma aplicação desktop para gerenciar acervos de leitura com foco em **acessibilidade total**. Integra-se com **Google Books API**, persiste dados em **SQLite3** local e oferece experiência otimizada para usuários de leitores de tela.

### Principais Características
- ✅ **100% acessível** - Compatível com NVDA (WCAG 2.1)
- ✅ **Google Books API** - Auto-preenchimento inteligente de livros
- ✅ **Gerenciamento completo** - Livros, leitores e empréstimos
- ✅ **Controle de estoque** - Rastreamento por quantidade de exemplares
- ✅ **Edição de dados** - Atualizar livros e leitores após cadastro
- ✅ **Atalhos de teclado** - Navegação rápida (Ctrl+1/2/3, Ctrl+S, Ctrl+Q)
- ✅ **Feedback auditivo** - StatusBar com anúncios para NVDA
- ✅ **Sem complexidade** - Apenas wxPython, sem dependências extras

## 📋 Pré-requisitos

- **Python 3.8+**
- **pip** ou **conda**
- **Conexão com internet** (para consulta Google Books API)

## 🚀 Instalação

### Windows
```bash
# 1. Crie ambiente virtual
python -m venv venv
venv\Scripts\activate

# 2. Instale dependências
pip install -r requirements.txt

# 3. Execute a aplicação
python main.py
```

### Linux/macOS
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py
```

## 📖 Como Usar

### Aba 1: Circulação 📤
Registre empréstimos e devoluções.

1. **Buscar livro** - Digite ISBN ou título
2. **Selecionar leitor** - Escolha ou crie novo leitor
3. **Registrar** - Confirme empréstimo (14 dias automáticos)
4. **Devolver** - Selecione e finalize

### Aba 2: Cadastro de Livros 📚
Adicione novos livros via Google Books.

1. **Digite ISBN/título** na barra de busca
2. **Revise os 10 resultados** na lista
3. **Selecione um livro** para preencher formulário
4. **Defina a quantidade** de exemplares (padrão: 1)
5. **Salve** no acervo (Ctrl+S)

**Editar um livro:**
- Selecione um livro da lista de resultados
- Clique em "Editar Selecionado"
- O botão muda para "Atualizar Livro"
- Modifique os dados necessários
- Clique em "Atualizar Livro"

### Aba 3: Leitores 👥
Gerencie cadastro de usuários.

1. **Novo leitor** - Preencha nome (obrigatório)
2. **Defina a turma** (opcional)
3. **Salve** o registro
4. **Busque** por nome para filtrar
5. **Veja detalhes** de um leitor registrado

**Editar um leitor:**
- Selecione um leitor na lista
- Clique em "Editar Selecionado"
- O botão muda para "Atualizar Leitor"
- Modifique nome ou turma
- Clique em "Atualizar Leitor"

## ⌨️ Atalhos de Teclado

| Atalho | Ação |
|--------|------|
| `Ctrl+1` | Ir para aba Circulação |
| `Ctrl+2` | Ir para aba Cadastro |
| `Ctrl+3` | Ir para aba Leitores |
| `Ctrl+S` | Salvar livro |
| `Ctrl+Q` | Sair da aplicação |

## 🗂️ Estrutura do Projeto

```
datalivros/
├── main.py                   # Controlador (MVC)
├── view.py                   # Interface (MVC)
├── database.py               # Banco de dados (MVC)
├── api_service.py            # Google Books API
├── requirements.txt          # Dependências
├── LICENSE                   # Licença MIT
│
└── docs/                     # Documentação
    ├── README.md             # Índice de documentação
    ├── ACESSIBILIDADE.md     # WCAG 2.1 e NVDA
    ├── ARQUITETURA.md        # Padrão MVC
    ├── DATABASE.md           # Schema SQLite3
    ├── API.md                # Google Books
    ├── CONTRIBUINDO.md       # Guia de desenvolvimento
    └── FAQ.md                # Perguntas frequentes
```

## 🔧 Configuração Avançada

### Alterar período de empréstimo
Em `main.py`, função `_on_registrar_emprestimo`:
```python
data_devolucao = (datetime.now() + timedelta(days=21)).strftime('%Y-%m-%d')  # 21 dias
```

### Usar chave de API do Google Books
Em `api_service.py`:
```python
API_KEY = 'sua_chave_aqui'
params['key'] = API_KEY
```

Para mais informações, consulte [docs/API.md](docs/API.md).

## 📚 Documentação Completa

- **Usuários NVDA**: [ACESSIBILIDADE.md](docs/ACESSIBILIDADE.md)
- **Arquitetura técnica**: [ARQUITETURA.md](docs/ARQUITETURA.md)
- **Banco de dados**: [DATABASE.md](docs/DATABASE.md)
- **Google Books API**: [API.md](docs/API.md)
- **Contribuir ao projeto**: [CONTRIBUINDO.md](docs/CONTRIBUINDO.md)
- **FAQ**: [FAQ.md](docs/FAQ.md)

## 📦 Dependências

| Pacote | Versão | Propósito |
|--------|--------|-----------|
| wxPython | 4.2.1 | Interface gráfica |
| requests | 2.31.0 | Requisições HTTP (Google Books) |

## 🤝 Contribuindo

Leia [docs/CONTRIBUINDO.md](docs/CONTRIBUINDO.md) para instruções sobre como contribuir ao projeto.

## 📋 Histórico de Mudanças

Veja [CHANGELOG.md](CHANGELOG.md) para detalhes das versões e mudanças.

## 📝 Licença

Este projeto está licenciado sob a Licença MIT - veja [LICENSE](LICENSE) para detalhes.

---

**Desenvolvido com ❤️ para acessibilidade**
