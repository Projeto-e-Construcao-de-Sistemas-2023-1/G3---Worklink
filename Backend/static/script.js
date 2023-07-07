var select = document.querySelector('#ml-show');
var post = document.getElementById('show-post-container');

select.addEventListener('click', function() {
   post.classList.toggle("hide");

});

document.addEventListener('DOMContentLoaded', function() {
   const searchInput = document.getElementById('searchInput'); // Obtém o elemento de input de pesquisa pelo ID
   const resultsContainer = document.getElementById('results'); // Obtém o elemento de contêiner de resultados pelo ID
  //  const data = ['Ana Clara', 'Pedro', 'Joana', 'Fernanda', 'Ana Beatriz', 'Roberto']; // Array de dados de exemplo
   let users = [];
  //  searchInput.addEventListener('input', function () {
  //    const searchTerm = searchInput.value.toLowerCase(); // Obtém o termo de pesquisa digitado e converte para minúsculas
  //    const filteredData = data.filter(item => item.toLowerCase().includes(searchTerm)); // Filtra os dados com base no termo de pesquisa
  //    displayResults(filteredData); // Chama a função para exibir os resultados filtrados
  //  });
   searchInput.addEventListener('input', function () {
    const searchTerm = searchInput.value.toLowerCase();
    // Fazer uma requisição AJAX para o back-end
    const xhr = new XMLHttpRequest();
    xhr.open('GET', '/pesquisa_usuario?nome=' + searchTerm);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onload = function () {
      if (xhr.status === 200) {
        const responseData = JSON.parse(xhr.responseText);
        users = responseData;
        displayResults(responseData);
      }
    };
    xhr.send();
    console.log(users)
  });

   searchInput.addEventListener('focus', function () {
     resultsContainer.classList.add('show'); // Adiciona a classe 'show' para exibir o conteiner de resultados ao focar no campo de pesquisa
   });

   searchInput.addEventListener('blur', function () {
     resultsContainer.classList.remove('show'); // Remove a classe 'show' para ocultar o conteiner de resultados ao perder o foco do campo de pesquisa
   });

   resultsContainer.addEventListener('click', function (event) {
    console.log('Evento de clique acionado');
     const clickedItem = event.target.textContent; // Obtém o texto do item de resultado clicado
     searchInput.value = clickedItem; // Preenche o campo de pesquisa com o texto do item clicado 
     const selectedUser = users.find(user => user.nome + ' ' + user.sobrenome === clickedItem);
     if (selectedUser) {
      // Redireciona para a página de destino com informações do usuário
       window.location.href = '/perfil/' + encodeURIComponent(JSON.stringify(selectedUser));
      //window.location.href = '/testtt/' 
    }
   });
    
   function displayResults(users) {
    const resultsList = document.getElementById('resultsList');
    resultsList.innerHTML = ''; // Limpa a lista de resultados antes de preencher novamente
    users.forEach(user => {
      const listItem = document.createElement('li');
      if (user.nome) {  // Usuário do tipo desenvolvedor
        listItem.textContent = user.nome + ' ' + user.sobrenome;
      } else if (user.razao_social) {  // Usuário do tipo empresa
        listItem.textContent = user.razao_social + ' - ' + user.area_negocio;
      }
      resultsList.appendChild(listItem);
    });
  }
  }
  //  function displayResults(data) {
  //    resultsContainer.innerHTML = ''; // Limpa o conteiner de resultados

  //    if (data.length === 0) {
  //      resultsContainer.innerHTML = '<p>Nenhum resultado encontrado.</p>'; // Exibe uma mensagem quando nenhum resultado é encontrado
  //    } else {
  //      const ul = document.createElement('ul'); // Cria uma lista não ordenada para os resultados

  //      data.forEach(item => {
  //        const li = document.createElement('li'); // Cria um item de lista para cada resultado
  //        li.textContent = item; // Define o texto do item de lista como o resultado atual
  //        ul.appendChild(li); // Adiciona o item de lista à lista não ordenada
  //      });

  //      resultsContainer.appendChild(ul); // Adiciona a lista não ordenada ao conteiner de resultados
  //    }
  //  }
//}
);

  function openForm() {
    document.getElementById("myForm").style.display = "block";
  }
  
  function closeForm() {
    document.getElementById("myForm").style.display = "none";
  }

  document.getElementById('carteira').addEventListener('click', function() {
    openPopup();
  });


  function confirmarTransacao(event) {
      event.preventDefault(); 

      if (confirm("Confirmar transação?")) {
          document.getElementById("formTransacao").submit(); 
      }
  }

      function confirmarDeposito(event) {
          event.preventDefault(); 

          if (confirm("Confirmar Deposito?")) {
              document.getElementById("formDepositar").submit(); 
          }
      }

          function confirmarSaque(event) {
              event.preventDefault(); 
  
              if (confirm("Confirmar Saque?")) {
                  document.getElementById("formSacar").submit(); 
              }
          }

  // Função para buscar o saldo atual da carteira do usuário
  function getSaldoAtual() {
      // Fazer uma requisição para o backend para buscar o saldo atual
      // Aqui você pode usar uma biblioteca como o Axios ou o fetch para fazer a requisição
      // Exemplo usando o Axios:
      axios.get('/saldoAtual')
          .then(response => {
              // Atualizar o elemento HTML com o saldo atual retornado do backend
              document.getElementById('saldoAtual').innerText = response.data.saldo;
          })
          .catch(error => {
              console.error(error);
          });
  }

  // Chamar a função para buscar o saldo atual assim que a página carregar
  window.addEventListener('load', getSaldoAtual);

  
// Função para mostrar o formulário correspondente ao botão clicado
function mostrarForm(formId) {
const forms = document.getElementsByTagName('form');
for (let i = 0; i < forms.length; i++) {
  forms[i].style.display = 'none';
}
document.getElementById(formId).style.display = 'block';
}

function confirmarTransacao(event) {
  event.preventDefault(); 

  if (confirm("Confirmar transação?")) {
      document.getElementById("formTransacao").submit(); 
  }
}

  function confirmarDeposito(event) {
      event.preventDefault(); 

      if (confirm("Confirmar Deposito?")) {
          document.getElementById("formDepositar").submit(); 
      }
  }

      function confirmarSaque(event) {
          event.preventDefault(); 

          if (confirm("Confirmar Saque?")) {
              document.getElementById("formSacar").submit(); 
          }
      }


// Função para buscar o saldo atual da carteira do usuário
function getSaldoAtual() {
  // Fazer uma requisição para o backend para buscar o saldo atual
  // Aqui você pode usar uma biblioteca como o Axios ou o fetch para fazer a requisição
  // Exemplo usando o Axios:
  axios.get('/saldoAtual')
      .then(response => {
          // Atualizar o elemento HTML com o saldo atual retornado do backend
          document.getElementById('saldoAtual').innerText = response.data.saldo;
      })
      .catch(error => {
          console.error(error);
      });
}

// Chamar a função para buscar o saldo atual assim que a página carregar
window.addEventListener('load', getSaldoAtual);


// Função para mostrar o formulário correspondente ao botão clicado
function mostrarForm(formId) {
const forms = document.getElementsByTagName('form');
for (let i = 0; i < forms.length; i++) {
forms[i].style.display = 'none';
}
document.getElementById(formId).style.display = 'block';
}

