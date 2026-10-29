/* ============================================================
   script.js: tema, menu e seção atual
   ============================================================ */

(function () {
  var raiz = document.documentElement;

  /* ---------- Tema Dia e Noite ---------- */
  // há dois seletores: um no topo e outro dentro do menu, no celular
  var botoesTema = document.querySelectorAll(".seletor-tema");

  function temaAtual() {
    var escolhido = raiz.getAttribute("data-theme");
    if (escolhido) return escolhido;
    return window.matchMedia("(prefers-color-scheme: dark)").matches ? "noite" : "dia";
  }

  var coresTema = document.querySelectorAll('meta[name="theme-color"]');

  // o nome acessível começa pela palavra visível no botão ("Dia" ou "Noite")
  function rotularTema() {
    var rotulo = temaAtual() === "noite" ? "Noite, mudar para Dia" : "Dia, mudar para Noite";
    botoesTema.forEach(function (botao) { botao.setAttribute("aria-label", rotulo); });
    // com um tema escolhido à mão, a barra do navegador acompanha a escolha e não o sistema
    if (raiz.getAttribute("data-theme")) {
      var cor = temaAtual() === "noite" ? "#0c1322" : "#ebedea";
      coresTema.forEach(function (meta) { meta.setAttribute("content", cor); });
    }
  }

  function aplicarTema(tema) {
    raiz.setAttribute("data-theme", tema);
    try { localStorage.setItem("tema", tema); } catch (e) {}
    rotularTema();
  }

  botoesTema.forEach(function (botao) {
    botao.addEventListener("click", function () {
      var proximo = temaAtual() === "noite" ? "dia" : "noite";
      var semMovimento = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
      // o giro do ícone vale só para esta troca; sem isso, ele giraria de novo ao abrir o menu
      raiz.classList.add("trocou-tema");
      setTimeout(function () { raiz.classList.remove("trocou-tema"); }, 450);

      // a página inteira passa do chão para o céu de uma vez; sem suporte, as cores mudam sozinhas
      if (!document.startViewTransition || semMovimento) {
        aplicarTema(proximo);
        return;
      }
      raiz.classList.add("tema-em-transicao");
      var liberar = function () { raiz.classList.remove("tema-em-transicao"); };
      var transicao = document.startViewTransition(function () { aplicarTema(proximo); });
      transicao.finished.then(liberar, liberar);
      setTimeout(liberar, 800); // por garantia, caso o navegador não termine a transição
    });
  });
  rotularTema();

  /* ---------- Menu no celular ---------- */
  var botaoMenu = document.querySelector(".botao-menu");
  var menu = document.getElementById("menu");

  function fecharMenu() {
    menu.classList.remove("aberto");
    botaoMenu.setAttribute("aria-expanded", "false");
  }

  botaoMenu.addEventListener("click", function () {
    var abrir = botaoMenu.getAttribute("aria-expanded") !== "true";
    menu.classList.toggle("aberto", abrir);
    botaoMenu.setAttribute("aria-expanded", String(abrir));
    if (abrir) menu.querySelector("a").focus();
  });

  menu.querySelectorAll("a").forEach(function (link) {
    link.addEventListener("click", fecharMenu);
  });

  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape" && botaoMenu.getAttribute("aria-expanded") === "true") {
      fecharMenu();
      botaoMenu.focus();
    }
  });

  /* ---------- Seção atual no menu ---------- */
  var links = menu.querySelectorAll("a");
  if ("IntersectionObserver" in window) {
    var observador = new IntersectionObserver(function (entradas) {
      entradas.forEach(function (entrada) {
        if (!entrada.isIntersecting) return;
        links.forEach(function (link) {
          if (link.getAttribute("href") === "#" + entrada.target.id) link.setAttribute("aria-current", "true");
          else link.removeAttribute("aria-current");
        });
      });
    }, { rootMargin: "-45% 0px -50% 0px" });
    document.querySelectorAll("main section[id]").forEach(function (secao) { observador.observe(secao); });
  }

  /* ---------- Ano no rodapé ---------- */
  document.getElementById("ano").textContent = new Date().getFullYear();
})();
