"""
Módulo de integração com Google Books API
Permite buscar informações de livros por ISBN ou Título
"""

import requests
from typing import Dict, List, Optional


def _extrair_dados_livro(livro_info: Dict) -> Dict:
    """
    Extrai dados estruturados de um item da API.
    
    Args:
        livro_info: Dicionário volumeInfo da API
        
    Returns:
        Dicionário com dados estruturados do livro
    """
    livro = {
        'titulo': livro_info.get('title', 'Sem título'),
        'autores': livro_info.get('authors', []),
        'editora': livro_info.get('publisher', 'Editora desconhecida'),
        'descricao': livro_info.get('description', 'Sem descrição disponível'),
        'categorias': livro_info.get('categories', []),
        'ano_publicacao': livro_info.get('publishedDate', '')[:4] if livro_info.get('publishedDate') else 0,
        'isbn': '',
        'thumbnail': ''
    }
    
    # Extrair ISBN
    identifiers = livro_info.get('industryIdentifiers', [])
    for identifier in identifiers:
        if identifier['type'] in ['ISBN_13', 'ISBN_10']:
            livro['isbn'] = identifier['identifier']
            break
    
    # URL da capa
    imagem = livro_info.get('imageLinks', {})
    livro['thumbnail'] = imagem.get('thumbnail', '')
    
    return livro


def buscar_livro_google_books(isbn_ou_titulo: str) -> Dict:
    """
    Busca informações de livros na Google Books API.
    
    Args:
        isbn_ou_titulo: ISBN ou título do livro a buscar
        
    Returns:
        Dicionário contendo:
        - 'sucesso': bool indicando se a busca foi bem-sucedida
        - 'livros': list de dicionários com dados dos livros encontrados
          Cada livro contém: titulo, autores, isbn, editora, ano_publicacao, 
          descricao, categorias, thumbnail
        - 'total': int número de livros encontrados
        - 'erro': str mensagem de erro (se sucesso for False)
    """
    
    resultado = {
        'sucesso': False,
        'livros': [],
        'total': 0,
        'erro': ''
    }
    
    try:
        # Determinar tipo de busca
        if isbn_ou_titulo.replace('-', '').isdigit() and len(isbn_ou_titulo.replace('-', '')) >= 10:
            # É um ISBN
            query = f'isbn:{isbn_ou_titulo.replace("-", "")}'
        else:
            # É um título
            query = f'intitle:{isbn_ou_titulo}'
        
        # Fazer requisição para Google Books API
        url = 'https://www.googleapis.com/books/v1/volumes'
        params = {
            'q': query,
            'maxResults': 10  # Buscar até 10 resultados
        }
        
        resposta = requests.get(url, params=params, timeout=10)
        resposta.raise_for_status()
        
        dados = resposta.json()
        
        # Verificar se encontrou algum resultado
        if dados.get('totalItems', 0) == 0:
            resultado['erro'] = 'Nenhum livro encontrado com esses dados.'
            return resultado
        
        # Extrair informações de todos os resultados
        resultado['total'] = dados.get('totalItems', 0)
        
        for item in dados.get('items', []):
            livro_info = item.get('volumeInfo', {})
            livro = _extrair_dados_livro(livro_info)
            resultado['livros'].append(livro)
        
        resultado['sucesso'] = True
        
    except requests.exceptions.Timeout:
        resultado['erro'] = 'Tempo limite da requisição excedido. Verifique sua conexão.'
    except requests.exceptions.ConnectionError:
        resultado['erro'] = 'Erro de conexão. Verifique sua internet.'
    except requests.exceptions.HTTPError as e:
        resultado['erro'] = f'Erro HTTP: {e.response.status_code}'
    except requests.exceptions.RequestException as e:
        resultado['erro'] = f'Erro na requisição: {str(e)}'
    except ValueError as e:
        resultado['erro'] = f'Erro ao processar resposta: {str(e)}'
    except Exception as e:
        resultado['erro'] = f'Erro inesperado: {str(e)}'
    
    return resultado
