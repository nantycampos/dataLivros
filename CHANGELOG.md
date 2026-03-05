# 📝 Changelog - DataLivros

## [1.1.0] - 5 de março de 2026

### ✨ Adicionado
- ✅ **Controle de estoque por quantidade** - Rastreamento de `quantidade_total` por livro
- ✅ **Edição de dados** - Modo de edição para livros e leitores com Salvar → Atualizar
- ✅ **Validação de disponibilidade** - Bloqueia empréstimo se quantidade_disponível = 0
- ✅ **Anúncio de quantidade** - NVDA anuncia "[X] disponíveis" ao selecionar livro
- ✅ **SetHelpText em todos os botões** - Acessibilidade NVDA completa para 10 botões
- ✅ **Campo de quantidade no cadastro** - SpinCtrl para definir exemplares (1-1000)
- ✅ **Simplificação de leitores** - Removido email/telefone/endereco, mantido nome/turma

### 🔧 Modificado
- ✅ **database.py**:
  - Adicionado `quantidade_total INTEGER DEFAULT 1` à tabela `livros`
  - Adicionado `status TEXT DEFAULT 'Disponível'` à tabela `livros`
  - Removido `email`, `telefone`, `endereco` da tabela `leitores`
  - Adicionado `turma TEXT` à tabela `leitores`
  - Novo método `contar_emprestimos_ativos_livro(livro_id)`
  - Atualizado `registrar_emprestimo()` para marcar livro como 'Emprestado'
  - Atualizado `registrar_devolucao()` para marcar livro como 'Disponível'
  - Atualizado `atualizar_livro()` para aceitar `quantidade_total`

- ✅ **main.py**:
  - Adicionado `self.editando_livro_id` para rastreamento de edição
  - Adicionado `self.editando_leitor_id` para rastreamento de edição
  - Novo método `_on_editar_livro()` para carregar livro em edição
  - Novo método `_on_editar_leitor()` para carregar leitor em edição
  - Modificado `_on_salvar_livro()` para diferençar criação vs atualização
  - Modificado `_on_salvar_leitor()` para diferenciar criação vs atualização
  - Melhorado `_on_limpar_campos_cadastro()` para cancelar edição
  - Adicionada validação em `_on_registrar_emprestimo()` para quantidade > 0
  - Atualizado `_atualizar_lista_resultados_livro()` com "[X] disponíveis"
  - Atualizado `_on_selecionar_livro_circulacao()` com anúncio de quantidade

- ✅ **view.py**:
  - Adicionado `texto_quantidade` (SpinCtrl) em CadastroPanel
  - Adicionado `btn_editar` com SetHelpText em CadastroPanel
  - Adicionado `btn_editar_leitor` com SetHelpText em LeitoresPanel
  - Removido `texto_email`, `texto_telefone`, `texto_endereco` em LeitoresPanel
  - SetHelpText em todos os 10 botões da aplicação
  - Melhorado layout de LeitoresPanel com estrutura button_sizer

### 📚 Documentação
- ✅ **README.md** - Adicionado Controle de estoque e Edição de dados nas features
- ✅ **docs/DATABASE.md** - Atualizado schema de leitores (removido email/telefone/endereco)
- ✅ **docs/CONTRIBUINDO.md** - Removido email, adicionado link direto ao GitHub
- ✅ **docs/FAQ.md** - Atualizadas respostas sobre suporte e comunidade
- ✅ **Novo: CHANGELOG.md** - Este arquivo com histórico detalhado

### 🧹 Removido
- ❌ Referências a `email`, `telefone`, `endereco` em todos os arquivos Python
- ❌ Código morto e variáveis obsoletas
- ❌ Comentários obsoletos

### ✅ Validação
- ✅ **Sintaxe**: main.py, view.py, database.py, api_service.py compilam 100%
- ✅ **Acessibilidade**: SetHelpText em todos os botões e campos
- ✅ **Persistência**: Métodos de atualização testados
- ✅ **NVDA**: Anúncios de status durante edição

---

## [1.0.0] - 4 de março de 2026

### ✨ Adicionado
- ✅ Sistema completo de gestão de sala de leitura
- ✅ Integração Google Books API com seleção de 10 resultados
- ✅ 3 abas funcionais (Circulação, Cadastro, Leitores)
- ✅ Banco de dados SQLite3 com 3 tabelas
- ✅ 100% compatível com NVDA (WCAG 2.1)
- ✅ 5 atalhos de teclado principais
- ✅ Validações e tratamento de erros

### 🐛 Corrigido
- ✅ **wx.AcceleratorTable TypeError** - Fixed 4-tuples → 3-tuples issue
- ✅ ID binding para atalhos funcionando corretamente

### 📚 Documentação
- ✅ README profissional e conciso
- ✅ docs/ACESSIBILIDADE.md - WCAG 2.1 + NVDA
- ✅ docs/ARQUITETURA.md - Padrão MVC
- ✅ docs/DATABASE.md - Schema e CRUD
- ✅ docs/API.md - Google Books integration
- ✅ docs/CONTRIBUINDO.md - Developer guide
- ✅ docs/FAQ.md - Perguntas frequentes

### 🗑️ Removido
- ❌ CORRECOES.md - Relatório de bug (obsoleto)
- ❌ CONCLUSAO.md - Documento de status (obsoleto)
- ❌ STRUCTURE.md - Arquivo duplicado (consolidado em ARQUITETURA.md)

### 🚀 Melhorias Futuras
- [ ] Testes unitários
- [ ] Backup automático
- [ ] Relatórios e estatísticas
- [ ] Interface web (Flask/Django)
- [ ] Suporte PostgreSQL para múltiplos usuários
- [ ] Sincronização em nuvem

---

**Status:** Produção-ready ✅
