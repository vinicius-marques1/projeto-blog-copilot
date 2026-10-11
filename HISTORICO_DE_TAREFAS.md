# Histórico de Tarefas

Registro das tarefas realizadas no projeto, para referência futura.

---

## 2026-10-10 — Criar página Home do Blog Green

- **Branch/worktree:** `vinic/task/criar-pagina-home-blog-green`
  (`../projeto_blog-criar-pagina-home-blog-green`), criada a partir de
  `develop`.
- **Resumo das mudanças:**
  - Substituída a página de boas-vindas genérica por uma Home real do
    "Blog Green", com nome do blog em destaque e texto de apresentação:
    "Esse é uma blog para postar coisa legais sobre tecnologia!! Seja bem
    vindo(a)!!".
  - Criado template base (`templates/base.html`) com barra de navegação
    (ícone SVG inline que leva à Home, links para Home, Posts e Sobre Nós) e
    layout clean reaproveitado pelas demais páginas.
  - Criadas páginas placeholder `templates/posts.html` e `templates/sobre.html`.
  - Atualizadas as views (`config/views.py`: `home`, `posts`, `sobre`) e as
    rotas (`config/urls.py`: `''`, `posts/`, `sobre/`), removendo a view/rota
    `welcome` antiga e o template `templates/welcome.html`.
  - Adicionados testes unitários (`config/tests.py`) cobrindo as três views
    (status 200, template usado e conteúdo esperado).
  - Configurado `pytest`/`pytest-django`/`coverage` (`pytest.ini`,
    `requirements-dev.txt`) para rodar a suíte com cobertura.
  - Atualizado `README.md` com a nova descrição do projeto e instruções de
    como rodar os testes/cobertura.
- **Principais arquivos afetados:**
  - `config/views.py`, `config/urls.py`
  - `templates/base.html`, `templates/home.html`, `templates/posts.html`,
    `templates/sobre.html`
  - `templates/welcome.html` (removido)
  - `config/tests.py` (novo)
  - `pytest.ini`, `requirements-dev.txt` (novos)
  - `README.md`, `.gitignore`
- **Testes criados/alterados:**
  - `config/tests.py`: `HomeViewTests`, `PostsViewTests`, `SobreViewTests`
    (10 testes no total, todos passando).
  - Cobertura de 100% em `config/views.py` e `config/urls.py` (arquivos
    alterados nesta tarefa); verificado via
    `pytest --cov=config --cov-report=annotate:cov_annotate`.
