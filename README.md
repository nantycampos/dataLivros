# DataLivros 📚

Sistema de gestão de sala de leitura com interface 100% acessível para **NVDA** e compatível com **WCAG 2.1**.

[![Python 3.8+](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![wxPython 4.2+](https://img.shields.io/badge/wxPython-4.2+-green.svg)](https://wxpython.org/)

## 🎯 Visão Geral

DataLivros é uma aplicação desktop para gerenciar acervos de leitura com foco em **acessibilidade total** e **controle inteligente de circulação**. Integra-se com **Google Books API**, persiste dados em **SQLite3** local e oferece experiência otimizada para usuários de leitores de tela.

### Principais Características
- ✅ **100% acessível** - Compatível com NVDA (WCAG 2.1)
- ✅ **Google Books API** - Auto-preenchimento inteligente de livros
- ✅ **Gestão de Acervo** - Edição completa e ajuste rápido de quantidades
- ✅ **Controle de Circulação** - Empréstimos com prazos automáticos (14 dias)
- ✅ **Inteligência de Alertas** - Ordenação por vencimento e resumo de abertura
- ✅ **Datas em Português** - Formato DD/MM/AAAA para melhor legibilidade
- ✅ **ListCtrl com Colunas** - Navegação por colunas acessível para NVDA
- ✅ **Diálogos de Erro** - Detalhamento técnico para fácil debug
- ✅ **Atalhos de teclado** - Navegação rápida (Ctrl+1/2/3/4, Ctrl+S, Ctrl+Q)
- ✅ **Feedback auditivo** - StatusBar com anúncios para NVDA
- ✅ **Sem complexidade** - Apenas wxPython, sem dependências extras

## 📋 Pré-requisitos

- **Python 3.8+**
- **pip** ou **conda**
- **Conexão com internet** (para consulta Google Books API)
- **NVDA** (opcional, mas recomendado para acessibilidade total)

## 🚀 Instalação

### Windows
```bash
# 1. Crie ambiente virtual
python -m venv venv
venv\Scripts\activate

# 2. Instale dependências
pip install -r requirements.txt

# 3. Configure a chave da Google Books API
# 3a. Copie o arquivo .env.example para .env
copy .env.example .env

# 3b. Abra o arquivo .env e adicione sua chave:
# GOOGLE_API_KEY=sua_chave_aqui

# 4. Execute a aplicação
python main.py
```

### Linux/macOS
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Configure a chave da API
cp .env.example .env
# Abra .env e adicione: GOOGLE_API_KEY=sua_chave_aqui

python main.py
```

### Obtendo a Chave da Google Books API
1. Acesse [Google Cloud Console](https://console.cloud.google.com/)
2. Crie um novo projeto
3. Ative a "Google Books API"
4. Crie uma "API key" em "Credenciais"
5. Copie a chave para o arquivo `.env`

## 📖 Como Usar - Rotina da Secretaria

### 🎬 Ao Abrir o Programa

Ao entrar na **aba de Circulação**, o sistema automaticamente anuncia via NVDA:

```
"Olá! Existem X livros vencidos e Y livro(s) vencendo hoje."
```

Isto permite identificar imediatamente quais empréstimos precisam de atenção.

---

### 📤 Aba 1: Circulação

**Para Registrar um Empréstimo:**

1. Digite o **ISBN ou título** do livro na busca
2. Pressione **Enter** ou clique "Buscar Livro"
3. Selecione o livro da lista
4. Digite o **nome do leitor** na busca de leitor
5. Selecione o leitor do combobox
6. Clique "Registrar Empréstimo"
7. Sistema calcula automaticamente:
   - Data do empréstimo: hoje
   - Data de devolução: hoje + 14 dias

**Para Registrar uma Devolução:**

1. Vá para a lista "Empréstimos Ativos"
2. Selecione o empréstimo (navegue pelas colunas)
3. Clique "Registrar Devolução"
4. Sistema registra a data da devolução

**Entendendo a Lista de Empréstimos:**

A lista mostra 5 colunas principais:
- **Livro**: Título do livro
- **Leitor**: Nome de quem pegou emprestado
- **Data Empréstimo**: Quando foi emprestado (DD/MM/AAAA)
- **Data Devolução Prevista**: Quando deve devolver (DD/MM/AAAA)
- **Status**: 🔴 VENCIDO | 🟡 VENCE HOJE | 🟢 NO PRAZO

**Dicas de Navegação com NVDA:**
- Use **setas para cima/baixo** para navegar linhas
- Use **setas para esquerda/direita** para navegar colunas
- NVDA anuncia cada coluna ao passar

---

### 📚 Aba 2: Cadastro de Livros

**Para Adicionar um Livro:**

1. Digite **ISBN ou título** na barra "Buscar na Google Books API"
2. Clique "Buscar Livro" ou pressione **Enter**
3. Aguarde a busca (máximo 5 segundos)
4. Selecione um dos 10 resultados
5. O formulário preenche automaticamente
6. **Revise os dados** (especialmente título, autores, editora)
7. Ajuste a **quantidade de exemplares** (padrão: 1)
8. Clique "Salvar Livro" ou pressione **Ctrl+S**

**Para Editar um Livro Existente:**

1. Na aba Catálogo, selecione um livro
2. Clique "Editar Detalhes"
3. Sistema abre a aba de Cadastro com os dados preenchidos
4. O botão "Salvar Livro" muda para "Atualizar Livro"
5. Faça as alterações necessárias
6. Clique "Atualizar Livro"

**Para Ajustar Quantidade Rapidamente:**

1. Na aba Catálogo, selecione um livro
2. Clique "Editar Quantidade"
3. Abre um diálogo com campo numérico
4. Digite a nova quantidade (1-1000)
5. Clique OK ou pressione **Enter**

---

### 📕 Aba 3: Catálogo

O catálogo mostra **TODOS os livros** cadastrados, incluindo aqueles com quantidade = 0.

**Para Buscar um Livro:**

1. Digite o **título ou ISBN** na barra de busca
2. A lista filtra em tempo real
3. Limpe o campo para ver o catálogo completo novamente

**Entendendo as Colunas:**

- **Título**: Nome do livro
- **Autor**: Autor(es) do livro
- **ISBN**: Código internacional
- **Editora**: Editora responsável
- **Quantidade**: Quantos exemplares temos

**Ações Disponíveis:**

- **Editar Quantidade**: Ajuste rápido (SpinCtrl)
- **Editar Detalhes**: Edição completa de todos os campos
- **Deletar Livro**: Remove o livro do sistema (pede confirmação)

---

### 👥 Aba 4: Leitores

**Para Registrar um Novo Leitor:**

1. Digite o **nome** do leitor (obrigatório)
2. Digite a **turma** (opcional)
3. Clique "Salvar Leitor" ou pressione **Enter**

**Para Buscar um Leitor:**

1. Digite o **nome** na barra de busca
2. A lista filtra em tempo real

**Para Ver Detalhes de um Leitor:**

1. Selecione um leitor na lista
2. Clique "Detalhes do Leitor"
3. Aparece um diálogo com nome e turma

**Para Editar um Leitor:**

1. Selecione um leitor na lista
2. Clique "Editar Selecionado"
3. Os campos preenchem com os dados atuais
4. O botão "Salvar Leitor" muda para "Atualizar Leitor"
5. Faça as alterações
6. Clique "Atualizar Leitor"

---

## ⌨️ Atalhos de Teclado

Atalhos de teclado facilitam muito o trabalho com NVDA:

| Atalho | Ação | Local |
|--------|------|-------|
| `Ctrl+1` | Ir para aba Circulação | Global |
| `Ctrl+2` | Ir para aba Cadastro | Global |
| `Ctrl+3` | Ir para aba Catálogo | Global |
| `Ctrl+4` | Ir para aba Leitores | Global |
| `Ctrl+S` | Salvar livro | Aba Cadastro |
| `Ctrl+Q` | Sair da aplicação | Global |
| `Enter` | Buscar (em campos de busca) | Várias abas |

**Dica:** Combine com NVDA para máxima eficiência. Pressione `Ctrl+1` para ir diretamente à Circulação, depois navegue com Tab.

---

### 📖 Como Usar - Aba 1: Circulação 📤
Registre empréstimos e devoluções.

1. **Buscar livro** - Digite ISBN ou título
2. **Selecionar leitor** - Escolha ou crie novo leitor
3. **Registrar** - Confirme empréstimo (14 dias automáticos)
4. **Devolver** - Selecione e finalize

### Aba 3: Catálogo �
Gerencie o acervo de livros.

1. **Busque por título ou ISBN** na barra de busca
2. **Visualize** todos os livros cadastrados
3. **Editar Quantidade** - Ajuste rápido de exemplares
4. **Editar Detalhes** - Edição completa dos dados
5. **Deletar** - Remove livro do sistema (pede confirmação)

**Entendendo as colunas:**
- **Título** - Nome do livro
- **Autor** - Autor(es)
- **ISBN** - Código internacional
- **Editora** - Editora responsável
- **Quantidade** - Quantos exemplares temos

### Aba 4: Leitores 👥
Gerencie cadastro de usuários.

1. **Novo leitor** - Preencha nome (obrigatório)
2. **Defina a turma** (opcional)
3. **Salve** o registro
4. **Busque** por nome ou turma para filtrar
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
| `Ctrl+3` | Ir para aba Catálogo |
| `Ctrl+4` | Ir para aba Leitores |
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
    ├── ATALHOS.md            # Atalhos de teclado
    ├── ARQUITETURA.md        # Padrão MVC
    ├── DATABASE.md           # Schema SQLite3
    ├── API.md                # Google Books
    ├── CATALOGO.md           # Gerenciamento de acervo
    ├── CONFIGURACAO.md       # Configurações da app
    ├── CONTRIBUINDO.md       # Guia de desenvolvimento
    ├── GUIA_USUARIO.md       # Tutorial completo
    ├── LOGGING.md            # Sistema de logs
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
| python-dotenv | 1.0.0 | Carregamento de variáveis de ambiente (.env) |

## 🤝 Contribuindo

Leia [docs/CONTRIBUINDO.md](docs/CONTRIBUINDO.md) para instruções sobre como contribuir ao projeto.

## 📋 Histórico de Mudanças

Veja [CHANGELOG.md](CHANGELOG.md) para detalhes das versões e mudanças.

## 📝 Licença

Este projeto está licenciado sob a Licença MIT - veja [LICENSE](LICENSE) para detalhes.

---

**Desenvolvido com ❤️ para acessibilidade**
