document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll("a[href], button").forEach((item) => {
      item.addEventListener("click", function (e) {
        e.preventDefault();
        document.body.style.opacity = 0;
        setTimeout(() => {
          if (item.tagName === "A") {
            window.location.href = item.getAttribute("href");
          } else if (item.getAttribute("onclick")) {
            eval(item.getAttribute("onclick"));
          }
        }, 500);
      });
    });
  });
  
  // script.js
  
  function salvarProduto() {
    // Aqui você pode adicionar o código para salvar o produto no banco de dados.
    // Por enquanto, vamos apenas exibir um alert.
  
    alert("Produto salvo no banco de dados");
  
    // Depois de salvar o produto, redirecione para a página "conclusao.html"
    window.location.href = "conclusao.html";
  }
  