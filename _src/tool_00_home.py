# Home / hub page
EXTRA_CSS = r'''<style>
.brand{font-family:var(--display);font-weight:800;font-size:1.1rem;letter-spacing:.02em}
.tools{list-style:none;padding:0;margin:0;display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:14px}
.tools li{min-width:0}
.tools a{display:block;background:var(--surface);border:1px solid var(--line);padding:18px;color:inherit;text-decoration:none;height:100%}
.tools a:hover,.tools a:focus-visible{border-color:var(--accent);outline:none}
.tools .cat{text-transform:uppercase;letter-spacing:.1em;font-size:.72rem;font-weight:700;color:var(--tag)}
.tools strong{display:block;font-family:var(--display);font-size:1.15rem;margin:.2rem 0 .3rem}
.tools span{color:var(--muted);font-size:.95rem}
.home h2{font-family:var(--display);font-size:1.3rem;margin:2rem 0 .8rem}
.about{max-width:65ch;margin-top:2.5rem}
.about p{margin:0 0 1rem}
</style>'''

TOOLS=[
 ("Livestock",[
   ("Hay & forage","Winter Hay Calculator","Pounds, tons, bales and cost for horses, cattle, goats and sheep, with feeder and storage waste built in.","/winter-hay-calculator/"),
   ("Poultry","Backyard Chicken Cost Calculator","What a flock really costs per month and per dozen eggs, and when the coop pays for itself.","/chicken-cost-calculator/"),
 ]),
 ("Hunting & processing",[
   ("Deer","Deer Meat Yield Calculator","Live or field-dressed weight in, pounds of boneless venison and freezer space out, cut by cut.","/deer-meat-yield-calculator/"),
 ]),
 ("Home & heat",[
   ("Wood heat","Firewood Calculator","Cords for the season by house size, climate, stove and species. Stack-to-cord converter included.","/firewood-calculator/"),
   ("Smoking","Brisket Smoking Time Calculator","Tell it when you want to eat; it tells you when to light the smoker, wrap, pull and rest.","/brisket-smoking-time-calculator/"),
 ]),
]

def build(page,header,footer,gear,faq_html):
    secs=''
    for cat,items in TOOLS:
        lis=''.join(f'<li><a href="{u}"><div class="cat">{k}</div><strong>{n}</strong><span>{d}</span></a></li>' for k,n,d,u in items)
        secs+=f'<h2>{cat}</h2>\n<ul class="tools">{lis}</ul>\n'
    body=EXTRA_CSS+'''
<div class="wrap home">
<header>
  <div class="brand">Back Forty Tools</div>
  <h1>Calculators for the farm, the barn and the woods</h1>
  <p class="lede">The arithmetic extension agents teach, done for you. Enter what you've got, get a number you can act on. No sign-up, no app, nothing to download.</p>
</header>
'''+secs+'''
<section class="about">
  <h2>Why this site exists</h2>
  <p>Most of these answers are buried in university extension PDFs or scattered across forum threads. The math is simple, but you have to find the right numbers for waste, intake and yield before you can use it. We pulled those numbers from the extension research, built the calculators, and put them on one fast page each.</p>
  <p>Some pages link to gear that fixes the problem the calculator just showed you. Those are affiliate links and may earn us a small commission. It is how the site stays free.</p>
</section>
<footer>Back Forty Tools · Northwest Georgia · Estimates only; your animals, your weather and your wood will vary.</footer>
</div>'''
    url=page('', 'Back Forty Tools: Free Calculators for the Farm, Barn and Woods','Back Forty Tools','Plain-spoken calculators for people who keep animals, heat with wood, hunt and smoke meat. Winter hay, deer meat yield, chicken costs, firewood cords and brisket timing. No sign-up, no app.',body,None,None,[{"@type":"WebSite","name":"Back Forty Tools","url":"https://backfortytools.com/"}])
    return None
