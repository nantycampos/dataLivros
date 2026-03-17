# ⌨️ Guia de Atalhos - DataLivros

Aprenda todos os atalhos de teclado para aumentar sua produtividade no DataLivros.

## 📌 Atalhos Globais (Funcionam em qualquer lugar)

| Atalho | O que faz | Onde usar |
|--------|-----------|-----------|
| `Ctrl+1` | Vai para aba **Circulação** | Global |
| `Ctrl+2` | Vai para aba **Cadastro** | Global |
| `Ctrl+3` | Vai para aba **Catálogo** | Global |
| `Ctrl+4` | Vai para aba **Leitores** | Global |
| `Ctrl+S` | Salva um livro | Aba Cadastro |
| `Ctrl+Q` | Sai do programa | Global |
| `Enter` | Busca / Confirma ação | Campos de busca, botões |
| `Escape` | Fecha diálogo/mensagem | Diálogos |
| `Tab` | Move para o próximo campo | Formulários |
| `Shift+Tab` | Move para o campo anterior | Formulários |
| `Seta Cima` | Move para cima | Listas, combobox |
| `Seta Baixo` | Move para baixo | Listas, combobox |
| `Seta Esquerda` | Move para coluna anterior | Tabelas (ListCtrl) |
| `Seta Direita` | Move para próxima coluna | Tabelas (ListCtrl) |

---

## 📋 Atalhos por Aba

### 🔄 Aba 1: Circulação (Ctrl+1)

**Para Registrar Empréstimo:**

```
Ctrl+1           → Abre aba Circulação
Tab              → Vai para campo "Buscar Livro"
[Digite ISBN]    → Busca o livro
Enter            → Busca
Seta Cima/Baixo  → Seleciona livro nos resultados
Tab              → Vai para combobox "Selecionar Leitor"
[Digite nome]    → Busca leitor
Seta Cima/Baixo  → Seleciona leitor
Tab              → Vai para botão "Registrar Empréstimo"
Enter            → Registra o empréstimo!
```

**Para Registrar Devolução:**

```
Ctrl+1           → Abre aba Circulação
Tab (várias x)   → Vai para lista "Empréstimos Ativos"
Seta Cima/Baixo  → Navega linhas da lista
Seta Esq/Dir     → Navega colunas para ler dados
Tab              → Vai para botão "Registrar Devolução"
Enter            → Registra a devolução!
```

---

### 📚 Aba 2: Cadastro (Ctrl+2)

**Para Adicionar Livro Novo:**

```
Ctrl+2              → Abre aba Cadastro
Tab                 → Vai para campo "Buscar Google Books"
[Digite ISBN]       → Digite o ISBN ou título
Enter               → Busca na Google Books
Aguarde...          → Sistema carrega resultados (máx 5 seg)
Seta Cima/Baixo     → Navega resultados
Enter               → Seleciona livro
Aguarde...          → Formulário preenche
Tab                 → Move entre campos (ISBN, Título, etc)
[Corrija se precisar]
Tab                 → Vai para campo "Quantidade"
[Mude para número correto]
Ctrl+S              → Salva o livro!
```

**Para Editar Livro (vindo do Catálogo):**

```
Ctrl+3              → Abre aba Catálogo
[Seleciona livro]   → Clica em "Editar Detalhes"
[Vai para Cadastro] → Sistema abre aba Cadastro
Tab                 → Move entre campos
[Faz mudanças]
Ctrl+S              → Atualiza o livro!
```

---

### 🗂️ Aba 3: Catálogo (Ctrl+3)

**Para Buscar um Livro:**

```
Ctrl+3              → Abre aba Catálogo
Tab                 → Vai para campo "Buscar no Catálogo"
[Digite título]     → Digite o que quer procurar
Aguarde...          → Lista filtra automaticamente
Seta Cima/Baixo     → Navega livros encontrados
```

**Para Editar Quantidade (Rápido):**

```
Ctrl+3              → Abre aba Catálogo
Tab (várias x)      → Vai para lista de livros
Seta Cima/Baixo     → Seleciona livro
Tab                 → Vai para botão "Editar Quantidade"
Enter               → Abre diálogo
[Digite novo valor] → Quantidade
Enter               → Pronto!
```

**Para Editar Detalhes (Completo):**

```
Ctrl+3              → Abre aba Catálogo
Tab (várias x)      → Vai para lista
Seta Cima/Baixo     → Seleciona livro
Tab                 → Vai para botão "Editar Detalhes"
Enter               → Vai para aba Cadastro
[Edita campos]
Ctrl+S              → Atualiza livro!
```

**Para Deletar um Livro:**

```
Ctrl+3              → Abre aba Catálogo
Tab (várias x)      → Vai para lista
Seta Cima/Baixo     → Seleciona livro
Tab                 → Vai para botão "Deletar Livro"
Enter               → Pede confirmação
Enter ou Espaço     → Confirma deletar
```

---

### 👥 Aba 4: Leitores (Ctrl+4)

**Para Registrar Novo Leitor:**

```
Ctrl+4              → Abre aba Leitores
Tab                 → Vai para campo "Nome"
[Digite nome]       → Nome completo
Tab                 → Vai para campo "Turma"
[Digite turma]      → Série/ano (opcional)
Tab                 → Vai para botão "Salvar Leitor"
Enter               → Salva leitor!
```

**Para Buscar um Leitor:**

```
Ctrl+4              → Abre aba Leitores
Tab                 → Vai para campo "Buscar Leitor"
[Digite nome]       → Parte do nome
Aguarde...          → Lista filtra automaticamente
Seta Cima/Baixo     → Navega leitores encontrados
```

**Para Editar um Leitor:**

```
Ctrl+4              → Abre aba Leitores
Tab (várias x)      → Vai para lista
Seta Cima/Baixo     → Seleciona leitor
Tab                 → Vai para botão "Editar Selecionado"
Enter               → Campos preenchem
[Edita nome/turma]
Tab                 → Vai para botão "Atualizar Leitor"
Enter               → Atualiza leitor!
```

---

## 🎯 Fluxos Completos

### Fluxo 1: Aluno Pega um Livro Novo

```
Ctrl+1                    → Circulação
Tab + [ISBN]              → Busca livro
Enter → Seta + Enter      → Seleciona livro
Tab + [Nome do aluno]     → Busca leitor
Seta + Seta               → Se existe, seleciona
  OU
Ctrl+4 → Tab + [Nome]     → Cria novo leitor
Ctrl+S → Tab + [Turma]    → Salva leitor
Ctrl+1 → [Repete busca]   → Volta à Circulação
Seta + Seta               → Seleciona novamente
Enter                     → Registra empréstimo!
```

### Fluxo 2: Aluno Devolve um Livro

```
Ctrl+1                  → Circulação
Tab (várias)            → Va para lista "Empréstimos"
Seta Cima/Baixo         → Procura o empréstimo
  DICA: Lista está ordenada por vencimento!
Seta Esq/Dir            → Lê colunas para confirmar
Tab                     → Va para botão "Devolução"
Enter                   → Registra devolução!
```

### Fluxo 3: Adicionar Novo Livro ao Acervo

```
Ctrl+2                  → Cadastro
Tab                     → Campo "Buscar Google Books"
[Digite ISBN]           → Busca rápida
Enter                   → Pesquisa
Aguarde...              → Carrega (máx 5 seg)
Seta Cima/Baixo         → Navega resultados
Enter                   → Seleciona livro
Aguarde...              → Preenche formulário
Tab                     → Move por campos (revisa dados)
[Corrija se erros]
Tab                     → Va para "Quantidade"
[Digite quantidade]
Ctrl+S                  → Salva livro!
```

### Fluxo 4: Corrigir Quantidade de Livro

```
Ctrl+3                  → Catálogo
Tab + [Título/ISBN]     → Busca livro
Seta Cima/Baixo         → Seleciona livro
Tab                     → Va para "Editar Quantidade"
Enter                   → Abre diálogo
[Digite novo número]
Enter                   → Atualiza!
```

---

## 🎓 Dicas Profissionais

### Para Máxima Velocidade

1. **Memorize Ctrl+1, Ctrl+2, Ctrl+3, Ctrl+4** → Navega entre abas em 1 segundo

2. **Use ISBN sempre que possível** → Mais rápido que procurar por título

3. **Combine Enter com Tab** → Não use mouse

4. **Use Seta + Enter em listas** → Mais eficiente que Tab+Tab+Tab

### Para Máxima Precisão (Com NVDA)

1. **Pressione Seta Esquerda/Direita** → Verifica cada coluna antes de confirmar

2. **Ouça o NVDA completamente** → Ele diz tudo que você precisa saber

3. **Se perdeu, pressione NVDA+Seta Cima** → Ele relê o último anúncio

### Para Evitar Erros

1. **Sempre revise o formulário** → Google Books às vezes erra

2. **Verifique o leitor correto** → Antes de registrar empréstimo

3. **Ouça o status** → 🟢 NO PRAZO / 🟡 VENCE HOJE / 🔴 VENCIDO

---

## 🔗 Combinações Úteis

### Pesquisa Rápida + Navegação

```
Ctrl+3          → Catálogo
Tab             → Campo busca
[Digita "Harry"]
Seta Cima       → 1º resultado (provavelmente "Harry Potter 1")
Seta Cima       → 2º resultado (provavelmente "Harry Potter 2")
... continua procurando
Enter           → Seleciona quando acha o correto
```

### Editar Rápido

```
Ctrl+3              → Catálogo
[Busca livro]
[Seleciona]
Tab                 → Botão "Editar Quantidade"
Enter               → Diálogo abre
[Digite quantidade]
Enter               → Salvo! (em 3 segundos)
```

### Registrar Empréstimo Rápido

```
Ctrl+1              → Circulação
Tab                 → Campo ISBN
[Digita "978..."]
Enter               → Busca
Seta Cima           → Seleciona 1º resultado
Tab                 → Combobox leitor
[Digita "João"]
Seta Cima           → Seleciona "João Silva"
Tab                 → Botão Registrar
Enter               → Pronto! (em ~10 segundos)
```

---

## 📞 Atalhos NVDA Complementares

Se está usando NVDA, esses atalhos ajudam bastante:

| Atalho NVDA | O que faz |
|-------------|-----------|
| `Insert + H` | Lista todos os atalhos NVDA |
| `Insert + N` | Menu do NVDA |
| `Insert + 1` | Liga/desliga modo voz contínua |
| `Insert + Espaço` | Liga/desliga NVDA |
| `Ctrl + Alt + N` | Abre console Python do NVDA |

---

## 🆘 Não Funciona?

- **Atalho não funciona?** Confira se está na aba correta
- **Seta não move?** Clique na lista/campo primeiro para ter foco
- **NVDA não fala?** Verifique se NVDA está ativo (Ctrl+Alt+N) ou reinicie
- **Perdeu atalho?** Volte para o README.md e procure por ⌨️

---

**Última atualização:** 2024  
**Desenvolvido para acessibilidade** ♿
