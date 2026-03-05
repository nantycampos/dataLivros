"""
Módulo Main - Controlador Principal (MVC Controller)
Orquestra a integração entre View, Database e API
Gerencia eventos, lógica de negócio e fluxos de dados
"""

import wx
from view import MainFrame, CirculacaoPanel, CadastroPanel, LeitoresPanel
from database import DatabaseGerenciador
from api_service import buscar_livro_google_books
from datetime import datetime, timedelta
from typing import Optional, Dict


class DataLivrosController:
    """Controlador principal da aplicação DataLivros."""
    
    def __init__(self):
        """Inicializa o controlador e seus componentes."""
        self.db = DatabaseGerenciador('datalibros.db')
        self.frame = MainFrame()
        self.livro_selecionado: Optional[Dict] = None
        self.leitor_selecionado: Optional[Dict] = None
        self.livros_api_resultados: list = []  # Armazena resultados da API
        self.livros_circulacao_resultados: list = []  # Armazena resultados de busca de livros disponíveis
        
        # Controle de modo de edição
        self.editando_livro_id: Optional[int] = None  # ID do livro em edição (None = novo)
        self.editando_leitor_id: Optional[int] = None  # ID do leitor em edição (None = novo)
        
        self._configurar_eventos()
        self._foco_inicial()
    
    def _foco_inicial(self):
        """Define o foco inicial para o campo de busca da aba Circulação."""
        aba_circ = self.frame.get_aba_circulacao()
        aba_circ.texto_busca_livro.SetFocus()
        self.frame.atualizar_status("Foco no campo de busca de livro. Digite para começar.")
    
    def _configurar_eventos(self):
        """Configura todos os eventos da aplicação."""
        aba_circ = self.frame.get_aba_circulacao()
        aba_cad = self.frame.get_aba_cadastro()
        aba_leit = self.frame.get_aba_leitores()
        
        # --- EVENTOS DA ABA CIRCULAÇÃO ---
        self.frame.vincular_evento(aba_circ.btn_buscar_livro, wx.EVT_BUTTON, 
                                   self._on_buscar_livro_circulacao)
        self.frame.vincular_evento(aba_circ.lista_resultados_livro, wx.EVT_LISTBOX,
                                   self._on_selecionar_livro_circulacao)
        self.frame.vincular_evento(aba_circ.texto_busca_leitor, wx.EVT_TEXT, 
                                   self._on_filtrar_leitores)
        self.frame.vincular_evento(aba_circ.btn_emprestar, wx.EVT_BUTTON, 
                                   self._on_registrar_emprestimo)
        self.frame.vincular_evento(aba_circ.btn_devolver, wx.EVT_BUTTON, 
                                   self._on_registrar_devolucao)
        
        # --- EVENTOS DA ABA CADASTRO ---
        self.frame.vincular_evento(aba_cad.btn_buscar_api, wx.EVT_BUTTON, 
                                   self._on_buscar_livro_api)
        self.frame.vincular_evento(aba_cad.lista_resultados_api, wx.EVT_LISTBOX,
                                   self._on_selecionar_resultado_api)
        self.frame.vincular_evento(aba_cad.btn_salvar, wx.EVT_BUTTON, 
                                   self._on_salvar_livro)
        self.frame.vincular_evento(aba_cad.btn_editar, wx.EVT_BUTTON, 
                                   self._on_editar_livro)
        self.frame.vincular_evento(aba_cad.btn_limpar, wx.EVT_BUTTON, 
                                   self._on_limpar_campos_cadastro)
        
        # --- EVENTOS DA ABA LEITORES ---
        self.frame.vincular_evento(aba_leit.btn_salvar_leitor, wx.EVT_BUTTON, 
                                   self._on_salvar_leitor)
        self.frame.vincular_evento(aba_leit.btn_editar_leitor, wx.EVT_BUTTON,
                                   self._on_editar_leitor)
        self.frame.vincular_evento(aba_leit.texto_busca_leitor_list, wx.EVT_TEXT, 
                                   self._on_filtrar_lista_leitores)
        self.frame.vincular_evento(aba_leit.btn_detalhes_leitor, wx.EVT_BUTTON, 
                                   self._on_detalhes_leitor)
        
        # --- EVENTOS GLOBAIS (ATALHOS) ---
        self.frame.Bind(wx.EVT_MENU, self._on_ir_aba_circulacao, id=self.frame.id_aba_circulacao)
        self.frame.Bind(wx.EVT_MENU, self._on_ir_aba_cadastro, id=self.frame.id_aba_cadastro)
        self.frame.Bind(wx.EVT_MENU, self._on_ir_aba_leitores, id=self.frame.id_aba_leitores)
        self.frame.Bind(wx.EVT_MENU, self._on_sair, id=wx.ID_EXIT)
    
    # ========== EVENTOS DA ABA CIRCULAÇÃO ==========
    
    def _on_buscar_livro_circulacao(self, event):
        """Evento: Busca livros na aba Circulação e popula ListBox de resultados."""
        aba_circ = self.frame.get_aba_circulacao()
        isbn_titulo = aba_circ.texto_busca_livro.GetValue().strip()
        
        if not isbn_titulo:
            self.frame.atualizar_status("Erro: Digite um ISBN ou título.")
            wx.Bell()
            return
        
        # Buscar no banco local primeiro por ISBN
        livro = self.db.buscar_livro_por_isbn(isbn_titulo)
        
        livros_encontrados = []
        if livro and livro.get('status') == 'Disponível':
            livros_encontrados = [livro]
        
        # Se não encontrou por ISBN, buscar por título com status Disponível
        if not livros_encontrados:
            livros = self.db.buscar_livros_por_titulo(isbn_titulo)
            livros_encontrados = [l for l in livros if l.get('status') == 'Disponível']
        
        # Popula a ListBox com resultados
        self._atualizar_lista_resultados_livro(livros_encontrados)
    
    def _atualizar_lista_resultados_livro(self, livros: list):
        """Atualiza a ListBox com resultados de busca de livros disponíveis."""
        aba_circ = self.frame.get_aba_circulacao()
        self.livros_circulacao_resultados = livros  # Armazenar para referência posterior
        
        aba_circ.lista_resultados_livro.Clear()
        
        if not livros:
            self.frame.atualizar_status("Nenhum livro disponível encontrado.")
            wx.Bell()
            return
        
        for livro in livros:
            titulo = livro.get('titulo', 'Sem título')
            autores = livro.get('autores', 'Autor desconhecido')
            quantidade_total = livro.get('quantidade_total', 1)
            emprestimos_ativos = self.db.contar_emprestimos_ativos_livro(livro['id'])
            quantidade_disponivel = quantidade_total - emprestimos_ativos
            
            label = f"{titulo} - {autores} [{quantidade_disponivel} disponíveis]"
            aba_circ.lista_resultados_livro.Append(label, livro['id'])
        
        self.frame.atualizar_status(f"Encontrados {len(livros)} livro(s) disponível(is).")
        aba_circ.lista_resultados_livro.SetFocus()
        
        # Anúncio para NVDA
        wx.SafeYield()
    
    def _on_selecionar_livro_circulacao(self, event):
        """Evento: Seleciona um livro da lista de resultados."""
        aba_circ = self.frame.get_aba_circulacao()
        
        selecionado = aba_circ.lista_resultados_livro.GetSelection()
        if selecionado == wx.NOT_FOUND:
            self.frame.atualizar_status("Nenhum livro selecionado.")
            return
        
        livro_id = aba_circ.lista_resultados_livro.GetClientData(selecionado)
        livro = self.db.buscar_livro_por_id(livro_id)
        
        if livro:
            self.livro_selecionado = livro
            titulo = livro.get('titulo', 'Sem título')
            quantidade_total = livro.get('quantidade_total', 1)
            emprestimos_ativos = self.db.contar_emprestimos_ativos_livro(livro['id'])
            quantidade_disponivel = quantidade_total - emprestimos_ativos
            
            # Anúncio claro da quantidade disponível para NVDA
            msg_status = f"Livro: {titulo} - {quantidade_disponivel} exemplar(es) disponível(is) de {quantidade_total}"
            self.frame.atualizar_status(msg_status)
            # O botão emprestar agora será habilitado
        else:
            self.frame.atualizar_status("Erro ao carregar livro.")
            wx.Bell()
    
    def _on_filtrar_leitores(self, event):
        """Evento: Filtra leitores conforme digitação."""
        aba_circ = self.frame.get_aba_circulacao()
        filtro = aba_circ.texto_busca_leitor.GetValue().strip()
        
        if not filtro:
            self._atualizar_combo_leitores([])
            return
        
        leitores = self.db.buscar_leitores_por_nome(filtro)
        self._atualizar_combo_leitores(leitores)
    
    def _atualizar_combo_leitores(self, leitores: list):
        """Atualiza o ComboBox de leitores."""
        aba_circ = self.frame.get_aba_circulacao()
        aba_circ.combo_leitores.Clear()
        
        for leitor in leitores:
            label = f"{leitor['nome']} (ID: {leitor['id']})"
            aba_circ.combo_leitores.Append(label, leitor['id'])
        
        if leitores:
            self.frame.atualizar_status(f"Encontrados {len(leitores)} leitor(es).")
    
    def _on_registrar_emprestimo(self, event):
        """Evento: Registra um empréstimo."""
        aba_circ = self.frame.get_aba_circulacao()
        
        if not self.livro_selecionado:
            self.frame.atualizar_status("Erro: Selecione um livro primeiro.")
            wx.Bell()
            return
        
        # Validar se há exemplares disponíveis
        quantidade_total = self.livro_selecionado.get('quantidade_total', 1)
        emprestimos_ativos = self.db.contar_emprestimos_ativos_livro(self.livro_selecionado['id'])
        quantidade_disponivel = quantidade_total - emprestimos_ativos
        
        if quantidade_disponivel <= 0:
            titulo = self.livro_selecionado.get('titulo', 'Livro desconhecido')
            self.frame.atualizar_status(f"Erro: Todos os exemplares de '{titulo}' estão emprestados.")
            wx.Bell()
            return
        
        leitor_idx = aba_circ.combo_leitores.GetSelection()
        if leitor_idx == wx.NOT_FOUND:
            self.frame.atualizar_status("Erro: Selecione um leitor.")
            wx.Bell()
            return
        
        leitor_id = aba_circ.combo_leitores.GetClientData(leitor_idx)
        
        try:
            # Data de devolução prevista: 14 dias após empréstimo
            data_devolucao = (datetime.now() + timedelta(days=14)).strftime('%Y-%m-%d')
            
            emprestimo_id = self.db.registrar_emprestimo(
                livro_id=self.livro_selecionado['id'],
                leitor_id=leitor_id,
                data_devolucao_prevista=data_devolucao
            )
            
            mensagem = f"Empréstimo #{emprestimo_id} registrado com sucesso. Devolução prevista: {data_devolucao}"
            self.frame.atualizar_status(mensagem)
            
            # Limpar campos
            aba_circ.texto_busca_livro.SetValue('')
            aba_circ.texto_busca_leitor.SetValue('')
            aba_circ.combo_leitores.Clear()
            self.livro_selecionado = None
            
            # Atualizar lista de empréstimos
            self._atualizar_lista_emprestimos()
            
        except Exception as e:
            self.frame.atualizar_status(f"Erro ao registrar empréstimo: {str(e)}")
            wx.Bell()
    
    def _on_registrar_devolucao(self, event):
        """Evento: Registra a devolução de um livro."""
        aba_circ = self.frame.get_aba_circulacao()
        
        selecionado = aba_circ.lista_emprestimos.GetSelection()
        if selecionado == wx.NOT_FOUND:
            self.frame.atualizar_status("Erro: Selecione um empréstimo da lista para registrar devolução.")
            wx.Bell()
            return
        
        try:
            # Obter ID do empréstimo selecionado
            emprestimo_id = aba_circ.lista_emprestimos.GetClientData(selecionado)
            
            # Registrar devolução no banco
            if self.db.registrar_devolucao(emprestimo_id):
                self.frame.atualizar_status("Livro devolvido com sucesso.")
                self._atualizar_lista_emprestimos()
            else:
                self.frame.atualizar_status("Erro: Não foi possível registrar a devolução.")
                wx.Bell()
        except Exception as e:
            self.frame.atualizar_status(f"Erro ao registrar devolução: {str(e)}")
            wx.Bell()
    
    def _atualizar_lista_emprestimos(self):
        """Atualiza a lista de empréstimos ativos."""
        aba_circ = self.frame.get_aba_circulacao()
        emprestimos = self.db.listar_emprestimos_ativos()
        
        aba_circ.lista_emprestimos.Clear()
        for empr in emprestimos:
            livro = self.db.buscar_livro_por_id(empr['livro_id'])
            leitor = self.db.buscar_leitor_por_id(empr['leitor_id'])
            
            if livro and leitor:
                label = f"{livro['titulo']} - {leitor['nome']} (Empr. #{empr['id']})"
                aba_circ.lista_emprestimos.Append(label, empr['id'])
    
    # ========== EVENTOS DA ABA CADASTRO ==========
    
    def _on_buscar_livro_api(self, event):
        """Evento: Busca livro na Google Books API e preenche a lista de resultados."""
        aba_cad = self.frame.get_aba_cadastro()
        isbn_titulo = aba_cad.texto_busca_api.GetValue().strip()
        
        if not isbn_titulo:
            self.frame.atualizar_status("Erro: Digite um ISBN ou título para buscar.")
            wx.Bell()
            return
        
        # Limpar lista anterior
        aba_cad.lista_resultados_api.Clear()
        self.livros_api_resultados = []
        
        self.frame.atualizar_status("Buscando na API Google Books...")
        wx.Yield()  # Processar mensagens para evitar travamento
        
        resultado = buscar_livro_google_books(isbn_titulo)
        
        if resultado['sucesso']:
            # Armazenar livros encontrados
            self.livros_api_resultados = resultado['livros']
            
            # Preencher ListBox com formato "Título - Autores"
            for livro in self.livros_api_resultados:
                autores_str = ', '.join(livro['autores']) if livro['autores'] else 'Autor desconhecido'
                label = f"{livro['titulo']} - {autores_str}"
                aba_cad.lista_resultados_api.Append(label)
            
            # Selecionar primeiro resultado
            aba_cad.lista_resultados_api.SetSelection(0)
            
            # Preencherprimeiro resultado automaticamente
            self._preencher_campos_com_livro(0)
            
            # Mover foco para a lista
            aba_cad.lista_resultados_api.SetFocus()
            
            mensagem = f"Encontrados {len(self.livros_api_resultados)} livro(s). Use as setas para navegar e selecionar."
            self.frame.atualizar_status(mensagem)
        else:
            self.frame.atualizar_status(f"Erro na busca: {resultado['erro']}")
            wx.Bell()
    
    def _on_selecionar_resultado_api(self, event):
        """Evento: Preenche campos ao selecionar um livro da lista."""
        indice = event.GetSelection()
        if indice != wx.NOT_FOUND:
            self._preencher_campos_com_livro(indice)
            self.frame.atualizar_status(f"Livro {indice + 1} selecionado. Revise os dados e salve.")
    
    def _preencher_campos_com_livro(self, indice: int):
        """Preenche os campos de formulário com dados de um livro específico."""
        if indice < 0 or indice >= len(self.livros_api_resultados):
            return
        
        aba_cad = self.frame.get_aba_cadastro()
        livro = self.livros_api_resultados[indice]
        
        # Preencher campos
        aba_cad.texto_titulo.SetValue(livro['titulo'])
        aba_cad.texto_isbn.SetValue(livro['isbn'])
        aba_cad.texto_autores.SetValue(', '.join(livro['autores']) if livro['autores'] else '')
        aba_cad.texto_editora.SetValue(livro['editora'])
        aba_cad.texto_ano.SetValue(str(livro['ano_publicacao']) if livro['ano_publicacao'] else '')
        aba_cad.texto_descricao.SetValue(livro['descricao'])
        aba_cad.texto_categorias.SetValue(', '.join(livro['categorias']) if livro['categorias'] else '')
    
    def _on_salvar_livro(self, event):
        """Evento: Salva um livro no banco de dados."""
        aba_cad = self.frame.get_aba_cadastro()
        
        # Validar campos obrigatórios
        titulo = aba_cad.texto_titulo.GetValue().strip()
        if not titulo:
            self.frame.atualizar_status("Erro: O título é obrigatório.")
            wx.Bell()
            return
        
        try:
            isbn = aba_cad.texto_isbn.GetValue().strip() or None
            autores = aba_cad.texto_autores.GetValue().strip() or None
            editora = aba_cad.texto_editora.GetValue().strip() or None
            ano_str = aba_cad.texto_ano.GetValue().strip()
            ano_publicacao = int(ano_str) if ano_str else None
            descricao = aba_cad.texto_descricao.GetValue().strip() or None
            categorias = aba_cad.texto_categorias.GetValue().strip() or None
            quantidade_total = aba_cad.texto_quantidade.GetValue()
            
            # Verificar se estamos editando ou criando novo livro
            if self.editando_livro_id is not None:
                # Modo de edição: atualizar livro existente
                self.db.atualizar_livro(
                    id=self.editando_livro_id,
                    titulo=titulo,
                    isbn=isbn,
                    autores=autores,
                    editora=editora,
                    ano_publicacao=ano_publicacao,
                    descricao=descricao,
                    categorias=categorias,
                    quantidade_total=quantidade_total
                )
                
                self.frame.atualizar_status(f"Livro '{titulo}' atualizado com sucesso!")
                
                # Limpar modo de edição
                self.editando_livro_id = None
                aba_cad.btn_salvar.SetLabel("Salvar Livro")
            else:
                # Modo de criação: adicionar novo livro
                livro_id = self.db.adicionar_livro(
                    titulo=titulo,
                    isbn=isbn,
                    autores=autores,
                    editora=editora,
                    ano_publicacao=ano_publicacao,
                    descricao=descricao,
                    categorias=categorias,
                    quantidade_total=quantidade_total
                )
                
                self.frame.atualizar_status(f"Livro salvo com sucesso! ID: {livro_id}")
            
            self._on_limpar_campos_cadastro(None)
            
        except ValueError:
            self.frame.atualizar_status("Erro: Ano de publicação deve ser um número.")
            wx.Bell()
        except Exception as e:
            self.frame.atualizar_status(f"Erro ao salvar livro: {str(e)}")
            wx.Bell()
    
    def _on_limpar_campos_cadastro(self, event):
        """Evento: Limpa os campos da aba Cadastro e cancela modo de edição."""
        aba_cad = self.frame.get_aba_cadastro()
        
        aba_cad.texto_busca_api.SetValue('')
        aba_cad.texto_titulo.SetValue('')
        aba_cad.texto_isbn.SetValue('')
        aba_cad.texto_autores.SetValue('')
        aba_cad.texto_editora.SetValue('')
        aba_cad.texto_ano.SetValue('')
        aba_cad.texto_descricao.SetValue('')
        aba_cad.texto_categorias.SetValue('')
        aba_cad.texto_quantidade.SetValue(1)
        
        # Cancelar modo de edição se ativo
        if self.editando_livro_id is not None:
            self.editando_livro_id = None
            aba_cad.btn_salvar.SetLabel("Salvar Livro")
            self.frame.atualizar_status("Edição cancelada.")
        else:
            self.frame.atualizar_status("Campos limpos.")
        
        aba_cad.texto_busca_api.SetFocus()
    
    # ========== EVENTOS DA ABA LEITORES ==========
    
    def _on_salvar_leitor(self, event):
        """Evento: Salva ou atualiza um leitor."""
        aba_leit = self.frame.get_aba_leitores()
        
        nome = aba_leit.texto_nome.GetValue().strip()
        if not nome:
            self.frame.atualizar_status("Erro: O nome é obrigatório.")
            wx.Bell()
            return
        
        try:
            turma = aba_leit.texto_turma.GetValue().strip() or None
            
            # Verificar se estamos editando ou criando novo leitor
            if self.editando_leitor_id is not None:
                # Modo de edição: atualizar leitor existente
                self.db.atualizar_leitor(
                    id=self.editando_leitor_id,
                    nome=nome,
                    turma=turma
                )
                
                self.frame.atualizar_status(f"Leitor '{nome}' atualizado com sucesso!")
                
                # Limpar modo de edição
                self.editando_leitor_id = None
                aba_leit.btn_salvar_leitor.SetLabel("Salvar Leitor")
            else:
                # Modo de criação: adicionar novo leitor
                leitor_id = self.db.adicionar_leitor(
                    nome=nome,
                    turma=turma
                )
                
                self.frame.atualizar_status(f"Leitor salvo com sucesso! ID: {leitor_id}")
            
            # Limpar campos
            aba_leit.texto_nome.SetValue('')
            aba_leit.texto_turma.SetValue('')
            
            # Atualizar lista
            self._atualizar_lista_leitores('')
            aba_leit.texto_nome.SetFocus()
            
        except Exception as e:
            self.frame.atualizar_status(f"Erro ao salvar leitor: {str(e)}")
            wx.Bell()
    
    def _on_filtrar_lista_leitores(self, event):
        """Evento: Filtra a lista de leitores conforme digitação."""
        aba_leit = self.frame.get_aba_leitores()
        filtro = aba_leit.texto_busca_leitor_list.GetValue().strip()
        
        self._atualizar_lista_leitores(filtro)
    
    def _atualizar_lista_leitores(self, filtro: str = ''):
        """Atualiza a lista de leitores."""
        aba_leit = self.frame.get_aba_leitores()
        
        if filtro:
            leitores = self.db.buscar_leitores_por_nome(filtro)
        else:
            leitores = self.db.listar_todos_leitores()
        
        aba_leit.lista_leitores.Clear()
        for leitor in leitores:
            turma_info = f" ({leitor['turma']})" if leitor.get('turma') else ""
            label = f"{leitor['nome']}{turma_info} - ID: {leitor['id']}"
            aba_leit.lista_leitores.Append(label, leitor['id'])
        
        if leitores:
            self.frame.atualizar_status(f"{len(leitores)} leitor(es) encontrado(s).")
        else:
            self.frame.atualizar_status("Nenhum leitor encontrado.")
    
    def _on_detalhes_leitor(self, event):
        """Evento: Exibe detalhes de um leitor selecionado."""
        aba_leit = self.frame.get_aba_leitores()
        
        selecionado = aba_leit.lista_leitores.GetSelection()
        if selecionado == wx.NOT_FOUND:
            self.frame.atualizar_status("Erro: Selecione um leitor para ver detalhes.")
            wx.Bell()
            return
        
        leitor_id = aba_leit.lista_leitores.GetClientData(selecionado)
        leitor = self.db.buscar_leitor_por_id(leitor_id)
        
        if leitor:
            turma_info = f"Turma: {leitor['turma']}" if leitor.get('turma') else "Turma: Não informada"
            msg = f"Nome: {leitor['nome']}\n{turma_info}"
            wx.MessageBox(msg, "Detalhes do Leitor", wx.OK | wx.ICON_INFORMATION)
    
    def _on_editar_livro(self, event):
        """Evento: Edita um livro selecionado da lista de busca."""
        aba_cad = self.frame.get_aba_cadastro()
        
        selecionado = aba_cad.lista_resultados_api.GetSelection()
        if selecionado == wx.NOT_FOUND:
            self.frame.atualizar_status("Erro: Selecione um livro para editar.")
            wx.Bell()
            return
        
        # Obter livro da lista de resultados da API ou banco
        if selecionado < len(self.livros_api_resultados):
            livro = self.livros_api_resultados[selecionado]
            livro_id = livro.get('id')
            
            # Se ainda não tem ID (resultado da API), buscar do banco ou usar None
            if livro_id is None:
                # Assumir que o livro precisa ser salvo antes de ser editado
                self.frame.atualizar_status("Erro: Salve o livro antes de editar.")
                return
        else:
            self.frame.atualizar_status("Erro: Livro não encontrado.")
            wx.Bell()
            return
        
        # Buscar dados completos do livro no banco
        livro_completo = self.db.buscar_livro_por_id(livro_id)
        if not livro_completo:
            self.frame.atualizar_status(f"Erro: Livro com ID {livro_id} não encontrado no banco de dados.")
            wx.Bell()
            return
        
        # Preencher campos com os dados atuais
        aba_cad.texto_titulo.SetValue(livro_completo.get('titulo', ''))
        aba_cad.texto_isbn.SetValue(livro_completo.get('isbn', ''))
        aba_cad.texto_autores.SetValue(', '.join(livro_completo.get('autores', [])) if livro_completo.get('autores') else '')
        aba_cad.texto_editora.SetValue(livro_completo.get('editora', ''))
        aba_cad.texto_ano.SetValue(str(livro_completo.get('ano_publicacao', '')))
        aba_cad.texto_descricao.SetValue(livro_completo.get('descricao', ''))
        aba_cad.texto_categorias.SetValue(', '.join(livro_completo.get('categorias', [])) if livro_completo.get('categorias') else '')
        aba_cad.texto_quantidade.SetValue(livro_completo.get('quantidade_total', 1))
        
        # Marcar como modo de edição
        self.editando_livro_id = livro_id
        
        # Mudar label do botão para "Atualizar"
        aba_cad.btn_salvar.SetLabel("Atualizar Livro")
        
        # Mover foco para o título
        aba_cad.texto_titulo.SetFocus()
        
        # Anunciar ao NVDA
        titulo = livro_completo.get('titulo', 'Livro desconhecido')
        self.frame.atualizar_status(f"Editando livro: {titulo}")
    
    def _on_editar_leitor(self, event):
        """Evento: Edita um leitor selecionado na lista de leitores."""
        aba_leit = self.frame.get_aba_leitores()
        
        selecionado = aba_leit.lista_leitores.GetSelection()
        if selecionado == wx.NOT_FOUND:
            self.frame.atualizar_status("Erro: Selecione um leitor para editar.")
            wx.Bell()
            return
        
        # Obter ID do leitor selecionado
        leitor_id = aba_leit.lista_leitores.GetClientData(selecionado)
        
        # Buscar dados completos do leitor no banco
        leitor = self.db.buscar_leitor_por_id(leitor_id)
        if not leitor:
            self.frame.atualizar_status(f"Erro: Leitor com ID {leitor_id} não encontrado no banco de dados.")
            wx.Bell()
            return
        
        # Preencher campos com os dados atuais
        aba_leit.texto_nome.SetValue(leitor.get('nome', ''))
        aba_leit.texto_turma.SetValue(leitor.get('turma', ''))
        
        # Marcar como modo de edição
        self.editando_leitor_id = leitor_id
        
        # Mudar label do botão para "Atualizar"
        aba_leit.btn_salvar_leitor.SetLabel("Atualizar Leitor")
        
        # Mover foco para o nome
        aba_leit.texto_nome.SetFocus()
        
        # Anunciar ao NVDA
        nome = leitor.get('nome', 'Leitor desconhecido')
        self.frame.atualizar_status(f"Editando leitor: {nome}")
    
    # ========== EVENTOS DOS ATALHOS ==========
    
    def _on_ir_aba_circulacao(self, event):
        """Atalho: Ctrl+1 - Navega para Circulação."""
        self.frame.ir_aba(0)
    
    def _on_ir_aba_cadastro(self, event):
        """Atalho: Ctrl+2 - Navega para Cadastro."""
        self.frame.ir_aba(1)
    
    def _on_ir_aba_leitores(self, event):
        """Atalho: Ctrl+3 - Navega para Leitores."""
        self.frame.ir_aba(2)
    
    def _on_sair(self, event):
        """Atalho: Ctrl+Q - Fecha a aplicação."""
        self.frame.Close()
    
    def executar(self):
        """Inicia o loop da aplicação."""
        # Esta função é chamada quando a aplicação começa
        pass


def main():
    """Função principal que inicia a aplicação."""
    app = wx.App(False)
    controller = DataLivrosController()
    app.MainLoop()


if __name__ == '__main__':
    main()
