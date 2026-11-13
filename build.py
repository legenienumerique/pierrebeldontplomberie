"""Générateur de la maquette Pierre Beldont Plomberie. Usage : python build.py <dossier-du-projet>
Contenus relevés en novembre 2026 : ancien site pierre-beldont-plomberie.fr (archives Wayback 2019-2021 : textes,
prestations, logo, couleurs cuivre #a85332 et bleu #4893a1, police Open Sans), fiche Google (avis, note 4,7).
Les deux photos d'outils viennent de l'ancien site (pas de photo de chantier disponible)."""
import os
import sys
OUT = sys.argv[1] if len(sys.argv) > 1 else "."
A = 'assets/'
PH = A + 'ph/'
V = 5  # cache : incrémenter à chaque changement de CSS ou JS
TEL, TELH = '06 25 22 00 17', 'tel:0625220017'
MAIL = 'beldontpierre@gmail.com'
ADR = ('113 rue Pasteur', '01400 Châtillon-sur-Chalaronne')

NAV = [('plomberie.html', 'Plomberie'), ('chauffage.html', 'Chauffage'), ('salles-de-bains.html', 'Salles de bains')]
PHONE_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.1.4 2.3.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1A17 17 0 0 1 3 4c0-.6.4-1 1-1h3.5c.6 0 1 .4 1 1 0 1.3.2 2.5.6 3.6.1.3 0 .7-.2 1z" fill="currentColor"/></svg>'


def pill(t, href, cls='', arrow='↗'):
    return f'<a class="pill {cls}" href="{href}"><span class="r"><span>{t}</span><span>{t}</span></span><b>{arrow}</b></a>'


def tile(src, cls='', style='', alt='', par=None, lazy=True):
    p = f' data-par="{par}" style="height:118%;width:100%"' if par else ''
    return f'<figure class="tile {cls}" style="{style}"><img src="{src}" alt="{alt}"{p}{" loading=lazy" if lazy else ""}></figure>'


def logo(cls=''):
    return f'<span class="lgo {cls}" aria-hidden="true"><i><img src="{A}logo.png" alt=""></i><span><span class="wm">Pierre Beldont</span><small>Plomberie · Chauffage</small></span></span>'


def head(title, desc, cur):
    def a(h, t, cls=''):
        return f'<a href="{h}"{" class="+cls if cls else ""}{" aria-current=page" if h == cur else ""}>{t}</a>'
    items = a('index.html', 'Accueil') + ''.join(a(h, t) for h, t in NAV) + a('contact.html', 'Devis gratuit', 'hl')
    return f'''<!doctype html>
<html lang="fr"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:type" content="website">
<meta name="theme-color" content="#14100e">
<meta name="robots" content="noindex, nofollow">
<link rel="icon" href="{A}logo.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{A}style.css?v={V}">
</head><body>
<div class="pipe" aria-hidden="true"><div class="pp"><i class="drop"></i></div></div>
<header class="top">
<a class="logo" href="index.html" aria-label="Pierre Beldont Plomberie, accueil">{logo()}</a>
<nav class="nav" aria-label="Navigation principale">{items}</nav>
<span class="side"><a class="tel" href="{TELH}" aria-label="Appeler le {TEL}">{PHONE_SVG}<span>{TEL}</span></a></span>
<button class="burger" aria-label="Menu" aria-expanded="false"><i></i><i></i></button>
</header>
<main>'''


def foot():
    return f'''</main>
<footer><div class="wrap"><div class="fg">
<div>{logo('big')}<p>Plombier chauffagiste à Châtillon-sur-Chalaronne, pour les particuliers et les professionnels. Neuf, rénovation et dépannage, dans un rayon de 15 km.</p></div>
<div><h4 class="micro">Prestations</h4><ul><li><a href="plomberie.html">Plomberie</a></li><li><a href="chauffage.html">Chauffage et climatisation</a></li><li><a href="salles-de-bains.html">Salles de bains</a></li><li><a href="plomberie.html#adoucisseur">Adoucisseurs d’eau</a></li><li><a href="chauffage.html#fumisterie">Poêles et fumisterie</a></li></ul></div>
<div><h4 class="micro">Contact</h4><ul><li><a href="{TELH}">{TEL}</a></li><li><a href="mailto:{MAIL}">{MAIL}</a></li><li><a href="contact.html">Demander un devis</a></li></ul></div>
<div><h4 class="micro">Atelier</h4><ul><li>{ADR[0]}</li><li>{ADR[1]}</li><li>Du lundi au vendredi</li></ul></div>
</div></div>
<div class="fw" aria-hidden="true">BELDONT</div>
<div class="fb micro"><span class="pad">© Pierre Beldont Plomberie</span><span class="pad">Maquette de site · Le Génie Numérique</span></div></footer>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>
<script src="https://unpkg.com/lenis@1.1.13/dist/lenis.min.js"></script>
<script src="{A}main.js?v={V}"></script></body></html>'''


def cta(t='Une fuite ? <em>On arrive.</em>'):
    return f'''<section class="sec cta"><div class="wrap"><span class="micro mute" style="display:block;margin-bottom:1.6rem">Devis gratuit · rappel gratuit · 15 km autour de Châtillon</span><h2 class="sp">{t}</h2>
<div class="row rv">{pill('Demander un devis', 'contact.html', 'blue')}{pill(TEL, TELH, 'ghost')}</div></div></section>'''


def pagehead(crumb, h1, lead, img, img2=None, extra=''):
    t2 = tile(img2, 'small', lazy=False) if img2 else ''
    return f'''<section class="ph"><div class="wrap"><div class="crumb micro"><a href="index.html">Accueil</a> / {crumb}</div><h1 class="sp">{h1}</h1><p class="lead rv">{lead}</p>{extra}</div>{tile(img, lazy=False)}{t2}</section>'''


def faq(its):
    return '<div class="faq">' + ''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in its) + '</div>'


# avis Google publiés (prénom affiché par l'auteur), relevés le 13/11/2026
AVIS = [('Geoffrey C.', '2021', 'Contacté la veille pour le lendemain, Pierre a su se rendre disponible rapidement et a été ponctuel. Venu pour un problème de bouchon dans nos canalisations, Pierre a fait preuve de persévérance et y a passé un long moment, jusqu’à la bonne évacuation du problème ! Un professionnel de confiance à contacter que je vous recommande.'),
        ('Chantal J.', '2025', 'Intervention très rapide pour une fuite bien mystérieuse. À suivre. Très pro, a tout contrôlé. Merci encore.'),
        ('Françoise R.', '2025', 'Merci pour votre disponibilité et votre efficacité sans nous assommer de frais. Bon travail. À recommander.'),
        ('Kwyze', '2026', 'Agréable, homme d’expérience, problème résolu en 10 min.'),
        ('Rithy B.', '2025', 'Efficace, rapide, de bon conseil !'),
        ('Patrick T.', '2021', 'Aucun problème bon travail donc bon plombier et de bons conseils.')]


def avis_cards(items):
    return '<div class="rcs">' + ''.join(f'<blockquote class="rc rv"><span class="micro mute">Google · {d}</span><p>« {t} »</p><footer><b>{n}</b><span>Avis Google</span><i>5/5</i></footer></blockquote>' for n, d, t in items) + '</div>'


PRESTA = [('Plombier', '(neuf, rénovation, dépannage)'), ('Salles de bains', 'clé en main'), ('Adoucisseurs d’eau', ': installation et réglage'),
          ('Bureau d’études', 'spécialisé chauffage et climatisation'), ('Poêles', 'et fumisterie')]


def service(file, title, desc, crumb, h1, lead, img, img2, intro_h, intro_p, checks, faqs, more=''):
    extra = f'<div class="row rv" style="display:flex;gap:10px;flex-wrap:wrap;margin-top:2.2rem">{pill("Demander un devis", "contact.html", "blue")}{pill(TEL, TELH, "ghost")}</div>'
    cl = ''.join(f'<li><span><b>{a}</b> {b}</span></li>' for a, b in checks)
    return head(title, desc, file) + pagehead(crumb, h1, lead, img, img2, extra) + f'''
<section class="sec"><div class="wrap split"><div><span class="micro mute" style="display:block;margin-bottom:1.2rem">Notre métier</span><h2 class="sp">{intro_h}</h2><p class="lead rv" style="margin-top:1.4rem">{intro_p}</p></div><ul class="checks rv">{cl}</ul></div></section>{more}
<section class="sec" style="padding-top:0"><div class="wrap split"><div><span class="micro mute" style="display:block;margin-bottom:1.2rem">Questions fréquentes</span><h2 class="sp">On vous <em>répond</em></h2></div><div class="rv">{faq(faqs)}</div></div></section>''' + cta() + foot()


FAQ_ZONE = ('Où intervenez-vous ?', 'À Châtillon-sur-Chalaronne et dans un rayon de 15 km autour, chez les particuliers comme chez les professionnels.')
FAQ_DEVIS = ('Le devis est-il gratuit ?', f'Oui. Appelez le {TEL} ou remplissez le formulaire : nous vous rappelons gratuitement.')
FAQ_GAR = ('Vos travaux sont-ils garantis ?', 'Oui, nous proposons des garanties sur les travaux réalisés.')


def pages():
    P = {}
    hero_tiles = [('t1', 'logo'), ('t4', 'outils'), ('t5', 'robinet')]
    ht = ''.join(f'<figure class="tile {c}{" lg" if f == "logo" else ""}"><div class="fl"><div class="in"><img src="{A + "logo.png" if f == "logo" else PH + f + ".webp"}" alt=""></div></div></figure>' for c, f in hero_tiles)
    items = [('plomberie.html', '01', 'Plomberie', 'Neuf, rénovation, dépannage en cas d’urgence.', 'robinet'),
             ('chauffage.html', '02', 'Chauffage', 'Chaudières, poêles, climatisation, bureau d’études.', 'outils'),
             ('salles-de-bains.html', '03', 'Salles de bains', 'Clé en main, selon vos envies et votre budget.', 'robinet'),
             ('plomberie.html#adoucisseur', '04', 'Adoucisseurs', 'Fini le calcaire, vos tuyaux vous disent merci.', 'outils'),
             ('chauffage.html#fumisterie', '05', 'Fumisterie', 'Conduits de fumée, poêles, cheminées, en sécurité.', 'robinet')]
    pl = ''.join(f'<a href="{h}"><span class="micro mute">{n}</span><span class="nm">{t}</span><span class="d">{d}</span></a>' for h, n, t, d, _ in items)
    prev = ''.join(tile(f'{PH}{it[4]}.webp', 'on' if i == 0 else '') for i, it in enumerate(items))
    steps = [('Expertise', 'Des travaux réalisés quelle que soit leur complexité.'),
             ('Savoir-faire', 'La maîtrise des techniques, et le bon matériel.'),
             ('Garanties', 'Des garanties sur les travaux réalisés.'),
             ('Finitions', 'Impeccables, dans un souci de qualité.')]
    st = ''.join(f'<div class="stp"><div class="n">{i + 1}</div><h3>{t}</h3><p>{d}</p></div>' for i, (t, d) in enumerate(steps))
    mq = ''.join(f'<span>{x}</span>' for x in ['Plomberie', 'Chauffage', 'Climatisation', 'Salles de bains', 'Adoucisseurs', 'Fumisterie', 'Dépannage'] * 2)

    P['index.html'] = head('Pierre Beldont Plomberie — Plombier chauffagiste à Châtillon-sur-Chalaronne (Ain)', 'Pierre Beldont Plomberie, plombier chauffagiste à Châtillon-sur-Chalaronne : plomberie, chauffage, climatisation, salles de bains clé en main, adoucisseurs, fumisterie. Devis gratuit, 4,7/5 sur Google.', 'index.html') + f'''
<section class="hero">
<div class="cap micro c1"><b>Plombier chauffagiste</b>à Châtillon-sur-Chalaronne</div>
<div class="cap micro c2"><b>4,7 / 5</b>14 avis Google</div>
<div class="cap micro c3"><b>15 km</b>autour de Châtillon</div>
<div class="go">{pill('Devis gratuit', 'contact.html')}</div>
{ht}
<p class="para">Neuf, rénovation et dépannage. Le partenaire des particuliers et des professionnels.</p>
<h1 class="word">BELDONT</h1>
<div class="scrollhint micro"><i></i>Défiler</div>
</section>

<div class="mq" aria-hidden="true"><div>{mq}</div></div>

<section class="sec"><div class="wrap fin"><div><span class="micro mute" style="display:block;margin-bottom:1.4rem">Châtillon-sur-Chalaronne et environs</span><h2 class="sp">Nous mènerons <em>à bien vos travaux</em></h2>
<p class="lead rv" style="margin:1.4rem 0 2rem">Plombiers chauffagistes qualifiés et expérimentés, nous assurons la qualité des travaux réalisés. Professionnalisme, efficacité et réactivité sont nos mots d’ordre.</p>
<ul class="checks rv" style="margin-bottom:2rem"><li><span><b>Particuliers et professionnels</b>, dans le neuf comme en rénovation.</span></li><li><span><b>Un bureau d’études</b> pour le chauffage et la climatisation.</span></li><li><span><b>Le bon matériel</b>, pour intervenir dans d’excellentes conditions.</span></li></ul>{pill('Nos prestations', '#services', 'blue')}</div>{tile(PH + 'outils.webp', '', par=8, alt='Outils et raccords de plomberie')}</div></section>

<section class="story"><span class="micro mute m3">L’atelier</span>
<h2><span class="w">Un</span> <span class="w">tuyau</span> <span class="w">qui</span> <span class="w"><em>fuit</em></span> <span class="w"><em>?</em></span></h2>
<div class="stack">{tile(PH + 'robinet.webp')}{tile(PH + 'outils.webp')}<figure class="tile lg"><img src="{A}logo.png" alt="" loading="lazy"></figure></div>
<p class="micro mute m1">Dépannage en cas d’urgence : panne, fuite, dysfonctionnement d’un équipement.</p><span class="micro mute m2">Rayon de 15 km</span></section>

<section class="sec" id="services"><div class="wrap"><span class="micro mute" style="display:block;margin-bottom:1.4rem">Un large domaine de compétences</span><h2 class="sp" style="margin-bottom:clamp(2rem,5vw,4rem)">Qu’est-ce qu’on <em>répare ?</em></h2>
<div class="plist">{pl}</div></div><div class="prev">{prev}</div></section>

<section class="sec"><div class="wrap"><span class="micro mute" style="display:block;margin-bottom:1.4rem">Avis Google</span><h2 class="sp">Ils nous <em>font confiance</em></h2>
<div class="cnt rv"><div><b data-to="4.7">0</b><span>sur 5, note moyenne sur Google</span></div><div><b data-to="14">0</b><span>avis publiés sur Google</span></div><div><b data-to="15">0</b><span>kilomètres autour de Châtillon-sur-Chalaronne</span></div></div>
<div style="margin-top:clamp(2rem,4vw,3rem)">{avis_cards(AVIS[:3])}</div><div style="margin-top:16px">{avis_cards(AVIS[3:])}</div></div></section>

<section class="sec" style="padding-top:0"><div class="wrap"><span class="micro mute" style="display:block;margin-bottom:1.4rem">4 raisons de nous confier les travaux</span><h2 class="sp">Du travail <em>bien fait</em></h2><div class="steps">{st}</div></div></section>
{cta()}''' + foot()

    adou = f'''
<section class="sec" id="adoucisseur" style="padding-top:0"><div class="wrap fin"><div><span class="micro mute" style="display:block;margin-bottom:1.2rem">Adoucisseurs d’eau</span><h2 class="sp">Un équipement <em>indispensable</em></h2>
<p class="lead rv" style="margin-top:1.4rem">Pour en finir avec le calcaire et prolonger la durée de vie des tuyaux, des équipements de plomberie et de l’électroménager. Nous travaillons étape par étape (raccordement, fixation, branchement) pour un réglage précis et une installation sûre.</p></div>{tile(PH + 'outils.webp', '', par=8, alt='Raccords et outils de plomberie')}</div></section>'''
    P['plomberie.html'] = service('plomberie.html', 'Plombier à Châtillon-sur-Chalaronne — Pierre Beldont Plomberie', 'Plomberie neuf, rénovation et dépannage, installation d’adoucisseurs d’eau. Pierre Beldont Plomberie, Châtillon-sur-Chalaronne (Ain), 15 km autour.',
        'Plomberie', 'Plombier <em>à Châtillon</em>', 'Passez par un plombier professionnel pour la réussite de vos travaux. Pierre Beldont Plomberie répond à toutes vos demandes.', PH + 'robinet.webp', PH + 'outils.webp',
        'Neuf, rénovation, <em>dépannage</em>', 'Dans le neuf, nous installons équipements sanitaires, canalisations, tuyauteries et robinetterie, et assurons leur mise en service. Nous rénovons tout système de plomberie et intervenons en urgence : panne, fuite, dysfonctionnement.',
        [('Équipements sanitaires', ', canalisations et tuyauteries.'), ('Robinetterie', ': pose et mise en service.'), ('Rénovation', 'de tout système de plomberie.'), ('Dépannage', 'en cas d’urgence.')],
        [('Intervenez-vous en urgence ?', 'Oui, pour un dépannage : dysfonctionnement d’un équipement, panne, fuite d’eau.'), FAQ_ZONE, FAQ_GAR, FAQ_DEVIS], adou)

    fum = f'''
<section class="sec" id="fumisterie" style="padding-top:0"><div class="wrap fin"><div><span class="micro mute" style="display:block;margin-bottom:1.2rem">Poêles et fumisterie</span><h2 class="sp">Chauffer <em>en toute sécurité</em></h2>
<p class="lead rv" style="margin-top:1.4rem">Vous envisagez d’installer un poêle ou une cheminée ? Nous créons les conduits de fumée, installons l’appareil et vérifions l’étanchéité, pour une maison ou un local professionnel.</p></div>{tile(PH + 'robinet.webp', '', par=8, alt='Outils de chauffagiste')}</div></section>'''
    P['chauffage.html'] = service('chauffage.html', 'Chauffagiste à Châtillon-sur-Chalaronne — Pierre Beldont Plomberie', 'Installation et remplacement de chaudières, climatisation, poêles et fumisterie, bureau d’études. Pierre Beldont Plomberie, Châtillon-sur-Chalaronne (Ain).',
        'Chauffage', 'Chauffage et <em>climatisation</em>', 'Nous installons vos équipements (chaudières, poêles…) et assurons leur mise en marche. Puis nous vous conseillons pour une utilisation optimale.', PH + 'outils.webp', PH + 'robinet.webp',
        'Un bureau <em>d’études</em>', 'Notre bureau d’études spécialisé en chauffage et climatisation vous conseille sur la faisabilité des travaux et propose des solutions adaptées, pour des installations performantes et fonctionnelles.',
        [('Chaudières', ': installation et remplacement.'), ('Climatisation', ': installation et mise en service.'), ('Poêles', 'et cheminées.'), ('Conseil', 'pour une utilisation optimale.')],
        [('Remplacez-vous une ancienne chaudière ?', 'Oui : installation et remplacement de chaudières, avec mise en marche et conseils d’utilisation.'), FAQ_ZONE, FAQ_GAR, FAQ_DEVIS], fum)

    P['salles-de-bains.html'] = service('salles-de-bains.html', 'Salle de bains clé en main à Châtillon-sur-Chalaronne — Pierre Beldont Plomberie', 'Installation de salles de bains clé en main, selon vos envies, votre style et votre budget. Pierre Beldont Plomberie, Châtillon-sur-Chalaronne (Ain).',
        'Salles de bains', 'Salle de bains <em>clé en main</em>', 'Nous installons et équipons la salle de bains selon vos envies et la configuration de la pièce.', PH + 'robinet.webp', PH + 'outils.webp',
        'Selon <em>vos envies</em>', 'Tout le travail se base sur vos exigences, votre style et votre budget. Après notre intervention : une salle de bains fonctionnelle, un espace agréable propice au bien-être.',
        [('Plomberie sanitaire', 'et équipements de salle de bains.'), ('Adoucisseur', 'si besoin.'), ('Suivi rigoureux', 'du bon déroulement des travaux.'), ('Délais', 'convenus ensemble.')],
        [('Gérez-vous tout le chantier ?', 'Oui, c’est le principe du clé en main : nous installons et équipons la salle de bains de A à Z.'), FAQ_ZONE, FAQ_GAR, FAQ_DEVIS])

    P['contact.html'] = head('Devis gratuit — Pierre Beldont Plomberie, Châtillon-sur-Chalaronne', f'Demandez un devis gratuit à Pierre Beldont Plomberie, {ADR[0]}, {ADR[1]}. {TEL}.', 'contact.html') + pagehead('Devis gratuit', 'Votre devis, <em>gratuit</em>', 'Un travail soigné, un service répondant à vos attentes, un tarif adapté à votre budget.', PH + 'outils.webp') + f'''
<section class="sec" id="devis"><div class="wrap split"><div><span class="micro mute" style="display:block;margin-bottom:1.2rem">Coordonnées</span><h2 class="sp">Ou <em>un appel</em></h2>
<div class="contactline rv" style="margin-top:2rem"><a href="{TELH}">{TEL}</a><a href="mailto:{MAIL}">{MAIL}</a></div>
<p class="lead rv" style="margin-top:1.6rem">{ADR[0]}<br>{ADR[1]}</p>
<div class="hor rv"><span><b>Du lundi au vendredi</b> · 9 h – 18 h</span><span class="micro">Horaires de l’ancien site, à confirmer</span></div></div>
<form class="f calc rv" id="resa"><div class="fld"><label for="pr">Demande</label><select id="pr"><option>Dépannage</option><option>Plomberie</option><option>Chauffage ou climatisation</option><option>Salle de bains</option><option>Adoucisseur d’eau</option><option>Poêle ou fumisterie</option><option>Autre</option></select></div>
<div class="fld"><label for="pc">Précisions</label><textarea id="pc" rows="4" placeholder="Décrivez votre besoin"></textarea></div>
<div class="r2"><div class="fld"><label for="rn">Nom</label><input id="rn" required></div><div class="fld"><label for="rt">Téléphone</label><input id="rt" type="tel" required></div></div>
<label class="chk"><input type="checkbox" id="rap"> Je souhaite être rappelé gratuitement</label>
<button class="pill blue" type="submit" style="justify-self:start"><span class="r"><span>Envoyer</span><span>Envoyer</span></span><b>↗</b></button><div class="ok">Merci ! (Maquette : aucune demande n’est envoyée.)</div></form></div></section>''' + foot()
    return P


for k, v in pages().items():
    open(os.path.join(OUT, k), 'w', encoding='utf-8').write(v)
print('ok')
