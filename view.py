"""
Módulo View - Interface gráfica com wxPython
Define as classes de interface com acessibilidade para NVDA
"""

import wx
from typing import Callable, Optional


class CirculacaoPanel(wx.Panel):
    """Painel para gerenciamento de circulação de livros (empréstimos e devoluções)."""
    
    def __init__(self, parent):
        super().__init__(parent)
        self.InitUI()
    
    def InitUI(self):
        """Inicializa os componentes da interface."""
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer.Add((0, 10))  # Espaçamento superior
        
        # --- SEÇÃO DE BUSCA DE LIVRO ---
        busca_livro_box = wx.StaticBox(self, label="Busca de Livro para Empréstimo")
        busca_livro_sizer = wx.StaticBoxSizer(busca_livro_box, wx.VERTICAL)
        busca_livro_sizer.Add((0, 5))
        
        # Label e campo de busca de livro
        self.label_busca_livro = wx.StaticText(self, label="ISBN ou Título do Livro:")
        busca_livro_sizer.Add(self.label_busca_livro)
        
        self.texto_busca_livro = wx.TextCtrl(self, name="busca_livro")
        self.texto_busca_livro.SetHelpText("Digite o ISBN ou título do livro")
        busca_livro_sizer.Add(self.texto_busca_livro, flag=wx.EXPAND)
        busca_livro_sizer.Add((0, 5))
        
        # Botão de busca
        self.btn_buscar_livro = wx.Button(self, label="Buscar Livro", name="btn_buscar_livro")
        busca_livro_sizer.Add(self.btn_buscar_livro, flag=wx.EXPAND)
        busca_livro_sizer.Add((0, 10))
        
        main_sizer.Add(busca_livro_sizer, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=10)
        
        # --- SEÇÃO DE SELEÇÃO DE LEITOR ---
        busca_leitor_box = wx.StaticBox(self, label="Seleção de Leitor")
        busca_leitor_sizer = wx.StaticBoxSizer(busca_leitor_box, wx.VERTICAL)
        busca_leitor_sizer.Add((0, 5))
        
        # Label e campo de busca de leitor
        self.label_busca_leitor = wx.StaticText(self, label="Nome do Leitor:")
        busca_leitor_sizer.Add(self.label_busca_leitor)
        
        self.texto_busca_leitor = wx.TextCtrl(self, name="busca_leitor")
        self.texto_busca_leitor.SetHelpText("Digite o nome do leitor")
        busca_leitor_sizer.Add(self.texto_busca_leitor, flag=wx.EXPAND)
        busca_leitor_sizer.Add((0, 5))
        
        # ComboBox de seleção de leitor
        self.label_leitor = wx.StaticText(self, label="Leitor:")
        busca_leitor_sizer.Add(self.label_leitor)
        
        self.combo_leitores = wx.ComboBox(self, choices=[], style=wx.CB_READONLY, name="combo_leitores")
        self.combo_leitores.SetHelpText("Selecione o leitor da lista")
        busca_leitor_sizer.Add(self.combo_leitores, flag=wx.EXPAND)
        busca_leitor_sizer.Add((0, 10))
        
        main_sizer.Add(busca_leitor_sizer, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=10)
        
        # --- SEÇÃO DE AÇÃO ---
        acao_box = wx.StaticBox(self, label="Ações")
        acao_sizer = wx.StaticBoxSizer(acao_box, wx.VERTICAL)
        acao_sizer.Add((0, 5))
        
        # Botões de ação
        btn_sizer = wx.BoxSizer(wx.HORIZONTAL)
        
        self.btn_emprestar = wx.Button(self, label="Registrar Empréstimo", name="btn_emprestar")
        btn_sizer.Add(self.btn_emprestar, proportion=1, flag=wx.EXPAND | wx.RIGHT, border=5)
        
        self.btn_devolver = wx.Button(self, label="Registrar Devolução", name="btn_devolver")
        btn_sizer.Add(self.btn_devolver, proportion=1, flag=wx.EXPAND)
        
        acao_sizer.Add(btn_sizer, flag=wx.EXPAND)
        acao_sizer.Add((0, 10))
        
        main_sizer.Add(acao_sizer, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=10)
        
        # --- SEÇÃO DE EMPRÉSTIMOS ATIVOS ---
        ativos_box = wx.StaticBox(self, label="Empréstimos Ativos")
        ativos_sizer = wx.StaticBoxSizer(ativos_box, wx.VERTICAL)
        ativos_sizer.Add((0, 5))
        
        self.lista_emprestimos = wx.ListBox(self, name="lista_emprestimos")
        self.lista_emprestimos.SetHelpText("Lista de empréstimos ativos")
        ativos_sizer.Add(self.lista_emprestimos, proportion=1, flag=wx.EXPAND)
        ativos_sizer.Add((0, 10))
        
        main_sizer.Add(ativos_sizer, proportion=1, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.BOTTOM, border=10)
        
        self.SetSizer(main_sizer)


class CadastroPanel(wx.Panel):
    """Painel para cadastro de novos livros."""
    
    def __init__(self, parent):
        super().__init__(parent)
        self.InitUI()
    
    def InitUI(self):
        """Inicializa os componentes da interface."""
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer.Add((0, 10))  # Espaçamento superior
        
        # --- SEÇÃO DE BUSCA NA API ---
        busca_api_box = wx.StaticBox(self, label="Buscar Livro na Google Books API")
        busca_api_sizer = wx.StaticBoxSizer(busca_api_box, wx.VERTICAL)
        busca_api_sizer.Add((0, 5))
        
        # Label e campo de busca
        self.label_busca_api = wx.StaticText(self, label="ISBN ou Título:")
        busca_api_sizer.Add(self.label_busca_api)
        
        self.texto_busca_api = wx.TextCtrl(self, name="busca_api")
        self.texto_busca_api.SetHelpText("Digite ISBN ou título para buscar")
        busca_api_sizer.Add(self.texto_busca_api, flag=wx.EXPAND)
        busca_api_sizer.Add((0, 5))
        
        # Botão de busca na API
        self.btn_buscar_api = wx.Button(self, label="Buscar na API", name="btn_buscar_api")
        busca_api_sizer.Add(self.btn_buscar_api, flag=wx.EXPAND)
        busca_api_sizer.Add((0, 10))
        
        # Label para resultados
        self.label_resultados_api = wx.StaticText(self, label="Resultados encontrados (Navegue e selecione para preencher):")
        busca_api_sizer.Add(self.label_resultados_api)
        
        # ListBox de resultados da API
        self.lista_resultados_api = wx.ListBox(self, name="lista_resultados_api")
        self.lista_resultados_api.SetHelpText("Selecione um livro para preencher os campos abaixo")
        busca_api_sizer.Add(self.lista_resultados_api, proportion=1, flag=wx.EXPAND)
        busca_api_sizer.Add((0, 10))
        
        main_sizer.Add(busca_api_sizer, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=10)
        
        # --- SEÇÃO DE DADOS DO LIVRO ---
        dados_box = wx.StaticBox(self, label="Dados do Livro")
        dados_sizer = wx.StaticBoxSizer(dados_box, wx.VERTICAL)
        dados_sizer.Add((0, 5))
        
        # Título
        self.label_titulo = wx.StaticText(self, label="Título:")
        dados_sizer.Add(self.label_titulo)
        self.texto_titulo = wx.TextCtrl(self, name="titulo")
        self.texto_titulo.SetHelpText("Título do livro")
        dados_sizer.Add(self.texto_titulo, flag=wx.EXPAND)
        dados_sizer.Add((0, 5))
        
        # ISBN
        self.label_isbn = wx.StaticText(self, label="ISBN:")
        dados_sizer.Add(self.label_isbn)
        self.texto_isbn = wx.TextCtrl(self, name="isbn")
        self.texto_isbn.SetHelpText("ISBN do livro (apenas números)")
        dados_sizer.Add(self.texto_isbn, flag=wx.EXPAND)
        dados_sizer.Add((0, 5))
        
        # Autores
        self.label_autores = wx.StaticText(self, label="Autores:")
        dados_sizer.Add(self.label_autores)
        self.texto_autores = wx.TextCtrl(self, name="autores")
        self.texto_autores.SetHelpText("Autores separados por vírgula")
        dados_sizer.Add(self.texto_autores, flag=wx.EXPAND)
        dados_sizer.Add((0, 5))
        
        # Editora
        self.label_editora = wx.StaticText(self, label="Editora:")
        dados_sizer.Add(self.label_editora)
        self.texto_editora = wx.TextCtrl(self, name="editora")
        self.texto_editora.SetHelpText("Nome da editora")
        dados_sizer.Add(self.texto_editora, flag=wx.EXPAND)
        dados_sizer.Add((0, 5))
        
        # Ano de Publicação
        self.label_ano = wx.StaticText(self, label="Ano de Publicação:")
        dados_sizer.Add(self.label_ano)
        self.texto_ano = wx.TextCtrl(self, name="ano_publicacao")
        self.texto_ano.SetHelpText("Ano de publicação (AAAA)")
        dados_sizer.Add(self.texto_ano, flag=wx.EXPAND)
        dados_sizer.Add((0, 5))
        
        # Descrição
        self.label_descricao = wx.StaticText(self, label="Descrição:")
        dados_sizer.Add(self.label_descricao)
        self.texto_descricao = wx.TextCtrl(self, style=wx.TE_MULTILINE | wx.TE_WORDWRAP, 
                                           value='', name="descricao")
        self.texto_descricao.SetHelpText("Descrição ou resumo do livro")
        dados_sizer.Add(self.texto_descricao, proportion=1, flag=wx.EXPAND)
        dados_sizer.Add((0, 5))
        
        # Categorias
        self.label_categorias = wx.StaticText(self, label="Categorias:")
        dados_sizer.Add(self.label_categorias)
        self.texto_categorias = wx.TextCtrl(self, name="categorias")
        self.texto_categorias.SetHelpText("Categorias separadas por vírgula")
        dados_sizer.Add(self.texto_categorias, flag=wx.EXPAND)
        dados_sizer.Add((0, 10))
        
        main_sizer.Add(dados_sizer, proportion=1, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=10)
        
        # --- SEÇÃO DE BOTÕES ---
        botoes_sizer = wx.BoxSizer(wx.HORIZONTAL)
        
        self.btn_salvar = wx.Button(self, label="Salvar Livro", name="btn_salvar")
        botoes_sizer.Add(self.btn_salvar, proportion=1, flag=wx.EXPAND | wx.RIGHT, border=5)
        
        self.btn_limpar = wx.Button(self, label="Limpar Campos", name="btn_limpar")
        botoes_sizer.Add(self.btn_limpar, proportion=1, flag=wx.EXPAND)
        
        main_sizer.Add(botoes_sizer, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.BOTTOM, border=10)
        
        self.SetSizer(main_sizer)


class LeitoresPanel(wx.Panel):
    """Painel para gerenciamento de leitores."""
    
    def __init__(self, parent):
        super().__init__(parent)
        self.InitUI()
    
    def InitUI(self):
        """Inicializa os componentes da interface."""
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer.Add((0, 10))  # Espaçamento superior
        
        # --- SEÇÃO DE NOVO LEITOR ---
        novo_leitor_box = wx.StaticBox(self, label="Novo Leitor")
        novo_leitor_sizer = wx.StaticBoxSizer(novo_leitor_box, wx.VERTICAL)
        novo_leitor_sizer.Add((0, 5))
        
        # Nome
        self.label_nome = wx.StaticText(self, label="Nome Completo:")
        novo_leitor_sizer.Add(self.label_nome)
        self.texto_nome = wx.TextCtrl(self, name="nome")
        self.texto_nome.SetHelpText("Nome completo do leitor")
        novo_leitor_sizer.Add(self.texto_nome, flag=wx.EXPAND)
        novo_leitor_sizer.Add((0, 5))
        
        # Email
        self.label_email = wx.StaticText(self, label="Email:")
        novo_leitor_sizer.Add(self.label_email)
        self.texto_email = wx.TextCtrl(self, name="email")
        self.texto_email.SetHelpText("Email do leitor")
        novo_leitor_sizer.Add(self.texto_email, flag=wx.EXPAND)
        novo_leitor_sizer.Add((0, 5))
        
        # Telefone
        self.label_telefone = wx.StaticText(self, label="Telefone:")
        novo_leitor_sizer.Add(self.label_telefone)
        self.texto_telefone = wx.TextCtrl(self, name="telefone")
        self.texto_telefone.SetHelpText("Telefone do leitor com DDD")
        novo_leitor_sizer.Add(self.texto_telefone, flag=wx.EXPAND)
        novo_leitor_sizer.Add((0, 5))
        
        # Endereço
        self.label_endereco = wx.StaticText(self, label="Endereço:")
        novo_leitor_sizer.Add(self.label_endereco)
        self.texto_endereco = wx.TextCtrl(self, name="endereco")
        self.texto_endereco.SetHelpText("Endereço completo do leitor")
        novo_leitor_sizer.Add(self.texto_endereco, flag=wx.EXPAND)
        novo_leitor_sizer.Add((0, 10))
        
        # Botão salvar leitor
        self.btn_salvar_leitor = wx.Button(self, label="Salvar Leitor", name="btn_salvar_leitor")
        novo_leitor_sizer.Add(self.btn_salvar_leitor, flag=wx.EXPAND)
        novo_leitor_sizer.Add((0, 10))
        
        main_sizer.Add(novo_leitor_sizer, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=10)
        
        # --- SEÇÃO DE LISTA DE LEITORES ---
        lista_box = wx.StaticBox(self, label="Leitores Cadastrados")
        lista_sizer = wx.StaticBoxSizer(lista_box, wx.VERTICAL)
        lista_sizer.Add((0, 5))
        
        # Campo de busca
        self.label_busca_leitor = wx.StaticText(self, label="Buscar leitor:")
        lista_sizer.Add(self.label_busca_leitor)
        
        self.texto_busca_leitor_list = wx.TextCtrl(self, name="busca_leitor_list")
        self.texto_busca_leitor_list.SetHelpText("Digite para filtrar leitores")
        lista_sizer.Add(self.texto_busca_leitor_list, flag=wx.EXPAND)
        lista_sizer.Add((0, 5))
        
        # Lista de leitores
        self.lista_leitores = wx.ListBox(self, name="lista_leitores")
        self.lista_leitores.SetHelpText("Lista de leitores cadastrados")
        lista_sizer.Add(self.lista_leitores, proportion=1, flag=wx.EXPAND)
        lista_sizer.Add((0, 5))
        
        # Botão de detalhes
        self.btn_detalhes_leitor = wx.Button(self, label="Ver Detalhes", name="btn_detalhes_leitor")
        lista_sizer.Add(self.btn_detalhes_leitor, flag=wx.EXPAND)
        lista_sizer.Add((0, 10))
        
        main_sizer.Add(lista_sizer, proportion=1, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.BOTTOM, border=10)
        
        self.SetSizer(main_sizer)


class MainFrame(wx.Frame):
    """Frame principal da aplicação com abas de navegação."""
    
    def __init__(self):
        super().__init__(parent=None, title='DataLivros - Sistema de Gestão de Sala de Leitura', 
                         size=(800, 600))
        
        self.InitUI()
        self.Centre()
        self.Show()
    
    def InitUI(self):
        """Inicializa a interface principal."""
        # Criar painel principal
        panel_principal = wx.Panel(self)
        sizer_principal = wx.BoxSizer(wx.VERTICAL)
        
        # Criar notebook (abas)
        self.notebook = wx.Notebook(panel_principal)
        
        # Criar painéis das abas
        self.aba_circulacao = CirculacaoPanel(self.notebook)
        self.aba_cadastro = CadastroPanel(self.notebook)
        self.aba_leitores = LeitoresPanel(self.notebook)
        
        # Adicionar abas ao notebook
        self.notebook.AddPage(self.aba_circulacao, "Circulação")
        self.notebook.AddPage(self.aba_cadastro, "Cadastro de Livros")
        self.notebook.AddPage(self.aba_leitores, "Leitores")
        
        sizer_principal.Add(self.notebook, proportion=1, flag=wx.EXPAND)
        panel_principal.SetSizer(sizer_principal)
        
        # Criar StatusBar para feedback
        self.CreateStatusBar()
        self.SetStatusText("Pronto para uso. Acesse Ctrl+1 para Circulação, Ctrl+2 para Cadastro, Ctrl+3 para Leitores")
        
        # Configurar AcceleratorTable para atalhos
        self._config_atalhos()
    
    def _config_atalhos(self):
        """Configura os atalhos de teclado."""
        # Criar IDs únicos para cada atalho
        self.id_aba_circulacao = wx.NewIdRef()
        self.id_aba_cadastro = wx.NewIdRef()
        self.id_aba_leitores = wx.NewIdRef()
        
        acel_entries = [
            (wx.ACCEL_CTRL, ord('1'), self.id_aba_circulacao),
            (wx.ACCEL_CTRL, ord('2'), self.id_aba_cadastro),
            (wx.ACCEL_CTRL, ord('3'), self.id_aba_leitores),
            (wx.ACCEL_CTRL, ord('S'), wx.ID_SAVE),
            (wx.ACCEL_CTRL, ord('Q'), wx.ID_EXIT),
        ]
        
        accel_table = wx.AcceleratorTable(acel_entries)
        self.SetAcceleratorTable(accel_table)
    
    def atualizar_status(self, mensagem: str):
        """
        Atualiza a mensagem na StatusBar e a reproduz via acessibilidade.
        
        Args:
            mensagem: Texto a ser exibido na StatusBar
        """
        self.SetStatusText(mensagem)
        # O NVDA lerá automaticamente a StatusBar quando ela for atualizada
    
    def get_aba_circulacao(self) -> CirculacaoPanel:
        """Retorna a aba de circulação."""
        return self.aba_circulacao
    
    def get_aba_cadastro(self) -> CadastroPanel:
        """Retorna a aba de cadastro."""
        return self.aba_cadastro
    
    def get_aba_leitores(self) -> LeitoresPanel:
        """Retorna a aba de leitores."""
        return self.aba_leitores
    
    def ir_aba(self, indice: int):
        """
        Navega para uma aba específica.
        
        Args:
            indice: Índice da aba (0, 1, ou 2)
        """
        if 0 <= indice < self.notebook.GetPageCount():
            self.notebook.SetSelection(indice)
            nomes_abas = ["Circulação", "Cadastro de Livros", "Leitores"]
            self.atualizar_status(f"Navegando para aba: {nomes_abas[indice]}")
    
    def vincular_evento(self, controle: wx.Window, evento: str, handler: Callable):
        """
        Vincula um handler a um evento de um controle.
        
        Args:
            controle: Controle wxPython
            evento: Tipo de evento (ex: wx.EVT_BUTTON)
            handler: Função a ser executada
        """
        controle.Bind(evento, handler)


if __name__ == '__main__':
    app = wx.App(False)
    frame = MainFrame()
    app.MainLoop()
