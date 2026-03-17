#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script para importar alunos do arquivo alunos.txt para o banco de dados.

Regras de negócio:
1. O arquivo segue o padrão: NOME DA TURMA {, seguido de ID em uma linha 
   e NOME na outra para cada aluno, fechando com }.
2. Ignora linhas em branco, IDs (números puros) e chaves { e }.
3. Extrai nome da turma e nome do aluno.
4. Insere os dados na tabela 'leitores' do banco datalibros.db.
5. Usa UTF-8 para evitar erros de acentuação.
"""

import sqlite3
import sys
from pathlib import Path
from typing import List, Tuple, Optional


class ImportadorAlunos:
    """Classe para importar alunos de um arquivo de texto para o banco de dados."""
    
    def __init__(self, caminho_db: str = 'datalibros.db'):
        """
        Inicializa o importador.
        
        Args:
            caminho_db: Caminho para o arquivo SQLite3
        """
        self.caminho_db = caminho_db
        self.conexao = None
        self.cursor = None
        self._conectar()
    
    def _conectar(self) -> None:
        """Estabelece conexão com o banco de dados."""
        try:
            self.conexao = sqlite3.connect(self.caminho_db)
            self.conexao.row_factory = sqlite3.Row
            self.cursor = self.conexao.cursor()
            print(f"✓ Conectado ao banco: {self.caminho_db}")
        except sqlite3.Error as e:
            print(f"✗ Erro ao conectar ao banco: {e}")
            sys.exit(1)
    
    def fechar(self) -> None:
        """Fecha a conexão com o banco de dados."""
        if self.conexao:
            self.conexao.close()
            print("✓ Conexão fechada")
    
    def _verificar_tabela(self) -> bool:
        """Verifica se a tabela leitores existe."""
        try:
            self.cursor.execute(
                "SELECT name FROM sqlite_master WHERE type='table' AND name='leitores'"
            )
            resultado = self.cursor.fetchone()
            if resultado:
                print("✓ Tabela 'leitores' encontrada")
                return True
            else:
                print("✗ Tabela 'leitores' não encontrada")
                return False
        except sqlite3.Error as e:
            print(f"✗ Erro ao verificar tabela: {e}")
            return False
    
    def _aluno_existe(self, nome: str, turma: str) -> bool:
        """
        Verifica se um aluno já existe no banco.
        
        Args:
            nome: Nome do aluno
            turma: Turma do aluno
            
        Returns:
            True se existe, False caso contrário
        """
        try:
            self.cursor.execute(
                "SELECT id FROM leitores WHERE nome = ? AND turma = ?",
                (nome, turma)
            )
            return self.cursor.fetchone() is not None
        except sqlite3.Error as e:
            print(f"✗ Erro ao verificar aluno: {e}")
            return False
    
    def inserir_aluno(self, nome: str, turma: str) -> bool:
        """
        Insere um aluno na tabela leitores.
        
        Args:
            nome: Nome do aluno
            turma: Turma do aluno
            
        Returns:
            True se inserido com sucesso, False caso contrário
        """
        try:
            self.cursor.execute(
                """INSERT INTO leitores (nome, turma, ativo) 
                   VALUES (?, ?, 1)""",
                (nome, turma)
            )
            self.conexao.commit()
            return True
        except sqlite3.IntegrityError:
            print(f"⚠ Aluno '{nome}' ({turma}) já existe, pulando...")
            return False
        except sqlite3.Error as e:
            print(f"✗ Erro ao inserir aluno: {e}")
            return False
    
    def _extrair_alunos_do_arquivo(self, caminho_arquivo: str) -> List[Tuple[str, str]]:
        """
        Extrai alunos e turmas do arquivo de texto.
        
        Args:
            caminho_arquivo: Caminho para o arquivo alunos.txt
            
        Returns:
            Lista de tuplas (turma, nome_aluno)
        """
        alunos = []
        
        try:
            with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
                linhas = arquivo.readlines()
        except FileNotFoundError:
            print(f"✗ Arquivo não encontrado: {caminho_arquivo}")
            return alunos
        except UnicodeDecodeError:
            print(f"✗ Erro de codificação. Certifique-se de que é UTF-8")
            return alunos
        
        turma_atual = None
        i = 0
        
        while i < len(linhas):
            linha = linhas[i].strip()
            
            # Ignora linhas em branco
            if not linha:
                i += 1
                continue
            
            # Identifica a turma (linha com {)
            if linha.endswith('{'):
                # Extrai o nome da turma (remove o { do final)
                turma_atual = linha[:-1].strip()
                print(f"\n📚 Processando turma: {turma_atual}")
                i += 1
                continue
            
            # Fecha a turma (linha com })
            if linha == '}':
                turma_atual = None
                i += 1
                continue
            
            # Se estamos dentro de uma turma
            if turma_atual:
                # Ignora linhas que contêm apenas números (IDs)
                if linha.isdigit():
                    i += 1
                    continue
                
                # Se for uma linha com nome (próxima linha após ID)
                # O nome é qualquer coisa que não seja um número
                if not linha.isdigit() and linha not in ['{', '}']:
                    nome_aluno = linha
                    alunos.append((turma_atual, nome_aluno))
                    print(f"  ✓ {nome_aluno} ({turma_atual})")
            
            i += 1
        
        return alunos
    
    def importar(self, caminho_arquivo: str) -> int:
        """
        Importa alunos do arquivo para o banco de dados.
        
        Args:
            caminho_arquivo: Caminho para o arquivo alunos.txt
            
        Returns:
            Número de alunos importados
        """
        print("\n" + "="*60)
        print("IMPORTADOR DE ALUNOS - DataLivros")
        print("="*60)
        
        # Verifica se arquivo existe
        if not Path(caminho_arquivo).exists():
            print(f"✗ Arquivo não encontrado: {caminho_arquivo}")
            return 0
        
        # Verifica se tabela existe
        if not self._verificar_tabela():
            print("✗ Não é possível continuar sem a tabela 'leitores'")
            return 0
        
        # Extrai alunos do arquivo
        print(f"\n📂 Lendo arquivo: {caminho_arquivo}")
        alunos = self._extrair_alunos_do_arquivo(caminho_arquivo)
        
        if not alunos:
            print("✗ Nenhum aluno encontrado no arquivo")
            return 0
        
        print(f"\n📋 Total de alunos encontrados: {len(alunos)}")
        
        # Importa alunos para o banco
        print("\n" + "-"*60)
        print("Importando para o banco de dados...")
        print("-"*60)
        
        importados = 0
        duplicados = 0
        
        for turma, nome in alunos:
            if self._aluno_existe(nome, turma):
                duplicados += 1
                print(f"⚠ '{nome}' ({turma}) - já existe")
            else:
                if self.inserir_aluno(nome, turma):
                    importados += 1
        
        # Resumo
        print("\n" + "="*60)
        print("RESUMO DA IMPORTAÇÃO")
        print("="*60)
        print(f"✓ Alunos importados:  {importados}")
        print(f"⚠ Alunos duplicados:  {duplicados}")
        print(f"📊 Total processado:   {len(alunos)}")
        print("="*60 + "\n")
        
        return importados


def main():
    """Função principal."""
    # Caminhos padrão
    caminho_db = 'datalibros.db'
    caminho_arquivo = 'alunos.txt'
    
    # Permite passar caminhos como argumentos
    if len(sys.argv) > 1:
        caminho_arquivo = sys.argv[1]
    if len(sys.argv) > 2:
        caminho_db = sys.argv[2]
    
    # Cria importador e executa
    importador = ImportadorAlunos(caminho_db)
    
    try:
        quantidade = importador.importar(caminho_arquivo)
        if quantidade > 0:
            print(f"✓ Sucesso! {quantidade} aluno(s) importado(s)")
            return 0
        else:
            print("⚠ Nenhum aluno foi importado")
            return 1
    except Exception as e:
        print(f"✗ Erro durante a importação: {e}")
        return 1
    finally:
        importador.fechar()


if __name__ == '__main__':
    sys.exit(main())
