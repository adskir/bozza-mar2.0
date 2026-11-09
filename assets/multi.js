(() => {
  const $ = (s, r = document) => r.querySelector(s), $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const WA = "393444084291";
  const burger = $("#burger"), nav = $("#nav");
  burger && burger.addEventListener("click", () => { const o = nav.classList.toggle("open"); burger.setAttribute("aria-expanded", o); });
  $$("[data-toggle]").forEach((box) => { const b = $$("button", box); b.forEach((x) => x.addEventListener("click", () => {
    b.forEach((y) => y.setAttribute("aria-pressed", y === x)); $$("[data-panel]").forEach((p) => (p.hidden = p.dataset.panel !== x.dataset.show)); })); });
  const OPTS = ["Lezione di prova", "Lezione privata", "Lezione online", "Viaja con MAR", "Evento / organizzatori", "Timba Criolla", "Folklore peruviano", "Mentoring", "Informazioni"];
  const m = $("#modal"), sel = $("#minterest"), f = $("#mform");
  OPTS.forEach((o) => { const e = document.createElement("option"); e.textContent = o; sel.appendChild(e); });
  $$("[data-modal]").forEach((b) => b.addEventListener("click", () => { sel.value = b.dataset.modal; $("#mtitle").textContent = b.textContent.trim(); m.showModal(); }));
  f.addEventListener("submit", (e) => {
    if (e.submitter && e.submitter.value === "cancel") return;
    e.preventDefault(); const d = new FormData(f);
    const t = `Ciao Mar! Ti scrivo dal sito.\n• Nome: ${d.get("nome")}\n• Interesse: ${d.get("interesse")}` + (d.get("telefono") ? `\n• Telefono: ${d.get("telefono")}` : "") + (d.get("messaggio") ? `\n• ${d.get("messaggio")}` : "");
    window.open(`https://wa.me/${WA}?text=${encodeURIComponent(t)}`, "_blank"); m.close();
  });
})();
