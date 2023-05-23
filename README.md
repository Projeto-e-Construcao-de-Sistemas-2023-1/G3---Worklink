# G3---Worklink

## Minimundo
WorkLink é uma plataforma para empresas e desenvolvedores freelancers, onde empresas postam trabalhos que precisam ser feitos e desenvolvedores se candidatam a esses trabalhos. Tais desenvolvedores trabalham de forma independente, oferecendo seus serviços de desenvolvimento a empresas em troca de remuneração acordada entre as partes. 

Na plataforma, as empresas se cadastram com nome e CNPJ e criam seus perfis, destacando sua área de negócio e projetos em aberto, que contam com suas especificações, como tags, prazos, requisitos técnicos e orçamento disponível. Os desenvolvedores, por sua vez, cadastram-se com nome, CPF, email, telefone e data de nascimento e criam seus próprios perfis, destacando suas habilidades através de tags que eles marcam em seu perfil (como java, front-end, full-stack, etc.), experiência no ramo e projetos feitos, para que as empresas possam encontrar o talento certo para o trabalho. Nesse sentido, empresas podem seguir desenvolvedores e vice-versa.

 Além dos perfis, a plataforma conta com um feed geral para navegação dos desenvolvedores de projetos de empresas que eles seguem, onde eles podem ver trabalhos requisitados em tempo real. Assim que os trabalhos são postados pelas empresas, os desenvolvedores podem se candidatar aos trabalhos que acham que se encaixam em suas habilidades e experiência se eles possuírem uma tag em comum com as tags do projeto. As empresas podem então revisar as inscrições e escolher o freelancer que melhor se adequa às suas necessidades.

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
| RF06 | O sistema deve exibir no perfil dos desenvolvedores em quais projetos eles estão atualmente trabalhando. |
| RF07 | O sistema deve permitir que os desenvolvedores escolham tags que mostrem quais são suas proficiências e área de atuação, além de um campo de descrição nas páginas dos usuários em que eles podem escrever. |
| RF08 | O sistema deve permitir aos desenvolvedores seguirem empresas e vice-versa. |
| RF09 | O sistema deve permitir a candidaturas de desenvolvedores a projetos de empresas. |
| RF10 | O sistema deve permitir que as empresas aceitem desenvolvedores para seus projetos. |
| RF11 | O sistema deve apresentar um feed geral para os desenvolvedores com os projetos apresentados pelas empresas. |
| RF12 | O sistema deve permitir que o desenvolvedor filtre os projetos apresentados no feed geral pelas tags, ou mostrar apenas projetos publicados por empresas que ele segue. |
| RF13 | O sistema deve permitir à empresa inserir dinheiro em sua própria carteira virtual. |
| RF14 | O sistema deve permitir a transação de fundos entre empresa e desenvolvedor. |
| RF15 | O sistema deve permitir marcar reuniões em calendário para conversas entre empresas e desenvolvedores. |
| RF16 | O sistema deve permitir que usuários pesquisem uns aos outros. |

 ### Não-Funcionais
 
| ID | Tipo |Descrição |
| --- | --- | --- |
| RNF1 | Segurança | O sistema deve ter um reCAPTCHA no login de usuário. |
| RNF2 | Compatibilidade | O sistema deve ser compatível com as versões atualizadas do Google Chrome.  |

## Regras de Negócio

| ID | Descrição |
| --- | --- |
| RN1 | Um desenvolvedor deve ter, no mínimo, 1 tag em comum com o projeto para poder se candidatar à ele. |
| RN2 | Usuário só pode acessar o sistema mediante cadastro. |
| RN3 | Uma empresa só poderá contratar desenvolvedores se possuir um valor na carteira maior ou igual ao valor a ser pago pelo projeto. |
| RN4 | (Se uma empresa excluir um projeto durante seu desenvolvimento, o que acontece com o pagamento? Ela deve pagar totalmente os desenvolvedores?) |

## Diagrama de Casos de Uso

<img src="https://github.com/Projeto-e-Construcao-de-Sistemas-2023-1/G3---Worklink/blob/main/Documentos/Print%20Diagrama%20CDU%20PNG.png" alt="Diagrama de Caso de Uso PNG">

## Descrições de Casos de Uso

### Caso 1: Manter Usuário

| 01 | Manter Usuário |
| --- | --- |
| Nome | Manter usuário |
| Objetivo | Manter usuário no sistema |
| Ator | Usuário |
| Pré-Condições | Ator sem cadastro |
| Trigger | Ator entra no endpoint de login do sistema |
| Fluxo Principal | 1 - Sistema exibe na tela as opções “Registre-se como Desenvolvedor” e “Registre-se como Empresa”. <br> 2 - Ator seleciona a opção desejada [A1][A2] |
| Fluxos Alternativos | <strong>A1. Ator seleciona a opção “Desenvolvedor”.</strong> <br> 1 - Sistema exibe os campos “Nome”, “CPF”, “Telefone”, “Data de nascimento”, “Email”, “Senha” e "Confirmar Senha” para serem preenchidos. <br> 2 - Ator preenche os dados e clica em “Cadastrar”. <br> 3 - Sistema registra o cadastro do ator como desenvolvedor. <br><br> <strong>A2. Ator seleciona a opção “Empresa”.</strong> <br> 1 - Sistema exibe os campos “Razão Social”, “CNPJ”, “Telefone”, “Email”, “Senha” e "Confirmar Senha” para serem preenchidos. <br> 2 - Ator preenche os dados e clica em “Cadastrar”. <br> 3 - Sistema registra o cadastro do ator como empresa. <br><br> <strong>A3. Ator seleciona a opção “Perfil” na tela de usuário</strong> <br> 1 - Sistema exibe a foto e os campos “Nome”, “Email”, “Telefone”, “Descrição”,  “Tags”, além dos projetos do ator, na tela. <br><br> <strong>A4. Ator seleciona a opção “Editar Perfil” em seu perfil.</strong> <br> 1 - Sistema exibe na tela a foto do ator e os campos “Nome”, “Email”, “Telefone”, “Descrição” e “Tags” preenchidos como anteriormente para serem alterados. <br> 2 - Ator altera os campos e seleciona o botão de “Confirmar”. <br> 3 - Sistema atualiza os campos do ator. <br><br> <strong>A5. Ator seleciona a opção “Deletar conta” em seu perfil.</strong> <br> 1 - Sistema deleta a conta do ator. |
| Extensões | N/A. |
| Pós-Condições | Ator é cadastrado no sistema com sucesso. |
| Regras de negócios | RN2 - Usuário só pode acessar o sistema mediante cadastro. |

### Caso 2: Iniciar Sessão

| 02 | Iniciar Sessão |
| --- | --- |
| Nome | Iniciar Sessão |
| Objetivo | Iniciar sessão do usuário |
| Ator | Usuário |
| Pré-Condições | Ator com cadastro |
| Trigger | Ator seleciona a opção de login. |
| Fluxo Principal | 1 - Sistema exibe na tela os campos “Email” e “Senha”. <br> 2 - Ator preenche os campos e seleciona a opção “Entrar”. <br> Sistema checa se o ator tem cadastro, realiza autenticação e permite acesso. [A1][A2] |
| Fluxos Alternativos |  <strong>A1. Sistema não consegue validar o email.</strong> <br> 1 - Sistema exibe a mensagem de email não cadastrado. <br> 2- Voltar para o passo 2. <br><br> <strong>A2. Sistema não consegue validar a senha.</strong> <br> 1 - Sistema exibe a mensagem de senha inválida. <br> 2- Voltar para o passo 2. |
| Extensões | N/A. |
| Pós-Condições | Ator autenticado. |
| Regras de negócios | RN2 - Usuário só pode acessar o sistema mediante cadastro. |

### Caso 3: Encerrar Sessão

| 03 | Encerrar Sessão |
| --- | --- |
| Nome | Encerrar Sessão |
| Objetivo | Encerrar sessão do usuário |
| Ator | Usuário |
| Pré-Condições | Ator com sessão em andamento. |
| Trigger | Ator seleciona a opção “Sair”. |
| Fluxo Principal | 1 - Sistema desautentica ator. |
| Fluxos Alternativos | N/A |
| Extensões | N/A. |
| Pós-Condições | Ator na tela de login. |
| Regras de negócios | RN2 - Usuário só pode acessar o sistema mediante cadastro. |

### Caso 4: Marcar Reunião

![image](https://user-images.githubusercontent.com/83520652/235238160-e3a541dd-262c-4315-b629-adaa19228c5c.png)

## Diagrama de Classes

![image](https://user-images.githubusercontent.com/83520652/236583380-6031a692-ae95-4bc9-acef-06afc2d38631.png)

