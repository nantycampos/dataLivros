# 📦 API - Google Books

Integração com Google Books API para buscar dados de livros.

## 🔧 Função Principal

```python
buscar_livro_google_books(isbn_ou_titulo: str) -> Dict
```

**Retorna:** Dicionário com até 10 resultados de livros.

## 📝 Exemplos

### Busca por ISBN
```python
from api_service import buscar_livro_google_books

resultado = buscar_livro_google_books('9788535929935')
if resultado['sucesso']:
    for livro in resultado['livros']:
        print(f"{livro['titulo']}")
```

### Busca por Título
```python
resultado = buscar_livro_google_books('O Cortiço')
```

## 🌐 Detalhes Técnicos

**Endpoint:** `https://www.googleapis.com/books/v1/volumes`

**Parâmetros:**
- `q` - Query (`isbn:`, `intitle:`, `inauthor:`)
- `maxResults` - 10 (fixado)
- `key` - API Key (opcional, free tier = 1000/dia)

**Timeout:** 10 segundos

## ⚙️ Configuração Avançada

Para usar API Key (se > 1000 requisições/dia):

1. Registre em [Google Cloud Console](https://console.cloud.google.com/)
2. Ativar Books API
3. Gerar API Key
4. Adicionar em `api_service.py`:
```python
API_KEY = 'sua_chave_aqui'
```

## 🚨 Tratamento de Erros

Trata automaticamente:
- Timeouts de rede (10s)
- Erros de conexão
- Respostas inválidas
- Livros não encontrados

Se erro: `resultado['sucesso']` = False

## 💡 Perguntas Comuns

**Funciona sem Internet?** Não, requer conexão. Livros já cadastrados funcionam offline.

**Não encontrou?** Cadastre manualmente (campos editáveis).

**Retorna imagens?** Sim, mas não exibidas (design acessível).

---

Veja [ARQUITETURA.md](ARQUITETURA.md) para integração com controller.

## � Como Usar

### Busca por ISBN
```python
from api_service import buscar_livro_google_books

resultado = buscar_livro_google_books('9788535929935')
if resultado['sucesso']:
    for livro in resultado['livros']:
        print(f"{livro['titulo']} - {', '.join(livro['autores'])}")
```

### Busca por Título
```python
resultado = buscar_livro_google_books('O Cortiço')
```

## � Endpoint

```
GET https://www.googleapis.com/books/v1/volumes
```

**Parâmetros:**
- `q` - Query com prefixo (`isbn:`, `intitle:`, `inauthor:`)
- `maxResults` - 10 (fixed)
- `key` - API Key (optional, free tier works)
| `inpublisher:` | Buscar por editora | `inpublisher:Companhia` |

### Implementação Atual
```python
# Determinar tipo de busca
if isbn_ou_titulo.replace('-', '').isdigit() and len(isbn_ou_titulo.replace('-', '')) >= 10:
    query = f'isbn:{isbn_ou_titulo.replace("-", "")}'
else:
    query = f'intitle:{isbn_ou_titulo}'

# Requisição
url = 'https://www.googleapis.com/books/v1/volumes'
params = {'q': query, 'maxResults': 1}
resposta = requests.get(url, params=params, timeout=10)
```

## 📊 Estrutura da Resposta da API

### JSON Completo (Simplificado)
```json
{
  "kind": "books#volumes",
  "totalItems": 1,
  "items": [
    {
      "kind": "books#volume",
      "id": "xxxxxx",
      "volumeInfo": {
        "title": "O Cortiço",
        "authors": ["Aluísio Azevedo"],
        "publisher": "Companhia das Letras",
        "publishedDate": "1890",
        "description": "...",
        "industryIdentifiers": [
          {
            "type": "ISBN_13",
            "identifier": "9788535929935"
          },
          {
            "type": "ISBN_10",
            "identifier": "8535929931"
          }
        ],
        "categories": ["Fiction", "Literature"],
        "imageLinks": {
          "smallThumbnail": "http://...",
          "thumbnail": "http://..."
        }
      }
    }
  ]
}
```

### Mapeamento para DataLivros
```python
# Extração implementada
livro['title'] → resultado['titulo']
livro['authors'] → resultado['autores']
livro['publisher'] → resultado['editora']
livro['publishedDate'] → resultado['ano_publicacao'] (primeiro 4 chars)
livro['description'] → resultado['descricao']
livro['categories'] → resultado['categorias']
livro['industryIdentifiers'] → resultado['isbn'] (busca ISBN_13 ou ISBN_10)
livro['imageLinks']['thumbnail'] → resultado['thumbnail'] (não usado)
```

## ⚙️ Configuração Avançada

### Usar API Key (Opcional)
Se atingir limite de requisições (free tier = 1000/dia):

1. **Obter chave:**
   - Ir a [Google Cloud Console](https://console.cloud.google.com/)
   - Criar projeto
   - Ativar Books API
   - Criar credencial (API Key)

2. **Usar em código:**
```python
# Adicionar em api_service.py
API_KEY = 'sua_chave_aqui'

params = {
    'q': query,
    'maxResults': 1,
    'key': API_KEY  # Adicionar aqui
}
```

### Variável de Ambiente
```bash
# .env ou variável do sistema
set GOOGLE_BOOKS_API_KEY=sua_chave_aqui
```

```python
import os
API_KEY = os.getenv('GOOGLE_BOOKS_API_KEY', '')
```

## 🚨 Tratamento de Erros

### Erros Implementados

```python
try:
    resposta = requests.get(url, params=params, timeout=10)
except requests.exceptions.Timeout:
    # Conexão demorou muito
    resultado['erro'] = 'Tempo limite da requisição excedido'
except requests.exceptions.ConnectionError:
    # Sem internet
    resultado['erro'] = 'Erro de conexão. Verifique sua internet.'
except requests.exceptions.HTTPError as e:
    # Erro HTTP (4xx, 5xx)
    resultado['erro'] = f'Erro HTTP: {e.response.status_code}'
except ValueError:
    # JSON inválido
    resultado['erro'] = f'Erro ao processar resposta'
except Exception as e:
    # Erro inesperado
    resultado['erro'] = f'Erro inesperado: {str(e)}'
```

### Casos de Erro Comuns

| Erro | Causa | Solução |
|------|-------|---------|
| `Nenhum livro encontrado` | ISBN/título não existe | Usar ISBN correto ou título mais específico |
| `Tempo limite excedido` | Internet lenta | Tentar novamente |
| `Erro de conexão` | Sem internet | Verificar conexão |
| `Erro HTTP 403` | Limite de requisições atingido | Usar API Key |

## 📈 Performance

### Tempo de Resposta
- **Primeira requisição:** ~500ms - 2s (varia com rede)
- **Subsequent requests:** ~200-800ms
- **Timeout:** 10 segundos

### Otimizações Possíveis

```python
# Cache em memória (futuro)
_cache = {}

def buscar_livro_google_books(isbn_ou_titulo: str) -> Dict:
    if isbn_ou_titulo in _cache:
        return _cache[isbn_ou_titulo]
    
    resultado = _fazer_requisicao(isbn_ou_titulo)
    _cache[isbn_ou_titulo] = resultado
    return resultado
```

### Requisições Paralelas (Futuro)
```python
import threading
from concurrent.futures import ThreadPoolExecutor

with ThreadPoolExecutor(max_workers=3) as executor:
    futures = [executor.submit(buscar_livro, isbn) for isbn in isbns]
    resultados = [f.result() for f in futures]
```

## 🧪 Testes

### Teste Manual
```python
from api_service import buscar_livro_google_books

# Teste 1: ISBN válido
r1 = buscar_livro_google_books('9788535929935')
assert r1['sucesso'] == True
assert r1['titulo'] == 'O Cortiço'

# Teste 2: Título válido
r2 = buscar_livro_google_books('1984 George Orwell')
assert r2['sucesso'] == True

# Teste 3: Valor inválido
r3 = buscar_livro_google_books('XXXXX000000')
assert r3['sucesso'] == False
assert 'Nenhum livro encontrado' in r3['erro']

# Teste 4: String vazia
r4 = buscar_livro_google_books('')
assert r4['sucesso'] == False
```

### Teste com Mock (Futuro)
```python
from unittest.mock import patch, MagicMock

@patch('api_service.requests.get')
def test_buscar_livro_mock(mock_get):
    # Mock resposta
    mock_response = MagicMock()
    mock_response.json.return_value = {
        'totalItems': 1,
        'items': [{
            'volumeInfo': {
                'title': 'Test Book',
                'authors': ['Author'],
                # ...
            }
        }]
    }
    mock_get.return_value = mock_response
    
    resultado = buscar_livro_google_books('test')
    assert resultado['sucesso'] == True
```

## 📚 Limitações Conhecidas

| Limitação | Detalhe | Impacto |
|-----------|---------|--------|
| Free tier | 1000 requisições/dia | Alto uso requer API Key |
| Dados incompletos | Alguns livros não têm ISBN | Usar título como alternativa |
| Imagens HTTP | Alcune capas em HTTP não HTTPS | Não afeta (não exibe imagens) |
| Texto truncado | Descrições podem ser cortadas | Usuário pode editar manualmente |
| Sem preço | API não fornece preço | Funcionalidade não implementada |
| Sem disponibilidade | API não informa se tem física | Futuro: integração com biblioteca |

## 🔮 Roadmap

- [ ] Caching de requisições
- [ ] Requisições paralelas
- [ ] Fallback para ISBN + título simultâneos
- [ ] Integração com viaCEP para dados de leitores
- [ ] Suporte a Open Library API como fallback
- [ ] Sincronização com serviços de bibliotecas

## 🌐 Recursos Externos

- [Google Books API Documentation](https://developers.google.com/books)
- [Books API Reference](https://developers.google.com/books/docs/v1/using)
- [ISBN Validation](https://en.wikipedia.org/wiki/International_Standard_Book_Number)
- [Open Library API](https://openlibrary.org/developers) (alternativa)

## 💬 FAQ

**P: Posso usar a API sem Internet?**  
R: Não. A API requer conexão com Google. Livros já cadastrados no banco local funcionam offline.

**P: Como aumentar o limite de requisições?**  
R: Registre uma chave de API no Google Cloud Console.

**P: E se a API não encontrar o livro?**  
R: O usuário pode cadastrar manualmente preenchendo os campos.

**P: A API retorna capa do livro?**  
R: Sim (thumbnail), mas não é exibida na interface por design de acessibilidade.

**P: Posso usar outras fontes de dados?**  
R: Sim! Veja `docs/CONTRIBUINDO.md` para adicionar novos serviços.

---

**DataLivros aproveita a Google Books API para riqueza de dados sem bloat local.**

