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

function salvarProduto() {
    alert("Produto salvo no banco de dados");
    window.location.href = "conclusao.html";
  }