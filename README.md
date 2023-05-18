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

### Caso 1: Criar Cadastro

![image](https://user-images.githubusercontent.com/83520652/235237886-286866f6-0594-4f36-bd50-c6aaf927eb51.png)

### Caso 2: Iniciar Sessão

![image](https://user-images.githubusercontent.com/83520652/235237977-52f7d74b-dbb5-4ae5-86e6-2e5f44d0aa76.png)

### Caso 3: Encerrar Sessão

![image](https://user-images.githubusercontent.com/83520652/235238058-0558c14f-0598-4bbd-9259-83bca2e203c4.png)

### Caso 4: Marcar Reunião

![image](https://user-images.githubusercontent.com/83520652/235238160-e3a541dd-262c-4315-b629-adaa19228c5c.png)

## Diagrama de Classes

![image](https://user-images.githubusercontent.com/83520652/236583380-6031a692-ae95-4bc9-acef-06afc2d38631.png)

