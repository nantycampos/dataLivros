"""
Módulo de integração com Google Books API
Permite buscar informações de livros por ISBN ou Título
Inclui tratamento robusto de erros e logging profissional
"""

import os
import requests
from typing import Dict, List, Optional
from dotenv import load_dotenv
from logger_config import logger, log_error_api, log_connection_error, log_busca_livro

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Carregar chave da API do Google Books a partir do arquivo .env
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY', '')

# Mensagens de erro amigáveis em português
MENSAGENS_ERRO = {
    401: 'Erro de Autenticação: Chave da API inválida ou expirada. Verifique o arquivo .env.',
    403: 'Limite de Cota Atingido: Você atingiu o limite diário de requisições. Tente novamente amanhã.',
    404: 'Livro não encontrado. Tente buscar com outro título ou ISBN.',
    500: 'Erro no servidor do Google Books. Tente novamente em alguns minutos.',
    503: 'Serviço indisponível. O Google Books está em manutenção. Tente novamente mais tarde.',
    'timeout': 'Tempo limite excedido. Verifique sua conexão de internet.',
    'conexao': 'Erro de conexão. Verifique se está conectado à internet.',
    'desconhecido': 'Erro desconhecido ao buscar livro. Tente novamente.'
}


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
    Busca informações de livros na Google Books API com tratamento robusto.
    
    Args:
        isbn_ou_titulo: ISBN ou título do livro a buscar
        
    Returns:
        Dicionário contendo:
        - 'sucesso': bool indicando se a busca foi bem-sucedida
        - 'livros': list de dicionários com dados dos livros encontrados
        - 'total': int número de livros encontrados
        - 'erro': str mensagem de erro amigável (se sucesso for False)
    """
    
    resultado = {
        'sucesso': False,
        'livros': [],
        'total': 0,
        'erro': ''
    }
    
    try:
        # ========== VALIDAÇÃO DE ENTRADA ==========
        if not isbn_ou_titulo or not isbn_ou_titulo.strip():
            resultado['erro'] = 'Por favor, digite um ISBN ou título válido.'
            logger.warning('Busca com entrada vazia')
            return resultado
        
        # ========== DETERMINAÇÃO DO TIPO DE BUSCA ==========
        if isbn_ou_titulo.replace('-', '').isdigit() and len(isbn_ou_titulo.replace('-', '')) >= 10:
            # É um ISBN
            query = f'isbn:{isbn_ou_titulo.replace("-", "")}'
            logger.debug(f'Busca por ISBN: {query}')
        else:
            # É um título
            query = f'intitle:{isbn_ou_titulo}'
            logger.debug(f'Busca por Título: {query}')
        
        # ========== PREPARAÇÃO DE REQUISIÇÃO ==========
        url = 'https://www.googleapis.com/books/v1/volumes'
        params = {
            'q': query,
            'maxResults': 10,  # Buscar até 10 resultados
        }
        
        # Adicionar chave de API se estiver configurada
        if GOOGLE_API_KEY:
            params['key'] = GOOGLE_API_KEY
            logger.debug('Usando chave da API Google Books')
        else:
            logger.warning('Chave da API não configurada. Limite: 100 requisições/dia')
        
        # ========== REQUISIÇÃO COM TIMEOUT ==========
        try:
            resposta = requests.get(url, params=params, timeout=10)
        except requests.exceptions.Timeout:
            # Erro: Tempo limite excedido
            msg_erro = MENSAGENS_ERRO['timeout']
            resultado['erro'] = msg_erro
            log_connection_error('Timeout', 'Requisição excedeu 10 segundos')
            logger.error(f'Timeout na busca: {isbn_ou_titulo}')
            return resultado
        except requests.exceptions.ConnectionError:
            # Erro: Problema de conexão
            msg_erro = MENSAGENS_ERRO['conexao']
            resultado['erro'] = msg_erro
            log_connection_error('Conexão', 'Impossível conectar ao servidor')
            logger.error(f'Erro de conexão ao buscar: {isbn_ou_titulo}')
            return resultado
        
        # ========== VERIFICAÇÃO DE STATUS HTTP ==========
        if resposta.status_code == 401:
            # Erro: Chave inválida ou expirada
            msg_erro = MENSAGENS_ERRO[401]
            resultado['erro'] = msg_erro
            log_error_api(401, 'Chave da API inválida', f'Query: {query}')
            logger.error(f'AUTENTICAÇÃO FALHOU: Chave inválida na busca {query}')
            return resultado
        
        elif resposta.status_code == 403:
            # Erro: Limite de cota atingido
            msg_erro = MENSAGENS_ERRO[403]
            resultado['erro'] = msg_erro
            log_error_api(403, 'Limite de cota atingido', f'Query: {query}')
            logger.error(f'COTA ATINGIDA: Limite diário na busca {query}')
            return resultado
        
        elif resposta.status_code == 404:
            # Aviso: Livro não encontrado (esperado)
            msg_erro = MENSAGENS_ERRO[404]
            resultado['erro'] = msg_erro
            log_error_api(404, 'Livro não encontrado', f'Query: {query}')
            logger.info(f'Livro não encontrado: {query}')
            return resultado
        
        elif resposta.status_code >= 500:
            # Erro: Problema no servidor
            msg_erro = MENSAGENS_ERRO.get(resposta.status_code, MENSAGENS_ERRO[500])
            resultado['erro'] = msg_erro
            log_error_api(resposta.status_code, f'Erro do servidor', f'Query: {query}')
            logger.error(f'Erro do servidor ({resposta.status_code}) na busca {query}')
            return resultado
        
        elif resposta.status_code != 200:
            # Erro genérico HTTP
            msg_erro = f'Erro HTTP {resposta.status_code}. Tente novamente.'
            resultado['erro'] = msg_erro
            log_error_api(resposta.status_code, f'Erro HTTP genérico', f'Query: {query}')
            logger.error(f'Erro HTTP {resposta.status_code} na busca {query}')
            return resultado
        
        # ========== PROCESSAMENTO DE RESPOSTA ==========
        try:
            dados = resposta.json()
        except ValueError as e:
            msg_erro = MENSAGENS_ERRO['desconhecido']
            resultado['erro'] = msg_erro
            logger.error(f'Erro ao processar JSON: {str(e)}')
            return resultado
        
        # Verificar se encontrou algum resultado
        total_items = dados.get('totalItems', 0)
        if total_items == 0:
            msg_erro = 'Nenhum livro encontrado com esses dados.'
            resultado['erro'] = msg_erro
            log_busca_livro(query, 0)
            logger.info(f'Busca sem resultados: {query}')
            return resultado
        
        # ========== EXTRAÇÃO DE RESULTADOS ==========
        resultado['total'] = total_items
        
        for item in dados.get('items', []):
            try:
                livro_info = item.get('volumeInfo', {})
                livro = _extrair_dados_livro(livro_info)
                resultado['livros'].append(livro)
            except Exception as e:
                logger.warning(f'Erro ao extrair dados de um livro: {str(e)}')
                continue  # Continua com o próximo livro
        
        # ========== SUCESSO ==========
        resultado['sucesso'] = True
        log_busca_livro(query, len(resultado['livros']))
        logger.info(f'Busca bem-sucedida: "{query}" - {len(resultado["livros"])} livro(s)')
        
    except Exception as e:
        # Erro não previsto
        msg_erro = MENSAGENS_ERRO['desconhecido']
        resultado['erro'] = msg_erro
        logger.error(f'Erro desconhecido durante busca: {type(e).__name__} - {str(e)}', exc_info=True)
    
    return resultado
