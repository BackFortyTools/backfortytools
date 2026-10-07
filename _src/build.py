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

def gear(title, intro, items):
    lis='\n'.join(f'<li><strong>{n}</strong><span>{d}</span><br><a href="{affiliate(u)}" rel="sponsored nofollow" target="_blank">{cta} →</a></li>' for n,d,u,cta in items)
    return f'''<section class="gear" aria-label="Recommended gear">
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
