# Instruções gerais para o agente de desenvolvimento

As instruções abaixo definem como o agente de IA deve atuar como desenvolvedor neste projeto, do início ao fim de cada task.

## Postura do agente

- Atue como um engenheiro de software sênior: seja criterioso e crítico com a qualidade do código, inclusive o seu próprio.
- Questione requisitos ambíguos, incompletos, mal definidos ou tecnicamente incorretos antes de implementá-los; proponha alternativas tecnicamente melhores quando identificar problemas, em vez de apenas executar o que foi pedido.
- Não implemente silenciosamente uma solução que você considera inadequada — explique o risco ou a limitação e peça confirmação antes de prosseguir.

## Fluxo de trabalho com worktrees e branches

1. Antes de criar qualquer worktree nova, atualize a branch `develop` local com as mudanças do remoto:
   ```bash
   git fetch origin
   git checkout develop
   git pull origin develop
   ```
2. Toda nova task deve ser trabalhada em uma worktree nova, criada sempre a partir da branch `develop` atualizada (nunca a partir de `main` ou de outra branch de trabalho).
3. O nome da branch de trabalho deve seguir obrigatoriamente este formato:
   ```
   <username_do_sistema_operacional>/task/<nome_da_task>
   ```
   Exemplo: se o usuário do SO for `vinic` e a task for "adicionar autenticação de usuário", a branch deve se chamar `vinic/task/adicionar-autenticacao-usuario`.
4. O nome do diretório da worktree também deve referenciar a task (ex.: `../projeto_blog-adicionar-autenticacao-usuario`).
5. Exemplo de comando para criar a worktree e a branch juntas:
   ```bash
   git worktree add ../projeto_blog-<nome_da_task> -b <username>/task/<nome_da_task> develop
   ```
6. Ao finalizar o trabalho da task, **não exclua** a branch nem a worktree criadas. Deixe ambas no sistema, mesmo após merge/PR, para preservar histórico e permitir retomada futura do trabalho.
7. Como podem existir múltiplas worktrees ativas ao mesmo tempo (cada uma com sua própria instância da aplicação rodando para validação/testes), antes de iniciar o servidor (ex.: `python manage.py runserver`) nessa worktree, verifique se a porta padrão (ex.: `8000`) já está em uso e, se estiver, escolha outra porta livre (ex.: `python manage.py runserver 8001`). Nunca assuma que a porta padrão está disponível.

### Autenticação Git (SSH)

Todas as operações Git descritas acima (`fetch`, `pull`, `push`, criação de worktrees/branches, etc.) devem usar **apenas autenticação SSH** neste projeto.

Contexto:

- Usamos chaves SSH protegidas por passphrase.
- Já existe uma chave SSH carregada no `ssh-agent`.
- Estamos usando keychain para gerenciar as chaves SSH.

Como agir:

1. Garanta que o remoto esteja em formato SSH (`git@github.com:owner/repo.git`) antes de qualquer operação.
2. Execute os comandos Git normalmente (`fetch`, `pull`, `push`) via SSH.
3. Se houver falha, informe o erro e verifique a configuração do SSH/agent sem mudar para HTTPS.

Restrições:

- Não trocar o remoto para HTTPS.
- Não solicitar autenticação interativa adicional.
- Não sobrescrever configurações globais ou locais sem necessidade.

## Testes automatizados

- Sempre que uma alteração criar, modificar ou corrigir um comportamento do sistema, crie ou atualize os testes unitários correspondentes.
- Utilize o framework de testes já adotado pelo projeto (ex.: `django.test` / `pytest`), seguindo os padrões e a estrutura de testes já existentes.
- Execute a suíte de testes antes de considerar a task concluída e garanta que todos os testes relevantes estejam passando.
- Não remova ou desative testes existentes sem justificativa explícita e validação do humano responsável.

## Documentação e histórico de tarefas

- Ao finalizar cada task, registre o que foi feito em um arquivo de histórico dedicado na raiz do projeto chamado `HISTORICO_DE_TAREFAS.md` (crie-o caso ainda não exista). Cada entrada deve conter, no mínimo: data, nome da task, branch/worktree utilizada, resumo das mudanças, principais arquivos afetados e testes criados/alterados.
- Atualize a documentação principal do projeto (`README.md` e demais documentos relevantes) sempre que a task alterar comportamento, instruções de uso, dependências ou arquitetura do sistema.

## Boas práticas de desenvolvimento de software

- Escreva código legível, coeso e com responsabilidade única (SRP); prefira funções e classes pequenas e bem nomeadas.
- Evite duplicação de código (DRY) e complexidade desnecessária (KISS, YAGNI).
- Siga rigorosamente os padrões, convenções e estrutura já utilizados pelos frameworks e bibliotecas do projeto (ex.: Django); não introduza padrões alternativos ou bibliotecas concorrentes sem necessidade comprovada.
- Prefira alterações pequenas, revisáveis e incrementais, com commits atômicos e mensagens claras e descritivas.
- Trate erros e casos de borda explicitamente; nunca ignore exceções silenciosamente.
- Nunca faça commit de segredos, credenciais ou dados sensíveis.
- Rode linters e formatadores já configurados no projeto antes de finalizar a task.
- Mantenha as dependências do projeto (`requirements.txt` ou equivalente) atualizadas e documentadas quando alteradas.

## Revisão humana e aprovação

- Ao final de cada task, pare o trabalho e solicite revisão humana das mudanças antes de prosseguir.
- Se o humano aprovar as mudanças, pergunte explicitamente se deve:
  1. Fazer o commit das alterações na branch de trabalho; e, em caso afirmativo,
  2. Abrir um Pull Request no repositório remoto (da branch de trabalho para `develop`).
- Nunca faça commit ou abra Pull Request sem aprovação explícita do humano responsável.
