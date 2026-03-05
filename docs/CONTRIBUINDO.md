# 🤝 Guia de Contribuição - DataLivros

Obrigado por considerar contribuir para o DataLivros! Este documento fornece orientações para contribuições.

## 📋 Índice

1. [Código de Conduta](#código-de-conduta)
2. [Como Começar](#como-começar)
3. [Desenvolvimento](#desenvolvimento)
4. [Commits](#commits)
5. [Pull Requests](#pull-requests)
6. [Padrões de Código](#padrões-de-código)
7. [Testes](#testes)
8. [Documentação](#documentação)
9. [Reportando Bugs](#reportando-bugs)
10. [Sugerindo Melhorias](#sugerindo-melhorias)

## 🚀 Código de Conduta

### Nossa Promessa
Nos comprometemos em criar um ambiente acolhedor para todos.

### Comportamentos Esperados
- Ser respeitoso com diferentes opiniões
- Aceitar crítica construtiva
- Focar no que é melhor para a comunidade

### Comportamentos Inaceitáveis
- Assédio de qualquer tipo
- Discriminação
- Spam ou auto-promoção

## 💡 Como Começar

### 1. Fork o Repositório
```bash
# No GitHub, clique "Fork"
git clone https://github.com/seu-usuario/datalivros.git
cd datalivros
```

### 2. Crie uma Branch
```bash
# Branch com nome descritivo
git checkout -b feature/adicionar-relatorios
# ou
git checkout -b fix/corrigir-acessibilidade
```

### 3. Instale Dependências
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
pip install -r requirements-dev.txt  # Para desenvolvimento
```

## 🔧 Desenvolvimento

### Estrutura de Pastas

```
datalivros/
├── main.py              # Controlador principal
├── view.py              # Interface (MVC)
├── database.py          # Modelo (MVC)
├── api_service.py       # Integração com APIs
├── tests/               # Testes unitários
├── docs/                # Documentação
└── requirements.txt     # Dependências
```

### Ambiente de Desenvolvimento

```bash
# Instalar ferramentas de desenvolvimento
pip install -r requirements-dev.txt

# Requirements-dev.txt deve conter:
# pytest==7.x
# pytest-cov==4.x
# black==23.x
# flake8==6.x
# mypy==1.x
```

### Executar Código Localmente

```bash
# Ativar ambiente
venv\Scripts\activate

# Executar aplicação
python main.py

# Testar módulo específico
python -m pytest tests/test_database.py -v
```

## 📝 Commits

### Mensagem de Commit

Siga o padrão [Conventional Commits](https://www.conventionalcommits.org/):

```
<tipo>[escopo opcional]: <descrição>

[corpo opcional]

[rodapé opcional]
```

### Tipos

| Tipo | Descrição |
|------|-----------|
| `feat` | Nova funcionalidade |
| `fix` | Correção de bug |
| `docs` | Alterações em documentação |
| `style` | Formatação, não altera lógica |
| `refactor` | Refatoração sem mudança de comportamento |
| `perf` | Melhoria de performance |
| `test` | Adição de testes |
| `chore` | Manutenção, dependências |

### Exemplos

```bash
# Feature nova
git commit -m "feat(circulacao): adicionar renovação de empréstimo"

# Bug fix
git commit -m "fix(api): tratar erro 403 de limite de requisições"

# Documentação
git commit -m "docs: atualizar README com exemplos"

# Múltiplas linhas
git commit -m "feat(database): adicionar índices para otimização

- Criar índice em coluna 'titulo'
- Criar índice em coluna 'data_emprestimo'
- Melhorar performance de buscas em 40%"
```

## 🔄 Pull Requests

### Antes de Enviar

1. **Atualize branch com main:**
```bash
git fetch origin
git rebase origin/main
```

2. **Execute testes locais:**
```bash
pytest tests/ --cov=.
```

3. **Verifique formatação:**
```bash
black . --check
flake8 .
mypy .
```

### Submeter PR

1. **Push para sua fork:**
```bash
git push origin feature/adicionar-relatorios
```

2. **Abra PR no GitHub:**
   - Compare: `sua-fork/feature-branch` → `main`
   - Título descritivo: `[Feature] Adicionar relatórios`
   - Descrição: veja template abaixo

### Template de PR

```markdown
## Descrição
Breve descrição do que esta PR faz.

## Tipo de Mudança
- [ ] Bug fix
- [ ] Nova funcionalidade
- [ ] Breaking change
- [ ] Atualização de documentação

## Relacionado a Issue
Fecha #123

## Como testar
Passos para validar:
1. Navegue para...
2. Clique em...
3. Verifique que...

## Checklist
- [ ] Meu código segue o estilo do projeto
- [ ] Atualizei a documentação
- [ ] Adicionei testes que falham sem mudanças
- [ ] Todos os testes passam
- [ ] Código é acessível (WCAG 2.1)
- [ ] Sem console.log ou debug statements
```

### Revisão

- Seus PR serão revisados em até 7 dias
- Forneça feedback construtivo em revisões
- Seja paciente e respeitoso

## 🎨 Padrões de Código

### Python

#### PEP 8
```python
# ✅ Bom
def adicionar_livro(titulo: str, isbn: Optional[str] = None) -> int:
    """Adiciona um livro ao banco."""
    livro_id = self.db.adicionar_livro(titulo, isbn)
    return livro_id

# ❌ Ruim
def AddLivro(titulo,isbn=None):
    livro_id=self.db.AddLivro(titulo,isbn)
    return livro_id
```

#### Type Hints
```python
# ✅ Bom
def buscar_livro(id: int) -> Optional[Dict[str, Any]]:
    pass

# ❌ Ruim
def buscar_livro(id):
    pass
```

#### Docstrings
```python
# ✅ Bom
def registrar_emprestimo(livro_id: int, leitor_id: int) -> int:
    """
    Registra um novo empréstimo.
    
    Args:
        livro_id: ID do livro
        leitor_id: ID do leitor
        
    Returns:
        ID do empréstimo registrado
        
    Raises:
        ValueError: Se IDs inválidos
    """
    pass

# ❌ Ruim
def registrar_emprestimo(livro_id, leitor_id):
    # Registra empréstimo
    pass
```

#### Formatação
```bash
# Usar Black para formatação automática
black .

# Usar Flake8 para linting
flake8 . --max-line-length=100

# Usar MyPy para type checking
mypy .
```

### Acessibilidade

**Obrigatório:** Toda mudança na UI deve manter/melhorar acessibilidade.

#### Regras WCAG 2.1
```python
# ✅ Bom - Campo com rótulo
self.label = wx.StaticText(self, label="Nome:")
self.texto = wx.TextCtrl(self)
self.texto.SetHelpText("Digite seu nome completo")

# ❌ Ruim - Campo sem rótulo
self.texto = wx.TextCtrl(self)
```

#### Feedback Auditivo
```python
# ✅ Bom
self.frame.atualizar_status("Livro salvo com sucesso!")

# ❌ Ruim
print("Livro salvo")  # NVDA não lê
```

### Nomes de Variáveis

```python
# ✅ Bom
data_emprestimo = datetime.now()
lista_livros = db.listar_todos_livros()
emprestimo_ativo = True

# ❌ Ruim
de = datetime.now()
ll = db.listar_todos_livros()
ea = True
```

## 🧪 Testes

### Estrutura

```
tests/
├── __init__.py
├── test_database.py
├── test_api_service.py
└── test_main.py
```

### Criar Teste

```python
# tests/test_database.py
import pytest
from database import DatabaseGerenciador

class TestDatabaseGerenciador:
    """Testes para DatabaseGerenciador."""
    
    @pytest.fixture
    def db(self):
        """Criar banco em memória para testes."""
        return DatabaseGerenciador(':memory:')
    
    def test_adicionar_livro(self, db):
        """Teste adicionar livro."""
        livro_id = db.adicionar_livro('Test Book')
        assert livro_id > 0
    
    def test_adicionar_livro_sem_titulo(self, db):
        """Teste validação de título."""
        with pytest.raises(Exception):
            db.adicionar_livro('')
    
    def test_buscar_livro_inexistente(self, db):
        """Teste buscar livro não cadastrado."""
        resultado = db.buscar_livro_por_id(999)
        assert resultado is None
```

### Executar Testes

```bash
# Todos os testes
pytest

# Testes específicos
pytest tests/test_database.py -v

# Com cobertura
pytest --cov=. --cov-report=html

# Watch mode (reexecuta ao salvar)
pytest-watch
```

### Cobertura Mínima

- **Obrigatório:** 70% de cobertura
- **Alvo:** 90% de cobertura

## 📚 Documentação

### Atualizar Documentação

```bash
# Ao adicionar feature
1. Atualizar docs/ correspondente
2. Atualizar README.md
3. Adicionar exemplos de uso
```

### Padrão de Documentação

```markdown
# Título da Seção

Descrição clara.

## Subseção

Mais detalhes.

### Exemplo

```python
# Código de exemplo
```

## Referências

- [Link relevante](url)
```

### Verificar Links

```bash
# Ferramentas úteis
# markdownlint - https://github.com/igorshubovych/markdownlint-cli
markdownlint docs/
```

## 🐛 Reportando Bugs

### Template

```markdown
## Descrição do Bug
Descrição clara do problema.

## Para Reproduzir
1. Navegue para...
2. Clique em...
3. Observe erro...

## Comportamento Esperado
O que deveria acontecer.

## Comportamento Atual
O que realmente acontece.

## Ambiente
- Windows 10/11
- Python 3.10
- NVDA 2023.1

## Logs/Screenshots
[Colar aqui se possível]

## Passos Adicionais
Informações extras se houver.
```

## 💡 Sugerindo Melhorias

### Template

```markdown
## Descrição da Melhoria
Descrição clara da sugestão.

## Motivação
Por que isso é útil?

## Exemplos
Como seria usado.

## Alternativas Consideradas
Outras soluções possíveis.

## Contexto Adicional
Qualquer informação relevante.
```

## 📊 Processo de Review

```
[Você cria PR] 
    ↓
[Reviewers análisam] (até 7 dias)
    ↓
[Solicita mudanças?] → Você atualiza → Novo review
    ↓ (Aprova)
[Merge para main]
    ↓
[Deploy para produção]
```

## 🎯 Áreas Procurando Contribuições

- [ ] **Testes:** Aumentar cobertura de testes
- [ ] **Performance:** Otimizar queries SQL
- [ ] **UI/UX:** Melhorar acessibilidade
- [ ] **Documentação:** Adicionar guias
- [ ] **Traducao:** Internacionalizar
- [ ] **Recursos:** Adicionar novos relatórios

## 📞 Contato

- **Issues:** Para bugs e features
- **Discussions:** Para perguntas
- **GitHub:** github.com/nantycampos/dataLivros

## ✅ Checklist Final

Antes de enviar PR:

- [ ] Código segue PEP 8
- [ ] Testes adicionados/atualizados
- [ ] Cobertura mantida/aumentada
- [ ] Documentação atualizada
- [ ] Sem breaking changes (ou documentado)
- [ ] Acessibilidade mantida
- [ ] Commit messages descritivas
- [ ] Branch atualizada com main

## 🙏 Agradecimentos

Obrigado por contribuir para tornar DataLivros melhor!

---

**Feliz contribuindo! Se tiver dúvidas, abra uma issue ou discussion.**

