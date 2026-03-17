# 📖 Guia Completo de Usuário - DataLivros

Bem-vindo ao DataLivros! Este guia descreve todas as funcionalidades do sistema de gerenciamento de biblioteca.

## 📑 Índice

1. [Visão Geral](#visão-geral)
2. [Rotina Diária da Secretaria](#rotina-diária-da-secretaria)
3. [Circulação de Livros](#circulação-de-livros)
4. [Cadastro de Livros](#cadastro-de-livros)
5. [Gestão do Catálogo](#gestão-do-catálogo)
6. [Registro de Leitores](#registro-de-leitores)
7. [Sistema de Alertas](#sistema-de-alertas)
8. [Navegação com NVDA](#navegação-com-nvda)
9. [Dicas Rápidas](#dicas-rápidas)

---

## 🎯 Visão Geral

O DataLivros é um sistema de gestão de biblioteca escolar com foco em acessibilidade para usuários de leitores de tela (NVDA). O programa funciona com **4 abas principais**:

1. **Circulação** (Ctrl+1) - Empréstimos e devoluções
2. **Cadastro** (Ctrl+2) - Adicionar novos livros
3. **Catálogo** (Ctrl+3) - Visualizar e editar catálogo
4. **Leitores** (Ctrl+4) - Gerenciar usuários

---

## 📅 Rotina Diária da Secretaria

### Ao Abrir o Programa

1. O sistema abre na **aba de Circulação**
2. Automaticamente anuncia via NVDA:
   ```
   "Olá! Existem X livros vencidos e Y livro(s) vencendo hoje."
   ```
3. Este anúncio acontece **automaticamente sempre que você entra nesta aba**

### Primeira Coisa: Verificar Atrasos

1. **Escute o anúncio** na abertura
2. A **lista de empréstimos** está ordenada por data de vencimento (mais antigos primeiro)
3. **Livros vencidos aparecem em VERMELHO** com emoji 🔴 VENCIDO
4. **Livros vencendo hoje** aparecem em LARANJA com emoji 🟡 VENCE HOJE

### Workflow Típico de Dia

**De Manhã:**
- Abra o programa
- Escute quantos livros estão atrasados
- Registre as **primeiras devoluções**

**Durante o Dia:**
- Registre **novos empréstimos** conforme os alunos pegam livros
- Registre **devoluções** conforme devolvem

**No Final do Dia:**
- Pressione **Ctrl+1** para visualizar saldo final
- Anote qualquer livro que ficou em atraso
- Feche o programa com **Ctrl+Q**

---

## 🔄 Circulação de Livros

### O que é Circulação?

A aba de Circulação gerencia o movimento de livros: **quem pega, quando devolve**.

### Registrando um Empréstimo

**Passo 1: Buscar o Livro**

1. Vai para a aba Circulação (pressione **Ctrl+1**)
2. No campo "Buscar Livro", digite:
   - **ISBN** (mais rápido), OU
   - **Parte do título** (ex: "Harry", "Aventura")
3. Pressione **Enter** ou clique "Buscar Livro"
4. A lista abaixo mostra resultados (máximo 10)

**Passo 2: Selecionar o Livro**

1. Use setas para cima/baixo para navegar os resultados
2. Quando encontrar o livro desejado, **memorize o nome**
3. NVDA anuncia: "Livro disponível, X exemplares"

**Passo 3: Buscar o Leitor**

1. No campo "Buscar ou Criar Leitor", digite:
   - **Nome completo** do aluno, OU
   - **Parte do nome** (ex: "João", "Silva")
2. A lista filtra automaticamente
3. Se o leitor **não aparece**, ele ainda não foi registrado

**Passo 4: Criar Leitor (se necessário)**

Se o leitor não existe:
1. Pressione **Ctrl+4** para ir à aba "Leitores"
2. Digite o nome completo
3. Digite a turma (se souber)
4. Clique "Salvar Leitor"
5. Volte à aba Circulação (**Ctrl+1**)
6. Busque o leitor novamente

**Passo 5: Registrar Empréstimo**

1. Selecione o **livro** na lista superior
2. Selecione o **leitor** no combobox abaixo
3. Clique "Registrar Empréstimo" (ou pressione Enter)
4. Sistema confirma: "Empréstimo registrado com sucesso!"
5. **Datas são calculadas automaticamente:**
   - Data de empréstimo: **hoje**
   - Data de devolução: **hoje + 14 dias**

### Registrando uma Devolução

**Cenário: O aluno devolveu o livro**

1. Vai para lista "Empréstimos Ativos"
2. Use setas para localizar o empréstimo:
   - Navigue por **linha** (seta cima/baixo)
   - Navigue por **coluna** (seta esquerda/direita) para ler os dados
3. NVDA anuncia:
   ```
   "Linha X: ID 5 | Harry Potter | João Silva | 15/01/2024 | 29/01/2024 | 🟢 NO PRAZO"
   ```
4. Com o empréstimo selecionado, clique "Registrar Devolução"
5. Sistema confirma: "Devolução registrada!"

### Entendendo as Colunas da Circulação

| Coluna | O que é | Exemplo |
|--------|---------|---------|
| **ID** | Número único do empréstimo | 5, 10, 150 |
| **Livro** | Título do livro | "Harry Potter e a Pedra Filosofal" |
| **Leitor** | Quem pegou emprestado | "João Silva Santos" |
| **Data Empréstimo** | Quando foi emprestado | 15/01/2024 |
| **Data Devolução Prevista** | Quando deve devolver | 29/01/2024 (14 dias depois) |
| **Status** | Situação do empréstimo | 🟢 NO PRAZO / 🟡 VENCE HOJE / 🔴 VENCIDO |

---

## 📚 Cadastro de Livros

### Como Funciona

A aba de Cadastro permite **adicionar novos livros** usando a **Google Books API** para preenchimento automático.

### Adicionando um Novo Livro

**Passo 1: Buscar o Livro na Google Books**

1. Vai para aba "Cadastro" (**Ctrl+2**)
2. No campo "Buscar na Google Books API", digite:
   - **ISBN** (muito rápido), OU
   - **Título do livro**
3. Clique "Buscar Livro" ou pressione **Enter**
4. Aguarde alguns segundos...

**Passo 2: Revisar Resultados**

1. A lista mostra até 10 resultados da Google Books
2. Navegue com setas para cima/baixo
3. Leia cada resultado até encontrar o livro certo
4. NVDA anuncia: "Livro X: [Título], [Autor]"

**Passo 3: Selecionar o Livro**

1. Com o livro desejado selecionado, clique nele (ou pressione Enter)
2. Aguarde o formulário preencher
3. Os campos aparecem preenchidos:
   - ISBN
   - Título
   - Autor(es)
   - Editora
   - Descrição
   - Quantidade (padrão: 1)

**Passo 4: Revisar e Ajustar**

1. **Revise todos os campos** (erros na Google Books são comuns)
2. **Corrija o que for necessário:**
   - Use Tab para passar de campo em campo
   - Edite título, autores, editora se tiverem erros
3. **Ajuste a quantidade:**
   - Se tem 3 exemplares do livro, mude de 1 para 3
   - Use o campo numérico ou clique nos botões +/-

**Passo 5: Salvar**

1. Clique "Salvar Livro" (ou pressione **Ctrl+S**)
2. Sistema confirma: "Livro salvo com sucesso!"
3. O livro agora aparece no **Catálogo**

### Editando um Livro Existente

Se você precisa **corrigir ou atualizar** um livro já cadastrado:

**Opção 1: Pela Aba Catálogo**

1. Vai para **Catálogo** (**Ctrl+3**)
2. Busque o livro que quer editar
3. Selecione-o na lista
4. Clique "Editar Detalhes"
5. Você será levado à aba **Cadastro** com dados preenchidos
6. O botão agora diz "Atualizar Livro"
7. Faça as mudanças necessárias
8. Clique "Atualizar Livro"

**Opção 2: Rápida (só a quantidade)**

1. Na aba **Catálogo**, selecione o livro
2. Clique "Editar Quantidade"
3. Abre um diálogo com SpinCtrl (campo de números)
4. Digite a nova quantidade (1-1000)
5. Clique OK ou pressione **Enter**

---

## 🗂️ Gestão do Catálogo

### O que é o Catálogo?

O Catálogo mostra **TODOS os livros** cadastrados no sistema, incluindo:
- Livros com quantidade > 0 (disponíveis)
- Livros com quantidade = 0 (todos emprestados ou sem exemplares)
- **O catálogo nunca filtra por disponibilidade** (ao contrário da Circulação)

### Visualizando o Catálogo

1. Vai para aba **Catálogo** (**Ctrl+3**)
2. Você vê uma tabela com colunas:
   - **Título**: Nome do livro
   - **Autor**: Autor(es)
   - **ISBN**: Código internacional
   - **Editora**: Quem publicou
   - **Quantidade**: Quantos exemplares temos

### Buscando um Livro no Catálogo

1. No campo "Buscar no Catálogo", digite:
   - **Título** (ex: "Harry")
   - **ISBN** (ex: "978")
   - **Autor** (ex: "Rowling")
2. A lista filtra **em tempo real**
3. Limpe o campo para ver tudo novamente

### Ações Disponíveis

**Editar Quantidade (Rápido)**

1. Selecione um livro
2. Clique "Editar Quantidade"
3. Mude para o número correto
4. OK - Atualizado!

**Editar Detalhes (Completo)**

1. Selecione um livro
2. Clique "Editar Detalhes"
3. Você vai para aba **Cadastro**
4. Edite qualquer campo
5. Clique "Atualizar Livro"

**Deletar Livro**

1. Selecione um livro
2. Clique "Deletar Livro"
3. Sistema pede confirmação: "Tem certeza?"
4. Clique "Sim" para confirmar
5. Livro é removido do sistema (não pode desfazer!)

### Quando Usar Cada Aba

| Você quer... | Use qual aba? |
|---------|-----------|
| Adicionar livro novo | **Cadastro** (Ctrl+2) |
| Ver todos os livros | **Catálogo** (Ctrl+3) |
| Rápido: mudar quantidade | **Catálogo** → Editar Quantidade |
| Completo: editar tudo | **Catálogo** → Editar Detalhes → **Cadastro** |
| Deletar um livro | **Catálogo** → Deletar Livro |

---

## 👥 Registro de Leitores

### O que é?

Leitores são os **alunos, professores ou visitantes** que pegam livros emprestados.

### Registrando um Novo Leitor

1. Vai para aba **Leitores** (**Ctrl+4**)
2. Preencha:
   - **Nome** (obrigatório): Nome completo
   - **Turma** (opcional): Série/ano (ex: "6A", "9B")
3. Clique "Salvar Leitor" ou pressione **Enter**
4. Sistema confirma: "Leitor salvo!"
5. O leitor agora pode emprestar livros

### Buscando um Leitor

1. No campo "Buscar Leitor", digite:
   - **Nome** (ex: "João Silva")
   - **Turma** (ex: "7A", "8º ano")
2. A lista filtra automaticamente
3. Exemplo: Digite "7A" e aparecem todos os leitores da turma 7A

### Vendo Detalhes de um Leitor

1. Na lista, selecione um leitor
2. Clique "Detalhes do Leitor"
3. Abre um diálogo mostrando:
   - Nome
   - Turma (se preenchida)

### Editando um Leitor

1. Selecione o leitor na lista
2. Clique "Editar Selecionado"
3. Os campos preenchem com dados atuais
4. O botão muda para "Atualizar Leitor"
5. Edite o nome ou turma conforme necessário
6. Clique "Atualizar Leitor"

---

## 🚨 Sistema de Alertas

### Como Funciona

O DataLivros **monitora automaticamente** os prazos de devolução e mostra alertas visuais e sonoros.

### Os 3 Status de Um Empréstimo

**🔴 VENCIDO** (em vermelho)
- A data de devolução passou
- Exemplo: Era para devolver em 15/01, estamos em 20/01
- **Ação:** Procure o aluno imediatamente!

**🟡 VENCE HOJE** (em laranja/amarelo)
- A data de devolução é hoje
- Exemplo: Era para devolver hoje 20/01
- **Ação:** Lembre o aluno antes do horário de saída

**🟢 NO PRAZO** (em verde)
- Ainda há tempo para devolver
- Exemplo: É para devolver em 25/01, estamos em 20/01
- **Ação:** Nenhuma ação necessária

### Anúncio Automático

**Sempre que você entra na aba Circulação**, o sistema anuncia:

```
"Olá! Existem 3 livros vencidos e 1 livro vencendo hoje."
```

Isto ajuda você a saber imediatamente se há alertas.

### Ordenação Automática

A lista de empréstimos **está sempre ordenada** por data de devolução:
- **Primeiro** (topo): Os vencidos (mais antigos)
- **Depois**: Os vencendo hoje
- **Por último**: Os no prazo

Assim você não precisa procurar, basta olhar o topo!

### Cores e Emojis

| Status | Emoji | Cor | Significado |
|--------|-------|------|-------------|
| Vencido | 🔴 | Vermelho | URGENTE |
| Vence Hoje | 🟡 | Amarelo | ATENÇÃO |
| No Prazo | 🟢 | Verde | OK |

---

## ⌨️ Navegação com NVDA

### Por que NVDA?

NVDA (NonVisual Desktop Access) é um **leitor de tela gratuito** que anuncia tudo que aparece na tela. DataLivros foi desenvolvido especificamente para funcionar bem com NVDA.

### Atalhos NVDA Úteis

| Tecla | O que faz |
|-------|-----------|
| `NVDA + F` | Ativa "Procurar" |
| `NVDA + Tab` | Anuncia elemento focado |
| `NVDA + Seta Cima` | Lê contexto do parágrafo anterior |
| `NVDA + Seta Baixo` | Lê contexto do parágrafo seguinte |
| `Insert + H` | Lista de atalhos NVDA |

### Navegação em ListCtrl (Tabelas)

As listas (Empréstimos, Catálogo, Leitores) são **tabelas com colunas**. Para navegar:

**Mover por Linhas:**
- Seta Cima / Seta Baixo: Move entre linhas

**Mover por Colunas:**
- Seta Esquerda / Seta Direita: Move entre colunas

**Exemplo de Navegação:**

1. Pressione Ctrl+1 (vai para Circulação)
2. Tab até chegar na lista de Empréstimos
3. NVDA anuncia: "Lista de empréstimos, linha 1"
4. Pressione Seta Cima para ir para linha 0
5. Pressione Seta Direita para navegar colunas
6. NVDA anuncia cada coluna conforme você move

### Diálogos e Mensagens

Quando o sistema mostra uma mensagem:

1. NVDA anuncia o título
2. NVDA anuncia o conteúdo
3. Você pode fechar com Enter ou Escape

**Dica:** Se perdeu o que NVDA falou, pressione `NVDA + Seta Cima` para que ele releia.

---

## 💡 Dicas Rápidas

### Velocidade

- **Abra direto na aba que precisa:** Pressione Ctrl+1, Ctrl+2, Ctrl+3 ou Ctrl+4
- **Não use o mouse:** Tudo funciona com Tab, Enter e setas
- **Combine com NVDA:** Menos leitura, mais eficiência

### Dados

- **ISBN é mais rápido:** Ao buscar livros, use ISBN ao invés de título
- **Revise sempre:** Google Books às vezes erra informações
- **Backup é importante:** Faça backup regular da pasta de dados

### Empréstimos

- **14 dias é padrão:** Todos os empréstimos começam com prazo de 14 dias
- **Altere se necessário:** Pode mudar em `main.py` (veja [CONFIGURAÇÃO.md](CONFIGURACAO.md))
- **Datas em português:** Sempre DD/MM/AAAA para fácil leitura

### Leitores

- **Use nomes completos:** "João Silva" é melhor que "João"
- **Turma ajuda:** Registre a turma para saber de quem é cada livro
- **Atualize regularmente:** No fim do ano, retire alunos que saíram

### Erros

- **Não pague pegar:** Se algo der erro, uma mensagem clara aparece
- **Mensagens em português:** Tudo é anunciado claramente
- **Suporte técnico:** Veja [SUPORTE.md](SUPORTE.md) para mais ajuda

---

## 🆘 Precisa de Ajuda?

- **Erros técnicos?** Veja [SUPORTE.md](SUPORTE.md)
- **Dúvidas de NVDA?** Veja [ACESSIBILIDADE.md](ACESSIBILIDADE.md)
- **Perguntas comuns?** Veja [FAQ.md](FAQ.md)

---

**Última atualização:** 2024
**Desenvolvido para acessibilidade total** ♿ 
