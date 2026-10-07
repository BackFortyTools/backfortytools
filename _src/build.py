#!/usr/bin/env python3
"""Build static pages for Back Forty Tools. Run from repo root: python3 _src/build.py"""
import json, os, re, datetime
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC=os.path.join(ROOT,'_src')
SITE='https://backfortytools.com'
CSS=open(os.path.join(SRC,'site.css')).read()
FAVICON="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='6' fill='%232f5d3a'/%3E%3Cpath d='M8 22h16M8 17h16M8 12h16' stroke='%23eef6ee' stroke-width='3' stroke-linecap='round'/%3E%3C/svg%3E"
FONTS='https://fonts.googleapis.com/css2?family=Bitter:wght@500;700;800&family=Source+Sans+3:wght@400;600;700&display=swap'
TODAY=datetime.date.today().isoformat()
IMPACT_TAG='<script type="text/javascript">(function(i,m,p,a,c,t){c.ire_o=p;c[p]=c[p]||function(){(c[p].a=c[p].a||[]).push(arguments)};t=a.createElement(m);var z=a.getElementsByTagName(m)[0];t.async=1;t.src=i;z.parentNode.insertBefore(t,z)})(\'https://utt.impactcdn.com/P-A7917150-9175-4770-95e5-6a4ddcaab8cf1.js\',\'script\',\'impactStat\',document,window);impactStat(\'trackImpression\');</script>'

def page(slug, title, h1_title, desc, body, faqs=None, app_name=None, extra_schema=None):
    url=f'{SITE}/{slug}/' if slug else SITE+'/'
    graph=[]
    if app_name:
        graph.append({"@type":"WebApplication","name":app_name,"url":url,"applicationCategory":"UtilitiesApplication","operatingSystem":"Any","offers":{"@type":"Offer","price":"0","priceCurrency":"USD"},"description":desc,"isPartOf":{"@type":"WebSite","name":"Back Forty Tools","url":SITE+'/'}})
    if faqs:
        graph.append({"@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faqs]})
    if extra_schema: graph.extend(extra_schema)
    schema=json.dumps({"@context":"https://schema.org","@graph":graph},ensure_ascii=False) if graph else ''
    html=f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:title" content="{h1_title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:site_name" content="Back Forty Tools">
<meta name='impact-site-verification' value='7f219c73-b5ef-4933-9e98-e80d3054c940'>
<link rel="icon" href="{FAVICON}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{FONTS}">
{('<script type="application/ld+json">'+schema+'</script>') if schema else ''}
<style>
{CSS}
</style>
</head>
<body>
{body}
{IMPACT_TAG}
</body>
</html>
'''
    out=os.path.join(ROOT,slug,'index.html') if slug else os.path.join(ROOT,'index.html')
    os.makedirs(os.path.dirname(out),exist_ok=True)
    open(out,'w').write(html)
    return url

def faq_html(faqs):
    return '\n'.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q,a in faqs)

def header(kicker, h1, lede):
    return f'''<header>
  <div class="kicker"><a href="/" style="color:inherit;text-decoration:none">Back Forty Tools</a> · {kicker}</div>
  <h1>{h1}</h1>
  <p class="lede">{lede}</p>
</header>'''

def footer(sources):
    return f'''<footer>
  {sources} Estimates only.<br>
  Part of <a href="/">Back Forty Tools</a>, free calculators for the farm, the barn and the woods.
</footer>'''


AMZ_TAG='backfortytool-20'
import urllib.parse as _up
def affiliate(url):
    """Route every gear link through Amazon with the Associates tag until other programs approve."""
    if 'tractorsupply.com' in url:
        q=_up.unquote(url.split('/search/')[-1])
        url='https://www.amazon.com/s?k='+_up.quote_plus(q)
    if 'amazon.com' in url and 'tag=' not in url:
        url+=('&' if '?' in url else '?')+'tag='+AMZ_TAG
    return url

ICONS={
 'feeder':'<path d="M4 10h24l-3 14H7z"/><path d="M10 10V6h12v4"/><path d="M8 17h16"/>',
 'tarp':'<path d="M4 22l6-12h12l6 12z"/><path d="M4 22h24"/><path d="M10 10l6 12 6-12"/>',
 'tape':'<path d="M6 12h20v8H6z"/><path d="M10 12v3M14 12v5M18 12v3M22 12v5"/>',
 'ring':'<ellipse cx="16" cy="12" rx="11" ry="4"/><path d="M5 12v8c0 2.2 4.9 4 11 4s11-1.8 11-4v-8"/><path d="M5 16c0 2.2 4.9 4 11 4s11-1.8 11-4"/>',
 'grinder':'<path d="M6 12h14v10H6z"/><path d="M20 15h6l2 3-2 3h-6"/><path d="M9 12V7h8v5"/><circle cx="10" cy="17" r="1.5"/>',
 'sealer':'<path d="M4 14h24v8H4z"/><path d="M4 18h24"/><path d="M8 14v-4h16v4"/>',
 'hoist':'<path d="M16 4v6"/><path d="M8 10h16"/><path d="M8 10v4M24 10v4"/><path d="M6 14h4M22 14h4"/><path d="M16 10v18"/><path d="M12 28h8"/>',
 'bag':'<path d="M9 10h14l2 18H7z"/><path d="M12 10V7a4 4 0 018 0v3"/>',
 'door':'<path d="M8 4h16v24H8z"/><path d="M8 12h16"/><path d="M20 20h2"/>',
 'water':'<path d="M16 4s-8 9-8 15a8 8 0 0016 0c0-6-8-15-8-15z"/>',
 'carton':'<path d="M4 12h24v12H4z"/><path d="M4 12l4-5h16l4 5"/><circle cx="10" cy="18" r="2"/><circle cx="16" cy="18" r="2"/><circle cx="22" cy="18" r="2"/>',
 'thermo':'<path d="M13 5a3 3 0 016 0v13a5 5 0 11-6 0z"/><path d="M16 11v9"/>',
 'paper':'<path d="M6 8h20v16H6z"/><path d="M6 12h20M10 8v16"/>',
 'cooler':'<path d="M5 12h22v14H5z"/><path d="M5 17h22"/><path d="M9 12V9h14v3"/><path d="M14 20h4"/>',
 'meter':'<path d="M10 4h12v16H10z"/><path d="M14 20v8M18 20v8"/><path d="M13 9h6M13 13h6"/>',
 'rack':'<path d="M4 26h24"/><path d="M6 26V10M26 26V10"/><circle cx="11" cy="21" r="3"/><circle cx="17" cy="21" r="3"/><circle cx="22" cy="21" r="3"/><circle cx="14" cy="15" r="3"/><circle cx="20" cy="15" r="3"/>',
 'splitter':'<path d="M16 4l6 10H10z"/><path d="M16 14v10"/><path d="M8 24h16v4H8z"/>',
 'wire':'<circle cx="16" cy="16" r="9"/><circle cx="16" cy="16" r="3"/><path d="M25 16h3M4 16h3"/>',
 'charger':'<path d="M8 8h16v16H8z"/><path d="M17 11l-4 6h6l-4 6"/>',
 'seed':'<path d="M16 28V14"/><path d="M16 14c-6 0-9-4-9-9 5 0 9 3 9 9z"/><path d="M16 18c6 0 9-4 9-9-5 0-9 3-9 9z"/>',
 'stick':'<path d="M16 4v24"/><path d="M12 8h4M12 12h4M12 16h4M12 20h4M12 24h4"/>',
 'driver':'<path d="M11 4h10v10H11z"/><path d="M14 14v12M18 14v12"/><path d="M16 4V2"/>',
 'stretcher':'<path d="M4 16h8M20 16h8"/><path d="M12 10h8v12h-8z"/><path d="M16 10V6M16 22v4"/>',
 'pliers':'<path d="M10 4l6 10 6-10"/><path d="M16 14v2"/><path d="M12 16l-4 12M20 16l4 12"/><path d="M14 16h4"/>',
 'compactor':'<path d="M6 22h20v4H6z"/><path d="M10 22V12h12v10"/><path d="M16 12V6h6"/>',
 'rake':'<path d="M16 4v16"/><path d="M6 20h20"/><path d="M8 20v6M12 20v6M16 20v6M20 20v6M24 20v6"/>',
 'fabric':'<path d="M4 10h24v12H4z"/><path d="M4 14l6 4 6-4 6 4 6-4"/>',
 'float':'<path d="M4 18h24v4H4z"/><path d="M16 18V8"/><path d="M12 8h8"/>',
 'freezer':'<path d="M6 8h20v18H6z"/><path d="M6 14h20"/><path d="M11 18v4"/>',
 'board':'<path d="M6 6h20v20H6z"/><path d="M9 12h14M9 16h10M9 20h12"/>',
 'alarm':'<path d="M16 6a8 8 0 018 8v6l2 3H6l2-3v-6a8 8 0 018-8z"/><path d="M13 26a3 3 0 006 0"/>',
 'cloth':'<path d="M5 5h22v22H5z"/><path d="M12 5v22M20 5v22M5 12h22M5 20h22"/>',
 'nest':'<path d="M6 12h20v14H6z"/><path d="M6 12l10-6 10 6"/><ellipse cx="16" cy="20" rx="4" ry="3"/>',
 'shavings':'<path d="M6 20c3-6 6-6 9 0s6 6 9 0"/><path d="M6 14c3-6 6-6 9 0s6 6 9 0"/><path d="M6 26c3-6 6-6 9 0s6 6 9 0"/>',
 'tool':'<path d="M20 4l8 8-10 10-8-8z"/><path d="M10 14L4 20l8 8 6-6"/>',
}
ICON_KEYS=[('hay net','feeder'),('feeder','feeder'),('tarp','tarp'),('weight tape','tape'),('ring','ring'),('grinder','grinder'),('sealer','sealer'),('hoist','hoist'),('game bag','bag'),('coop door','door'),('waterer','water'),('carton','carton'),('thermometer','thermo'),('instant-read','thermo'),('butcher paper','paper'),('cooler','cooler'),('moisture meter','meter'),('firewood rack','rack'),('kindling','splitter'),('stove thermometer','thermo'),('polywire','wire'),('charger','charger'),('seed','seed'),('grazing stick','stick'),('post driver','driver'),('stretcher','stretcher'),('strainer','wire'),('pliers','pliers'),('compactor','compactor'),('rake','rake'),('fabric','fabric'),('float','float'),('freezer','freezer'),('whiteboard','board'),('alarm','alarm'),('hardware cloth','cloth'),('nest box','nest'),('shavings','shavings')]
def icon_for(name):
    n=name.lower()
    for k,v in ICON_KEYS:
        if k in n: return ICONS[v]
    return ICONS['tool']

def gear(title, intro, items):
    lis='\n'.join(f'<li><div class="ico" aria-hidden="true"><svg viewBox="0 0 32 32">{icon_for(n)}</svg></div><strong>{n}</strong><span>{d}</span><a class="buy" href="{affiliate(u)}" rel="sponsored nofollow" target="_blank">See it on Amazon →</a></li>' for n,d,u,cta in items)
    return f'''<section class="gear" aria-label="Recommended gear">
  <div class="eyebrow">Recommended gear</div>
  <h2>{title}</h2>
  <p>{intro}</p>
  <ul>
{lis}
  </ul>
  <p class="disc">As an Amazon Associate, Back Forty Tools earns from qualifying purchases. Links above are affiliate links; buying through them costs you nothing extra and keeps the calculators free.</p>
</section>'''

if __name__=='__main__':
    import importlib.util, glob
    urls=[]
    for f in sorted(glob.glob(os.path.join(SRC,'tool_*.py'))):
        spec=importlib.util.spec_from_file_location('t',f); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
        u=m.build(page,header,footer,gear,faq_html)
        if u: urls.append(u)
        print('built',u)
    # sitemap
    sm='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    sm+=f'  <url><loc>{SITE}/</loc><lastmod>{TODAY}</lastmod></url>\n'
    for u in urls: sm+=f'  <url><loc>{u}</loc><lastmod>{TODAY}</lastmod></url>\n'
    sm+='</urlset>\n'
    open(os.path.join(ROOT,'sitemap.xml'),'w').write(sm)
