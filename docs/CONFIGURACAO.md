# 🔐 Configuração e Segurança - DataLivros

Guia completo para configurar a Google Books API de forma segura usando variáveis de ambiente.

---

## 🔑 Configuração da Google Books API

### Por que usar variáveis de ambiente?

A chave da API da Google é uma **credencial sensível**. Nunca deve ser:
- ✗ Commitada no Git
- ✗ Compartilhada publicamente
- ✗ Inserida no código-fonte

A solução: **Usar arquivo `.env` com `python-dotenv`**

---

## 📋 Passo a Passo - Setup Inicial

### 1. Instalar Dependências

```bash
pip install -r requirements.txt
```

Isso instala:
- wxPython (interface)
- requests (HTTP)
- **python-dotenv** (carregamento de .env)

### 2. Criar Arquivo `.env`

```bash
# Windows
copy .env.example .env

# Linux/macOS
cp .env.example .env
```

### 3. Obter Chave da API Google

**Opção A: Sem Chave (Limite 100 requisições/dia)**

Deixe `GOOGLE_API_KEY=` em branco no `.env`. Funciona, mas com limite.

**Opção B: Com Chave (Recomendado - 10.000+ requisições/dia)**

1. Acesse: https://console.cloud.google.com/
2. Crie uma **nova conta** ou use existente
3. Crie um **novo projeto**:
   - Nome: "DataLivros" ou similar
   - Clique "Criar"

4. **Ative a Google Books API**:
   - Menu "APIs e Serviços"
   - "Ativar APIs e serviços"
   - Procure "Google Books"
   - Clique "Ativar"

5. **Crie uma chave de API**:
   - Menu "Credenciais"
   - Clique "+ Criar credenciais"
   - Selecione "Chave de API"
   - Copie a chave exibida

### 4. Adicionar Chave ao `.env`

```bash
# Abra o arquivo .env com um editor de texto
# Adicione (sem aspas):

GOOGLE_API_KEY=AIzaSyDxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

### 5. Testar Configuração

```bash
python -c "from dotenv import load_dotenv; import os; load_dotenv(); print('Chave carregada!' if os.getenv('GOOGLE_API_KEY') else 'Chave não encontrada')"
```

---

## 📂 Estrutura de Arquivos

### Arquivos de Configuração

```
datalivros/
├── .env                  ← PRIVADO (variáveis sensíveis)
├── .env.example          ← PÚBLICO (template)
├── .gitignore            ← Ignora .env automaticamente
└── requirements.txt      ← Todas as dependências
```

### Conteúdo do `.env`

```bash
# Nunca compartilhe este arquivo!
GOOGLE_API_KEY=sua_chave_aqui
```

### Conteúdo do `.env.example`

```bash
# Cópia segura para compartilhar/versionamento
# Mostre como preencher, sem dados reais
GOOGLE_API_KEY=
```

---

## 🔒 Segurança

### ✅ Checklist

- [x] `.env` está no `.gitignore`?
- [x] Nunca facer `git add .env`
- [x] `.env.example` é público (sem dados sensíveis)
- [x] Chave regenerada se vazar por acidente
- [x] Usar variáveis de ambiente em produção

### Arquivo `.gitignore` (Confirmar)

```ignore
# Arquivos de configuração sensíveis
# NUNCA faça commit de .env com credenciais reais!
.env
.env.local
.env.*.local
.env*.local
```

---

## 🚀 Como o Código Funciona

### Em `api_service.py`

```python
from dotenv import load_dotenv
import os

# 1. Carregar .env
load_dotenv()

# 2. Ler variável
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY', '')

# 3. Usar na requisição
params = {
    'q': query,
    'maxResults': 10,
}

if GOOGLE_API_KEY:
    params['key'] = GOOGLE_API_KEY  # Adiciona se disponível

# 4. Requisição (com ou sem chave)
resposta = requests.get(url, params=params)
```

### Comportamento

| Situação | Resultado |
|----------|-----------|
| Chave configurada | ✅ 10.000+ requisições/dia |
| Sem chave (.env vazio) | ⚠️ 100 requisições/dia (limite free) |
| Arquivo .env não existe | ⚠️ 100 requisições/dia (sem erro) |

---

## 🆘 Troubleshooting

### Problema: "ModuleNotFoundError: No module named 'dotenv'"

**Solução:**
```bash
pip install python-dotenv==1.0.0
```

### Problema: "Chave não carregada / Requisição falha"

**Checklist:**
1. Arquivo `.env` existe?
2. Variável está escrita corretamente? `GOOGLE_API_KEY=...`
3. Espaços? Remova: `GOOGLE_API_KEY = AIza...` ❌
4. Aspas? Remova: `GOOGLE_API_KEY="AIza..."` ❌
5. Arquivo `.env` está na raiz do projeto?

**Verificar:**
```bash
# Abra terminal na pasta raiz
python -c "from dotenv import load_dotenv; import os; load_dotenv(); print(f'Chave: {os.getenv(\"GOOGLE_API_KEY\")}')"
```

### Problema: "Muitas requisições / Limite atingido"

**Soluções:**
1. Registre uma chave de API (veja passo 3)
2. Configure limite em Google Cloud Console
3. Implemente cache local (futuro)

---

## 🌍 Variáveis de Ambiente Diferentes

### Desenvolvimento

```bash
# .env (local, NUNCA commitar)
GOOGLE_API_KEY=sua_chave_real_aqui
```

### Produção (Servidor)

```bash
# Em variáveis de ambiente do servidor
# Linux/Cloud: export GOOGLE_API_KEY=...
# Docker: ENV GOOGLE_API_KEY=...
```

O código funciona igual em ambos os casos!

---

## 📚 Leitura Adicional

- [Python-dotenv Documentação](https://github.com/theskumar/python-dotenv)
- [Google Books API](https://developers.google.com/books)
- [Variáveis de Ambiente em Python](https://docs.python.org/3/library/os.html)
- [Boas Práticas de Segurança](https://owasp.org/www-project-top-ten/)

---

## ✨ Resumo

| Item | Status |
|------|--------|
| Chave armazenada com segurança | ✅ |
| Não vaza para Git | ✅ |
| Funciona offline (sem chave) | ✅ |
| Suporta múltiplos ambientes | ✅ |
| Setup simples para novos usuários | ✅ |

---

**DataLivros v1.1.0** com suporte seguro a variáveis de ambiente.

Data: 6 de março de 2026
