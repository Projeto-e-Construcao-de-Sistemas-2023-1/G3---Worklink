# G3---Worklink

## Minimundo
WorkLink é uma plataforma para empresas e desenvolvedores freelancers, onde empresas postam trabalhos que precisam ser feitos e desenvolvedores se candidatam a esses trabalhos. Tais desenvolvedores trabalham de forma independente, oferecendo seus serviços de desenvolvimento a empresas em troca de remuneração acordada entre as partes. 

Na plataforma, as empresas se cadastram com nome e CNPJ e criam seus perfis, destacando sua área de negócio e projetos em aberto, que contam com suas especificações, como hashtags, prazos, requisitos técnicos e orçamento disponível. Os desenvolvedores, por sua vez, cadastram-se com nome, CPF, email, telefone e data de nascimento e criam seus próprios perfis, destacando suas habilidades através de hashtags que eles marcam em seu perfil (como java, front-end, full-stack, etc.), experiência no ramo e projetos feitos, para que as empresas possam encontrar o talento certo para o trabalho. Nesse sentido, empresas podem seguir desenvolvedores e vice-versa.

 Além dos perfis, a plataforma conta com um feed geral para navegação dos desenvolvedores de projetos de empresas que eles seguem, onde eles podem ver trabalhos requisitados em tempo real. Assim que os trabalhos são postados pelas empresas, os desenvolvedores podem se candidatar aos trabalhos que acham que se encaixam em suas habilidades e experiência se eles possuírem uma tag em comum com as hashtags do projeto. As empresas podem então revisar as inscrições e escolher o freelancer que melhor se adequa às suas necessidades.

O feed geral também conta com filtros, para ajudar os desenvolvedores a encontrar o trabalho que desejam.

 Além disso, a plataforma inclui ferramentas para pagamentos online com integração com Mercado Pago (ou outra API), permitindo que as empresas gerenciem e paguem seus desenvolvedores através da plataforma, e estes acumulem dinheiro na carteira de seu perfil, possibilitando um futuro saque.

 Para as empresas, a plataforma conta com uma seção de gerenciamento de projetos, na qual é possível observar projetos a fazer, projetos em andamento e projetos concluídos, com informações pertinentes ao projeto e desenvolvedores envolvidos.

 Assim que um desenvolvedor é alocado em um projeto, reuniões esporádicas são adicionadas a um calendário do desenvolvedor com integração com Google Calendar, onde atualizações regulares são feitas com o cliente para garantir que o projeto esteja em andamento de acordo com as expectativas. Dessa forma, as empresas encontram os talentos que precisam para realizar trabalhos desejados enquanto os freelancers encontram oportunidades de trabalho temporárias para ganhar um dinheiro extra.
 
 ## Requisitos
 
 ### Funcionais
 
| ID | Descrição |
| --- | --- |
| RF01 | O sistema deve permitir cadastro de empresas, com razão social, CNPJ, e-mail, telefone e senha. |
| RF02 | O sistema deve permitir cadastro de desenvolvedores, com nome, CPF, data de nascimento, telefone, e-mail e senha. |
| RF03 | O sistema deve permitir login de usuário mediante e-mail e senha cadastrados. |
| RF04 | O sistema deve permitir manter usuário. |
| RF05 | O sistema deve permitir que empresas publiquem projetos que estão em andamento ou que precisam ser iniciados em um feed geral, definindo prazos, requisitos técnicos e orçamento disponível. |
| RF06 | O sistema deve permitir a exibição no perfil dos desenvolvedores em quais projetos eles estão atualmente trabalhando. |
| RF07 | O sistema deve permitir que os desenvolvedores escolham hashtags que mostrem quais são suas proficiências e área de atuação, além de um campo de descrição nas páginas dos usuários em que eles podem escrever. |
| RF08 | O sistema deve permitir aos desenvolvedores seguirem empresas e vice-versa. |
| RF09 | O sistema deve permitir a candidaturas de desenvolvedores a projetos de empresas. |
| RF10 | O sistema deve permitir que as empresas aceitem desenvolvedores para seus projetos. |
| RF11 | O sistema deve apresentar um feed geral para os desenvolvedores com os projetos apresentados pelas empresas. |
| RF12 | O sistema deve permitir que o desenvolvedor filtre os projetos apresentados no feed geral pelas hashtags, ou mostrar apenas projetos publicados por empresas que ele segue. |
| RF13 | O sistema deve permitir à empresa inserir dinheiro em sua própria carteira virtual. |
| RF14 | O sistema deve permitir a transação de fundos entre empresa e desenvolvedor. |
| RF15 | O sistema deve permitir marcar reuniões em calendário para conversas entre empresas e desenvolvedores. |
| RF16 | O sistema deve permitir que usuários pesquisem uns aos outros. |

 ### Não-Funcionais
 
| ID | Tipo |Descrição |
| --- | --- | --- |
| RNF1 | Segurança | O sistema deve ter um reCAPTCHA no login de usuário. |
| RNF2 | Compatibilidade | O sistema deve ser compatível com as versões atualizadas do Google Chrome. |
| RNF3 | Compatibilidade | Verificação de CPF/CEP.  |

## Regras de Negócio

| ID | Descrição |
| --- | --- |
| RN1 | Um desenvolvedor deve ter, no mínimo, 1 tag em comum com o projeto para poder se candidatar à ele. |
| RN2 | Um Usuário só pode acessar o sistema mediante cadastro. |
| RN3 | Uma empresa só poderá contratar desenvolvedores se possuir um valor na carteira maior ou igual ao valor a ser pago pelo projeto. |
| RN4 | A empresa não poderá deletar o projeto após estar "Em Desenvolvimento". |
| RN5 | O usuário não pode alterar CPF ou CNPJ após o cadastro. |
| RN6 | O usuário não poderá deletar a conta caso tenha projetos ativos. |
| RN7 | Somente empresas podem realizar criação de projetos. |
| RN8 | Uma empresa não poderá editar o projeto caso algum desenvolvedor tenha se candidatado. |

## Casos de Uso

| ID | Nome |
| --- | --- |
| CDU01 | Manter Desenvolvedor. |
| CDU02 | Manter Empresa. |
| CDU03 | Iniciar sessão. |
| CDU04 | Realizar reCAPTCHA. |
| CDU05 | Pesquisar usuário. |
| CDU06 | Navegar por calendário. |
| CDU07 | Marcar reunião. |
| CDU08 | Encerrar sessão. |
| CDU09 | Seguir usuário. |
| CDU10 | Candidatar-se a um projeto. |
| CDU11 | Filtrar feed. |
| CDU12 | Sacar dinheiro. |
| CDU13 | Cancelar candidatura. |
| CDU14 | Manter projeto. |
| CDU15 | Escolher desenvolvedor. |
| CDU16 | Encerrar inscrições. |
| CDU17 | Inserir dinheiro na carteira virtual. |
| CDU18 | Realizar transação. |
| CDU19 | Copiar link de compartilhamento de perfi |
| CDU20 | Redefinir senha. |


## Diagrama de Casos de Uso

<img src="https://github.com/Projeto-e-Construcao-de-Sistemas-2023-1/G3---Worklink/blob/main/Documentos/Print%20Diagrama%20CDU%20PNG.png" alt="Diagrama de Caso de Uso PNG">

## Descrições de Casos de Uso

### Caso 1.1: Cadastrar Desenvolvedor

| 01.1 | Cadastrar Desenvolvedor |
| --- | --- |
| Nome | Cadastrar Desenvolvedor |
| Objetivo | Cadastrar novo desenvolvedor no sistema |
| Ator | Desenvolvedor |
| Pré-Condições | O ator não possui cadastro |
| Trigger | O ator seleciona a opção “Registre-se como Desenvolvedor” na tela de sessão. |
| Fluxo Principal | 1 - O sistema exibe os campos “Nome”, “CPF”, “Telefone”, “Data de nascimento”, “Email”, “Senha” e "Confirmar Senha” para serem preenchidos. <br> 2 - O ator preenche os dados e clica em “Cadastrar”. [A1] <br> 3 - O sistema registra o cadastro do ator como desenvolvedor. |
| Fluxos Alternativos | <strong>A1. Ator seleciona a opção “Registre-se como Desenvolvedor”.</strong> <br> 1 - O sistema exibe uma mensagem “Dados inválidos, por favor preencha-os novamente”. <br> 2 - Voltar para o passo 1. |
| Extensões | N/A. |
| Pós-Condições | O ator é cadastrado no sistema com sucesso. |
| Regras de negócios | RN2 - Usuário só pode acessar o sistema mediante cadastro. |

### Caso 1.2: Visualizar Desenvolvedor

| 01.2 | Visualizar  Desenvolvedor |
| --- | --- |
| Nome | Visualizar Desenvolvedor |
| Objetivo | Mostrar dados do desenvolvedor |
| Ator | Desenvolvedor |
| Pré-Condições | O ator está com sessão em andamento |
| Trigger | O ator seleciona a opção “Perfil” em sua tela de usuário. |
| Fluxo Principal | 1 - O sistema exibe os campos “Nome”, “Email”, “Telefone”, “Descrição” e “Hashtags”, além dos projetos do ator, na tela. |
| Fluxos Alternativos | N/A |
| Extensões | N/A. |
| Pós-Condições | Os dados do ator são exibidos na tela. |
| Regras de negócios | N/A |

### Caso 1.3: Editar Desenvolvedor

| 01.3 | Editar Desenvolvedor |
| --- | --- |
| Nome | Editar Desenvolvedor |
| Objetivo | Editar dados do desenvolvedor |
| Ator | Desenvolvedor |
| Pré-Condições | O ator está com sessão em andamento |
| Trigger | O ator seleciona a opção “Editar Perfil” em sua tela de usuário. |
| Fluxo Principal | 1 - O sistema exibe na tela os campos “Nome”, “Email”, “Telefone”, “Descrição” e “Hastags” preenchidos como anteriormente para serem alterados. <br> 2 - O ator altera os campos e seleciona o botão de “Confirmar”. [A1] <br> 3 - O sistema atualiza os campos do ator. |
| Fluxos Alternativos | <strong>A1. Dados inválidos</strong> <br> 1 - O sistema exibe uma mensagem “Dados inválidos, por favor preencha-os novamente”. <br> 2 - Voltar para o passo 1. |
| Extensões | N/A. |
| Pós-Condições | Os dados do ator são alterados. |
| Regras de negócios | RN5 - O usuário não pode alterar CPF ou CNPJ. |

### Caso 1.4: Deletar Desenvolvedor

| 01.4 | Deletar Desenvolvedor |
| --- | --- |
| Nome | Deletar Desenvolvedor |
| Objetivo | Deletar conta do desenvolvedor |
| Ator | Desenvolvedor |
| Pré-Condições | O ator possui cadastro |
| Trigger | O ator seleciona a opção “Deletar conta” em sua tela de usuário. |
| Fluxo Principal | 1 - O sistema exibe um pop-up perguntando se o ator deseja realmente deletar sua conta do sistema, com as opções “Sim” ou “Não”. <br> 2 - O ator confirma a deleção de conta. [A1] <br> 3 - O sistema verifica possíveis pendências e deleta a conta. [A2] |
| Fluxos Alternativos | <strong>A1. O ator seleciona a opção “Não” na pergunta de deleção de conta.</strong> <br> 1 - O ator não confirma a deleção. <br> 2 - Voltar para o passo 1. <br><br ><strong>2 - O ator tem alguma pendência no sistema.</strong> <br> 1 - O sistema exibe mensagem informando que a conta não pode ser deletada. <br> 2 - Voltar para o passo 1. |
| Extensões | N/A. |
| Pós-Condições | A conta do ator é deletada. |
| Regras de negócios | N/A |

### Caso 2.1: Cadastrar Empresa

| 02.1 | Cadastrar Empresa |
| --- | --- |
| Nome | Cadastrar Empresa |
| Objetivo | Cadastrar nova empresa no sistema |
| Ator | Empresa |
| Pré-Condições | O ator não possui cadastro |
| Trigger | O ator seleciona a opção “Registre-se como Empresa” na tela de sessão. |
| Fluxo Principal | 1 - O sistema exibe os campos “Razão Social”, “CNPJ”, “Telefone”, “Email”, “Senha” e "Confirmar Senha” para serem preenchidos. <br> 2 - O ator preenche os dados e clica em “Cadastrar”. [A1] <br> 3 -O sistema registra o cadastro do ator como empresa. |
| Fluxos Alternativos | <strong>A1. Dados inválidos</strong> <br> 1 - O sistema exibe uma mensagem “Dados inválidos, por favor preencha-os novamente”. <br> 2 - Voltar para o passo 1. |
| Extensões | N/A. |
| Pós-Condições | O ator é cadastrado no sistema com sucesso. |
| Regras de negócios | RN2 - Usuário só pode acessar o sistema mediante cadastro. |

### Caso 2.2: Visualizar Empresa

| 02.2 | Visualizar  Empresa |
| --- | --- |
| Nome | Visualizar Empresa |
| Objetivo | Mostrar dados da empresa |
| Ator | Empresa |
| Pré-Condições | O ator está com sessão em andamento |
| Trigger | O ator seleciona a opção “Perfil” em sua tela de usuário. |
| Fluxo Principal | 1 - O sistema exibe os campos “Razão Social”, “Email”, “Telefone”, “Descrição”, além dos projetos do ator, na tela. |
| Fluxos Alternativos | N/A |
| Extensões | N/A. |
| Pós-Condições | Os dados do ator são exibidos na tela. |
| Regras de negócios | N/A |

### Caso 2.3: Editar Empresa

| 02.3 | Editar Empresa |
| --- | --- |
| Nome | Editar Empresa |
| Objetivo | Editar dados da empresa |
| Ator | Empresa |
| Pré-Condições | O ator está com sessão em andamento |
| Trigger | O ator seleciona a opção “Editar Perfil” em sua tela de usuário. |
| Fluxo Principal | 1 - O sistema exibe na tela os campos “Razão Social”, “Telefone”, “Email”, “Senha” e "Confirmar Senha” preenchidos como anteriormente para serem alterados. <br> 2 - O ator altera os campos e seleciona o botão de “Confirmar”. [A1] <br> 3 - O sistema atualiza os campos do ator. |
| Fluxos Alternativos | <strong>A1. Dados inválidos</strong> <br> 1 - O sistema exibe uma mensagem “Dados inválidos, por favor preencha-os novamente”. <br> 2 - Voltar para o passo 1. |
| Extensões | N/A. |
| Pós-Condições | Os dados do ator são alterados. |
| Regras de negócios | RN5 - O usuário não pode alterar CPF ou CNPJ. |

### Caso 2.4: Deletar  Empresa

| 02.4 | Deletar Empresa |
| --- | --- |
| Nome | Deletar Empresa |
| Objetivo | Deletar conta da empresa |
| Ator | Empresa |
| Pré-Condições | O ator possui cadastro |
| Trigger | O ator seleciona a opção “Excluir conta” em sua tela de usuário. |
| Fluxo Principal | 1 - O sistema exibe um pop-up perguntando se o ator deseja realmente deletar sua conta do sistema, com as opções “Sim” ou “Não”. <br> 2 - O ator confirma a deleção de conta. [A1] <br> 3 - O sistema verifica possíveis pendências e deleta a conta. [A2] |
| Fluxos Alternativos | <strong>A1. O ator seleciona a opção “Não” na pergunta de deleção de conta.</strong> <br> 1 - O ator não confirma a desativação. <br> 2 - Voltar para o passo 1. <br><br> <strong> 2 - O ator tem alguma pendência no sistema.</strong> <br> 1 - O sistema exibe mensagem informando que a conta não pode ser desativada. <br> 2 - Voltar para o passo 1. |
| Extensões | N/A. |
| Pós-Condições | A conta do ator é deletada. |
| Regras de negócios | N/A |

### Caso 3: Iniciar Sessão

| 03 | Iniciar Sessão |
| --- | --- |
| Nome | Iniciar Sessão |
| Objetivo | Iniciar sessão do usuário |
| Ator | Usuário |
| Pré-Condições | O ator possui cadastro. |
| Trigger | O ator entra na tela de sessão do sistema. |
| Fluxo Principal | 1 - O sistema exibe na tela os campos “Entrar como Desenvolvedor” e “Entrar como Empresa”. <br> 2 - Ator seleciona a opção desejada. <br> 3 - Sistema exibe os campos "Email" e "Senha" para serem preenchidos. <br> 4 - Ator preenche os campos e seleciona a opção "Entrar". [A1] <br> 5 - Sistema checar se o ator tem cadastro, realiza autenticação e permite acesso. |
| Fluxos Alternativos | <strong>A1. Dados Inválidos</strong> <br> 1 - O sistema exibe uma mensagem “Dados inválidos, por favor preencha-os novamente”. <br> 2 - Voltar para o passo 1. |
| Extensões | N/A. |
| Pós-Condições | O ator está autenticado. |
| Regras de negócios | RN2 - Usuário só pode acessar o sistema mediante cadastro. |

### Caso 4: Encerrar Sessão

| 04 | Encerrar Sessão |
| --- | --- |
| Nome | Encerrar Sessão |
| Objetivo | Encerrar sessão do usuário |
| Ator | Usuário |
| Pré-Condições | O ator possui sessão em andamento. |
| Trigger | O ator seleciona a opção “Sair”. |
| Fluxo Principal | 1 - O sistema exibe uma mensagem para confirmação de encerramento de sessão. <br> 2 - O ator confirma o encerramento da sessão. <br> 3 - O sistema desconecta o ator e retorna para página de login. |
| Fluxos Alternativos | <strong>A1. Usuário não confirma o encerramento.</strong> <br> 1 - O sistema retorna para página inicial. |
| Extensões | N/A. |
| Pós-Condições | O ator está na tela de sessão. |
| Regras de negócios | N/A. |

### Caso 5: Marcar Reunião

| 05 | Marcar Reunião |
| --- | --- |
| Nome | Marcar Reunião |
| Objetivo | Desenvolvedor e empresa se reunirem para comunicação |?
| Ator | Usuário |
| Pré-Condições | O ator está com sessão em andamento. |
| Trigger | O ator seleciona a opção “Marcar Reunião”. |
| Fluxo Principal | 1 - O sistema exibe campos “Nome”, “Email” e “Horário” para serem preenchidos. <br> 2 - O ator preenche os campos.[A1][A2] <br> 3 - O sistema envia um aviso de reunião para a pessoa solicitada. |
| Fluxos Alternativos |  <strong>A1. O sistema não consegue autenticar o nome preenchido.</strong> <br> 1 - O sistema exibe a mensagem de nome não cadastrado. <br> 2- Voltar para o passo 2. <br><br> <strong>A2. O sistema não consegue autenticar email.</strong> <br> 1 - O sistema exibe mensagem de email não cadastrado. <br> 2 - Voltar para o passo 2. |
| Extensões | N/A. |
| Pós-Condições | O ator recebe notificação da reunião. |
| Regras de negócios | RN2 - Usuário só pode acessar o sistema mediante cadastro. |

### Caso 6.1: Criar Projeto

| 01 | Criar Projeto |
| --- | --- |
| Nome | Criar Projeto |
| Objetivo | Criar um novo projeto da empresa |
| Ator | Empresa |
| Pré-Condições | O ator está com sessão em andamento |
| Trigger | O ator seleciona o botão “Criar Novo Projeto” em sua tela de usuário |
| Fluxo Principal | 1 - O sistema exibe a tela com campos “Nome do Projeto”, “Descrição”, “Número de desenvolvedores”, “Hashtag”, “Remuneração” e “Tempo de Contrato”. <br> 2 - O ator preenche os campos e clica na opção “Publicar Projeto”. [A1] <br> 3 - O sistema cria e publica o novo projeto da empresa. |
| Fluxos Alternativos | <strong>A1.  Os campos “Nome do Projeto”, “Número de Desenvolvedores” ou “Hashtags” estão inválidos</strong> <br> 1 - O sistema exibe uma mensagem “Dados inválidos, por favor preencha-os novamente”. <br> 2 - Voltar para o passo 1. |
| Extensões | N/A. |
| Pós-Condições | O ator cria um novo projeto em seu perfil. |
| Regras de negócios | RN7 - Somente empresas podem realizar criação de projetos. |

### Caso 6.2: Visualizar Projeto

| 01 | Visualizar  Projeto |
| --- | --- |
| Nome | Visualizar Projeto |
| Objetivo | Visualizar detalhes de um projeto feito pela empresa |
| Ator | Empresa |
| Pré-Condições | O ator está com sessão em andamento |
| Trigger | O ator seleciona a opção “Ver mais” em um projeto |
| Fluxo Principal | 1 -O sistema exibe o “Nome do Projeto”, “Nome da empresa responsável pelo projeto”, “Descrição”, “Número de desenvolvedores necessários”, “Hashtag”, “Remuneração” e “Tempo de Contrato” e “Vagas disponíveis. |
| Fluxos Alternativos | N/A |
| Extensões | N/A. |
| Pós-Condições | O ator visualiza detalhes do projeto. |
| Regras de negócios | N/A |

### Caso 6.3: Editar Projeto

| 01 | Editar Projeto |
| --- | --- |
| Nome | Editar Projeto |
| Objetivo | Editar dados do projeto da empresa |
| Ator | Empresa |
| Pré-Condições | O ator está com sessão em andamento |
| Trigger | O ator seleciona o botão “Editar Projeto” em um projeto |
| Fluxo Principal | 1 - O sistema exibe tela com campos “Nome do Projeto”, “Descrição”, “Número de desenvolvedores”, “Hashtag”, “Remuneração” e “Tempo de Contrato” preenchidos como anteriormente para serem alterados. <br> 2 - O ator altera os campos e seleciona o botão de “Confirmar”. [A1] <br> 3 - O sistema atualiza os campos do projeto. |
| Fluxos Alternativos | <strong>A1. Campos “Nome do Projeto”, “Número de Desenvolvedores” ou “Hashtags” estão inválidos </strong> <br> 1 - O sistema exibe uma mensagem “Dados inválidos, por favor preencha-os novamente”. <br> 2 - Voltar para o passo 1. |
| Extensões | N/A. |
| Pós-Condições | Os dados do projeto do ator são alterados. |
| Regras de negócios | RN8 - A empresa não poderá editar o projeto caso algum desenvolvedor tenha se candidatado. |

### Caso 6.4: Deletar Projeto

| 01 | Deletar Projeto |
| --- | --- |
| Nome | Deletar Projeto |
| Objetivo | Deletar projeto da empresa |
| Ator | Empresa |
| Pré-Condições | O ator possui um projeto criado |
| Trigger | O ator seleciona o botão “Deletar Projeto” em um projeto. |
| Fluxo Principal | 1 - O sistema exibe um pop-up perguntando se o ator deseja realmente deletar sua conta do sistema, com as opções “Sim” ou “Não”. <br> 2 -O ator confirma a desativação do projeto. [A1] <br> 3 - O sistema verifica possíveis pendências e desativa o projeto. [A2] |
| Fluxos Alternativos | <strong>A1. O ator seleciona a opção “Não” na pergunta de deleção de conta.</strong> <br> 1 - O ator não confirma a desativação. <br> 2 - Voltar para o passo 1. <br><br ><strong>2 - Status do Projeto é “Em desenvolvimento”.</strong> <br> 1 - O sistema exibe mensagem informando que o projeto não pode ser desativado. <br> 2 - Voltar para o passo 1. |
| Extensões | N/A. |
| Pós-Condições | O ator desativa o projeto de seu perfil. |
| Regras de negócios | RN4 - A empresa não poderá deletar o projeto após estar "Em Desenvolvimento" |

### Caso 7: Escolher Desenvolvedor

| 07 | Escolher Desenvolvedor |
| --- | --- |
| Nome | Escolher Desenvolvedor |
| Objetivo | Escolher o(s) desenvolvedor(es) que participará/participarão do projeto. |
| Ator | Empresa |
| Pré-Condições | O projeto publicado possui candidaturas de desenvolvedores. |
| Trigger | O ator clica no botão “Selecionar desenvolvedores” na aba do projeto. |
| Fluxo Principal | 1 - O sistema exibe na tela uma lista com nome e descrição de todos os desenvolvedores que se candidataram ao projeto.[A1] <br> 2 - O ator clica no botão “Escolher Desenvolvedor” ao lado do desenvolvedor desejado. <br> 3 - O sistema exibe a opção “Confirmar Desenvolvedores” após o número de desenvolvedores para o projeto ser totalizado. <br> 4 - Ator clica no botão “Confirmar Desenvolvedores”. |
| Fluxos Alternativos |  <strong>A1. O projeto não possui candidaturas de desenvolvedores.</strong> <br> 1 - O sistema exibe a mensagem “Projeto não possui desenvolvedores candidatados, tente novamente mais tarde.” <br> 2- Voltar para o passo 1. |
| Extensões | N/A. |
| Pós-Condições | Os desenvolvedores para o projeto são confirmados. |
| Regras de negócios | RN1 - Um desenvolvedor deve ter, no mínimo, 1 tag em comum com o projeto para poder se candidatar à ele. |

### Caso 8: Pesquisar Usuário

| 08 | Pesquisar Usuário |
| --- | --- |
| Nome | Pesquisar Usuário |
| Objetivo | Pesquisar um usuário |
| Ator | Usuário |
| Pré-Condições | O ator está com sessão em andamento |
| Trigger | O ator clica no botão de lupa após inserir o nome de um usuário na barra de pesquisa. |
| Fluxo Principal | 1 - O sistema exibe na tela uma lista com nome dos usuários pelo nome pesquisado na barra de pesquisa, com um botão de “Ver mais” ao lado de cada usuário. [A1] |
| Fluxos Alternativos | <strong>A1.Não há usuários com o nome pesquisado.</strong> <br> 1 - O sistema exibe a mensagem “Sua pesquisa não encontrou usuários, por favor tente novamente.” <br> 2 - Voltar para o passo 1. |
| Extensões | N/A. |
| Pós-Condições | Os usuários pesquisados são mostrados na tela. |
| Regras de negócios | N/A |

### Caso 9: Seguir Usuário

| 09 | Seguir Usuário |
| --- | --- |
| Nome | Seguir Usuário |
| Objetivo | Seguir um usuário |
| Ator | Usuário |
| Pré-Condições | O ator está no perfil do usuário. |
| Trigger | O ator clica no botão “Seguir” no usuário. |
| Fluxo Principal | 1 - O sistema registra a ação do ator e muda o botão para “Seguindo”. |
| Fluxos Alternativos | N/A |
| Extensões | N/A |
| Pós-Condições | O ator está seguindo o usuário. |
| Regras de negócios | N/A |

### Caso 10: Realizar Recaptcha

| 10 | Realizar Recaptcha |
| --- | --- |
| Nome | Realizar Recaptcha |
| Objetivo | Passar pela verificação do Recaptcha para iniciar sessão. |
| Ator | Usuário |
| Pré-Condições | O ator tem cadastro. |
| Trigger | O ator entra na tela de sessão do sistema. |
| Fluxo Principal | 1 - O sistema exibe o Recaptcha na tela. <br> 2 - O ator clica no Recaptcha e o preenche. <br> 3 - O sistema verifica a pontuação do ator e confirma o preenchimento. |
| Fluxos Alternativos | N/A. |
| Extensões | N/A. |
| Pós-Condições | O Recaptcha está preenchido. |
| Regras de negócios | N/A. |

### Caso 11: Filtrar Feed

| 11 | Filtrar Feed |
| --- | --- |
| Nome | Filtrar Feed |
| Objetivo | Filtrar Feed e acordo com as hashtags |
| Ator | Usuário |
| Pré-Condições | O ator estar com sessão em andamento |
| Trigger | O ator seleciona a opção “Tags em altas” ou “Tags Seguidas”. |
| Fluxo Principal | 1 - O sistema filtra e exibe todos os projetos que têm as hashtags selecionadas pelo ator. |
| Fluxos Alternativos | N/A. |
| Extensões | N/A. |
| Pós-Condições | Feed filtrado com as hashtags desejadas. |
| Regras de negócios | N/A. |

### Caso 12: Redefinir Senha

| 12 | Redefinir Senha |
| --- | --- |
| Nome | Redefinir Senha |
| Objetivo | Alterar a senha |
| Ator | Usuário |
| Pré-Condições | O usuário tem cadastro. |
| Trigger | Usuário seleciona a opção “Redefinir Senha”. |
| Fluxo Principal | 1 - O sistema exibe o campo de “Senha” e “Confirmar Senha”. <br> 2 - O ator preenche os campos e confirma. <br> 3 - O sistema registra a ação do ator e redireciona para a página de perfil do usuário. |
| Fluxos Alternativos | N/A. |
| Extensões | N/A. |
| Pós-Condições | A senha foi alterada. |
| Regras de negócios | N/A. |

## Diagrama de Classes

<img src="https://github.com/Projeto-e-Construcao-de-Sistemas-2023-1/G3---Worklink/blob/main/Documentos/Print%20Diagrama%20Classe%20PNG.png" alt="Diagrama de classes PNG">
 
## Integrações
 
| Nome | Descrição |
| --- | --- |
| reCAPTCHA | Verifica se o usuário que está iniciando sessão é um humano. |
| Google Calendar API | API de Calendário para visualizar datas e marcar reuniões. |
| email.mime | Envio de email para redefinição de senha. |
 
## Slides e Entregas
 
Entrega Final 1: https://github.com/Projeto-e-Construcao-de-Sistemas-2023-1/G3---Worklink/blob/main/Documentos/PCS%20ENTREGA%20FINAL.pdf
<br>Entrega Final 2: https://github.com/Projeto-e-Construcao-de-Sistemas-2023-1/G3---Worklink/blob/main/Documentos/PCS-ENTREGA-FINAL-2.pdf  
