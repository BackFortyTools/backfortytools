# Pasture stocking rate calculator
CALC = r'''<section class="calc" aria-label="Pasture stocking rate calculator">
  <form class="panel" id="psform" autocomplete="off">
    <h2>Your pasture</h2>
    <div class="grid">
      <label>Grazeable acres <small>not counting woods, ponds, barn lot</small>
        <input id="acres" type="number" min="0.1" step="0.5" value="10" inputmode="decimal">
      </label>
      <label>Pasture productivity
        <select id="yield">
          <option value="2.0">Poor — weedy, thin, unfertilized (2 tons/acre/yr)</option>
          <option value="3.5" selected>Average fescue or bermuda, some fertilizer (3.5 tons)</option>
          <option value="5.0">Good — fertilized, limed, rotated (5 tons)</option>
          <option value="7.0">Excellent — irrigated or intensively managed (7 tons)</option>
        </select>
      </label>
      <label>Grazing days per year <small>Southeast: 240–300</small>
        <input id="days" type="number" min="30" max="365" step="10" value="270" inputmode="numeric">
      </label>
      <label>Grazing style <small>sets how much of the grass they actually eat</small>
        <select id="util">
          <option value="0.35">Continuous — one big field (35% used)</option>
          <option value="0.50" selected>Simple rotation, 3–6 paddocks (50%)</option>
          <option value="0.65">Intensive rotation, daily moves (65%)</option>
        </select>
      </label>
      <label>Animal
        <select id="animal">
          <option value="1.0" data-wt="1000">Beef cow, dry (1,000 lb)</option>
          <option value="1.3" data-wt="1200" selected>Beef cow + calf (1,200 lb pair)</option>
          <option value="0.7" data-wt="700">Yearling / stocker (700 lb)</option>
          <option value="1.25" data-wt="1100">Horse (1,100 lb)</option>
          <option value="0.2" data-wt="150">Sheep / goat (150 lb)</option>
          <option value="0.1" data-wt="80">Meat goat kid / lamb (80 lb)</option>
        </select>
      </label>
      <label>Head you have or want
        <input id="head" type="number" min="0" step="1" value="4" inputmode="numeric">
      </label>
    </div>
  </form>

  <aside class="panel results" aria-live="polite">
    <div class="tag">
      <div class="lbl">Your pasture can carry</div>
      <div class="big" id="r-head">—</div>
      <div class="sub" id="r-au">—</div>
    </div>
    <dl class="rows">
      <dt>Forage grown per year</dt><dd id="r-grown">—</dd>
      <dt>Forage actually eaten</dt><dd id="r-eaten">—</dd>
      <dt>Each animal needs per year</dt><dd id="r-need">—</dd>
      <dt class="total">Acres per head</dt><dd class="total" id="r-acres">—</dd>
      <dt>Your current plan</dt><dd id="r-plan">—</dd>
      <dt class="total">Verdict</dt><dd class="total" id="r-verdict">—</dd>
      <dt>Hay to cover the gap</dt><dd id="r-hay">—</dd>
    </dl>
    <p class="note" id="r-note"></p>
    <div style="display:flex;gap:10px;flex-wrap:wrap;align-items:center">
      <button class="btn" type="button" id="copy">Copy summary</button>
      <button class="btn ghost" type="button" id="reset">Reset</button>
      <span class="copied" id="copied" hidden>Copied</span>
    </div>
  </aside>
</section>'''

ARTICLE = r'''<article>
  <h2>How the calculator works</h2>
  <p>Stocking rate is forage supply divided by forage demand. Extension agents measure both in "animal units," where one AU is a 1,000-pound cow eating about 26 pounds of dry forage a day.</p>
  <div class="formula">acres × tons grown × utilization = forage available &nbsp;·&nbsp; head × AU × 26 lb × grazing days = forage needed</div>
  <p>Ten average acres in north Georgia grow about 35 tons of dry matter a year. With a simple rotation the cattle eat half of it, 17.5 tons. A cow-calf pair needs about 4.5 tons over a 270-day grazing season, so those ten acres carry about four pairs, or 2.5 acres per pair. That is close to the "2 to 3 acres per cow" rule most Georgia cattlemen use, and it is why the same ten acres in a drought year leaves you buying hay in August.</p>

  <h2>Acres per cow by region</h2>
  <p>Rough carrying capacity for a 1,200-pound cow-calf pair on unirrigated, moderately managed pasture.</p>
  <div class="tbl"><table>
    <thead><tr><th>Region</th><th>Acres per pair</th><th>Grazing season</th></tr></thead>
    <tbody>
      <tr><td>Southeast (GA, AL, TN, Carolinas)</td><td>2–3</td><td>240–300 days</td></tr>
      <tr><td>Mid-South, lower Midwest (KY, MO, AR)</td><td>2–4</td><td>210–240 days</td></tr>
      <tr><td>Upper Midwest, Northeast</td><td>2–3 (short season)</td><td>150–180 days</td></tr>
      <tr><td>Great Plains (KS, NE, OK)</td><td>5–10</td><td>180–240 days</td></tr>
      <tr><td>Mountain West, Southwest range</td><td>20–60+</td><td>varies</td></tr>
    </tbody>
  </table></div>

  <h2>Animal unit equivalents</h2>
  <div class="tbl"><table>
    <thead><tr><th>Animal</th><th>Animal units</th><th>Dry forage per day</th></tr></thead>
    <tbody>
      <tr><td>Dry cow, 1,000 lb</td><td>1.0</td><td>26 lb</td></tr>
      <tr><td>Cow with calf, 1,200 lb</td><td>1.3</td><td>34 lb</td></tr>
      <tr><td>Yearling, 700 lb</td><td>0.7</td><td>18 lb</td></tr>
      <tr><td>Bull, 1,800 lb</td><td>1.5</td><td>39 lb</td></tr>
      <tr><td>Horse, 1,100 lb</td><td>1.25</td><td>32 lb</td></tr>
      <tr><td>Ewe or doe with offspring</td><td>0.2</td><td>5 lb</td></tr>
    </tbody>
  </table></div>

  <h2>Why rotation doubles your pasture</h2>
  <p>In a single big field, cattle eat the best grass to the dirt and leave the rest to go to seed. Half the forage is wasted by trampling, manure and selective grazing. Split that field into four and move them every week and utilization climbs from 35 to 50 percent. Move them daily and it reaches 65. A reel of polywire and a solar charger costs less than one round bale per month of winter feeding, and it buys you the equivalent of several more acres.</p>

  <h2>The gap is normal; plan for it</h2>
  <p>No pasture grows evenly. Fescue surges in April and goes dormant in July; bermuda is the reverse. The calculator's hay line shows how much you'll feed to cover the days the grass can't. If that number is bigger than you expected, that is the honest cost of the herd size you entered, and it is better to know in spring than in February.</p>

  <h2>Frequently asked</h2>
'''

FAQS=[
("How many cows can I have on 10 acres?","On average Southeastern pasture with simple rotation, about four cow-calf pairs. Poor, continuously grazed pasture carries two; well-managed, fertilized pasture with rotation can carry six or seven."),
("How many acres per cow in Georgia?","Two to three acres per cow-calf pair on decent fescue or bermuda pasture. Count only grazeable acres, not woods or the barn lot."),
("How many goats per acre?","Six to eight does with kids per acre on good pasture, two to four on brushy or thin ground. Goats browse rather than graze, so wooded acres count for more with goats than with cattle."),
("How many horses per acre?","Plan on 2 acres for the first horse and 1 to 2 more for each additional horse. Horses graze closer than cattle and damage pasture faster, so rotation matters even more."),
("What is an animal unit?","A 1,000-pound cow with or without a calf under six months, eating about 26 pounds of dry forage a day. Every other animal is expressed as a fraction or multiple of that."),
]

GEAR=[
("Polywire reel and step-in posts","The cheapest way to split one field into four. A reel, 50 posts and a charger set up a rotation in an afternoon.","https://www.tractorsupply.com/tsc/search/polywire%20reel","Shop polywire"),
("Solar fence charger","Lets you rotate paddocks far from the barn with no extension cord.","https://www.tractorsupply.com/tsc/search/solar%20fence%20charger","Shop chargers"),
("Pasture seed mix","Overseeding clover into fescue adds nitrogen and summer grazing without buying fertilizer.","https://www.tractorsupply.com/tsc/search/pasture%20seed","Shop seed"),
("Grazing stick","A $10 ruler that tells you when a paddock is ready and when to pull the cattle off.","https://www.amazon.com/s?k=pasture+grazing+stick","Shop grazing sticks"),
]

TAIL = r'''</div>
<script>
(function(){
  var $=function(id){return document.getElementById(id)};
  var f={acres:$('acres'),yield:$('yield'),days:$('days'),util:$('util'),animal:$('animal'),head:$('head')};
  var fmt=function(n,d){return n.toLocaleString('en-US',{maximumFractionDigits:d==null?0:d,minimumFractionDigits:d==null?0:d})};
  var last='';
  function calc(){
    var acres=+f.acres.value||0, y=+f.yield.value, days=+f.days.value||0, util=+f.util.value, au=+f.animal.value, head=+f.head.value||0;
    var grown=acres*y;                 // tons DM/yr
    var eaten=grown*util;              // tons usable
    var needPer=au*26*days/2000;       // tons per head over grazing season
    var canCarry=needPer>0?eaten/needPer:0;
    var acresPer=canCarry>0?acres/canCarry:0;
    var planNeed=head*needPer;
    var gap=Math.max(0,planNeed-eaten); // tons
    var hayTons=gap*1.15;              // hay is ~87% DM
    var name=f.animal.options[f.animal.selectedIndex].text.split(' (')[0];
    $('r-head').textContent=fmt(canCarry,1)+' head';
    $('r-au').textContent=name.toLowerCase()+' · '+fmt(canCarry*au,1)+' animal units';
    $('r-grown').textContent=fmt(grown,1)+' tons dry matter';
    $('r-eaten').textContent=fmt(eaten,1)+' tons';
    $('r-need').textContent=fmt(needPer,2)+' tons';
    $('r-acres').textContent=fmt(acresPer,1)+' acres';
    $('r-plan').textContent=head+' head need '+fmt(planNeed,1)+' tons';
    var v= head===0?'—': head<=canCarry*0.85?'Understocked, room for '+Math.floor(canCarry-head)+' more': head<=canCarry*1.1?'About right':'Overstocked by '+fmt(head-canCarry,1)+' head';
    $('r-verdict').textContent=v;
    $('r-hay').textContent=gap>0?fmt(hayTons,1)+' tons ('+fmt(hayTons*2000/50)+' square bales)':'none, grass covers it';
    $('r-note').textContent='Beyond the grazing days you entered, winter hay is extra. Use the Winter Hay Calculator for that.';
    last='Stocking rate: '+acres+' acres × '+y+' t/ac × '+Math.round(util*100)+'% used = '+fmt(eaten,1)+' tons. '+name+' needs '+fmt(needPer,2)+' t over '+days+' days → carries '+fmt(canCarry,1)+' head ('+fmt(acresPer,1)+' ac/head). Plan '+head+' head: '+v+(gap>0?'; hay gap '+fmt(hayTons,1)+' t':'')+'.';
  }
  Object.keys(f).forEach(function(k){ f[k].addEventListener('input',calc); f[k].addEventListener('change',calc); });
  $('psform').addEventListener('submit',function(e){e.preventDefault();calc();});
  $('reset').addEventListener('click',function(){ f.acres.value=10;f.yield.value='3.5';f.days.value=270;f.util.value='0.50';f.animal.selectedIndex=1;f.head.value=4;calc(); });
  $('copy').addEventListener('click',function(){
    var done=function(){$('copied').hidden=false;setTimeout(function(){$('copied').hidden=true},1800)};
    function fallback(){var t=document.createElement('textarea');t.value=last;document.body.appendChild(t);t.select();try{document.execCommand('copy');done()}catch(e){}document.body.removeChild(t)}
    if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(last).then(done,fallback)}else{fallback()}
  });
  calc();
})();
</script>'''

def build(page,header,footer,gear,faq_html):
    body='<div class="wrap">\n'+header('Livestock','How many cows (or goats, or horses) can your land carry?','Acres, pasture quality and grazing style in; head count, acres per animal and the hay gap out. Uses the animal-unit method extension agents teach.')+'\n'+CALC+'\n'+gear('Carry more on the same acres','Rotation is the lever. Everything here is about making rotation cheap enough to actually do.',GEAR)+'\n'+ARTICLE+faq_html(FAQS)+'\n</article>\n'+footer('Animal-unit values and forage yields from UGA Extension, Mississippi State Extension and the USDA NRCS grazing guides.')+'\n'+TAIL
    return page('pasture-stocking-rate-calculator','Pasture Stocking Rate Calculator: How Many Cows Per Acre? | Back Forty Tools','Pasture Stocking Rate Calculator','Free pasture stocking rate calculator. Enter acres, pasture quality, grazing days and animal type to get how many cattle, horses, goats or sheep your land can carry, acres per head, and the hay gap.',body,FAQS,'Pasture Stocking Rate Calculator')
