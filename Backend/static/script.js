var select = document.querySelector('#ml-show');
var post = document.getElementById('show-post-container');

select.addEventListener('click', function() {
   post.classList.toggle("hide");

});

document.addEventListener('DOMContentLoaded', function() {
   const searchInput = document.getElementById('searchInput');
   const resultsContainer = document.getElementById('results');
   const data = ['Ana Clara', 'Pedro', 'Joana', 'Fernanda', 'Ana Beatriz', 'Roberto'];

   searchInput.addEventListener('input', function () {
     const searchTerm = searchInput.value.toLowerCase();
     const filteredData = data.filter(item => item.toLowerCase().includes(searchTerm));

     displayResults(filteredData);
   });

   searchInput.addEventListener('focus', function () {
     resultsContainer.classList.add('show');
   });

   searchInput.addEventListener('blur', function () {
     resultsContainer.classList.remove('show');
   });

   resultsContainer.addEventListener('click', function (event) {
     const clickedItem = event.target.textContent;
     searchInput.value = clickedItem;
     window.location.href = 'pagina-de-destino.html'; // substitua 'pagina-de-destino.html' pela URL da página para a qual você deseja redirecionar
   });

   function displayResults(data) {
     resultsContainer.innerHTML = '';

     if (data.length === 0) {
       resultsContainer.innerHTML = '<p>Nenhum resultado encontrado.</p>';
     } else {
       const ul = document.createElement('ul');

       data.forEach(item => {
         const li = document.createElement('li');
         li.textContent = item;
         ul.appendChild(li);
       });

       resultsContainer.appendChild(ul);
     }
   }
});