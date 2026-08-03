/* ============================================================
   Linha 04 — script da página
   1) mostra "execução local" quando os marcadores ainda não
      foram substituídos pelo pipeline
   2) anima os contadores dos indicadores
   ============================================================ */

// ---------- 1. selo de publicação ----------
document.querySelectorAll("[data-build]").forEach(function (el) {
  if (el.textContent.indexOf("{{") !== -1) {
    el.textContent = "execução local";
  }
});

// ---------- 2. contadores ----------
(function () {
  "use strict";

  var alvos = document.querySelectorAll("[data-contador]");
  var semMovimento = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  function anima(el) {
    var destino = Number(el.dataset.contador);

    if (semMovimento) {
      el.textContent = destino;
      return;
    }

    var duracao = 900;
    var inicio = performance.now();

    function passo(agora) {
      var p = Math.min((agora - inicio) / duracao, 1);
      el.textContent = Math.round(destino * (1 - Math.pow(1 - p, 3)));
      if (p < 1) requestAnimationFrame(passo);
    }

    requestAnimationFrame(passo);
  }

  var observador = new IntersectionObserver(function (entradas) {
    entradas.forEach(function (entrada) {
      if (entrada.isIntersecting) {
        anima(entrada.target);
        observador.unobserve(entrada.target);
      }
    });
  }, { threshold: 0.4 });

  alvos.forEach(function (el) { observador.observe(el); });
})();
