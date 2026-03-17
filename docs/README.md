# 📚 Documentação DataLivros - Índice Completo

Bem-vindo à documentação completa do DataLivros! Este é o índice central de toda a documentação do projeto.

## 🎯 Comece Aqui

### 👤 Você é um Usuário? (Secretária, Professor, Aluno)
**[→ GUIA_USUARIO.md](GUIA_USUARIO.md)** - Tudo que você precisa saber
- Rotina diária da secretaria
- Passo-a-passo para cada aba
- Exemplos com NVDA
- Sistema de alertas explicado
- Dicas rápidas

**[→ ATALHOS.md](ATALHOS.md)** - Todos os atalhos de teclado
- Atalhos globais
- Atalhos por aba
- Fluxos completos passo-a-passo
- Dicas profissionais para velocidade

### ♿ Usa NVDA ou Leitor de Tela?
**[→ ACESSIBILIDADE.md](ACESSIBILIDADE.md)** - Guia completo para leitores de tela
- Setup do NVDA (passo-a-passo)
- Navegação detalhada com NVDA
- WCAG 2.1 Compliance details
- Componentes acessíveis explicados
- Exemplos práticos com NVDA
- Troubleshooting

**Resumo:**
- ✅ WCAG 2.1 Nível A completo
- ✅ NVDA 2020.1+ totalmente suportado
- ✅ 100% navegável por teclado
- ✅ Sem dependência de mouse

### 🧑‍💻 Você é um Desenvolvedor?
**[→ ARQUITETURA.md](ARQUITETURA.md)** - Estrutura técnica
- Padrão MVC
- Classes principais
- Fluxo de dados
- Integração com Google Books API

**[→ DATABASE.md](DATABASE.md)** - Banco de dados
- Schema SQLite3
- Tabelas (livros, leitores, emprestimos)
- Relacionamentos
- Queries principais

**[→ API.md](API.md)** - Google Books API
- Como integrar
- Tratamento de erros
- Rate limiting
- Exemplos de uso

**[→ LOGGING.md](LOGGING.md)** - Sistema de logging
- Estrutura de logs
- Níveis (DEBUG, INFO, WARNING, ERROR)
- Arquivo de log rotativo
- Análise de erros

### 🛠️ Setup e Configuração
**[→ CONFIGURACAO.md](CONFIGURACAO.md)** - Como configurar
- Requisitos do sistema
- Instalação passo-a-passo
- Variáveis de ambiente (.env)
- Troubleshooting

### 📖 Contribuir ao Projeto
**[→ CONTRIBUINDO.md](CONTRIBUINDO.md)** - Guia de desenvolvimento
- Ambiente de desenvolvimento
- Padrões de código
- Submissão de PRs
- Reporting de bugs

### ❓ Dúvidas Frequentes
**[→ FAQ.md](FAQ.md)** - Perguntas e respostas
- "Como faço X?"
- "Por que Y não funciona?"
- Dúvidas de NVDA
- Dúvidas de banco de dados
- Troubleshooting

---

## 📑 Mapa de Documentação

### Para Usuários (Secretaria/Biblioteca)

| Documento | Descrição | Quando usar |
|-----------|-----------|-----------|
| [GUIA_USUARIO.md](GUIA_USUARIO.md) | **Comece aqui** | Primeira vez usando |
| [ATALHOS.md](ATALHOS.md) | Atalhos de teclado | Quer trabalhar mais rápido |
| [ACESSIBILIDADE.md](ACESSIBILIDADE.md) | Guia NVDA | Usa NVDA ou leitor de tela |
| [FAQ.md](FAQ.md) | Perguntas frequentes | Dúvida comum |
| [../README.md](../README.md) | Visão geral | Entender o projeto |

### Para Desenvolvedores

| Documento | Descrição | Quando usar |
|-----------|-----------|-----------|
| [ARQUITETURA.md](ARQUITETURA.md) | Estrutura do código | Entender o design MVC |
| [DATABASE.md](DATABASE.md) | Schema do banco | Trabalhar com dados |
| [API.md](API.md) | Google Books API | Integração com busca |
| [LOGGING.md](LOGGING.md) | Sistema de logs | Debug e monitoramento |
| [CONFIGURACAO.md](CONFIGURACAO.md) | Setup | Primeira instalação |
| [CONTRIBUINDO.md](CONTRIBUINDO.md) | Dev guide | Contribuir ao projeto |
| [../CHANGELOG.md](../CHANGELOG.md) | Histórico de mudanças | Entender evolução |

---

## 🚀 Quick Start (Diferente por Perfil)

### Usuário (Secretária/Biblioteca)
```
1. Abra o programa: python main.py
2. Leia: GUIA_USUARIO.md (Seção "Rotina Diária")
3. Pratique 5 minutos
4. Consulte ATALHOS.md quando precisar ir mais rápido
5. Use FAQ.md para dúvidas
```

### Usuário com NVDA
```
1. Configure NVDA: ACESSIBILIDADE.md (Seção "Setup Inicial")
2. Abra o programa: python main.py
3. Leia: ACESSIBILIDADE.md (Seção "Navegação com NVDA")
4. Escute o anúncio de alertas
5. Pratique os exemplos
```

### Desenvolvedor
```
1. Clone o repositório
2. Leia: CONFIGURACAO.md (setup)
3. Leia: ARQUITETURA.md (entender design)
4. Leia: DATABASE.md (entender dados)
5. Leia: CONTRIBUINDO.md (padrões)
6. Comece a codar!
```

---

## 📊 Estrutura de Documentação

```
[raiz do projeto]/
├── README.md                    ← Visão geral principal
├── CHANGELOG.md                 ← Histórico de versões
├── requirements.txt             ← Dependências
├── main.py                      ← Código principal
│
└── docs/
    ├── README.md               ← Você está aqui!
    ├── GUIA_USUARIO.md         ← Para usuários (COMECE AQUI)
    ├── ATALHOS.md              ← Atalhos de teclado
    ├── ACESSIBILIDADE.md       ← Guia NVDA (WCAG 2.1)
    ├── ARQUITETURA.md          ← Design técnico (MVC)
    ├── DATABASE.md             ← Schema SQLite3
    ├── API.md                  ← Google Books API
    ├── CONFIGURACAO.md         ← Setup do projeto
    ├── LOGGING.md              ← Sistema de logs
    ├── CONTRIBUINDO.md         ← Dev guide
    └── FAQ.md                  ← Perguntas frequentes
```

---

## 🎓 Aprenda Por Caso de Uso

### "Sou novo no programa e nunca usei"
1. Leia [GUIA_USUARIO.md](GUIA_USUARIO.md) - Seção "Rotina Diária"
2. Abra o programa e pratique 5 minutos
3. Consulte [ATALHOS.md](ATALHOS.md) quando quiser ir mais rápido

### "Uso NVDA e tenho dúvidas"
1. Leia [ACESSIBILIDADE.md](ACESSIBILIDADE.md) - Seção "Setup NVDA"
2. Siga o guia de navegação com exemplos
3. Veja troubleshooting se algo não funcionar

### "Tenho uma dúvida específica"
1. Procure em [FAQ.md](FAQ.md)
2. Se não encontrar, procure em outros documentos
3. Se continuar na dúvida, abra uma issue no GitHub

### "Quero entender como funciona"
1. Leia [../README.md](../README.md) (visão geral)
2. Leia [ARQUITETURA.md](ARQUITETURA.md) (design)
3. Leia [DATABASE.md](DATABASE.md) (dados)
4. Explore o código-fonte (`main.py`, `view.py`, `database.py`)

### "Quero contribuir com código"
1. Leia [CONTRIBUINDO.md](CONTRIBUINDO.md)
2. Leia [CONFIGURACAO.md](CONFIGURACAO.md) (setup dev)
3. Leia [ARQUITETURA.md](ARQUITETURA.md) (estrutura)
4. Faça um fork e comece!

### "Algo não funciona / Encontrei um bug"
1. Procure em [FAQ.md](FAQ.md) - Seção "Troubleshooting"
2. Veja [LOGGING.md](LOGGING.md) para analisar logs em `logs/`
3. Se não conseguir resolver, abra uma issue descrevendo:
   - Ação que fez
   - Erro que apareceu
   - Versão do NVDA (se aplicável)
   - Arquivo de log relevante

---

## 💡 Dicas de Navegação

### Buscar em Documentos
- **Com navegador:** Ctrl+F (buscar)
- **Com NVDA:** NVDA+F (procurar)

### Links
Todos os links internos têm `[→ ARQUIVO.md]` para fácil identificação

### Volta ao Índice
Cada documento tem link de volta a este índice

---

## 📞 Mapa de Dúvidas

| Sua Dúvida | Documento |
|----------|-----------|
| "Como uso o programa?" | [GUIA_USUARIO.md](GUIA_USUARIO.md) |
| "Qual é o atalho para X?" | [ATALHOS.md](ATALHOS.md) |
| "NVDA não funciona" | [ACESSIBILIDADE.md](ACESSIBILIDADE.md#troubleshooting) |
| "Como faço X?" | [FAQ.md](FAQ.md) |
| "Algo não funciona / bug" | [FAQ.md](FAQ.md) + [LOGGING.md](LOGGING.md) |
| "Como instalar?" | [CONFIGURACAO.md](CONFIGURACAO.md) |
| "Quero modificar código" | [ARQUITETURA.md](ARQUITETURA.md) |
| "Como contribuir?" | [CONTRIBUINDO.md](CONTRIBUINDO.md) |

---

## ✨ Status da Documentação

**Documentação de Usuário:**
- ✅ [GUIA_USUARIO.md](GUIA_USUARIO.md) - Completo, pronto para uso
- ✅ [ATALHOS.md](ATALHOS.md) - Completo, todos os atalhos
- ✅ [ACESSIBILIDADE.md](ACESSIBILIDADE.md) - Completo, WCAG 2.1, NVDA
- ✅ [FAQ.md](FAQ.md) - Completo

**Documentação Técnica:**
- ✅ [ARQUITETURA.md](ARQUITETURA.md) - Presente
- ✅ [DATABASE.md](DATABASE.md) - Presente
- ✅ [API.md](API.md) - Presente
- ✅ [LOGGING.md](LOGGING.md) - Presente
- ✅ [CONFIGURACAO.md](CONFIGURACAO.md) - Presente
- ✅ [CONTRIBUINDO.md](CONTRIBUINDO.md) - Presente

**Documentação de Projeto:**
- ✅ [../README.md](../README.md) - Principal atualizado
- ✅ [../CHANGELOG.md](../CHANGELOG.md) - Histórico completo

---

## 🎯 Próximos Passos

### Se Você é Usuário
1. **Clique aqui:** [GUIA_USUARIO.md](GUIA_USUARIO.md)
2. Leia a seção "Rotina Diária da Secretaria"
3. Pratique por 5 minutos
4. Use [ATALHOS.md](ATALHOS.md) para ficar mais rápido

### Se Você é Desenvolvedor
1. **Clique aqui:** [ARQUITETURA.md](ARQUITETURA.md)
2. Entenda o padrão MVC
3. Explore [DATABASE.md](DATABASE.md)
4. Siga [CONFIGURACAO.md](CONFIGURACAO.md) para setup
5. Comece a codar!

### Se Você Tem Dúvida
1. **Clique aqui:** [FAQ.md](FAQ.md)
2. Procure sua pergunta
3. Se não encontrar, veja acima qual documento é relevante

---

## 🔗 Documentação Relacionada (Fora desta pasta)

- **[../README.md](../README.md)** - Visão geral e instalação rápida
- **[../CHANGELOG.md](../CHANGELOG.md)** - Histórico de mudanças e versões
- **[../LICENSE](../LICENSE)** - MIT License

---

## 📊 Estatísticas da Documentação

- **Total de documentos:** 11 (incluindo este)
- **Total de páginas (markdown):** ~50+
- **Idioma:** Português Brasileiro
- **Acessibilidade:** WCAG 2.1 Nível A
- **Cobertura:** Usuários e Desenvolvedores

---

**Última atualização:** 2024  
**Desenvolvido com ❤️ para acessibilidade** ♿

**👉 Clique em um link acima para começar!**
6. Clique "Salvar Livro"
👉 Veja: [../README.md](../README.md#-como-usar)

### Registrar Empréstimo
1. Abra a aplicação
2. Vá para aba "Circulação" (Ctrl+1)
3. Busque livro por ISBN/título
4. Selecione leitor
5. Clique "Registrar Empréstimo"
👉 Veja: [../README.md](../README.md#-como-usar)

### Adicionar Nova Feature
1. Crie branch: `git checkout -b feature/nome`
2. Edite código
3. Escreva testes
4. Abra Pull Request
👉 Veja: [CONTRIBUINDO.md](CONTRIBUINDO.md)

### Reportar Bug
1. Vá para Issues no GitHub
2. Clique "New Issue"
3. Escolha "Bug Report"
4. Preencha template
👉 Veja: [CONTRIBUINDO.md](CONTRIBUINDO.md#reportando-bugs)

## 📈 Diagrama de Tópicos

```
                    DataLivros
                        │
        ┌───────────────┼───────────────┐
        │               │               │
     Usuários      Desenvolvedores      TI
        │               │               │
    README.md      ARQUITETURA.md   DATABASE.md
    FAQ.md         API.md           ACESSIBILIDADE.md
    ACESSIBILIDADE DATABASE.md      CONTRIBUINDO.md
                   CONTRIBUINDO.md
```

## 🎓 Aprendizado Progressivo

### Nível 1: Iniciante
- [ ] Ler README.md
- [ ] Instalar e executar
- [ ] Navegar na interface

**Tempo:** 15 minutos

### Nível 2: Usuário
- [ ] Ler FAQ.md
- [ ] Usar todas as abas
- [ ] Cadastrar livro via API
- [ ] Registrar empréstimo

**Tempo:** 1 hora

### Nível 3: Acessibilidade
- [ ] Ler ACESSIBILIDADE.md
- [ ] Usar com NVDA
- [ ] Entender WCAG 2.1
- [ ] Validar conformidade

**Tempo:** 2 horas

### Nível 4: Desenvolvimento
- [ ] Ler ARQUITETURA.md
- [ ] Entender MVC
- [ ] Estudar DATABASE.md
- [ ] Estudar API.md

**Tempo:** 4 horas

### Nível 5: Contribução
- [ ] Ler CONTRIBUINDO.md
- [ ] Fork repositório
- [ ] Criar feature
- [ ] Enviar Pull Request

**Tempo:** 4-8 horas por feature

## 🔍 Buscar na Documentação

### Por Tópico
| Tópico | Arquivo |
|--------|---------|
| Instalação | README.md |
| Atalhos | README.md, ACESSIBILIDADE.md |
| NVDA | ACESSIBILIDADE.md |
| MVC | ARQUITETURA.md |
## 🏠 Arquivos da Documentação

| Arquivo | Descrição |
|---------|-----------|
| **ACESSIBILIDADE.md** | WCAG 2.1, NVDA, navegação |
| **ARQUITETURA.md** | MVC, fluxos, estrutura |
| **DATABASE.md** | Schema, CRUD, relacionamentos |
| **API.md** | Google Books, exemplos |
| **CONTRIBUINDO.md** | Como desenvolver |
| **FAQ.md** | Perguntas e respostas |

## 🔗 Documentação Estendida

Cada arquivo contém:
- **Visão geral** - O que é abordado
- **Exemplos práticos** - Código e casos de uso
- **Referência técnica** - Detalhes completos
- **Troubleshooting** - Soluções de problemas

---

**Pronto?** Comece pelo [README principal](../README.md)

