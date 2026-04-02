const CAT_LABELS = {
  'notas-gcp': 'Google Cloud Platform',
  'notas-git': 'Git & GitHub',
};

let notes = [];
let currentFilter = 'all';
let tocObserver = null;

// ── Cargar notas desde notes.json ──
async function cargarNotas() {
  try {
    const res = await fetch('notes.json');
    notes = await res.json();
    init();
  } catch (e) {
    console.error('Error cargando notes.json:', e);
  }
}

// ── Inicializar ──
function init() {
  const categorias = [...new Set(notes.map(n => n.category))];

  const catGrid = document.getElementById('catGrid');
  catGrid.innerHTML = categorias.map(cat => `
    <a class="category-card" onclick="setFilter('${cat}', null)">
      <div class="cat-name">${CAT_LABELS[cat] || cat}</div>
      <div class="cat-count">${notes.filter(n => n.category === cat).length} notas</div>
      <span class="cat-tag">${cat}</span>
    </a>
  `).join('');

  document.getElementById('totalNotes').textContent = notes.length;
  document.getElementById('totalGroups').textContent = categorias.length;

  buildSidebar();
  renderRecientes();
}

// ── Sidebar dinámico ──
function buildSidebar() {
  const navSection = document.getElementById('navSection');

  // Limpiar folders anteriores excepto "Todas las notas"
  navSection.querySelectorAll('.nav-item:not(#nav-all), .nav-children').forEach(el => el.remove());

  const categorias = [...new Set(notes.map(n => n.category))];

  categorias.forEach(cat => {
    const label = CAT_LABELS[cat] || cat;
    const key = cat.replace('notas-', '');

    const folder = document.createElement('div');
    folder.className = 'nav-item';
    folder.id = `nav-${key}`;
    folder.onclick = () => toggleFolder(key, folder);
    folder.innerHTML = `<span class="dot"></span> ${label} <span class="chevron">▶</span>`;

    const children = document.createElement('div');
    children.className = 'nav-children';
    children.id = `children-${key}`;

    const grupos = [...new Set(notes.filter(n => n.category === cat).map(n => n.grupo))];
    children.innerHTML = grupos.map(grupo => {
      const notasDelGrupo = notes.filter(n => n.grupo === grupo);
      return `
        <div class="nav-group-item">${grupo}</div>
        ${notasDelGrupo.map(n => `
          <a class="nav-child-item" onclick="abrirNota('${n.slug}', '${n.title.replace(/'/g, "\\'")}', '${n.grupo.replace(/'/g, "\\'")}', '${(CAT_LABELS[n.category] || n.category).replace(/'/g, "\\'")}', this); closeSidebar();">
            <span class="line"></span>${n.title}
          </a>
        `).join('')}
      `;
    }).join('');

    navSection.appendChild(folder);
    navSection.appendChild(children);
  });
}

// ── Toggle folder en sidebar ──
function toggleFolder(key, el) {
  const children = document.getElementById('children-' + key);
  const isOpen = children.classList.contains('open');
  children.classList.toggle('open', !isOpen);
  el.classList.toggle('open', !isOpen);
  const cat = `notas-${key}`;
  if (!isOpen) setFilter(cat, el);
}

// ── Filtrar por categoría ──
function setFilter(cat, el) {
  document.getElementById('noteWrapper').classList.remove('active');
  document.getElementById('indexView').style.display = '';
  document.querySelector('.hero-row').style.display = cat === 'all' ? '' : 'none';
  document.getElementById('recientesSection').style.display = cat === 'all' ? '' : 'none';
  currentFilter = cat;

  document.querySelectorAll('.nav-item').forEach(i => i.classList.remove('active'));
  document.querySelectorAll('.nav-child-item').forEach(i => i.classList.remove('active'));

  if (el) {
    el.classList.add('active');
  } else if (cat === 'all') {
    document.getElementById('nav-all').classList.add('active');
  } else {
    const key = cat.replace('notas-', '');
    const navEl = document.getElementById(`nav-${key}`);
    if (navEl) navEl.classList.add('active');
  }

  const filtered = cat === 'all' ? notes : notes.filter(n => n.category === cat);
  renderGroups(filtered);

  const label = CAT_LABELS[cat] || cat;
  document.getElementById('breadcrumbCat').textContent = cat === 'all' ? 'inicio' : label;
  document.getElementById('notesSectionLabel').style.display = cat === 'all' ? 'none' : '';
  document.getElementById('notesSectionLabel').textContent = label;
  document.getElementById('catGrid').style.display = cat === 'all' ? '' : 'none';
  document.getElementById('catSectionLabel').style.display = cat === 'all' ? '' : 'none';
  document.getElementById('totalNotes').textContent = filtered.length;
  const grupos = [...new Set(filtered.map(n => n.grupo))];
  document.getElementById('totalGroups').textContent = grupos.length;

  if (cat === 'all') {
    document.getElementById('catHeader').style.display = 'none';
  } else {
    document.getElementById('catHeader').style.display = '';
    document.getElementById('catHeaderTitle').textContent = CAT_LABELS[cat] || cat;
    document.getElementById('catHeaderMeta').textContent = `${filtered.length} notas · ${grupos.length} grupos`;
  }
}

// ── Buscar notas ──
function filterNotes(query) {
  const q = query.toLowerCase();
  const base = currentFilter === 'all' ? notes : notes.filter(n => n.category === currentFilter);
  const filtered = q ? base.filter(n => n.title.toLowerCase().includes(q) || n.grupo.toLowerCase().includes(q)) : base;
  renderGroups(filtered);
  document.getElementById('totalNotes').textContent = filtered.length;
}

// ── Renderizar grupos ──
function renderGroups(list) {
  const container = document.getElementById('groupsContainer');
  if (!list.length) {
    container.innerHTML = '<div class="empty-state">No se encontraron notas.</div>';
    return;
  }
  const grupos = {};
  list.forEach(n => {
    if (!grupos[n.grupo]) grupos[n.grupo] = [];
    grupos[n.grupo].push(n);
  });
  container.innerHTML = Object.entries(grupos).map(([grupo, notas]) => `
    <div class="group-block">
      <div class="group-title">${grupo}</div>
      <table class="notes-table">
        <tbody>
          ${notas.map(n => `
            <tr onclick="abrirNota('${n.slug}', '${n.title.replace(/'/g, "\\'")}', '${n.grupo.replace(/'/g, "\\'")}', '${(CAT_LABELS[n.category] || n.category).replace(/'/g, "\\'")}')">
              <td><a class="note-link">${n.title}</a></td>
              <td style="width:160px"><span class="note-tag">${CAT_LABELS[n.category] || n.category}</span></td>
            </tr>
          `).join('')}
        </tbody>
      </table>
    </div>
  `).join('');
}

// ── Notas recientes ──

function renderRecientes() {
  const recientes = [...notes]
    .sort((a, b) => new Date(b.fecha_modificacion) - new Date(a.fecha_modificacion))
    .slice(0, 8);

  const container = document.getElementById('recientesContainer');
  container.innerHTML = recientes.map(n => {
    const cat = CAT_LABELS[n.category] || n.category;
    const fecha = new Date(n.fecha_modificacion).toLocaleDateString('es-PE');
    return `
      <tr onclick="abrirNota('${n.slug}', '${n.title.replace(/'/g, "\\'")}', '${n.grupo.replace(/'/g, "\\'")}', '${cat}')">
        <td>
          <a class="note-link">${n.title}</a>
          <div class="reciente-meta-mobile">${cat} · ${fecha}</div>
        </td>
        <td class="reciente-cat"><span class="note-tag">${cat}</span></td>
        <td class="reciente-fecha">${fecha}</td>
      </tr>`;
  }).join('');
}

// ── Abrir nota inline ──
async function abrirNota(slug, titulo, grupo, catLabel, el) {
  const content = document.getElementById('noteContent');
  const indexView = document.getElementById('indexView');

  indexView.style.display = 'none';
  document.getElementById('noteWrapper').classList.add('active');
  content.innerHTML = '<div class="note-loading">Cargando...</div>';

  // Botón volver → categoría padre
  const cat = slug.split('/')[0];
  const key = cat.replace('notas-', '');
  document.querySelector('.note-back').onclick = () => setFilter(cat, document.getElementById(`nav-${key}`));

  // Breadcrumb navegable
  document.getElementById('breadcrumbCat').innerHTML = `
    <a onclick="setFilter('${cat}', document.getElementById('nav-${key}'))" style="cursor:pointer">${catLabel}</a>
    <span>/</span> ${titulo}
  `;

  // Marcar activo en sidebar
  document.querySelectorAll('.nav-child-item').forEach(i => i.classList.remove('active'));
  if (el) el.classList.add('active');

  try {
    const res = await fetch(`docs/${slug}.html`);
    if (!res.ok) throw new Error('No encontrado');
    const html = await res.text();
    const parser = new DOMParser();
    const doc = parser.parseFromString(html, 'text/html');
    const noteContent = doc.querySelector('.note-content');
    content.innerHTML = noteContent ? noteContent.innerHTML : doc.body.innerHTML;
    if (typeof hljs !== 'undefined') hljs.highlightAll();
    buildTOC();
  } catch (e) {
    content.innerHTML = `<div class="empty-state">Error cargando la nota: ${e.message}</div>`;
  }

  window.scrollTo(0, 0);
}

// ── TOC ──
function buildTOC() {
  const headings = document.querySelectorAll('#noteContent h1, #noteContent h2, #noteContent h3');
  const tocNav = document.getElementById('tocNav');
  const tocPanel = document.getElementById('tocPanel');

  if (tocObserver) { tocObserver.disconnect(); tocObserver = null; }

  if (headings.length < 2) {
    tocPanel.style.visibility = 'hidden';
    return;
  }
  tocPanel.style.visibility = '';

  headings.forEach((h, i) => { h.id = `h-${i}`; });

  tocNav.innerHTML = Array.from(headings).map(h => {
    const level = h.tagName.toLowerCase();
    return `<a class="toc-item toc-${level}" data-id="${h.id}">${h.textContent}</a>`;
  }).join('');

  tocNav.querySelectorAll('.toc-item').forEach(a => {
    a.addEventListener('click', () => {
      const target = document.getElementById(a.dataset.id);
      if (target) window.scrollTo({ top: target.offsetTop - 64, behavior: 'smooth' });
    });
  });

  tocObserver = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      const link = tocNav.querySelector(`[data-id="${entry.target.id}"]`);
      if (link) link.classList.toggle('toc-active', entry.isIntersecting);
    });
  }, { rootMargin: '-10% 0px -75% 0px' });

  headings.forEach(h => tocObserver.observe(h));
}

// ── Volver al índice ──
function showIndex() {
  document.getElementById('noteWrapper').classList.remove('active');
  if (tocObserver) { tocObserver.disconnect(); tocObserver = null; }
  document.getElementById('indexView').style.display = '';
  document.querySelector('.hero-row').style.display = ''; 
  document.getElementById('catHeader').style.display = 'none';  
  document.querySelectorAll('.nav-item').forEach(i => i.classList.remove('active'));
  document.querySelectorAll('.nav-child-item').forEach(i => i.classList.remove('active'));
  document.getElementById('nav-all').classList.add('active');
  currentFilter = 'all';
  document.getElementById('breadcrumbCat').textContent = 'inicio';
  document.getElementById('catGrid').style.display = '';
  document.getElementById('catSectionLabel').style.display = '';
  document.getElementById('notesSectionLabel').style.display = 'none';
  document.getElementById('totalNotes').textContent = notes.length;
  const categorias = [...new Set(notes.map(n => n.category))];
  document.getElementById('totalGroups').textContent = categorias.length;
  document.getElementById('groupsContainer').innerHTML = '';
  document.getElementById('recientesSection').style.display = '';
}

// ── Sidebar mobile ──
function openSidebar() {
  document.getElementById('sidebar').classList.add('open');
  document.getElementById('sidebarOverlay').classList.add('open');
}

function closeSidebar() {
  document.getElementById('sidebar').classList.remove('open');
  document.getElementById('sidebarOverlay').classList.remove('open');
}

// ── Arrancar ──
cargarNotas();