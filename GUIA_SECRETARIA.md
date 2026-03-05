# 📖 Guia Rápido - DataLivros v1.1.0 para Secretaria

> Instruções simples e diretas para a secretaria operacionalizar o sistema.

---

## 🚀 Primeira Execução

### Windows
```bash
# 1. Abra o CMD na pasta do projeto
cd c:\Users\Remakker\jogos\programas\dataLivros

# 2. Ative o ambiente virtual
venv\Scripts\activate

# 3. Execute o programa
python main.py
```

### macOS/Linux
```bash
cd ~/caminho/para/datalivros
source venv/bin/activate
python main.py
```

---

## 📚 As 3 Abas Principais

### Aba 1️⃣: CIRCULAÇÃO (Emprestar/Devolver)

**Use para:** Registrar empréstimos e devoluções de livros

#### Emprestar um Livro
1. **Busque o livro**
   - Digite ISBN ou título do livro
   - Clique "Buscar Livro"
   
2. **Selecione o leitor**
   - Digite nome ou procure na lista
   - Clique para selecionar

3. **Registre o empréstimo**
   - Clique "Registrar Empréstimo"
   - Sistema calcula automaticamente devolução em 14 dias

4. **Pronto!**
   - NVDA anuncia: "Livro emprestado com sucesso"
   - Lista de empréstimos atualiza automaticamente

#### Devolver um Livro
1. Selecione o empréstimo na lista "Empréstimos Ativos"
2. Clique "Registrar Devolução"
3. Sistema marca livro como "Disponível"

---

### Aba 2️⃣: CADASTRO DE LIVROS

**Use para:** Adicionar novos livros ao acervo

#### Adicionar um Livro via Google Books
1. **Busque na API**
   - Digite ISBN (código de barras) ou título
   - Clique "Buscar na API"
   - Sistema mostra até 10 resultados

2. **Selecione um resultado**
   - Use SETAS para navegar
   - ENTER para selecionar
   - Formulário popula automaticamente

3. **Revise e ajuste**
   - Verifique título, autor, ano
   - **IMPORTANTE:** Defina a quantidade de exemplares
     - Se tem 3 cópias do livro: digite "3"
     - Se tem 1 cópia: deixe "1" (padrão)

4. **Salve**
   - Clique "Salvar Livro" ou Ctrl+S
   - NVDA anuncia: "Livro salvo com sucesso"

#### Adicionar Livro Manual
1. Se o livro não está no Google Books:
   - Preencha manualmente: título, autor, editora, etc.
   - Clique "Salvar Livro"

#### Editar um Livro Já Cadastrado
1. Busque novamente na API (mesma sequência)
2. Selecione o livro da lista
3. Clique "Editar Selecionado"
4. Botão muda para "Atualizar Livro"
5. Modifique o que quiser (ex: aumentar quantidade)
6. Clique "Atualizar Livro"
7. NVDA anuncia: "Livro atualizado com sucesso"

---

### Aba 3️⃣: LEITORES

**Use para:** Registrar estudantes e usuários da biblioteca

#### Adicionar um Novo Leitor
1. **Preencha o cadastro**
   - **Nome:** Completo do aluno (obrigatório)
   - **Turma:** Classe/série (opcional, ex: "8º A", "1º EM")

2. **Salve o registro**
   - Clique "Salvar Leitor"
   - NVDA anuncia: "Leitor salvo com sucesso"

3. **Pronto!**
   - Leitor aparece na lista
   - Pode emprestar livros imediatamente

#### Buscar um Leitor
1. Na lista "Leitores", use o campo de busca
2. Digite nome ou parte do nome
3. Lista filtra em tempo real

#### Editar Dados de um Leitor
1. Selecione o leitor na lista
2. Clique "Editar Selecionado"
3. Botão muda para "Atualizar Leitor"
4. Modifique nome ou turma
5. Clique "Atualizar Leitor"

#### Ver Detalhes
1. Selecione leitor
2. Clique "Ver Detalhes"
3. Abre caixa mostrando: Nome e Turma

---

## ⌨️ Atalhos de Teclado Principais

| Tecla | Ação |
|-------|------|
| **Ctrl+1** | Ir para Circulação |
| **Ctrl+2** | Ir para Cadastro |
| **Ctrl+3** | Ir para Leitores |
| **Ctrl+S** | Salvar livro |
| **Ctrl+Q** | Sair do programa |

---

## 🎯 Fluxos Mais Comuns

### Fluxo 1: Aluno Vem Pegar Livro
```
1. Circulação → Buscar Livro
2. Digite título/ISBN → Buscar
3. Selecione livro (vê "[X] disponíveis")
4. Busque o nome do aluno → Selecione
5. Clique "Registrar Empréstimo"
✅ Pronto! Aluno leva livro, devolve em 14 dias
```

### Fluxo 2: Aluno Devolve Livro
```
1. Circulação → Lista "Empréstimos Ativos"
2. Procure o empréstimo do aluno
3. Selecione → Clique "Registrar Devolução"
✅ Pronto! Livro marca como "Disponível"
```

### Fluxo 3: Adicionar Livro Novo
```
1. Cadastro → Digite ISBN do livro
2. Buscar na API → Selecione resultado
3. Defina quantidade (ex: 2 cópias)
4. Salvar Livro
✅ Pronto! Livro entra no acervo
```

### Fluxo 4: Corrigir Informação de um Livro
```
1. Cadastro → Busque livro na API
2. Selecione → Clique "Editar Selecionado"
3. Corrija informação (ex: aumentar quantidade de 1 para 3)
4. Atualizar Livro
✅ Pronto! Mudança salva
```

---

## ✅ Checklist Diário

### No Início do Dia
- [ ] Abrir DataLivros
- [ ] Verificar empréstimos em "Circulação"
- [ ] Notar quais livros estão com "0 disponíveis" (todos emprestados)

### No Fim do Dia
- [ ] Registrar todas as devoluções
- [ ] Contar livros retornados
- [ ] Fechar o programa (Ctrl+Q)

### Semanalmente
- [ ] Revisar "Empréstimos Ativos"
- [ ] Identificar atrasos (14 dias passados)
- [ ] Notificar alunos que precisam devolver

---

## 🆘 Problemas Comuns e Soluções

### Problema: "Livro não encontrado na busca"
**Solução:**
1. Tente buscar apenas por título (sem ISBN)
2. Se ainda não encontrar, adicione manualmente:
   - Preencha os campos manualmente
   - Clique "Salvar Livro"

### Problema: "Não consigo emprestar - diz que não tem exemplares"
**Solução:**
1. O livro está com "0 disponíveis" (todos emprestados)
2. Aguarde alguém devolver
3. Ou adicione mais cópias: Editar livro → aumentar quantidade

### Problema: "Aluno não aparece na lista"
**Solução:**
1. Você já o cadastrou?
   - Se não: Aba Leitores → Novo Leitor
   - Se sim: Procure digitando o nome

### Problema: "Programa não abre"
**Solução:**
1. Verifique se Python está instalado: `python --version`
2. Ative ambiente: `venv\Scripts\activate`
3. Execute: `python main.py`
4. Se der erro, salve a mensagem e envie para suporte

---

## 💡 Dicas de Ouro

### 1. ISBN do Livro
- Código de barras na capa/contracapa
- 10 ou 13 dígitos
- Buscar por ISBN é mais preciso que por título

### 2. Gerenciar Quantidades
- Se tem 3 exemplares do mesmo livro → cadastre com "quantidade: 3"
- Sistema controla automáticamente quanto está disponível
- Todos podem ser emprestados ao mesmo tempo para diferentes alunos

### 3. Dados do Leitor
- **Obrigatório:** Nome
- **Recomendado:** Turma (para saber de qual classe é)
- Sem email ou telefone = mais privacidade + mais rápido

### 4. Acessibilidade NVDA
- Se usar leitor de tela: sistema anuncia tudo
- Todos os botões têm descrição clara
- Use Tab para navegar entre campos

---

## 📊 Relatório Básico (Manual)

Para saber quantos livros estão emprestados:

1. Vá para **Circulação**
2. Olhe para a seção "Empréstimos Ativos"
3. Conte quantas linhas tem = livros que saíram da biblioteca

**Exemplo:**
```
Empréstimos Ativos: 15 itens
= 15 livros estão com alunos
= Semanal precisa trazer de volta até 14 dias
```

---

## 📞 Suporte

| Dúvida | Resposta |
|--------|----------|
| **Programa travou** | Feche e abra novamente (Ctrl+Q) |
| **Esqueci senha** | Não existe senha! Qualquer um pode usar |
| **Perdeu algum dado** | Arquivo `datalibros.db` tem tudo salvo |
| **Quer mais features** | Abra uma Issue no GitHub |

---

## ✨ Tela Inicial Bem-vindo

Quando abre DataLivros:
1. **Você vê 3 abas** - cada cor diferente
2. **Primeira aba (Circulação)** - é onde você começa
3. **Tudo já conectado** - só usar!

---

**Versão:** 1.1.0  
**Data:** 5 de março de 2026  
**Status:** ✅ Pronto para Secretaria

---

## 🎓 Feedback da Secretaria

Depois de usar por uma semana, você pode:
1. Reportar bugs no GitHub
2. Sugerir melhorias
3. Contar se facilitou o trabalho! 📚

**GitHub:** https://github.com/nantycampos/dataLivros
