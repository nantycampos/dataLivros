"""
Módulo de Configuração de Logging
Configura logging profissional para DataLivros com gravação em arquivo
"""

import logging
import logging.handlers
import os
from datetime import datetime

# Criar diretório de logs se não existir
LOGS_DIR = 'logs'
if not os.path.exists(LOGS_DIR):
    os.makedirs(LOGS_DIR)

# Nome do arquivo de log com data
LOG_FILENAME = os.path.join(LOGS_DIR, f'datalibros_{datetime.now().strftime("%Y%m%d")}.log')

# Criar logger
logger = logging.getLogger('DataLivros')
logger.setLevel(logging.DEBUG)

# Formato detalhado com data, hora, nível e mensagem
log_format = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Handler para arquivo (com rotação diária)
file_handler = logging.handlers.RotatingFileHandler(
    LOG_FILENAME,
    maxBytes=5 * 1024 * 1024,  # 5 MB
    backupCount=5,  # Mantém 5 logs antigos
    encoding='utf-8'
)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(log_format)
logger.addHandler(file_handler)

# Handler para console (apenas warnings e errors)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.WARNING)
console_handler.setFormatter(log_format)
logger.addHandler(console_handler)


def log_error_api(status_code: int, error_message: str, details: str = ''):
    """
    Registra erro específico de API com código de status.
    
    Args:
        status_code: Código HTTP da resposta
        error_message: Mensagem de erro legível
        details: Detalhes adicionais do erro
    """
    if status_code == 401:
        logger.error(f'ERRO DE AUTENTICAÇÃO (401): {error_message}. Chave da API inválida ou expirada. {details}')
    elif status_code == 403:
        logger.error(f'ERRO DE COTA (403): {error_message}. Limite diário atingido. {details}')
    elif status_code == 404:
        logger.warning(f'LIVRO NÃO ENCONTRADO (404): {error_message}. {details}')
    elif status_code >= 500:
        logger.error(f'ERRO DO SERVIDOR ({status_code}): {error_message}. {details}')
    else:
        logger.error(f'ERRO HTTP ({status_code}): {error_message}. {details}')


def log_connection_error(error_type: str, error_message: str):
    """
    Registra erro de conexão (timeout, rede, etc).
    
    Args:
        error_type: Tipo de erro (Timeout, Conexão, etc)
        error_message: Mensagem do erro
    """
    logger.error(f'ERRO DE CONEXÃO ({error_type}): {error_message}')


def log_busca_livro(query: str, total_resultados: int):
    """
    Registra uma busca bem-sucedida de livro.
    
    Args:
        query: Termo de busca usado
        total_resultados: Número de resultados encontrados
    """
    logger.info(f'Busca executada: "{query}" - {total_resultados} resultado(s) encontrado(s)')


def log_acesso_banco(operacao: str, status: str = 'sucesso'):
    """
    Registra acesso ao banco de dados.
    
    Args:
        operacao: Tipo de operação (leitura, escrita, atualização)
        status: Status da operação
    """
    logger.info(f'Banco de dados - Operação: {operacao} - Status: {status}')


# Teste de inicialização
if __name__ == '__main__':
    logger.info('Logging inicializado com sucesso')
    logger.debug('Mensagem de debug')
    logger.warning('Mensagem de aviso')
    logger.error('Mensagem de erro')
    print(f'Arquivo de log: {LOG_FILENAME}')
