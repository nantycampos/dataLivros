"""
Módulo de gerenciamento do banco de dados SQLite3
Cria e gerencia as tabelas: livros, leitores, emprestimos
"""

import sqlite3
from pathlib import Path
from datetime import datetime
from typing import List, Tuple, Optional


class DatabaseGerenciador:
    """Gerenciador de banco de dados para o sistema de sala de leitura."""
    
    def __init__(self, caminho_db: str = 'datalibros.db'):
        """
        Inicializa o gerenciador de banco de dados.
        
        Args:
            caminho_db: Caminho para o arquivo SQLite3
        """
        self.caminho_db = caminho_db
        self.conexao = None
        self.cursor = None
        self._conectar()
        self._criar_tabelas()
    
    def _conectar(self) -> None:
        """Estabelece conexão com o banco de dados."""
        try:
            self.conexao = sqlite3.connect(self.caminho_db)
            self.conexao.row_factory = sqlite3.Row
            self.cursor = self.conexao.cursor()
        except sqlite3.Error as e:
            raise
    
    def _criar_tabelas(self) -> None:
        """Cria as tabelas do banco de dados se não existirem."""
        try:
            # Tabela de Livros
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS livros (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    titulo TEXT NOT NULL,
                    autores TEXT,
                    isbn TEXT UNIQUE,
                    editora TEXT,
                    ano_publicacao INTEGER,
                    descricao TEXT,
                    categorias TEXT,
                    thumbnail TEXT,
                    quantidade_total INTEGER DEFAULT 1,
                    status TEXT DEFAULT 'Disponível',
                    data_adicao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            # Tabela de Leitores
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS leitores (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    turma TEXT,
                    data_inscricao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    ativo BOOLEAN DEFAULT 1
                )
            ''')
            
            # Tabela de Empréstimos
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS emprestimos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    livro_id INTEGER NOT NULL,
                    leitor_id INTEGER NOT NULL,
                    data_emprestimo TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    data_devolucao_prevista TIMESTAMP,
                    data_devolucao_real TIMESTAMP,
                    renovacoes INTEGER DEFAULT 0,
                    status TEXT DEFAULT 'ativo',
                    observacoes TEXT,
                    FOREIGN KEY (livro_id) REFERENCES livros(id) ON DELETE CASCADE,
                    FOREIGN KEY (leitor_id) REFERENCES leitores(id) ON DELETE CASCADE
                )
            ''')
            
            self.conexao.commit()
        except sqlite3.Error as e:
            raise
    
    # ========== OPERAÇÕES COM LIVROS ==========
    
    def adicionar_livro(self, titulo: str, isbn: Optional[str] = None, 
                       autores: Optional[str] = None, editora: Optional[str] = None,
                       ano_publicacao: Optional[int] = None, descricao: Optional[str] = None,
                       categorias: Optional[str] = None, thumbnail: Optional[str] = None,
                       quantidade_total: int = 1) -> int:
        """
        Adiciona um novo livro ao banco de dados.
        
        Args:
            titulo: Título do livro (obrigatório)
            isbn: ISBN do livro
            autores: Autores separados por vírgula
            editora: Nome da editora
            ano_publicacao: Ano de publicação
            descricao: Descrição do livro
            categorias: Categorias separadas por vírgula
            thumbnail: URL da capa
            quantidade_total: Quantidade total de exemplares (padrão 1)
            
            Returns:
                ID do livro inserido
        """
        try:
            self.cursor.execute('''
                INSERT INTO livros 
                (titulo, isbn, autores, editora, ano_publicacao, descricao, categorias, thumbnail, quantidade_total)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (titulo, isbn, autores, editora, ano_publicacao, descricao, categorias, thumbnail, quantidade_total))
            
            self.conexao.commit()
            livro_id = self.cursor.lastrowid
            return livro_id
        except sqlite3.IntegrityError:
            raise
        except sqlite3.Error as e:
            raise
    
    def buscar_livro_por_id(self, livro_id: int) -> Optional[dict]:
        """
        Busca um livro pelo ID.
        
        Args:
            livro_id: ID do livro
            
        Returns:
            Dicionário com dados do livro ou None
        """
        try:
            self.cursor.execute('SELECT * FROM livros WHERE id = ?', (livro_id,))
            resultado = self.cursor.fetchone()
            return dict(resultado) if resultado else None
        except sqlite3.Error:
            return None
    
    def buscar_livro_por_isbn(self, isbn: str) -> Optional[dict]:
        """
        Busca um livro pelo ISBN.
        
        Args:
            isbn: ISBN do livro
            
        Returns:
            Dicionário com dados do livro ou None
        """
        try:
            self.cursor.execute('SELECT * FROM livros WHERE isbn = ?', (isbn,))
            resultado = self.cursor.fetchone()
            return dict(resultado) if resultado else None
        except sqlite3.Error:
            return None
    
    def buscar_livros_por_titulo(self, titulo: str) -> List[dict]:
        """
        Busca livros por título (busca parcial).
        
        Args:
            titulo: Título ou parte do título
            
        Returns:
            Lista de dicionários com dados dos livros
        """
        try:
            self.cursor.execute(
                'SELECT * FROM livros WHERE titulo LIKE ? ORDER BY titulo',
                (f'%{titulo}%',)
            )
            resultados = self.cursor.fetchall()
            return [dict(row) for row in resultados]
        except sqlite3.Error:
            return []
    
    def listar_todos_livros(self) -> List[dict]:
        """
        Lista todos os livros.
        
        Returns:
            Lista de dicionários com dados de todos os livros
        """
        try:
            self.cursor.execute('SELECT * FROM livros ORDER BY titulo')
            resultados = self.cursor.fetchall()
            return [dict(row) for row in resultados]
        except sqlite3.Error:
            return []
    
    def atualizar_livro(self, livro_id: int, **kwargs) -> bool:
        """
        Atualiza dados de um livro.
        
        Args:
            livro_id: ID do livro
            **kwargs: Campos a atualizar (titulo, autores, status, quantidade_total, etc)
            
        Returns:
            True se atualizado com sucesso
        """
        try:
            campos_validos = {'titulo', 'isbn', 'autores', 'editora', 'ano_publicacao', 
                             'descricao', 'categorias', 'thumbnail', 'status', 'quantidade_total'}
            campos_atualizacao = {k: v for k, v in kwargs.items() if k in campos_validos}
            
            if not campos_atualizacao:
                return False
            
            campos_atualizacao['data_atualizacao'] = datetime.now()
            
            set_clause = ', '.join([f'{k} = ?' for k in campos_atualizacao.keys()])
            valores = list(campos_atualizacao.values()) + [livro_id]
            
            self.cursor.execute(f'UPDATE livros SET {set_clause} WHERE id = ?', valores)
            self.conexao.commit()
            return self.cursor.rowcount > 0
        except sqlite3.Error:
            return False
    
    def deletar_livro(self, livro_id: int) -> bool:
        """
        Deleta um livro.
        
        Args:
            livro_id: ID do livro
            
        Returns:
            True se deletado com sucesso
        """
        try:
            self.cursor.execute('DELETE FROM livros WHERE id = ?', (livro_id,))
            self.conexao.commit()
            return self.cursor.rowcount > 0
        except sqlite3.Error:
            return False
    
    # ========== OPERAÇÕES COM LEITORES ==========
    
    def adicionar_leitor(self, nome: str, turma: Optional[str] = None) -> int:
        """
        Adiciona um novo leitor.
        
        Args:
            nome: Nome do leitor (obrigatório)
            turma: Turma do leitor
            
        Returns:
            ID do leitor inserido
        """
        try:
            self.cursor.execute('''
                INSERT INTO leitores (nome, turma)
                VALUES (?, ?)
            ''', (nome, turma))
            
            self.conexao.commit()
            leitor_id = self.cursor.lastrowid
            return leitor_id
        except sqlite3.IntegrityError:
            raise
        except sqlite3.Error:
            raise
    
    def buscar_leitor_por_id(self, leitor_id: int) -> Optional[dict]:
        """
        Busca um leitor pelo ID.
        
        Args:
            leitor_id: ID do leitor
            
        Returns:
            Dicionário com dados do leitor ou None
        """
        try:
            self.cursor.execute('SELECT * FROM leitores WHERE id = ?', (leitor_id,))
            resultado = self.cursor.fetchone()
            return dict(resultado) if resultado else None
        except sqlite3.Error:
            return None
    
    def buscar_leitores_por_nome_ou_turma(self, termo: str) -> List[dict]:
        """
        Busca leitores por nome OU turma (busca parcial em ambos os campos).
        
        Args:
            termo: Nome ou parte do nome, ou turma ou parte da turma
            
        Returns:
            Lista de dicionários com dados dos leitores ordenados por nome
        """
        try:
            self.cursor.execute(
                'SELECT * FROM leitores WHERE (nome LIKE ? OR turma LIKE ?) AND ativo = 1 ORDER BY nome',
                (f'%{termo}%', f'%{termo}%')
            )
            resultados = self.cursor.fetchall()
            return [dict(row) for row in resultados]
        except sqlite3.Error:
            return []
    
    def listar_todos_leitores(self, apenas_ativos: bool = True) -> List[dict]:
        """
        Lista todos os leitores.
        
        Args:
            apenas_ativos: Se True, lista apenas leitores ativos
            
        Returns:
            Lista de dicionários com dados dos leitores
        """
        try:
            if apenas_ativos:
                self.cursor.execute('SELECT * FROM leitores WHERE ativo = 1 ORDER BY nome')
            else:
                self.cursor.execute('SELECT * FROM leitores ORDER BY nome')
            
            resultados = self.cursor.fetchall()
            return [dict(row) for row in resultados]
        except sqlite3.Error:
            return []
    
    def atualizar_leitor(self, leitor_id: int, **kwargs) -> bool:
        """
        Atualiza dados de um leitor.
        
        Args:
            leitor_id: ID do leitor
            **kwargs: Campos a atualizar (nome, turma, ativo)
            
        Returns:
            True se atualizado com sucesso
        """
        try:
            campos_validos = {'nome', 'turma', 'ativo'}
            campos_atualizacao = {k: v for k, v in kwargs.items() if k in campos_validos}
            
            if not campos_atualizacao:
                return False
            
            campos_atualizacao['data_atualizacao'] = datetime.now()
            
            set_clause = ', '.join([f'{k} = ?' for k in campos_atualizacao.keys()])
            valores = list(campos_atualizacao.values()) + [leitor_id]
            
            self.cursor.execute(f'UPDATE leitores SET {set_clause} WHERE id = ?', valores)
            self.conexao.commit()
            return self.cursor.rowcount > 0
        except sqlite3.Error:
            return False
    
    # ========== OPERAÇÕES COM EMPRÉSTIMOS ==========
    
    def registrar_emprestimo(self, livro_id: int, leitor_id: int,
                            data_devolucao_prevista: Optional[str] = None,
                            observacoes: Optional[str] = None) -> int:
        """
        Registra um novo empréstimo.
        
        Args:
            livro_id: ID do livro
            leitor_id: ID do leitor
            data_devolucao_prevista: Data prevista para devolução (YYYY-MM-DD)
            observacoes: Observações sobre o empréstimo
            
        Returns:
            ID do empréstimo registrado
        """
        try:
            self.cursor.execute('''
                INSERT INTO emprestimos 
                (livro_id, leitor_id, data_devolucao_prevista, observacoes, status)
                VALUES (?, ?, ?, ?, 'ativo')
            ''', (livro_id, leitor_id, data_devolucao_prevista, observacoes))
            
            emprestimo_id = self.cursor.lastrowid
            self.conexao.commit()
            return emprestimo_id
        except sqlite3.Error:
            raise
    
    def contar_emprestimos_ativos_livro(self, livro_id: int) -> int:
        """
        Conta quantos exemplares de um livro estão ativos (emprestados).
        
        Args:
            livro_id: ID do livro
            
        Returns:
            Número de empréstimos ativos para este livro
        """
        try:
            self.cursor.execute(
                'SELECT COUNT(*) FROM emprestimos WHERE livro_id = ? AND status = "ativo"',
                (livro_id,)
            )
            resultado = self.cursor.fetchone()
            return resultado[0] if resultado else 0
        except sqlite3.Error:
            return 0
    
    def buscar_emprestimo_por_id(self, emprestimo_id: int) -> Optional[dict]:
        """
        Busca um empréstimo pelo ID.
        
        Args:
            emprestimo_id: ID do empréstimo
            
        Returns:
            Dicionário com dados do empréstimo ou None
        """
        try:
            self.cursor.execute('SELECT * FROM emprestimos WHERE id = ?', (emprestimo_id,))
            resultado = self.cursor.fetchone()
            return dict(resultado) if resultado else None
        except sqlite3.Error:
            return None
    
    def listar_emprestimos_ativos(self, leitor_id: Optional[int] = None) -> List[dict]:
        """
        Lista empréstimos ativos.
        
        Args:
            leitor_id: Se informado, lista apenas empréstimos deste leitor
            
        Returns:
            Lista de dicionários com dados dos empréstimos
        """
        try:
            if leitor_id:
                self.cursor.execute(
                    'SELECT * FROM emprestimos WHERE status = "ativo" AND leitor_id = ? ORDER BY data_emprestimo DESC',
                    (leitor_id,)
                )
            else:
                self.cursor.execute(
                    'SELECT * FROM emprestimos WHERE status = "ativo" ORDER BY data_emprestimo DESC'
                )
            
            resultados = self.cursor.fetchall()
            return [dict(row) for row in resultados]
        except sqlite3.Error:
            return []
    
    def registrar_devolucao(self, emprestimo_id: int, data_devolucao_real: Optional[str] = None) -> bool:
        """
        Registra a devolução de um livro.
        
        Args:
            emprestimo_id: ID do empréstimo
            data_devolucao_real: Data da devolução (padrão: hoje)
            
        Returns:
            True se registrado com sucesso
        """
        try:
            if not data_devolucao_real:
                data_devolucao_real = datetime.now().isoformat()
            
            # Obter ID do livro antes de atualizar o empréstimo
            self.cursor.execute('SELECT livro_id FROM emprestimos WHERE id = ?', (emprestimo_id,))
            resultado = self.cursor.fetchone()
            if not resultado:
                return False
            
            livro_id = resultado[0]
            
            # Atualizar empréstimo
            self.cursor.execute('''
                UPDATE emprestimos 
                SET data_devolucao_real = ?, status = 'finalizado'
                WHERE id = ?
            ''', (data_devolucao_real, emprestimo_id))
            
            self.conexao.commit()
            return self.cursor.rowcount > 0
        except sqlite3.Error:
            return False
    
    def renovar_emprestimo(self, emprestimo_id: int, nova_data_devolucao: str) -> bool:
        """
        Renova um empréstimo.
        
        Args:
            emprestimo_id: ID do empréstimo
            nova_data_devolucao: Nova data prevista para devolução (YYYY-MM-DD)
            
        Returns:
            True se renovado com sucesso
        """
        try:
            self.cursor.execute('''
                UPDATE emprestimos 
                SET data_devolucao_prevista = ?, renovacoes = renovacoes + 1
                WHERE id = ?
            ''', (nova_data_devolucao, emprestimo_id))
            
            self.conexao.commit()
            return self.cursor.rowcount > 0
        except sqlite3.Error:
            return False
    
    def fechar(self) -> None:
        """Fecha a conexão com o banco de dados."""
        if self.conexao:
            self.conexao.close()
