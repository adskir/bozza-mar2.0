import json, os, re, shutil, sys
SRC = "/home/claude/bozza-mar"; OUT = sys.argv[1]
shutil.rmtree(OUT, ignore_errors=True); os.makedirs(OUT)
shutil.copytree(f"{SRC}/_site/assets", f"{OUT}/assets", ignore=shutil.ignore_patterns("app.js","audio"))
site_html = open(f"{SRC}/_site/index.html", encoding="utf8").read()
social = re.search(r'<ul class="social mini".*?</ul>', site_html, re.S).group(0)
wa_icon = re.search(r'<a class="wa-fab".*?(<svg.*?</svg>)', site_html, re.S).group(1)
prezzi = json.load(open(f"{SRC}/src/_data/prezzi.json"))
old = json.load(open(sys.argv[2]))
online = old["online"]; online["include"] = [x for x in online["include"] if "fondatore" not in x]

NAV = [("lezioni-private.html","Lezioni Private"),("chi-sono.html","Chi sono"),("viaja-con-mar.html","Viaja con MAR"),("timba-criolla.html","Timba Criolla"),("folklore-peruviano.html","Folklore"),("mentoring.html","Mentoring"),("organizzatori.html","Organizzatori")]
FOOT = NAV + [("privacy.html","Privacy e cookie")]
PH = lambda t: f'<span class="ph">[{t}]</span>'

def page(fname, title, body, active=None):
    nav = "".join(f'<a href="{h}"{" aria-current=\"page\"" if h==active else ""}>{t}</a>' for h,t in NAV)
    foot = "".join(f'<a href="{h}">{t}</a>' for h,t in FOOT)
    html = f'''<!doctype html><html lang="it"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow"><title>{title} · Mar La Criolla</title>
<link rel="stylesheet" href="assets/style.css"><link rel="stylesheet" href="assets/multi.css"></head>
<body><a class="skip" href="#main">Vai al contenuto</a>
<header class="top"><div class="wrap">
<a class="brand logo" href="index.html"><img src="assets/img/logo-timba-criolla.webp" alt="Timba Criolla · Mar La Criolla" width="1200" height="711"></a>
<nav class="nav" id="nav" aria-label="Menu principale">{nav}</nav>
<button class="burger" id="burger" aria-label="Apri il menu" aria-expanded="false" aria-controls="nav"><span></span><span></span></button>
</div></header>
<main id="main">{body}</main>
<footer class="foot"><div class="wrap">
<div><img class="foot-logo" src="assets/img/logo-timba-criolla.webp" alt="Timba Criolla" width="1200" height="711" loading="lazy">
<p>Timba, salsa cubana, bachata e folklore peruviano.<br>Bari e online.</p>
<p class="contacts" id="contatti"><a href="https://wa.me/393444084291">WhatsApp +39 344 408 4291</a><br>{PH("email")}</p></div>
<nav aria-label="Menu">{foot}</nav>
<div class="foot-social">{social}</div>
<p class="credit">© 2026 Mar La Criolla · Sito realizzato da <a href="https://clickbari.it" target="_blank" rel="noopener">ClickBari</a></p>
</div></footer>
<a class="wa-fab" href="https://wa.me/393444084291" target="_blank" rel="noopener" aria-label="Scrivi a Mar su WhatsApp">{wa_icon}<span>Scrivimi</span></a>
<dialog class="modal" id="modal"><form method="dialog" class="mform" id="mform" name="contatto" data-netlify="true">
<button class="mclose" value="cancel" aria-label="Chiudi">×</button>
<h3 id="mtitle">Scrivimi</h3><p class="msub">Lascia i tuoi dati: ti rispondo su WhatsApp.</p>
<label>Nome<input name="nome" required autocomplete="given-name" placeholder="Il tuo nome"></label>
<label>Telefono<input name="telefono" type="tel" autocomplete="tel" placeholder="+39 …"></label>
<label>Ti interessa<select name="interesse" id="minterest"></select></label>
<label><span>Messaggio <i>(facoltativo)</i></span><textarea name="messaggio" rows="3" placeholder="Raccontami cosa cerchi…"></textarea></label>
<button class="btn wa-send" type="submit" value="send">{wa_icon}<span>Invia su WhatsApp</span></button>
<small>Nella versione finale la richiesta si salva anche nel sito (Netlify Forms) e arriva a Mar per email.</small>
</form></dialog>
<script src="assets/multi.js"></script></body></html>'''
    open(f"{OUT}/{fname}","w",encoding="utf8").write(html)

def cta(label, interest, cls="btn"):
    return f'<button class="{cls}" type="button" data-modal="{interest}">{label}</button>'

def hero(kicker, h1, sub, btns, side=""):
    return f'''<section class="hero ph-hero"><div class="wrap"><div>
<p class="kick">{kicker}</p><h1>{h1}</h1>{sub}<div class="cta">{btns}</div></div>
<div class="portrait"><div class="ph-img">{PH("foto di Mar")}</div>{side}</div></div></section>'''

trust = '<ul class="trust"><li><b>Bicampionessa</b> di Timba</li><li><b>Oltre 550</b> allievi</li><li>Balla <b>dal 2014</b></li></ul>'
facts = '''<div class="wrap facts"><div class="f-stats">
<div><b>2014</b><span>balla il folklore peruviano</span></div><div><b>2015</b><span>salsa e bachata</span></div>
<div><b>2019</b><span>inizia a insegnare</span></div><div><b>550+</b><span>allievi formati</span></div>
<div><b>4</b><span>paesi: Spagna, Perù, Germania e Italia</span></div></div>
<ul class="f-awards">
<li><i>1°</i><div><b>Bicampionessa di Timba</b><span>1° posto come solista nella competizione di Timba 1vs1 al Timbeando Festival 2020 e 2024</span></div></li>
<li><i>1°</i><div><b>Riconoscimento internazionale</b><span>1° posto alla competizione internazionale online Ven Baila Cuba 2020</span></div></li>
<li><i>1°</i><div><b>Radici e tradizione</b><span>1° posto in competizioni di folklore peruviano (modalità gruppo, festejo e marinera nella categoria singolo)</span></div></li>
</ul></div>'''

doors = [("lezioni-private.html","Lezioni Private","In presenza a Bari e online.","Disponibile"),
         ("viaja-con-mar.html","Viaja con MAR","Biglietti e codici sconto per congressi di salsa e timba.","Disponibile"),
         ("timba-criolla.html","Timba Criolla","Cuba & Peru Dance Fusion: il mio progetto.","Progetto"),
         ("organizzatori.html","Per gli Organizzatori","Workshop, show, giuria e social dancing.","Eventi"),
         ("folklore-peruviano.html","Folklore peruviano","Marinera, festejo e le radici del Perù.","Lezioni"),
         ("mentoring.html","Mentoring","Per chi insegna: metodo e correzione tecnica.","Insegnanti")]
doors_html = "".join(f'<a class="door{" big" if i<2 else ""}" href="{h}"><span class="state">{s}</span><h3>{t}</h3><p>{d}</p></a>' for i,(h,t,d,s) in enumerate(doors))
reviews = "".join(f'<figure class="rev"><div class="stars">★★★★★</div><blockquote>{PH("recensione reale da Google")}</blockquote><figcaption>{PH("nome")} · Google</figcaption></figure>' for _ in range(4))

# --- home
page("index.html","Corso di Salsa e Bachata a Bari", hero(
 "Bari · Online",
 "Corso di Salsa e Bachata a <em>Bari</em>",
 '<p class="lead">Lezioni private di Timba, Salsa Cubana, Bachata e Folklore Peruviano a Bari. Impara più in fretta con un\'insegnante bicampionessa di Timba.</p>'+trust,
 cta("Prenota una lezione","Lezione privata")+'<a class="btn ghost" href="#percorsi">Scopri cosa faccio</a>',
 '<div class="tag"><b>Mar La Criolla</b><span>Fondatrice di Timba Criolla</span></div>')+
 f'''<section id="percorsi"><div class="wrap"><h2>Cosa posso fare per te</h2><p class="sub">Due obiettivi principali: le lezioni private e Viaja con MAR. E tutto il mondo di Timba Criolla.</p>
<div class="doors six">{doors_html}</div></div></section>
<section class="dark-sec"><div class="wrap"><h2>Chi sono</h2><p class="sub">Sono Mar - La Criolla, ballerina e insegnante di Timba, salsa cubana, bachata e folklore peruviano. Sono fondatrice del progetto Timba Criolla.</p></div>{facts.replace('wrap facts','wrap facts on-dark')}<div class="wrap"><a class="btn mango" href="chi-sono.html">La mia storia</a></div></section>
<section id="recensioni"><div class="wrap"><h2>Dicono di me</h2><p class="sub">Le ultime 4 recensioni dalla scheda Google, aggiornate in automatico.</p><div class="revs">{reviews}</div></div></section>
<section class="final"><div class="wrap"><h2>Balliamo insieme?</h2><p class="sub">Scrivimi: ti aiuto a trovare la strada giusta per te.</p><div class="cta">{cta("Scrivimi","Informazioni","btn mango")}</div></div></section>''')

# --- lezioni private (tabs)
def plist(k): 
    return "".join(f'<div class="pitem{" top" if v.get("top") else ""}"><div><b>{v["nome"]}</b><small>{v["desc"]}</small></div><div class="eur">{v["prezzo"]} €</div></div>' for v in k["voci"])
def inc(k): return "".join(f"<li>{i}</li>" for i in k["include"])
steps = [("Scegli il formato","In presenza a Bari o online."),("Definiamo gli obiettivi","Disegniamo il tuo piano personalizzato."),("Scegli l'orario","Troviamo il momento migliore per te."),("Inizi le lezioni","Impari con accompagnamento e feedback."),("Evolvi","Un progresso misurabile e sostenibile.")]
page("lezioni-private.html","Lezioni private", hero("Lezioni Private","Lezioni private di salsa e bachata, <em>a Bari e online</em>",
 '<p class="lead">Un percorso adattato al 100% a te.</p>'+trust, cta("Prenota la prova","Lezione di prova")) +
 f'''<section id="prezzi"><div class="wrap"><div class="price-head"><div><h2>Prezzi chiari, senza sorprese</h2><p class="sub">Scegli la modalità più adatta al tuo momento.</p></div>
<div class="toggle" data-toggle role="group" aria-label="Modalità"><button aria-pressed="true" data-show="presenza">In presenza</button><button aria-pressed="false" data-show="online">Online</button></div></div>
<div class="prices" data-panel="presenza"><div class="plist">{plist(prezzi["presenza"])}</div><details class="include"><summary>Cosa include ogni lezione</summary><ul class="checks">{inc(prezzi["presenza"])}</ul></details></div>
<div class="prices" data-panel="online" hidden><div class="plist">{plist(online)}</div><details class="include"><summary>Cosa include la lezione online</summary><ul class="checks">{inc(online)}</ul></details></div>
<div class="cta">{cta("Prenota la tua lezione","Lezione privata")}</div></div></section>
<section class="dark-sec"><div class="wrap"><h2>Il metodo in 5 passi</h2><ol class="tracks">{"".join(f'<li><span>{i+1:02d}</span><div><b>{a}</b><small>{b}</small></div><time></time></li>' for i,(a,b) in enumerate(steps))}</ol></div></section>''',"lezioni-private.html")

# --- chi sono
page("chi-sono.html","Chi sono", hero("Chi sono","Sono <em>Mar - La Criolla</em>",
 '<p class="lead">Ballerina e insegnante di Timba, salsa cubana, bachata e folklore peruviano. Sono fondatrice del progetto Timba Criolla.</p>',
 cta("Scrivimi","Informazioni")) +
 f'''<section><div class="wrap narrow"><h2>Alcuni fatti su di me</h2><p class="sub" style="margin-top:14px">Il ballo mi ha cambiato la vita e, da allora, il mio obiettivo è condividerlo con chi vuole imparare davvero, curando sia la tecnica sia l'aspetto umano. Credo fermamente che il ballo sia per tutti. La mia ispirazione nasce dalla vita di ogni giorno, dagli artisti che ammiro e dalle esperienze vissute.</p>
</div>{facts}
<div class="wrap narrow"><h2 style="margin-top:40px">Certificati e premi</h2><div class="gallery">{"".join(f'<div class="ph-img small">{PH("certificato / foto premio")}</div>' for _ in range(3))}</div>
<p class="sub" style="margin-top:28px">Sono disponibile per Workshop, show, giuria &amp; social dancing.</p><div class="cta"><a class="btn" href="organizzatori.html">Per gli organizzatori</a></div></div></section>''',"chi-sono.html")

# --- viaja con mar
ev = "".join(f'<div class="card ev"><span class="who">{PH("data · città")}</span><h3>{PH("nome congresso / festival")}</h3><p>{PH("salsa / timba · descrizione breve")}</p><div class="code">Codice sconto: <b>{PH("CODICE")}</b></div>{cta("Voglio il biglietto","Viaja con MAR","btn small")}</div>' for _ in range(3))
page("viaja-con-mar.html","Viaja con MAR", hero("Viaja con MAR","Viaggia con me ai <em>congressi di salsa e timba</em>",
 f'<p class="lead">Promozione e vendita di biglietti e codici sconto per congressi di salsa e timba.</p><p class="sub">{PH("come funziona: biglietti, sconti, viaggio insieme")}</p>',
 cta("Chiedi informazioni","Viaja con MAR")) +
 f'''<section><div class="wrap"><h2>Prossimi eventi</h2><div class="grid3">{ev}</div>
<p class="demo-note" style="margin-top:20px">Nota legale: se i codici sono di affiliazione, va scritto in modo chiaro sul sito.</p></div></section>''',"viaja-con-mar.html")

# --- timba criolla
page("timba-criolla.html","Timba Criolla", hero("Il progetto","Timba Criolla · <em>Cuba &amp; Peru Dance Fusion</em>",
 f'<p class="lead">{PH("cos\'è Timba Criolla, con parole di Mar")}</p><p class="sub">{PH("una frase: cos\'è la timba, per chi non l\'ha mai ballata")}</p>',
 '<a class="btn" href="https://www.youtube.com/@timbacriolla_it" target="_blank" rel="noopener">Guarda su YouTube</a>'+cta("Scrivimi","Timba Criolla","btn ghost")) +
 f'''<section><div class="wrap"><h2>Video</h2><div class="gallery">{"".join(f'<div class="ph-img video">{PH("video YouTube")}</div>' for _ in range(3))}</div></div></section>''',"timba-criolla.html")

# --- organizzatori
svc = [("Workshop","Lezioni per la tua scuola o il tuo festival."),("Show","Esibizioni per eventi e serate."),("Giuria","Giudice per competizioni di timba e salsa."),("Social dancing","Presenza alle tue serate e ai congressi.")]
cards = "".join(f'<div class="card"><span class="who">{a}</span><h3>{a}</h3><p>{PH(b)}</p></div>' for a,b in svc)
page("organizzatori.html","Per gli Organizzatori", hero("Per gli Organizzatori","Porta Mar La Criolla <em>al tuo evento</em>",
 '<p class="lead">Sono disponibile per Workshop, show, giuria &amp; social dancing.</p>'+trust, cta("Richiedi disponibilità","Evento / organizzatori")) +
 f'''<section><div class="wrap"><h2>Cosa posso portare</h2><div class="grid2">{cards}</div>
<h2 style="margin-top:44px">Dove ho insegnato</h2><p class="sub">Spagna, Perù, Germania e Italia. {PH("scuole, festival, congressi")}</p>
<div class="cta">{cta("Richiedi disponibilità","Evento / organizzatori")}</div></div></section>''',"organizzatori.html")

# --- folklore
page("folklore-peruviano.html","Folklore peruviano", hero("Radici e tradizione","Folklore <em>peruviano</em> a Bari",
 f'<p class="lead">Marinera, festejo ed espressione culturale con tecnica e radici.</p><p class="sub">Ballo folklore peruviano dal 2014. {PH("lezioni private, gruppi, eventi?")}</p>',
 cta("Chiedi informazioni","Folklore peruviano")) +
 f'''<section><div class="wrap"><div class="grid2"><div class="card"><span class="who">Marinera</span><h3>Marinera</h3><p>{PH("descrizione")}</p></div><div class="card"><span class="who">Festejo</span><h3>Festejo</h3><p>{PH("descrizione")}</p></div></div>
<p class="sub" style="margin-top:24px">1° posto in competizioni di folklore peruviano (modalità gruppo, festejo e marinera nella categoria singolo).</p></div></section>''',"folklore-peruviano.html")

# --- mentoring
page("mentoring.html","Mentoring per insegnanti", hero("Mentoring","Mentoring <em>per chi insegna</em>",
 '<p class="lead">Revisione della tua metodologia, risorse didattiche, correzione tecnica e strumenti per lezioni più chiare e sicure.</p>',
 cta("Chiedi informazioni","Mentoring")) +
 f'''<section><div class="wrap"><ul class="checks big">{"".join(f"<li>{x}</li>" for x in ["Revisione della tua metodologia","Risorse didattiche","Correzione tecnica","Strumenti per lezioni più chiare e sicure"])}</ul><p class="sub" style="margin-top:20px">{PH("formato, durata, prezzo")}</p></div></section>''',"mentoring.html")

# --- privacy (dal landing)
pv = open(f"{SRC}/_site/privacy/index.html",encoding="utf8").read()
body = re.search(r'<main id="main">(.*)</main>', pv, re.S).group(1).replace('href="/"','href="index.html"')
page("privacy.html","Privacy e cookie", body)
print("ok", sorted(os.listdir(OUT)))
