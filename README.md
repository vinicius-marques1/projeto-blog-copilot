# projeto-blog-copilot

Aplicativo Django do **Blog Green**, com página inicial, navegação para Posts
e Sobre Nós.

## Como executar

1. Crie e ative um ambiente virtual (opcional, mas recomendado).
2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Aplique as migrações:

```bash
python manage.py migrate
```

4. Inicie o servidor:

```bash
python manage.py runserver
```

5. Acesse `http://127.0.0.1:8000/` para ver a Home do Blog Green. As páginas
   `/posts/` e `/sobre/` são acessíveis pela barra de navegação.

## Testes

1. Instale as dependências de desenvolvimento (inclui `pytest`, `pytest-django`
   e `coverage`):

```bash
pip install -r requirements-dev.txt
```

2. Rode a suíte de testes:

```bash
pytest
```

3. Para gerar um relatório de cobertura:

```bash
pytest --cov=config --cov-report=term-missing
```
