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
        self.btn_buscar_livro.SetHelpText("Busca livros disponíveis no banco de dados")
        busca_livro_sizer.Add(self.btn_buscar_livro, flag=wx.EXPAND)
        busca_livro_sizer.Add((0, 10))
        
        # Label para lista de resultados
        self.label_resultados_livro = wx.StaticText(self, label="Resultados da Busca:")
        busca_livro_sizer.Add(self.label_resultados_livro)
        
        # ListBox para resultados de busca de livros
        self.lista_resultados_livro = wx.ListBox(self, name="lista_resultados_livro")
        self.lista_resultados_livro.SetHelpText("Resultados da busca de livros, use as setas para selecionar")
        busca_livro_sizer.Add(self.lista_resultados_livro, proportion=1, flag=wx.EXPAND)
        busca_livro_sizer.Add((0, 10))
        
        main_sizer.Add(busca_livro_sizer, proportion=1, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=10)
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
        self.btn_emprestar.SetHelpText("Registra um novo empréstimo de um livro para um leitor")
        btn_sizer.Add(self.btn_emprestar, proportion=1, flag=wx.EXPAND | wx.RIGHT, border=5)
        
        self.btn_devolver = wx.Button(self, label="Registrar Devolução", name="btn_devolver")
        self.btn_devolver.SetHelpText("Registra a devolução de um livro emprestado")
        btn_sizer.Add(self.btn_devolver, proportion=1, flag=wx.EXPAND)
        
        acao_sizer.Add(btn_sizer, flag=wx.EXPAND)
        acao_sizer.Add((0, 10))
        
        main_sizer.Add(acao_sizer, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=10)
        
        # --- SEÇÃO DE EMPRÉSTIMOS ATIVOS ---
        ativos_box = wx.StaticBox(self, label="Empréstimos Ativos")
        ativos_sizer = wx.StaticBoxSizer(ativos_box, wx.VERTICAL)
        ativos_sizer.Add((0, 5))
        
        # ListCtrl em modo Report (tabela) para empréstimos
        self.lista_emprestimos = wx.ListCtrl(self, style=wx.LC_REPORT | wx.LC_SINGLE_SEL, 
                                             name="lista_emprestimos")
        self.lista_emprestimos.SetHelpText("Lista de empréstimos ativos. Use as setas para navegar.")
        
        # Adicionar colunas (ID armazenado internamente via SetItemData, não exibido)
        self.lista_emprestimos.AppendColumn("Livro", width=170)
        self.lista_emprestimos.AppendColumn("Leitor", width=140)
        self.lista_emprestimos.AppendColumn("Data Empréstimo", width=130)
        self.lista_emprestimos.AppendColumn("Data Devolução Prevista", width=160)
        self.lista_emprestimos.AppendColumn("Status", width=100)
        
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
        self.btn_buscar_api.SetHelpText("Busca livros na Google Books API")
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
        dados_sizer.Add((0, 5))
        
        # Quantidade Total
        self.label_quantidade = wx.StaticText(self, label="Quantidade:")
        dados_sizer.Add(self.label_quantidade)
        self.texto_quantidade = wx.SpinCtrl(self, value='1', min=1, max=1000, name="quantidade_total")
        self.texto_quantidade.SetHelpText("Quantidade total de exemplares (padrão 1)")
        dados_sizer.Add(self.texto_quantidade, flag=wx.EXPAND)
        dados_sizer.Add((0, 10))
        
        main_sizer.Add(dados_sizer, proportion=1, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=10)
        
        # --- SEÇÃO DE BOTÕES ---
        botoes_sizer = wx.BoxSizer(wx.HORIZONTAL)
        
        self.btn_salvar = wx.Button(self, label="Salvar Livro", name="btn_salvar")
        self.btn_salvar.SetHelpText("Salva um novo livro ou atualiza o livro selecionado")
        botoes_sizer.Add(self.btn_salvar, proportion=1, flag=wx.EXPAND | wx.RIGHT, border=5)
        
        self.btn_editar = wx.Button(self, label="Editar Selecionado", name="btn_editar")
        self.btn_editar.SetHelpText("Carrega o livro selecionado para edição")
        botoes_sizer.Add(self.btn_editar, proportion=1, flag=wx.EXPAND | wx.RIGHT, border=5)
        
        self.btn_limpar = wx.Button(self, label="Limpar Campos", name="btn_limpar")
        self.btn_limpar.SetHelpText("Limpa todos os campos e cancela edição")
        botoes_sizer.Add(self.btn_limpar, proportion=1, flag=wx.EXPAND)
        
        main_sizer.Add(botoes_sizer, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.BOTTOM, border=10)
        
        self.SetSizer(main_sizer)


class CatalogoPanel(wx.Panel):
    """Painel para visualização e gerenciamento do catálogo de livros."""
    
    def __init__(self, parent):
        super().__init__(parent)
        self.InitUI()
    
    def InitUI(self):
        """Inicializa os componentes da interface."""
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer.Add((0, 10))  # Espaçamento superior
        
        # --- SEÇÃO DE BUSCA ---
        busca_box = wx.StaticBox(self, label="Busca de Livros")
        busca_sizer = wx.StaticBoxSizer(busca_box, wx.VERTICAL)
        busca_sizer.Add((0, 5))
        
        # Label e campo de busca
        self.label_busca_catalogo = wx.StaticText(self, label="Buscar por Título ou ISBN:")
        busca_sizer.Add(self.label_busca_catalogo)
        
        self.texto_busca_catalogo = wx.TextCtrl(self, name="busca_catalogo")
        self.texto_busca_catalogo.SetHelpText("Digite título ou ISBN para filtrar livros")
        busca_sizer.Add(self.texto_busca_catalogo, flag=wx.EXPAND)
        busca_sizer.Add((0, 10))
        
        main_sizer.Add(busca_sizer, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=10)
        
        # --- SEÇÃO DE LISTA DE LIVROS ---
        lista_box = wx.StaticBox(self, label="Catálogo de Livros")
        lista_sizer = wx.StaticBoxSizer(lista_box, wx.VERTICAL)
        lista_sizer.Add((0, 5))
        
        # ListCtrl em modo Report (tabela)
        self.lista_catalogo = wx.ListCtrl(self, style=wx.LC_REPORT | wx.LC_SINGLE_SEL, 
                                          name="lista_catalogo")
        self.lista_catalogo.SetHelpText("Lista de todos os livros cadastrados. Use as setas para navegar.")
        
        # Adicionar colunas (ID armazenado internamente via SetItemData, não exibido)
        self.lista_catalogo.AppendColumn("Título", width=220)
        self.lista_catalogo.AppendColumn("Autor", width=160)
        self.lista_catalogo.AppendColumn("ISBN", width=110)
        self.lista_catalogo.AppendColumn("Editora", width=130)
        self.lista_catalogo.AppendColumn("Quantidade", width=90)
        
        lista_sizer.Add(self.lista_catalogo, proportion=1, flag=wx.EXPAND)
        lista_sizer.Add((0, 10))
        
        # --- SEÇÃO DE BOTÕES DE AÇÃO ---
        botoes_sizer = wx.BoxSizer(wx.HORIZONTAL)
        
        self.btn_editar_catalogo = wx.Button(self, label="Editar Quantidade", 
                                             name="btn_editar_catalogo")
        self.btn_editar_catalogo.SetHelpText("Edita a quantidade do livro selecionado")
        botoes_sizer.Add(self.btn_editar_catalogo, proportion=1, flag=wx.EXPAND | wx.RIGHT, border=5)
        
        self.btn_editar_detalhes = wx.Button(self, label="Editar Detalhes", 
                                             name="btn_editar_detalhes")
        self.btn_editar_detalhes.SetHelpText("Edita todos os dados do livro selecionado")
        botoes_sizer.Add(self.btn_editar_detalhes, proportion=1, flag=wx.EXPAND | wx.RIGHT, border=5)
        
        self.btn_deletar_catalogo = wx.Button(self, label="Deletar Livro", 
                                              name="btn_deletar_catalogo")
        self.btn_deletar_catalogo.SetHelpText("Deleta o livro selecionado do banco de dados")
        botoes_sizer.Add(self.btn_deletar_catalogo, proportion=1, flag=wx.EXPAND)
        
        lista_sizer.Add(botoes_sizer, flag=wx.EXPAND)
        lista_sizer.Add((0, 10))
        
        main_sizer.Add(lista_sizer, proportion=1, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.BOTTOM, border=10)
        
        self.SetSizer(main_sizer)
    
    def adicionar_livro_lista(self, livro_id: int, isbn: str, titulo: str, 
                             autores: str, editora: str, quantidade: int):
        """
        Adiciona um livro à lista do catálogo.
        
        Args:
            livro_id: ID do livro
            isbn: ISBN do livro
            titulo: Título do livro
            autores: Autores do livro
            editora: Editora do livro
            quantidade: Quantidade de exemplares
        """
        indice = self.lista_catalogo.InsertItem(self.lista_catalogo.GetItemCount(), titulo)
        self.lista_catalogo.SetItem(indice, 1, autores or "")
        self.lista_catalogo.SetItem(indice, 2, isbn or "")
        self.lista_catalogo.SetItem(indice, 3, editora or "")
        self.lista_catalogo.SetItem(indice, 4, str(quantidade))
        self.lista_catalogo.SetItemData(indice, livro_id)  # Armazenar ID para referência
    
    def limpar_lista(self):
        """Limpa a lista de livros."""
        self.lista_catalogo.DeleteAllItems()
    
    def obter_livro_selecionado(self) -> Optional[int]:
        """
        Obtém o ID do livro selecionado.
        
        Returns:
            ID do livro ou None se nenhum estiver selecionado
        """
        indice = self.lista_catalogo.GetFirstSelected()
        if indice != -1:
            return self.lista_catalogo.GetItemData(indice)
        return None
    
    def remover_livro_selecionado(self):
        """Remove o livro selecionado da lista."""
        indice = self.lista_catalogo.GetFirstSelected()
        if indice != -1:
            self.lista_catalogo.DeleteItem(indice)


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
        
        # Turma
        self.label_turma = wx.StaticText(self, label="Turma:")
        novo_leitor_sizer.Add(self.label_turma)
        self.texto_turma = wx.TextCtrl(self, name="turma")
        self.texto_turma.SetHelpText("Turma do leitor (opcional)")
        novo_leitor_sizer.Add(self.texto_turma, flag=wx.EXPAND)
        novo_leitor_sizer.Add((0, 10))
        
        # Botão salvar leitor
        self.btn_salvar_leitor = wx.Button(self, label="Salvar Leitor", name="btn_salvar_leitor")
        self.btn_salvar_leitor.SetHelpText("Salva um novo leitor ou atualiza o leitor selecionado")
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
        
        # Botões de ação
        botoes_leitores_sizer = wx.BoxSizer(wx.HORIZONTAL)
        
        self.btn_editar_leitor = wx.Button(self, label="Editar Selecionado", name="btn_editar_leitor")
        self.btn_editar_leitor.SetHelpText("Carrega o leitor selecionado para edição")
        botoes_leitores_sizer.Add(self.btn_editar_leitor, proportion=1, flag=wx.EXPAND | wx.RIGHT, border=5)
        
        self.btn_detalhes_leitor = wx.Button(self, label="Ver Detalhes", name="btn_detalhes_leitor")
        self.btn_detalhes_leitor.SetHelpText("Exibe detalhes completos do leitor selecionado")
        botoes_leitores_sizer.Add(self.btn_detalhes_leitor, proportion=1, flag=wx.EXPAND)
        
        lista_sizer.Add(botoes_leitores_sizer, flag=wx.EXPAND)
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
        self.aba_catalogo = CatalogoPanel(self.notebook)
        self.aba_leitores = LeitoresPanel(self.notebook)
        
        # Adicionar abas ao notebook
        self.notebook.AddPage(self.aba_circulacao, "Circulação")
        self.notebook.AddPage(self.aba_cadastro, "Cadastro de Livros")
        self.notebook.AddPage(self.aba_catalogo, "Catálogo")
        self.notebook.AddPage(self.aba_leitores, "Leitores")
        
        sizer_principal.Add(self.notebook, proportion=1, flag=wx.EXPAND)
        panel_principal.SetSizer(sizer_principal)
        
        # Criar StatusBar para feedback
        self.CreateStatusBar()
        self.SetStatusText("Pronto para uso. Acesse Ctrl+1 para Circulação, Ctrl+2 para Cadastro, Ctrl+3 para Catálogo, Ctrl+4 para Leitores")
        
        # Configurar AcceleratorTable para atalhos
        self._config_atalhos()
    
    def _config_atalhos(self):
        """Configura os atalhos de teclado."""
        # Criar IDs únicos para cada atalho
        self.id_aba_circulacao = wx.NewIdRef()
        self.id_aba_cadastro = wx.NewIdRef()
        self.id_aba_catalogo = wx.NewIdRef()
        self.id_aba_leitores = wx.NewIdRef()
        
        acel_entries = [
            (wx.ACCEL_CTRL, ord('1'), self.id_aba_circulacao),
            (wx.ACCEL_CTRL, ord('2'), self.id_aba_cadastro),
            (wx.ACCEL_CTRL, ord('3'), self.id_aba_catalogo),
            (wx.ACCEL_CTRL, ord('4'), self.id_aba_leitores),
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
    
    def bind_evento_cambio_aba(self, handler):
        """
        Vincula um handler ao evento de mudança de aba.
        
        Args:
            handler: Função a chamar quando a aba mudar
        """
        self.notebook.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED, handler)
    
    def get_aba_circulacao(self) -> CirculacaoPanel:
        """Retorna a aba de circulação."""
        return self.aba_circulacao
    
    def get_aba_cadastro(self) -> CadastroPanel:
        """Retorna a aba de cadastro."""
        return self.aba_cadastro
    
    def get_aba_catalogo(self) -> CatalogoPanel:
        """Retorna a aba de catálogo."""
        return self.aba_catalogo
    
    def get_aba_leitores(self) -> LeitoresPanel:
        """Retorna a aba de leitores."""
        return self.aba_leitores
    
    def ir_aba(self, indice: int):
        """
        Navega para uma aba específica.
        
        Args:
            indice: Índice da aba (0, 1, 2, ou 3)
        """
        if 0 <= indice < self.notebook.GetPageCount():
            self.notebook.SetSelection(indice)
            nomes_abas = ["Circulação", "Cadastro de Livros", "Catálogo", "Leitores"]
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
