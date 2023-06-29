var select = document.querySelector('#ml-show');
var post = document.getElementById('show-post-container');

select.addEventListener('click', function() {
   post.classList.toggle("hide");

});

function alterarTexto() {
   var btn = document.getElementById("follow-button");
   if (btn.innerHTML === "Seguir") {
     btn.innerHTML = "Seguindo";
     btn.classList.remove("seguir");
     btn.classList.add("seguindo");
   } else {
     btn.innerHTML = "Seguir";
     btn.classList.remove("seguindo");
     btn.classList.add("seguir");
   }
 }