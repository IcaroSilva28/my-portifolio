/* ============================================================
   script.js — Portifólio
   ============================================================ */

/* ---------- Alinhar menu com seção da página ---------- */
const header = document.getElementById('header');
window.addEventListener('scroll', () => {
  header.classList.toggle('scrolled', window.scrollY > 30);
});

/* ---------- Menu mobile ---------- */
const menuToggle = document.querySelector('.menu-toggle');
const navList    = document.querySelector('.nav-list');

menuToggle.addEventListener('click', () => {
  menuToggle.classList.toggle('open');
  navList.classList.toggle('open');
});

/* Fechar ao clicar em um link */
document.querySelectorAll('.nav-link').forEach(link => {
  link.addEventListener('click', () => {
    menuToggle.classList.remove('open');
    navList.classList.remove('open');
  });
});

/* ---------- Navegação através de links ---------- */
const sections = document.querySelectorAll('section[id]');
const navLinks  = document.querySelectorAll('.nav-link');

const observer = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      navLinks.forEach(l => l.classList.remove('active'));
      const active = document.querySelector(`.nav-link[href="#${entry.target.id}"]`);
      if (active) active.classList.add('active');
    }
  });
}, { rootMargin: '-40% 0px -55% 0px' });

sections.forEach(s => observer.observe(s));

/* ---------- Animações de revelação do scroll ---------- */
const revealEls = document.querySelectorAll('[data-animate]');

const revealObserver = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      revealObserver.unobserve(entry.target);
    }
  });
}, { threshold: 0.15 });

revealEls.forEach(el => revealObserver.observe(el));

/* Transição dos cards de projetos */
document.querySelectorAll('.portfolio-card').forEach((card, i) => {
  card.style.transitionDelay = `${i * 0.1}s`;
});

/* ---------- Paralax para revelação dos itens ---------- */
const timelineItems = document.querySelectorAll('.timeline-item');
const timelineObserver = new IntersectionObserver(entries => {
  entries.forEach((entry, idx) => {
    if (entry.isIntersecting) {
      setTimeout(() => {
        entry.target.classList.add('visible');
      }, entry.target.dataset.delay || 0);
      timelineObserver.unobserve(entry.target);
    }
  });
}, { threshold: 0.2 });

timelineItems.forEach((item, i) => {
  item.dataset.delay = i * 150;
  timelineObserver.observe(item);
});

/* ---------- Formulário de contato ---------- */
const form     = document.getElementById('contato-form');
const feedback = document.getElementById('form-feedback');

form.addEventListener('submit', e => {
  e.preventDefault();
  const btn = form.querySelector('button[type="submit"]');
  btn.textContent = 'Enviando…';
  btn.disabled = true;

  /* Simulação de envio — substituir por fetch real após atualização do código */
  setTimeout(() => {
    feedback.textContent = 'Mensagem enviada com sucesso! Retornarei em breve.';
    form.reset();
    btn.textContent = 'Enviar Mensagem';
    btn.disabled = false;
    setTimeout(() => (feedback.textContent = ''), 5000);
  }, 1200);
});

/* ---------- Data do footer ---------- */
document.getElementById('year').textContent = new Date().getFullYear();
