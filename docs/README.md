# 📚 Documentação - DataLivros

Bem-vindo à documentação técnica! Para começar rápido, veja o [README principal](../README.md).

## 🎯 Tópicos Principais

### 👤 Usuários
- **[ACESSIBILIDADE.md](ACESSIBILIDADE.md)** - Guia NVDA, WCAG 2.1, navegação por teclado
- **[FAQ.md](FAQ.md)** - Respostas às dúvidas mais comuns

### 👨‍💻 Desenvolvedores
- **[ARQUITETURA.md](ARQUITETURA.md)** - Padrão MVC, fluxo de dados, estrutura do código
- **[DATABASE.md](DATABASE.md)** - Schema SQLite3, CRUD, relacionamentos
- **[API.md](API.md)** - Integração Google Books, exemplos de uso
- **[CONTRIBUINDO.md](CONTRIBUINDO.md)** - Como contribuir, padrões de código

## � Começando

**Instalação:**
```bash
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r ../requirements.txt
python ../main.py
```

**Primeiros passos:**
1. Navegue com `Tab` entre campos
2. Use `Ctrl+1`, `Ctrl+2`, `Ctrl+3` para trocar abas
3. Cadastre livros via API (Aba 2)
4. Registre empréstimos (Aba 1)

## 📖 Documentação Completapython main.py
```
👉 Veja: [../README.md](../README.md#-instalação)

### Criar Novo Leitor
1. Abra a aplicação
2. Vá para aba "Leitores" (Ctrl+3)
3. Preencha dados
4. Clique "Salvar Leitor"
👉 Veja: [../README.md](../README.md#-como-usar)

### Cadastrar Novo Livro
1. Abra a aplicação
2. Vá para aba "Cadastro de Livros" (Ctrl+2)
3. Digite ISBN ou título
4. Clique "Buscar na API"
5. Revise dados
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

