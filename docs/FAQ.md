# ❓ FAQ - Perguntas Frequentes

Respostas para as perguntas mais comuns sobre DataLivros.

## 🚀 Instalação e Execução

### P: Como instalar DataLivros?
R: 
```bash
git clone https://github.com/usuario/datalivros.git
cd datalivros
python -m venv venv
venv\Scripts\activate  # Windows ou source venv/bin/activate no Linux
pip install -r requirements.txt
python main.py
```

### P: Qual versão de Python é necessária?
R: Python 3.8 ou superior. Testado em Python 3.10 e 3.11.

### P: Pode usar em macOS?
R: wxPython tem suporte limitado em macOS. A interface funciona, mas NVDA não está disponível naquela plataforma.

### P: Funciona em Linux?
R: Sim, funciona em Linux com NVDA via Wine ou NVDA nativo (em desenvolvimento).

### P: Posso usar em um Raspberry Pi?
R: Não recomendado. wxPython é heavy e o Pi pode ficar lento.

## 🔐 Banco de Dados

### P: Onde fica o arquivo do banco de dados?
R: Em `datalibros.db` no diretório raiz da aplicação (configurável em `main.py`).

### P: Posso compartilhar o banco entre vários usuários?
R: Não recomendado com SQLite3. Use PostgreSQL para múltiplos usuários simultâneos.

### P: Como fazer backup do banco?
R: 
```bash
copy datalibros.db datalibros_backup.db
```
Ou use o módulo `shutil`:
```python
import shutil
shutil.copy('datalibros.db', 'datalibros_backup.db')
```

### P: Posso restaurar de um backup?
R: Sim, copie o arquivo de backup sobre o original:
```bash
copy datalibros_backup.db datalibros.db
```

### P: Posso excluir um livro?
R: Sim, via código ou interface (futuro). Cuidado: remove empréstimos relacionados.

### P: Posso desativar um leitor sem excluir?
R: Sim, use o campo `ativo = 0` (soft delete). Veja `docs/DATABASE.md`.

## 🌐 Integração com Google Books API

### P: Preciso de API Key?
R: Não obrigatoriamente. Free tier permite 1000 requisições/dia. Se precisar mais, registre em [Google Cloud Console](https://console.cloud.google.com/).

### P: Como usar API Key?
R: Edite `api_service.py` e adicione:
```python
API_KEY = 'sua_chave_aqui'
params['key'] = API_KEY
```

### P: E se a internet cair?
R: Livros já cadastrados funcionam offline. Novas buscas na API falharão com mensagem clara.

### P: A API retorna capa do livro?
R: Sim, mas não é exibida (design de acessibilidade). URL está em `resultado['thumbnail']`.

### P: Posso integrar outra fonte de dados?
R: Sim! Copie `api_service.py`, crie `api_service_alternativo.py`, implemente `buscar_livro()` e integre em `main.py`.

### P: Qual é o timeout da API?
R: 10 segundos configurável em `api_service.py` (parâmetro `timeout=10`).

## ♿ Acessibilidade

### P: Funciona com NVDA?
R: Totalmente! Desenvolvido para NVDA.

### P: E com JAWS?
R: Compatível, mas com testes limitados. Reporte problemas.

### P: E com Narrator (Windows)?
R: Funcionalidade básica, mas não ideal. Use NVDA.

### P: Posso usar sem leitor de tela?
R: Sim, é uma aplicação gráfica normal. Mas foi otimizada para NVDA.

### P: Quais são os atalhos de teclado?
R: Veja tabela em `README.md`:
- Ctrl+1/2/3 = Trocar abas
- Ctrl+S = Salvar
- Ctrl+Q = Sair

### P: Como navegar com NVDA?
R: Use Tab/Shift+Tab para navegar, Enter para ativar, Seta para expandir listas.

### P: Qual é a conformidade WCAG?
R: WCAG 2.1 Nível A completo. Veja `docs/ACESSIBILIDADE.md` para detalhes.

## 🐛 Problemas Comuns

### P: "ModuleNotFoundError: No module named 'wx'"
R: Instale wxPython:
```bash
pip install wxPython
```

### P: "Database is locked"
R: Aumentar timeout em `database.py`:
```python
conn = sqlite3.connect('datalibros.db', timeout=10)
```

### P: NVDA não anuncia ações
R: Verifique se StatusBar está sendo atualizada:
```python
self.frame.atualizar_status("Sua mensagem aqui")
```

### P: Aplicação trava ao buscar API
R: Use `wx.Yield()` para permitir processamento:
```python
wx.Yield()  # Permite NVDA processar
resultado = buscar_livro_google_books(...)
```

### P: Botão não funciona
R: Verifique se está vinculado ao evento em `main.py`:
```python
self.frame.vincular_evento(botao, wx.EVT_BUTTON, self._on_handler)
```

### P: Caracteres acentuados aparecem errados
R: Garanta encoding UTF-8 no início do arquivo Python:
```python
# -*- coding: utf-8 -*-
```

## 🔄 Atualização e Migração

### P: Como atualizar para nova versão?
R: 
```bash
git pull origin main
pip install -r requirements.txt  # Se dependências mudaram
python main.py
```

### P: Banco é compatível com novas versões?
R: Sim, schema é compatível para trás. Migrações automáticas quando necessário.

### P: Posso migrar de SQLite para PostgreSQL?
R: Sim, mas requer trabalho manual. Veja `docs/DATABASE.md` para migração.

## 💾 Performance e Otimização

### P: App está lenta
R: Verifique:
1. Número de empréstimos (listar ativo demora com muitos)
2. NVDA consumindo CPU
3. Disco cheio ou muito fragmentado

Soluções:
```python
# Otimizar banco
db.cursor.execute('VACUUM;')
db.cursor.execute('ANALYZE;')
```

### P: API está lenta
R: Requer ~2s primeira vez. Requisições subsequentes são ~500ms.

Solução (futuro): Implementar cache em memória ou Redis.

### P: Posso usar múltiplas instâncias simultaneamente?
R: Não recomendado com SQLite3. Use PostgreSQL para isso.

## 🎓 Desenvolvimento e Contribuição

### P: Como contribuir?
R: Veja `docs/CONTRIBUINDO.md` para detalhes completos.

### P: Como adicionar nova feature?
R: 
1. Fork repositório
2. Crie branch: `git checkout -b feature/nome`
3. Implemente e teste
4. Abra Pull Request

### P: Posso usar DataLivros em projeto comercial?
R: Sim, está sob licença MIT. Veja `LICENSE`.

### P: Como reportar bug?
R: Abra [Issue no GitHub](https://github.com/usuario/datalivros/issues) com detalhes.

### P: Há roadmap de features?
R: Sim, veja seção "🔮 Roadmap" em `README.md`.

## 🤔 Conceitual

### P: Por que wxPython e não Tkinter?
R: wxPython é muito mais acessível para NVDA. Tkinter tem suporte limitado.

### P: Por que SQLite3 e não PostgreSQL?
R: SQLite3 é simples, sem servidor. PostgreSQL é futuro para múltiplos usuários.

### P: Por que Google Books API?
R: Massivo banco de dados, sem manutenção, gratuito (com limites).

### P: Pode funcionar offline?
R: Sim, parcialmente. Livros já cadastrados funcionam. Novas buscas na API não.

### P: Dados são armazenados em nuvem?
R: Não, tudo é local no `datalibros.db`. Privacidade garantida.

### P: Como dados são sincronizados entre computadores?
R: Não há sincronização automática. Use Dropbox/OneDrive/Git para compartilhar arquivo.

## 📞 Suporte Técnico

### P: Aonde reportar bug?
R: [Issues no GitHub](https://github.com/usuario/datalivros/issues)

### P: Como pedir uma feature?
R: [Discussions no GitHub](https://github.com/usuario/datalivros/discussions)

### P: Há comunidade ou fórum?
R: Use Issues/Discussions no repositório GitHub.

### P: Como reportar um bug ou sugerir melhorias?
R: Abra uma Issue no repositório GitHub com detalhes claros.

## 🔗 Recursos Úteis

- [wxPython Docs](https://docs.wxpython.org/)
- [Google Books API](https://developers.google.com/books)
- [SQLite Documentation](https://www.sqlite.org/docs.html)
- [NVDA Documentation](https://www.nvaccess.org/documentation/)
- [WCAG 2.1 Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)

---

**Não encontrou sua pergunta? [Abra uma Discussion!](https://github.com/usuario/datalivros/discussions)**

