# G3---Worklink

## Minimundo
WorkLink é uma plataforma para empresas e desenvolvedores freelancers, onde empresas postam trabalhos que precisam ser feitos e desenvolvedores se candidatam a esses trabalhos. Tais desenvolvedores trabalham de forma independente, oferecendo seus serviços de desenvolvimento a empresas em troca de remuneração acordada entre as partes. 

Na plataforma, as empresas se cadastram com nome e CNPJ e criam seus perfis, destacando sua área de negócio e projetos em aberto, que contam com suas especificações, como hashtags, prazos, requisitos técnicos e orçamento disponível. Os desenvolvedores, por sua vez, cadastram-se com nome, CPF, email, telefone e data de nascimento e criam seus próprios perfis, destacando suas habilidades através de hashtags que eles marcam em seu perfil (como java, front-end, full-stack, etc.), experiência no ramo e projetos feitos, para que as empresas possam encontrar o talento certo para o trabalho. Nesse sentido, empresas podem seguir desenvolvedores e vice-versa.

 Além dos perfis, a plataforma conta com um feed geral para navegação dos desenvolvedores de projetos de empresas que eles seguem, onde eles podem ver trabalhos requisitados em tempo real. Assim que os trabalhos são postados pelas empresas, os desenvolvedores podem se candidatar aos trabalhos que acham que se encaixam em suas habilidades e experiência se eles possuírem uma tag em comum com as hashtags do projeto. As empresas podem então revisar as inscrições e escolher o freelancer que melhor se adequa às suas necessidades.

O feed geral também conta com filtros, para ajudar os desenvolvedores a encontrar o trabalho que desejam.

 Além disso, a plataforma inclui ferramentas para pagamentos online, permitindo que as empresas gerenciem e paguem seus desenvolvedores através da plataforma, e estes acumulem dinheiro na carteira de seu perfil, possibilitando um futuro saque.

 Para as empresas, a plataforma conta com uma seção de gerenciamento de projetos, na qual é possível observar projetos a fazer, projetos em andamento e projetos concluídos, com informações pertinentes ao projeto e desenvolvedores envolvidos.

 Assim que um desenvolvedor é alocado em um projeto, reuniões esporádicas são adicionadas a um calendário do desenvolvedor, onde atualizações regulares são feitas com o cliente para garantir que o projeto esteja em andamento de acordo com as expectativas. Dessa forma, as empresas encontram os talentos que precisam para realizar trabalhos desejados enquanto os freelancers encontram oportunidades de trabalho temporárias para ganhar um dinheiro extra.
 
 ## Requisitos
 
 ### Funcionais
 
| ID | Descrição |
| --- | --- |
| RF01 | O sistema deve permitir cadastro de empresas, com razão social, CNPJ, e-mail, telefone, CEP e senha. |
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
| CDU12 | Escolher desenvolvedor. |
| CDU13 | Manter projeto. |
| CDU14 | Sacar dinheiro. |
| CDU15 | Depositar dinheiro. |
| CDU16 | Realizar transação. |
| CDU17 | Copiar link de compartilhamento de perfil |
| CDU18 | Redefinir senha. |
| CDU19 | Realizar publicação |

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
| Fluxo Principal | 1 -O sistema exibe os campos “Nome”, “CPF”, “Telefone”, “Data de nascimento”, “Email”, “Descrição”, “Senha” e "Confirmar Senha” para serem preenchidos. <br> 2 - O ator preenche os dados e clica em “Cadastrar-se”. [A1] <br> 3 - O sistema registra o cadastro do ator como desenvolvedor e redireciona o ator para o perfil do desenvolvedor.|
| Fluxos Alternativos | <strong>Dados inválidos ou campos sem preenchimentos.</strong> <br> 1 - O sistema exibe um pop up “Preencha este campo”. <br> 2 - Voltar para o passo 1. |
| Extensões | N/A. |
| Pós-Condições | O ator cadastrado no sistema com sucesso.|
| Regras de negócios | RN2 - Usuário só pode acessar o sistema mediante cadastro. |

### Caso 1.2: Visualizar Desenvolvedor

| 01.2 | Visualizar  Desenvolvedor |
| --- | --- |
| Nome | Visualizar Desenvolvedor |
| Objetivo | Mostrar dados do desenvolvedor |
| Ator | Desenvolvedor |
| Pré-Condições | O ator está com sessão em andamento |
| Trigger |O ator seleciona a opção “Ver Perfil” em sua tela de usuário.|
| Fluxo Principal | 1 - O sistema exibe os campos “Nome”, “Email”, “Sobre”, “Projetos ativos” e “Projetos Concluídos” e “Seguindo”.|
| Fluxos Alternativos | N/A |
| Extensões | N/A. |
| Pós-Condições | Os dados do ator exibidos na tela. |
| Regras de negócios | N/A |

### Caso 1.3: Editar Desenvolvedor

| 01.3 | Editar Desenvolvedor |
| --- | --- |
| Nome | Editar Desenvolvedor |
| Objetivo | Editar dados do desenvolvedor |
| Ator | Desenvolvedor |
| Pré-Condições | O ator com sessão em andamento |
| Trigger | O ator seleciona a opção “Editar Perfil” em sua tela de usuário. |
| Fluxo Principal | 1 - O sistema exibe na tela os campos “Nome”, “Sobrenome”, “Gênero”, “Descrição”, “Telefone”, “Foto”, “Hashtag”, “Conta bancária” e “Senha” preenchidos anteriormente para serem alterados. <br> 2 - O ator altera os campos e seleciona o botão de “Salvar alterações”. [A1] <br> 3 - O sistema atualiza os campos do ator e redireciona o ator para o perfil do desenvolvedor. |
| Fluxos Alternativos | <strong>A1. Cancelar edição.</strong> <br> 1 - O usuário clica na opção de voltar para tela anterior. <br> 2 - O sistema redireciona o ator para o perfil do desenvolvedor.|
| Extensões | N/A. |
| Pós-Condições | Os dados do ator alterados |
| Regras de negócios | RN5 - O usuário não pode alterar CPF ou CNPJ após o cadastro. |

### Caso 1.4: Excluir Desenvolvedor

| 01.4 | Excluir Desenvolvedor |
| --- | --- |
| Nome | Excluir Desenvolvedor |
| Objetivo | Excluir conta do desenvolvedor |
| Ator | Desenvolvedor |
| Pré-Condições | O ator possui cadastro |
| Trigger | O ator seleciona a opção “Excluir conta” em sua tela de “Editar Perfil” |
| Fluxo Principal | 1 - O sistema exibe um pop-up perguntando se o ator deseja realmente excluir sua conta do sistema, com as opções “Excluir Conta” ou “Cancelar”.  <br> 2 - O ator confirma a exclusão de conta [A1] <br> 3 - O sistema realiza a exclusão da conta e exibe pop up com a mensagem “Conta excluída com sucesso”[A2] |
| Fluxos Alternativos | <strong>A1. O ator seleciona a opção “Cancelar” na pergunta de excluir a conta.</strong> <br> 1 - O sistema redireciona o ator para a página de “Editar Perfil”. <br ><strong>A2 - O ator tem alguma pendência no sistema.</strong> <br> 1 - O sistema exibe mensagem informando que a conta não pode ser deletada e redireciona o ator para a página de perfil de empresa |
| Extensões | N/A. |
| Pós-Condições | A conta do ator excluída. |
| Regras de negócios | RN6 - O usuário não poderá excluir a conta, caso tenha projetos ativos. |

### Caso 2.1: Cadastrar Empresa

| 02.1 | Cadastrar Empresa |
| --- | --- |
| Nome | Cadastrar Empresa |
| Objetivo | Cadastrar nova empresa no sistema |
| Ator | Empresa |
| Pré-Condições | O ator sem cadastro |
| Trigger | O ator seleciona a opção “Cadastre-se como Empresa” na tela de sessão. |
| Fluxo Principal | 1 - O sistema exibe os campos “Razão Social”, “CNPJ”, “Telefone”, “Email”, “Conta Bancária”, “Área de negócio”, “Senha” e "CEP” para serem preenchidos. <br> 2 - O ator preenche os dados e clica em “Cadastrar-se”. [A1] <br> 3 - O sistema registra o cadastro do ator como empresa e redireciona o ator para a tela inicial. |
| Fluxos Alternativos | <strong>A1.  Dados inválidos ou campos sem preenchimentos</strong> <br> 1 - O sistema exibe um pop up “Preencha este campo”. <br> 2 - Voltar para o passo 1. |
| Extensões | N/A. |
| Pós-Condições | O ator cadastrado no sistema com sucesso. |
| Regras de negócios | RN2 - Usuário só pode acessar o sistema mediante cadastro. |

### Caso 2.2: Visualizar Empresa

| 02.2 | Visualizar  Empresa |
| --- | --- |
| Nome | Visualizar Empresa |
| Objetivo | Mostrar dados da empresa |
| Ator | Empresa |
| Pré-Condições | O ator com sessão em andamento |
| Trigger | O ator seleciona a opção “Perfil” em sua tela de usuário. |
| Fluxo Principal | 1 - O sistema exibe os campos “Sobre”, “Email”, “Telefone”, Projetos Ativos”, “Projetos Concluídos”,  “Razão Social” e “Seguindo”. |
| Fluxos Alternativos | N/A |
| Extensões | N/A. |
| Pós-Condições | Os dados do ator exibidos na tela |
| Regras de negócios | N/A |

### Caso 2.3: Editar Empresa

| 02.3 | Editar Empresa |
| --- | --- |
| Nome | Editar Empresa |
| Objetivo | Editar dados da empresa |
| Ator | Empresa |
| Pré-Condições | O ator com sessão em andamento |
| Trigger | O ator seleciona a opção “Editar Perfil” em sua tela de usuário. |
| Fluxo Principal | 1 - O sistema exibe os campos “Razão Social”, “Telefone”, “Hashtag”, “Conta Bancária”, “Área de negócio”, “Senha” e "Foto” para serem preenchidos. <br> 2 - O ator altera os campos e seleciona o botão de “Salvar alterações”. [A1] <br> 3 - Sistema atualiza os campos do ator e redireciona o ator para o perfil da empresa. |
| Fluxos Alternativos | <strong>A1. Cancelar edição.</strong> <br> 1 - O usuário clica na opção de voltar para tela anterior <br> 2 - O sistema redireciona o ator para o perfil do desenvolvedor. |
| Extensões | N/A. |
| Pós-Condições | Os dados do ator alterados |
| Regras de negócios | RN5 - O usuário não pode alterar CPF ou CNPJ após cadastro. |

### Caso 2.4: Excluir Empresa

| 02.4 | Excluir Empresa |
| --- | --- |
| Nome | Excluir Empresa |
| Objetivo | Excluir conta da empresa |
| Ator | Empresa |
| Pré-Condições | O ator possui cadastro |
| Trigger | O ator seleciona a opção “Excluir conta” em sua tela de usuário. |
| Fluxo Principal | 1 - O sistema exibe um pop-up perguntando se o ator deseja realmente excluir sua conta do sistema, com as opções “Excluir Conta” ou “Cancelar”. [A1] <br> 2 - O ator confirma a exclusão da conta. [A2] <br> 3 - O sistema realiza a exclusão da conta. |
| Fluxos Alternativos | <strong>A1. O ator seleciona a opção “Cancelar” na pergunta de excluir a conta.</strong> <br> 1 - O sistema redireciona o ator para a página de “Editar Perfil”. <br> <strong> A2 - O ator tem alguma pendência no sistema.</strong> <br> 1- O sistema exibe mensagem informando que a conta não pode ser excluída redireciona o ator para a página de perfil de empresa. |
| Extensões | N/A. |
| Pós-Condições | A conta do ator excluída |
| Regras de negócios | RN6 - O usuário não poderá excluir a conta, caso tenha projetos ativos. |

### Caso 3: Iniciar Sessão

| 03 | Iniciar Sessão |
| --- | --- |
| Nome | Iniciar Sessão |
| Objetivo | Iniciar sessão do usuário |
| Ator | Usuário |
| Pré-Condições | O ator possui cadastro. |
| Trigger | O ator entra na tela de sessão do sistema. |
| Fluxo Principal | 1 - O sistema exibe na tela os campos “Entrar”. <br> 2 - O ator seleciona a opção desejada. <br> 3 - O sistema exibe os campos "Email", "Senha" e o “reCAPTCHA” para serem preenchidos. <br> 4 - O ator preenche os campos e seleciona a opção "Entrar". [A1] <br> 5 -  sistema checa se o ator tem cadastro, verifica se o reCAPTCHA validou, realiza autenticação e permite acesso.|
| Fluxos Alternativos | <strong>A1. Dados Inválidos</strong> <br> 1 - O sistema exibe uma mensagem “***EMAIL OU SENHA INCORRETOS***”. <br> 2 - Voltar para o passo 1. |
| Extensões | N/A. |
| Pós-Condições | O ator autenticado. |
| Regras de negócios | RN2 - Usuário só pode acessar o sistema mediante cadastro. |

### Caso 04: Realizar reCAPTCHA

| 04 | Realizar reCAPTCHA |
| --- | --- |
| Nome | Realizar reCAPTCHA |
| Objetivo | Passar pela verificação do reCAPTCHA para iniciar sessão. |
| Ator | Usuário |
| Pré-Condições | O ator com cadastro. |
| Trigger | O ator entra na tela de sessão do sistema |
| Fluxo Principal | 1 - O sistema exibe o reCAPTCHA na tela. <br> 2 - O ator clica no reCAPTCHA e o preenche. <br> 3 - O sistema verifica e confirma o preenchimento. |
| Fluxos Alternativos |<strong>A1. O Ator falha no reCAPTCHA.</strong> <br> 1 - O sistema exibe uma mensagem “Por favor, marque a caixa de verificação reCAPTCHA.” |
| Extensões | N/A. |
| Pós-Condições | O reCAPTCHA preenchido. |
| Regras de negócios | N/A. |

### Caso 5: Pesquisar Usuário

| 05 | Pesquisar Usuário |
| --- | --- |
| Nome | Pesquisar Usuário |
| Objetivo | Pesquisar um usuário |
| Ator | Usuário |
| Pré-Condições | O ator com sessão em andamento |
| Trigger | O ator digita o nome na barra de pesquisa |
| Fluxo Principal | 1 - O sistema exibe na tela uma lista com nome dos usuários pelo nome pesquisado na barra de pesquisa, com um botão de “Ver perfil” ao lado de cada usuário. [A1] |
| Fluxos Alternativos | <strong>A1.Não há usuários com o nome pesquisado.</strong> <br> 1 - O sistema exibe a mensagem “Sua pesquisa não encontrou usuários, por favor tente novamente.” <br> 2 - Voltar para o passo 1. |
| Extensões | N/A |
| Pós-Condições | Os usuários pesquisados mostrados na tela. |
| Regras de negócios | N/A |

### Caso 06: Navegar por calendário

| 06 | Navegar por calendário |
| --- | --- |
| Nome | Navegar por calendário |
| Objetivo | Visualizar os dias do ano e reuniões marcadas |
| Ator | Usuário |
| Pré-Condições | O ator com sessão em andamento |
| Trigger | O ator seleciona o botão de calendário na sua tela de perfil |
| Fluxo Principal | 1 - O sistema exibe o calendário do ator, com os dias do mês atual e suas reuniões marcadas. |
| Fluxos Alternativos | N/A. |
| Extensões | CDU07 - Marcar Reunião |
| Pós-Condições | O calendário é exibido na tela do ator. |
| Regras de negócios | N/A |

### Caso 7: Marcar Reunião

| 07 | Marcar Reunião |
| --- | --- |
| Nome | Marcar Reunião |
| Objetivo | Desenvolvedor e empresa se reunirem para comunicação |
| Ator | Usuário |
| Pré-Condições | O ator com sessão em andamento. |
| Trigger | O ator seleciona a opção “+” |
| Fluxo Principal | 1 - O sistema exibe um pop-up com campos “Começo”, “Fim”, “Cor de Texto”, “Cor de Fundo” e “Evento” para serem preenchidos. <br> 2 - O ator preenche os campos.[A1][A2] <br> 3 - O sistema salva a reunião no sistema e envia um email para a pessoa solicitada na reunião. |
| Fluxos Alternativos |  <strong>A1. Ator preenche uma data de fim antes da data de início.</strong> <br> 1 - O sistema exibe a mensagem “A data de início não pode ser após a data de fim!”.<br> 2- Voltar para o passo 2. <br><br> <strong>A2. Ator deixa um campo vazio.</strong> <br> 1 - O sistema exibe a mensagem “Insira um valor válido. O campo está incompleto ou tem uma data inválida.”|
| Extensões | N/A. |
| Pós-Condições | A reunião salva no sistema e email enviado. |
| Regras de negócios | RN2 - Usuário só pode acessar o sistema mediante cadastro. |

### Caso 8: Encerrar Sessão

| 08 | Encerrar Sessão |
| --- | --- |
| Nome | Encerrar Sessão |
| Objetivo | Encerrar sessão do usuário |
| Ator | Usuário |
| Pré-Condições | O ator com sessão em andamento. |
| Trigger | O ator seleciona a opção “Sair”. |
| Fluxo Principal | 1 -O sistema desconecta o ator e retorna para tela inicial. |
| Fluxos Alternativos | N/A |
| Extensões | N/A |
| Pós-Condições | O ator na tela de sessão. |
| Regras de negócios | N/A |

### Caso 9: Seguir Usuário

| 09 | Seguir Usuário |
| --- | --- |
| Nome | Seguir Usuário |
| Objetivo | Seguir um usuário |
| Ator | Usuário |
| Pré-Condições | O ator no perfil do usuário. |
| Trigger | O ator clica no botão “Seguir” no usuário |
| Fluxo Principal | 1 - O sistema registra a ação do ator e muda o botão para “Seguindo”. |
| Fluxos Alternativos | N/A |
| Extensões | N/A |
| Pós-Condições | O ator seguindo o usuário. |
| Regras de negócios | N/A |

### Caso 10: Candidatar-se a um projeto

| 10 | Candidatar-se a um projeto |
| --- | --- |
| Nome | Candidatar-se a um projeto |
| Objetivo | Candidatar-se a um projeto desejado |
| Ator | Desenvolvedor |
| Pré-Condições | O ator possui uma hashtag em comum com o projeto |
| Trigger | O ator seleciona a opção “Candidatar-se” na tela do projeto |
| Fluxo Principal | 1 - O sistema exibe a mensagem “Você se candidatou a esse projeto”. |
| Fluxos Alternativos | N/A |
| Extensões | N/A |
| Pós-Condições | A candidatura realizada com sucesso |
| Regras de negócios | RN1 - Um desenvolvedor deve ter, no mínimo, 1 hashtag em comum com o projeto para poder se candidatar à ele. |

### Caso 11: Filtrar Feed

| 11 | Filtrar Feed |
| --- | --- |
| Nome | Filtrar Feed |
| Objetivo | Filtrar Feed e acordo com as hashtags |
| Ator | Usuário |
| Pré-Condições | O ator com sessão em andamento |
| Trigger | O ator seleciona a opção “Hashtags em alta” ou “Hashtags seguidas” |
| Fluxo Principal | 1 - O sistema filtra e exibe todos os projetos que têm as hashtags selecionadas pelo ator. |
| Fluxos Alternativos | N/A. |
| Extensões | N/A. |
| Pós-Condições | Feed filtrado com as hashtags desejadas. |
| Regras de negócios | N/A. | 

### Caso 12: Escolher Desenvolvedor

| 12 | Escolher Desenvolvedor |
| --- | --- |
| Nome | Escolher Desenvolvedor |
| Objetivo | Escolher o(s) desenvolvedor(es) que participará/participarão do projeto. |
| Ator | Empresa |
| Pré-Condições | O projeto publicado possui candidaturas de desenvolvedores. |
| Trigger | O ator clica no botão “Selecionar desenvolvedores” na aba do projeto. |
| Fluxo Principal | 1 - O sistema exibe na tela uma lista com nome e descrição de todos os desenvolvedores que se candidataram ao projeto.[A1] <br> 2 - O ator clica no botão “Escolher Desenvolvedor” ao lado do desenvolvedor desejado. <br> 3 - O sistema exibe a opção “Confirmar Desenvolvedores” após o número de desenvolvedores para o projeto ser totalizado. <br> 4 - Ator clica no botão “Confirmar Desenvolvedores”. |
| Fluxos Alternativos |  N/A |
| Extensões | N/A. |
| Pós-Condições | Os desenvolvedores confirmados no projeto |
| Regras de negócios | RN1 - Um desenvolvedor deve ter, no mínimo, 1 tag em comum com o projeto para poder se candidatar à ele. |

### Caso 13.1: Criar Projeto

| 13.1 | Criar Projeto |
| --- | --- |
| Nome | Criar Projeto |
| Objetivo | Criar um novo projeto da empresa |
| Ator | Empresa |
| Pré-Condições | O ator com sessão em andamento |
| Trigger | O ator seleciona o botão “Criar Novo Projeto” em sua tela de usuário |
| Fluxo Principal | 1 - O sistema exibe a tela com campos “Nome do Projeto”, “Descrição”, “Número de desenvolvedores”, “Hashtag”, “Remuneração” e “Tempo de Contrato”. <br> 2 - O ator preenche os campos e clica na opção “Publicar Projeto”. [A1] <br> 3 - O sistema cria e publica o novo projeto da empresa. |
| Fluxos Alternativos | <strong>A1.  Os campos “Nome do Projeto”, “Número de Desenvolvedores” ou “Hashtags” estão inválidos</strong> <br> 1 - O sistema exibe uma mensagem “Dados inválidos, por favor preencha-os novamente”. <br> 2 - Voltar para o passo 1. |
| Extensões | N/A. |
| Pós-Condições | Projeto criado com sucesso |
| Regras de negócios | RN7 - Somente empresas podem realizar criação de projetos. |

### Caso 13.2: Visualizar Projeto

| 13.2 | Visualizar  Projeto |
| --- | --- |
| Nome | Visualizar Projeto |
| Objetivo | Visualizar detalhes de um projeto feito pela empresa |
| Ator | Empresa |
| Pré-Condições | O ator com sessão em andamento |
| Trigger | O ator seleciona a opção “Ver mais” em um projeto |
| Fluxo Principal | 1 -O sistema exibe o “Nome do Projeto”, “Nome da empresa responsável pelo projeto”, “Descrição”, “Número de desenvolvedores necessários”, “Hashtag”, “Remuneração” e “Tempo de Contrato” e “Vagas disponíveis. |
| Fluxos Alternativos | N/A |
| Extensões | N/A. |
| Pós-Condições | Detalhes do projetos exibidos na tela do ator |
| Regras de negócios | N/A |

### Caso 13.3: Editar Projeto

| 13.3 | Editar Projeto |
| --- | --- |
| Nome | Editar Projeto |
| Objetivo | Editar dados do projeto da empresa |
| Ator | Empresa |
| Pré-Condições | O ator com sessão em andamento |
| Trigger | O ator seleciona o botão “Editar Projeto” em um projeto |
| Fluxo Principal | 1 - O sistema exibe tela com campos “Nome do Projeto”, “Descrição”, “Número de desenvolvedores”, “Hashtag”, “Remuneração” e “Tempo de Contrato” preenchidos como anteriormente para serem alterados. <br> 2 - O ator altera os campos e seleciona o botão de “Confirmar”. [A1] <br> 3 - O sistema atualiza os campos do projeto. |
| Fluxos Alternativos | <strong>A1. Campos “Nome do Projeto”, “Número de Desenvolvedores” ou “Hashtags” estão inválidos </strong> <br> 1 - O sistema exibe uma mensagem “Dados inválidos, por favor preencha-os novamente”. <br> 2 - Voltar para o passo 1. |
| Extensões | N/A. |
| Pós-Condições | Os dados do projeto do ator alterados. |
| Regras de negócios | RN8 - A empresa não poderá editar o projeto caso algum desenvolvedor tenha se candidatado. |

### Caso 13.4: Excluir Projeto

| 13.4 | Excluir Projeto |
| --- | --- |
| Nome | Excluir Projeto |
| Objetivo | Excluir projeto da empresa |
| Ator | Empresa |
| Pré-Condições | O ator possui um projeto criado |
| Trigger | O ator seleciona o botão “Excluir Projeto” em um projeto |
| Fluxo Principal | 1 - O sistema exibe um pop-up perguntando se o ator deseja realmente excluir sua conta do sistema, com as opções “Sim” ou “Não”. <br> 2 -O ator confirma a exclusão do projeto. [A1][A2] <br> 3 - O sistema exclui o projeto |
| Fluxos Alternativos | <strong>A1. O ator seleciona a opção “Não” na pergunta de exclusão de conta.</strong> <br> 1 - O ator não confirma exclusão. <br> 2 - O sistema redireciona para a página de peril do usuário. <br><br ><strong>A2 - Status do Projeto é “Em desenvolvimento”.</strong> <br> 1 - O sistema exibe mensagem informando que o projeto não pode ser excluído. <br> 2 - Voltar para o passo 1. |
| Extensões | N/A. |
| Pós-Condições | Projeto excluido do sistema |
| Regras de negócios | RN4 - A empresa não poderá excluir o projeto após estar "Em Desenvolvimento" |

### Caso 14: Sacar Dinheiro

| 14 | Sacar Dinheiro |
| --- | --- |
| Nome | Sacar dinheiro |
| Objetivo | Sacar dinheiro para sua conta |
| Ator | Usuário |
| Pré-Condições | O ator está na tela de carteira e possui dinheiro para sacar |
| Trigger | O ator seleciona a opção “Sacar” na tela de carteira |
| Fluxo Principal | 1 - O sistema exibe o campo “Valor” para ser preenchido pelo ator. <br> 2 - O ator preenche o campo para o saque. <br> 3 - O sistema valida se o usuário tem o valor necessário, realiza o saque e exibe uma tela com mensagem “Saque realizado com sucesso”. [A1][A2]|
| Fluxos Alternativos |  <strong>A1.Saldo Insuficiente.</strong> <br> 1 - O sistema exibe uma página com a mensagem “Erro ao realizar saque”. <br> 2- Voltar para o passo 1. <br><br ><strong>A2 - Valor inválido.</strong> <br> 1 - O sistema exibe uma página com a mensagem “Erro ao realizar depósito”. <br> 2 - Voltar para o passo 1. |
| Extensões | N/A. |
| Pós-Condições | O saldo na carteira do ator atualizada com sucesso |
| Regras de negócios | N/A |

### Caso 15: Depositar Dinheiro

| 15 | Depositar Dinheiro |
| --- | --- |
| Nome | Depositar Dinheiro |
| Objetivo | Depositar Dinheiro na carteira virtual |
| Ator | Empresa|
| Pré-Condições | O ator está na tela de carteira |
| Trigger | O ator seleciona a opção “Depositar” na tela de carteira |
| Fluxo Principal | 1 - O sistema exibe o campo “Valor” para ser preenchido pelo ator. <br> 2 - O ator preenche o campo para o depósito. <br> 3 - O sistema valida o depósito e exibe uma tela com mensagem “Depósito realizado com sucesso”. [A1] |
| Fluxos Alternativos |  <strong>A1. Valor inválido.</strong> <br> 1 - O sistema exibe uma página com a mensagem “Erro ao realizar depósito”. <br> 2- Voltar para o passo 1. |
| Extensões | N/A. |
| Pós-Condições | O saldo na carteira do ator atualizada com sucesso |
| Regras de negócios | RN9 - Somente a empresa poderá realizar depósito na carteira. |

### Caso 16: Realizar transação

| 16 | Realizar transação |
| --- | --- |
| Nome | Realizar transação |
| Objetivo | Realizar transferência de dinheiro da empresa pro desenvolvedor |
| Ator | Empresa|
| Pré-Condições | O ator está na tela de carteira e possui dinheiro para realizar transação |
| Trigger | O ator seleciona a opção “Transação” na tela de carteira |
| Fluxo Principal | 1 - O sistema exibe os campos “Código do recebedor”, “Valor” e “Descrição” para serem preenchidos pelo ator. <br> 2 -O ator preenche os campos para a transação. <br> 3 - O sistema valida a transação e exibe uma tela com mensagem “Transação realizada com sucesso”. [A1][A2] |
| Fluxos Alternativos |  <strong>A1. Sistema não encontra o desenvolvedor.</strong> <br> 1 - O sistema exibe uma página com a mensagem “Erro ao realizar transação”. <br> 2- Voltar para o passo 1. <br><br ><strong>A2 - Valor inválido.</strong> <br> 1 - O sistema exibe uma página com a mensagem “Erro ao realizar depósito”. <br> 2 - Voltar para o passo 1.|
| Extensões | N/A. |
| Pós-Condições | A transação realizada com sucesso |
| Regras de negócios | N/A |

### Caso 17: Copiar link de compartilhamento

| 17 | Copiar link de compartilhamento |
| --- | --- |
| Nome | Copiar link de compartilhamento |
| Objetivo |Compartilhar links dos usuários |
| Ator | Usuário |
| Pré-Condições | O usuário com sessão em andamento |
| Trigger | O ator seleciona a opção “Copiar link do perfil” na tela do perfil do usuário |
| Fluxo Principal | 1 -O sistema exibe a mensagem “Link Copiado”. |
| Fluxos Alternativos | N/A |
| Extensões | N/A. |
| Pós-Condições | O usuário com a cópia do link de perfil do usuário selecionado |
| Regras de negócios | N/A |

### Caso 18: Redefinir Senha

| 18 | Redefinir Senha |
| --- | --- |
| Nome | Redefinir Senha |
| Objetivo | Alterar a senha |
| Ator | Usuário |
| Pré-Condições | O ator com cadastro. |
| Trigger | O ator seleciona a opção “Redefinir Senha”. |
| Fluxo Principal | 1 - O sistema exibe o campo de “Senha” e “Confirmar Senha”. <br> 2 - O ator preenche os campos e confirma. <br> 3 - O sistema registra a ação do ator e redireciona para a página de perfil do usuário. |
| Fluxos Alternativos | N/A. |
| Extensões | N/A. |
| Pós-Condições | A senha redefinida |
| Regras de negócios | N/A. |

### Caso 19: Realizar publicação

| 19 | Realizar publicação |
| --- | --- |
| Nome | Realizar publicação |
| Objetivo | Realizar uma publicação sobre um acontecimento |
| Ator | Usuário |
| Pré-Condições | O usuário com sessão em andamento |
| Trigger | O ator seleciona a opção “Comece uma publicação” na página inicial |
| Fluxo Principal | 1 - O sistema exibe os campos “Hashtags” e “Texto da publicação” para serem preenchidos. <br> 2 - O ator preenche os campos e seleciona a opção “Publicar”. <br> 3 - O sistema registra e confirma a publicação. [A1][A2] |
| Fluxos Alternativos | <strong>A1. SCampo “Hashtags” vazio.</strong> <br> 1 - O sistema exibe a mensagem “Campo de hashtags vazio!”. <br> 2- Voltar para o passo 1. <br><br ><strong>A2 - Campo “Texto da publicação” vazio.</strong> <br> 1 - O sistema exibe a mensagem “Campo de texto da publicação vazio!”. <br> 2 - Voltar para o passo 1. |
| Extensões | N/A. |
| Pós-Condições | O usuário com a cópia do link de perfil do usuário selecionado |
| Regras de negócios | N/A. |

## Diagrama de Classes

<img src="https://github.com/Projeto-e-Construcao-de-Sistemas-2023-1/G3---Worklink/blob/main/Documentos/Print%20Diagrama%20Classe%20PNG.png" alt="Diagrama de classes PNG">
 
## Integrações
 
| Nome | Descrição |
| --- | --- |
| reCAPTCHA | Verifica se o usuário que está iniciando sessão é um humano. |
| Email.message | Envio de email, utilizado ao marcar ou excluir reuniões. |
| Via CEP | Verificar se o CEP das empresas é válido |
 
## Slides e Entregas
 
Entrega Final 1: https://github.com/Projeto-e-Construcao-de-Sistemas-2023-1/G3---Worklink/blob/main/Documentos/PCS%20ENTREGA%20FINAL.pdf
<br>Entrega Final 2: https://github.com/Projeto-e-Construcao-de-Sistemas-2023-1/G3---Worklink/blob/main/Documentos/PCS-ENTREGA-FINAL-2.pdf
<br>Entrega Final 3: https://github.com/Projeto-e-Construcao-de-Sistemas-2023-1/G3---Worklink/blob/main/Documentos/PCS-ENTREGA-FINAL-3.pdf
<br>Entrega Parcial 4: https://github.com/Projeto-e-Construcao-de-Sistemas-2023-1/G3---Worklink/blob/main/Documentos/PCS-ENTREGA-PARCIAL-4.pdf
<br>Entrega Final 5: https://github.com/Projeto-e-Construcao-de-Sistemas-2023-1/G3---Worklink/blob/main/Documentos/pcs5.pdf
