# 📝 Changelog - DataLivros

## [2.0.1] - 17 de março de 2026 (Refatoração e Limpeza)

### 🔧 Refatoração
- ✅ **Remoção de Funções Mortas**
  - Removido `executar()` em DataLivrosController (nunca era chamado)
  - Removido `buscar_leitores_por_nome()` em DatabaseGerenciador (substituído por `buscar_leitores_por_nome_ou_turma()`)

- ✅ **Busca por Turma em Leitores**
  - Aba Leitores agora permite buscar por nome **OU turma** (como na aba Circulação)
  - Alterado em main.py: `_atualizar_lista_leitores()` agora usa `buscar_leitores_por_nome_ou_turma()`

- ✅ **Remoção de IDs da Visualização**
  - IDs técnicos removidos das labels de leitores (mantém internamente via SetItemData)
  - Consistência com CirculacaoPanel e CatalogoPanel

- ✅ **Documentação Sincronizada**
  - README.md: Atualizado com Aba 3 (Catálogo) e Aba 4 (Leitores) corretos
  - README.md: Tabela de atalhos completa (Ctrl+1 a Ctrl+4)
  - docs/GUIA_USUARIO.md: Removido "ID" do Catálogo, adicionado "busca por turma" em Leitores
  - Estrutura de docs/ atualizada (12 arquivos documentados)

### 🧹 Limpeza de Código
- ✅ Documentação consolidada (nenhum novo .txt criado)
- ✅ Sem código morto ou funções não utilizadas
- ✅ Padrão DRY aplicado (reutilização de `buscar_leitores_por_nome_ou_turma()`)

---

## [2.0.0] - 16 de março de 2026 (Versão Final com Documentação Completa)

### ✨ Adicionado
- ✅ **Documentação Completa** 
  - `docs/GUIA_USUARIO.md` - Guia passo-a-passo para secretaria
  - `docs/ATALHOS.md` - Todos os atalhos de teclado
  - `docs/ACESSIBILIDADE.md` - Guia NVDA completo (WCAG 2.1)
  - `CHANGELOG.md` - Histórico de mudanças

- ✅ **README.md Atualizado**
  - Seção "Como Usar" com 4 abas detalhadas
  - Exemplos práticos com NVDA
  - Tabela de atalhos
  - Links para documentação

### 🎯 Melhorias de Qualidade
- ✅ Documentação em português claro e objetivo
- ✅ Exemplos práticos em cada seção
- ✅ Screenshots/referências para documentação visual futura
- ✅ Troubleshooting para problemas comuns

### 📊 Status Geral
- ✅ **8 Phases Completados:**
  1. Implementação do Catálogo
  2. Fix: Quantidade por exemplar
  3. Fix: Livros antigos visíveis
  4. Fix: Edição de livros
  5. Feature: Datas automáticas (14 dias)
  6. Feature: Sistema de alertas com ordenação
  7. Feature: Tratamento centralizado de erros
  8. Documentation: Guias completos (ATUAL)

- ✅ **Acessibilidade Total**: WCAG 2.1 Nível A
- ✅ **NVDA**: Totalmente suportado e testado
- ✅ **Testes**: 8/8 e 5/5 testes passaram nas fases críticas

---

## [1.1.2] - 6 de março de 2026

### ✨ Adicionado
- ✅ **Sistema profissional de logging** com arquivo de log rotativo
- ✅ **Módulo `logger_config.py`** - Logging centralizado com 4 funções especializadas
- ✅ **Tratamento robusto de exceções em API** - Captura de 401, 403, 404, 500, 503, timeouts
- ✅ **Mensagens de erro amigáveis em português** - Para cada tipo de falha da API
- ✅ **Método `_exibir_erro_dialog()`** em main.py - Diálogos acessíveis para NVDA
- ✅ **Diretório `logs/`** - Armazena histórico de operações com rotação diária
- ✅ **Script `test_error_handling.py`** - Validação completa do sistema de erros
- ✅ **Documentação `docs/LOGGING.md`** - Guia detalhado de logging e tratamento de erros

### 🔧 Modificado
- ✅ **api_service.py**:
  - Dicionário `MENSAGENS_ERRO` com 8 mensagens de erro localizadas
  - Função `buscar_livro_google_books()` completamente refatorada com:
    - Seções comentadas para clarity (VALIDAÇÃO, REQUISIÇÃO, VERIFICAÇÃO, etc)
    - Validação de entrada
    - Tratamento granular de exceções (timeout, connection, HTTP codes)
    - Logging em cada ponto crítico
    - Fallback gracioso em erro de parsing
  - Integração com funções de logging de `logger_config`
  
- ✅ **main.py**:
  - Importação de `logger` de `logger_config`
  - Novo método `_exibir_erro_dialog(titulo, mensagem, tipo)` com:
    - Atualização de StatusBar ANTES do diálogo (para NVDA anunciar)
    - Logging de erro no arquivo
    - Diálogo wx.MessageDialog bloqueante
    - Re-anúncio após fechar (acessibilidade NVDA)
  - Método `_on_buscar_livro_api()` atualizado com:
    - Tratamento de erros com `_exibir_erro_dialog()`
    - Mensagem de sucesso com número de resultados

### 📊 Logging
- ✅ **Arquivo de log diário**: `logs/datalibros_YYYYMMDD.log`
- ✅ **Rotação**: 5 MB por arquivo, mantém 5 backups
- ✅ **Formato**: `timestamp - logger - level - funcao:linha - mensagem`
- ✅ **Níveis**: DEBUG (arquivo), INFO (arquivo), WARNING (arquivo+console), ERROR (arquivo+console)
- ✅ **Funções especializadas**:
  - `log_error_api()` - Erros de HTTP com status code
  - `log_connection_error()` - Timeouts e problemas de rede
  - `log_busca_livro()` - Rastreamento de uso
  - `log_acesso_banco()` - Auditoria de banco de dados

### 🎯 Acessibilidade (NVDA)
- ✅ Diálogos de erro com feedback automático via StatusBar
- ✅ Anúncio ANTES de exibir diálogo (status + mensagem)
- ✅ Re-anúncio APÓS fechar diálogo
- ✅ Mensagens de erro em português clara e objetivas
- ✅ Sem dependência de dialetos/vozes específicas

### 🧪 Testes
- ✅ **test_error_handling.py**: 7 cenários de teste
  - Logging básico (info, warning, error)
  - Erros de API (401, 403, 404, 500, 503)
  - Erros de conexão (timeout, connection, DNS)
  - Buscas bem-sucedidas
  - Operações de banco de dados
  - Criação e verificação de arquivo de log
  - Validação de mensagens de erro em português
- ✅ **Resultado**: 17 linhas registradas no log (100% sucesso)

### 📚 Documentação
- ✅ **Novo: docs/LOGGING.md** - 400+ linhas com:
  - Visão geral do sistema de logging
  - Estrutura de arquivo de logs
  - Formato e níveis de severidade
  - Documentação de cada função de logging
  - Mensagens de erro em português
  - Integração com NVDA
  - Exemplos práticos de 3 cenários
  - Instruções de configuração
  - Análise de logs (powershell)
  - Troubleshooting
  - Checklist de implementação

### ✅ Validação
- ✅ **Sintaxe**: Todos 5 arquivos Python sem erros
  - main.py ✅
  - api_service.py ✅
  - logger_config.py ✅
  - database.py ✅
  - view.py ✅
- ✅ **Testes**: test_error_handling.py passou 100%
- ✅ **Integração**: Todos os módulos funcionando juntos

### 🔒 Segurança
- ✅ Nenhuma exposição de dados sensíveis em logs
- ✅ Arquivo de log não versionado (.gitignore)
- ✅ Mensagens de erro não revelam estrutura interna

---

## [1.1.1] - 6 de março de 2026

### ✨ Adicionado
- ✅ **Suporte a python-dotenv** - Carregamento seguro de variáveis de ambiente
- ✅ **Arquivo .env** - Armazena GOOGLE_API_KEY de forma segura
- ✅ **Arquivo .env.example** - Template público para novos desenvolvedores
- ✅ **Documento CONFIGURACAO.md** - Guia completo de setup da Google Books API

### 🔧 Modificado
- ✅ **requirements.txt**: Adicionado `python-dotenv==1.0.0`
- ✅ **api_service.py**:
  - Importado `load_dotenv` e `os`
  - Carregamento automático de `.env` no início do módulo
  - Variável `GOOGLE_API_KEY` carregada via `os.getenv()`
  - Função `buscar_livro_google_books()` agora inclui chave nas requisições se configurada
- ✅ **README.md**: Adicionado passo-a-passo de setup de .env e obtenção de chave
- ✅ **.gitignore**: Melhorado com mais padrões de configuração sensível

### 🔒 Segurança
- ✅ `.env` protegido (no .gitignore)
- ✅ Chave da API não exposta no código
- ✅ Funcionamento offline sem erro (sem chave = 100 req/dia)
- ✅ Suporte para múltiplos ambientes (dev, prod)

### 📚 Documentação
- ✅ **Novo: docs/CONFIGURACAO.md** - Segurança, setup, troubleshooting
- ✅ **Novo: .env.example** - Template para usuários

---

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
