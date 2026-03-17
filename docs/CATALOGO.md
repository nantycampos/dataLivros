# 📚 Guia da Aba Catálogo

## Visão Geral

A **Aba Catálogo** permite visualizar, buscar e gerenciar todos os livros cadastrados no sistema. Você pode filtrar livros, editar quantidade, editar todos os detalhes ou deletar livros.

## Como Acessar

### Opção 1: Clicando na Aba
1. Na janela principal, clique na aba **"Catálogo"**

### Opção 2: Atalho de Teclado
- Pressione **Ctrl+3** para ir direto para o Catálogo

## Componentes da Aba

```
┌─────────────────────────────────────────────────────────────┐
│  Catálogo                                                   │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  ┌─ BUSCA DE LIVROS ──────────────────────────────────────┐ │
│  │ Buscar por Título ou ISBN:                             │ │
│  │ [________________(campo de busca)_________________]    │ │
│  └────────────────────────────────────────────────────────┘ │
│                                                               │
│  ┌─ CATÁLOGO DE LIVROS ───────────────────────────────────┐ │
│  │ ID   ISBN        Título        Autor    Editora Qtd    │ │
│  │ ┌──────────────────────────────────────────────────┐  │ │
│  │ │ 1   978...     Python para...  John Doe  Python 2  │ │
│  │ │ 2   979...     Clean Code      Robert    Prentice 1 │ │
│  │ │ 3   980...     1984            Orwell    Secker   3  │ │
│  │ │                                                    │  │ │
│  │ └──────────────────────────────────────────────────┘  │ │
│  │                                                        │ │
│  │ [Editar Quantidade] [Editar Detalhes] [Deletar Livro] │ │
│  └────────────────────────────────────────────────────────┘ │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

## Funcionalidades

### 1️⃣ VER TODOS OS LIVROS

Quando você entra na aba Catálogo, **todos os livros** cadastrados aparecem na lista automaticamente.

**Colunas exibidas:**
- **ID** - Número identificador do livro
- **ISBN** - Código ISBN do livro
- **Título** - Nome do livro
- **Autor** - Autor(es) do livro
- **Editora** - Editora do livro
- **Quantidade** - Quantos exemplares você tem

### 2️⃣ BUSCAR POR TÍTULO OU ISBN

No campo **"Buscar por Título ou ISBN:"** no topo, você pode:

#### Buscar por Título:
```
Digite: python
Resultado: Mostra livros com "python" no título
          (ex: Python 3, Python para Iniciantes, etc)
```

#### Buscar por ISBN:
```
Digite: 978-3-16-148410-0
Resultado: Mostra o livro com esse ISBN exato
```

#### Limpar Busca:
```
Apague o texto (deixe vazio)
Resultado: Mostra TODOS os livros novamente
```

**⚡ Funciona em tempo real:** Conforme você digita, a lista é filtrada automaticamente!

### 3️⃣ EDITAR QUANTIDADE

Quando você precisa mudar quantos exemplares tem de um livro:

**Passos:**
1. Clique no livro na lista para selecioná-lo
2. Clique no botão **"Editar Quantidade"**
3. Uma caixa de diálogo abre:
   ```
   Editar Quantidade
   ┌──────────────────────────────┐
   │ Digite a nova quantidade:     │
   │ Quantidade de exemplares:     │
   │ [___] (entre 1 e 1000)       │
   │ [OK] [Cancelar]             │
   └──────────────────────────────┘
   ```
4. Digite o novo número
5. Clique **OK**
6. A quantidade é atualizada no banco e na lista

### 4️⃣ EDITAR DETALHES COMPLETOS

Quando você precisa editar TUDO de um livro (título, ISBN, autores, editora, etc):

**Passos:**
1. Clique no livro na lista para selecioná-lo
2. Clique no botão **"Editar Detalhes"**
3. Você é automaticamente levado à aba **"Cadastro de Livros"**
4. Todos os campos estão preenchidos com os dados atuais do livro
5. O botão "Salvar Livro" muda para **"Atualizar Livro"**
6. Edite os campos desejados:
   - Título
   - ISBN
   - Autores
   - Editora
   - Ano de Publicação
   - Descrição
   - Categorias
   - Quantidade
7. Clique **"Atualizar Livro"**
8. Volta para o Catálogo e recarrega a lista

### 5️⃣ DELETAR LIVRO

Quando você quer remover um livro do sistema:

**⚠️ ATENÇÃO:** Esta ação **NÃO PODE SER DESFEITA!**

**Passos:**
1. Clique no livro na lista para selecioná-lo
2. Clique no botão **"Deletar Livro"**
3. Uma confirmação aparece:
   ```
   Confirmar Deletação
   ┌──────────────────────────────────────────┐
   │ Tem certeza que deseja deletar            │
   │ 'Python para Iniciantes'?                │
   │                                           │
   │ Esta ação não pode ser desfeita.         │
   │                                           │
   │ [Sim] [Não]                             │
   └──────────────────────────────────────────┘
   ```
4. Clique **Sim** para confirmar ou **Não** para cancelar
5. Se confirmado:
   - O livro é removido do banco de dados
   - A lista é atualizada
   - Uma mensagem de sucesso aparece

## Dados Recuperados do Banco

Todos os dados são recuperados corretamente da tabela `livros`:

| Campo | Tipo | Descrição |
|-------|------|-----------|
| **id** | INTEGER | ID único do livro |
| **isbn** | TEXT | ISBN do livro |
| **titulo** | TEXT | Título do livro |
| **autores** | TEXT | Autores (separados por vírgula) |
| **editora** | TEXT | Editora |
| **quantidade_total** | INTEGER | ⭐ **Quantidade de exemplares** |

## Exemplos de Uso

### Exemplo 1: Aumentar Quantidade de um Livro

```
Situação: Você recebeu mais 3 exemplares de um livro que já tinha 2.
Ação:
  1. Busque o livro na lista (ou deixe em branco para ver tudo)
  2. Clique no livro
  3. Clique "Editar Quantidade"
  4. Mude de 2 para 5
  5. Clique OK
Resultado: O livro agora mostra 5 exemplares
```

### Exemplo 2: Corrigir Dados de um Livro

```
Situação: O título de um livro está escrito errado: "Pyton" em vez de "Python"
Ação:
  1. Busque o livro (digite "pyton")
  2. Clique no livro
  3. Clique "Editar Detalhes"
  4. Vai para a aba Cadastro com os dados preenchidos
  5. Corrija o título para "Python"
  6. Clique "Atualizar Livro"
Resultado: O livro agora tem o título correto
```

### Exemplo 3: Remover Livro Danificado

```
Situação: Um livro foi danificado e você quer removê-lo do sistema
Ação:
  1. Busque o livro
  2. Clique no livro
  3. Clique "Deletar Livro"
  4. Confirme a deletação
Resultado: O livro é removido do banco de dados
```

## Dicas Importantes

✅ **DO:**
- Use a busca para encontrar rapidamente um livro
- Sempre confirme deletações
- Atualize a quantidade regularmente
- Corrija dados incorretos quando encontrar

❌ **NÃO FAÇA:**
- Não delete livros por acidente (use a confirmação!)
- Não esqueça de salvar alterações na edição de detalhes
- Não deixe quantidades negativas (mínimo é 1)

## Atalhos de Teclado

| Atalho | Ação |
|--------|------|
| **Ctrl+3** | Ir para Catálogo (e carrega livros) |
| **Ctrl+1** | Ir para Circulação |
| **Ctrl+2** | Ir para Cadastro de Livros |
| **Ctrl+4** | Ir para Leitores |

## Mensagens de Status

A barra inferior mostra mensagens sobre ações:

```
✓ "Catálogo carregado: 15 livro(s) encontrado(s)"
  → Significa que 15 livros estão na lista

✓ "3 livro(s) encontrado(s)"
  → Significa que sua busca achou 3 resultados

✓ "Nenhum livro encontrado para 'xyz'"
  → Significa que não há livros com esse termo

✓ "Quantidade atualizada: 5 exemplares"
  → Significa que a quantidade foi atualizada com sucesso

✗ "Erro: Selecione um livro na lista."
  → Significa que você precisa clicar em um livro antes de editar/deletar
```

## Acessibilidade (NVDA)

A aba Catálogo é completamente acessível para leitores de tela:

✓ Todos os botões têm descrições
✓ A lista é navegável com setas de teclado
✓ Mensagens de status são anunciadas
✓ Diálogos de confirmação são claros

---

**Pronto!** Agora você pode navegar, buscar e editar o catálogo completo de livros! 📚✨
