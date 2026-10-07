# Chicken coop size calculator
CALC = r'''<section class="calc" aria-label="Chicken coop size calculator">
  <form class="panel" id="cpform" autocomplete="off">
    <h2>Your flock</h2>
    <div class="grid">
      <label>Number of birds
        <input id="birds" type="number" min="1" max="500" step="1" value="8" inputmode="numeric">
      </label>
      <label>Breed size
        <select id="size">
          <option value="bantam" data-coop="2" data-run="5" data-roost="6" data-nest="5">Bantam</option>
          <option value="standard" data-coop="4" data-run="10" data-roost="9" data-nest="4" selected>Standard (Leghorn, sex-link, Australorp)</option>
          <option value="large" data-coop="5" data-run="12" data-roost="12" data-nest="3">Large / dual-purpose (Orpington, Brahma, Jersey Giant)</option>
          <option value="duck" data-coop="5" data-run="15" data-roost="0" data-nest="3">Ducks</option>
        </select>
      </label>
      <label>How much time outside?
        <select id="access">
          <option value="1.5">Locked in the coop most days (cold climate, predators)</option>
          <option value="1" selected>Coop at night, run by day</option>
          <option value="0.75">Free-range most days</option>
        </select>
      </label>
      <label>Plan to grow the flock?
        <select id="grow">
          <option value="0" selected>No, this is it</option>
          <option value="0.25">Maybe a few more (+25%)</option>
          <option value="0.5">Chicken math is real (+50%)</option>
        </select>
      </label>
      <label>Coop shape <small>sets the footprint suggestion</small>
        <select id="shape">
          <option value="1.5" selected>Rectangle, 3:2</option>
          <option value="1">Square</option>
          <option value="2">Long and narrow, 2:1</option>
        </select>
      </label>
    </div>
  </form>

  <aside class="panel results" aria-live="polite">
    <div class="tag">
      <div class="lbl">Coop floor</div>
      <div class="big" id="r-coop">—</div>
      <div class="sub" id="r-coopdim">—</div>
    </div>
    <dl class="rows">
      <dt class="total">Run</dt><dd class="total" id="r-run">—</dd>
      <dt>Suggested run footprint</dt><dd id="r-rundim">—</dd>
      <dt class="total">Roost bar</dt><dd class="total" id="r-roost">—</dd>
      <dt>Nest boxes</dt><dd id="r-nest">—</dd>
      <dt>Feeder trough length</dt><dd id="r-feed">—</dd>
      <dt>Waterers</dt><dd id="r-water">—</dd>
      <dt>Ventilation (openings, not drafts)</dt><dd id="r-vent">—</dd>
      <dt>Pop door</dt><dd id="r-door">—</dd>
      <dt class="total">Bedding per month, deep litter</dt><dd class="total" id="r-bed">—</dd>
    </dl>
    <p class="note" id="r-note"></p>
    <div style="display:flex;gap:10px;flex-wrap:wrap;align-items:center">
      <button class="btn" type="button" id="copy">Copy spec</button>
      <button class="btn ghost" type="button" id="reset">Reset</button>
      <span class="copied" id="copied" hidden>Copied</span>
    </div>
  </aside>
</section>'''

ARTICLE = r'''<article>
  <h2>How the calculator works</h2>
  <p>Every extension poultry guide uses the same square-foot-per-bird rules. The numbers below are the ones that keep hens from pecking each other, keep the coop dry, and keep eggs in the boxes instead of on the floor.</p>
  <div class="formula">coop = birds × 4 sq ft &nbsp;·&nbsp; run = birds × 10 sq ft &nbsp;·&nbsp; roost = birds × 9 in &nbsp;·&nbsp; 1 nest box per 4 hens</div>
  <p>Eight standard hens need a 32-square-foot coop (a 4 by 8 sheet of plywood is the floor, which is why so many coops are that size), an 80-square-foot run, 6 feet of roost and 2 nest boxes. Lock them inside through a northern winter and the coop should grow by half; let them free-range daily and you can shave a quarter off.</p>

  <h2>Space per bird</h2>
  <div class="tbl"><table>
    <thead><tr><th>Bird</th><th>Coop floor</th><th>Run</th><th>Roost</th><th>Hens per nest box</th></tr></thead>
    <tbody>
      <tr><td>Bantam</td><td>2 sq ft</td><td>5 sq ft</td><td>6 in</td><td>5</td></tr>
      <tr><td>Standard layer</td><td>3–4 sq ft</td><td>8–10 sq ft</td><td>8–10 in</td><td>4</td></tr>
      <tr><td>Large / dual-purpose</td><td>4–5 sq ft</td><td>10–12 sq ft</td><td>12 in</td><td>3</td></tr>
      <tr><td>Meat birds (Cornish Cross)</td><td>2 sq ft in tractor</td><td>n/a</td><td>none</td><td>none</td></tr>
      <tr><td>Ducks</td><td>4–6 sq ft</td><td>15 sq ft + water</td><td>none, floor nests</td><td>3</td></tr>
    </tbody>
  </table></div>

  <h2>Why crowding costs you eggs</h2>
  <p>Under about 3 square feet per bird, flocks start feather-pecking, egg-eating and bullying the lowest hen off the feeder. Ammonia builds faster than bedding can absorb it, and damp litter is where coccidiosis and respiratory trouble start. Hens that are stressed lay less, so a cheap coop that is too small is the most expensive coop you can build.</p>

  <h2>Ventilation without drafts</h2>
  <p>A coop needs about one square foot of permanent opening per ten square feet of floor, placed high, above roost height, so moist air leaves without wind blowing across the birds. Hardware cloth over the openings, never chicken wire; raccoons go straight through chicken wire. In the South, add a second set of openings you can close in January and open in June.</p>

  <h2>Roosts and nests</h2>
  <p>A 2 by 4 laid flat (wide side up) is the roost most backyard keepers settle on: hens can sit on their feet in the cold. Set it 18 to 24 inches off the floor, higher than the nest boxes, or they'll sleep in the boxes and foul the eggs. Nest boxes are 12 by 12 by 12 inches for standard breeds, 14 inches for the big ones, with a lip to hold bedding in and a slanted top so nobody roosts on it.</p>

  <h2>Frequently asked</h2>
'''

FAQS=[
("How big should a coop be for 6 chickens?","24 square feet of floor (4 by 6), a 60-square-foot run, 4.5 feet of roost and 2 nest boxes. A 4 by 8 coop gives you room for two more, which you will want."),
("How many chickens fit in a 4x8 coop?","Eight standard hens comfortably, ten if they free-range daily, six if they'll be locked in through winter. Twelve bantams."),
("How much run space per chicken?","10 square feet each for standard breeds, 8 if they get out to forage regularly. Less than that and the run turns to bare mud and manure within a month."),
("How many nest boxes for 10 chickens?","Three. One box per four hens is plenty; they'll all want the same one anyway."),
("Do chickens need a run if they free-range?","Yes, for the days you can't let them out and for the first week in a new place. Size it at 8 square feet per bird instead of 10."),
]

GEAR=[
("Hardware cloth, ½-inch","The only wire that stops raccoons, weasels and rats. Chicken wire keeps chickens in; it keeps nothing out.","https://www.tractorsupply.com/tsc/search/hardware%20cloth","Shop hardware cloth"),
("Automatic coop door","Opens at first light and closes at dusk. The one upgrade every coop owner wishes they'd done first.","https://www.amazon.com/s?k=automatic+chicken+coop+door","Shop coop doors"),
("Roll-away nest box","Eggs roll to a covered tray the second they're laid. No egg-eating, no broken eggs, no poop on them.","https://www.amazon.com/s?k=roll+away+nest+box","Shop nest boxes"),
("Pine shavings, compressed bale","Deep-litter bedding that composts under the birds. One bale covers a 4 by 8 coop 4 inches deep.","https://www.tractorsupply.com/tsc/search/pine%20shavings","Shop shavings"),
]

TAIL = r'''</div>
<script>
(function(){
  var $=function(id){return document.getElementById(id)};
  var f={birds:$('birds'),size:$('size'),access:$('access'),grow:$('grow'),shape:$('shape')};
  var fmt=function(n,d){return n.toLocaleString('en-US',{maximumFractionDigits:d==null?0:d,minimumFractionDigits:d==null?0:d})};
  var last='';
  function dims(area,ratio){ var w=Math.sqrt(area/ratio); var l=w*ratio; var r=function(x){return Math.ceil(x*2)/2}; return r(w)+' × '+r(l)+' ft'; }
  function calc(){
    var n=Math.max(0,+f.birds.value||0), o=f.size.options[f.size.selectedIndex];
    var acc=+f.access.value, grow=+f.grow.value, ratio=+f.shape.value;
    var N=n*(1+grow);
    var coop=Math.ceil(N*(+o.getAttribute('data-coop'))*acc);
    var run=Math.ceil(N*(+o.getAttribute('data-run'))*(acc<1?0.8:1));
    var roostIn=N*(+o.getAttribute('data-roost'));
    var nest=Math.max(1,Math.ceil(N/(+o.getAttribute('data-nest'))));
    var isDuck=f.size.value==='duck';
    $('r-coop').textContent=fmt(coop)+' sq ft';
    $('r-coopdim').textContent='about '+dims(coop,ratio)+(grow?' (sized for '+fmt(N)+' birds)':'');
    $('r-run').textContent=fmt(run)+' sq ft'+(isDuck?' + a pool':'');
    $('r-rundim').textContent=dims(run,ratio);
    $('r-roost').textContent=isDuck?'none, ducks sleep on the floor':fmt(roostIn/12,1)+' ft total ('+fmt(roostIn)+' in)';
    $('r-nest').textContent=fmt(nest)+(isDuck?' floor nests':' boxes, 12×12×12 in');
    $('r-feed').textContent=fmt(N*3)+' in of trough, or '+Math.max(1,Math.ceil(N/15))+' hanging feeder'+(N>15?'s':'');
    $('r-water').textContent=Math.max(1,Math.ceil(N/10))+' × 3-gal'+(isDuck?' + open water':'');
    $('r-vent').textContent=fmt(coop/10,1)+' sq ft, high on the wall';
    $('r-door').textContent=(f.size.value==='large'||isDuck)?'12 × 14 in':'10 × 12 in';
    $('r-bed').textContent=Math.max(1,Math.ceil(coop/32))+' bale'+(coop>32?'s':'')+' pine shavings';
    $('r-note').textContent='A 4 × 8 ft floor (one sheet of plywood) is 32 sq ft and the most common backyard coop size for a reason.';
    last='Coop for '+n+' '+o.text+': coop '+coop+' sq ft ('+dims(coop,ratio)+'), run '+run+' sq ft, roost '+fmt(roostIn/12,1)+' ft, '+nest+' nest boxes, vent '+fmt(coop/10,1)+' sq ft.';
  }
  Object.keys(f).forEach(function(k){ f[k].addEventListener('input',calc); f[k].addEventListener('change',calc); });
  $('cpform').addEventListener('submit',function(e){e.preventDefault();calc();});
  $('reset').addEventListener('click',function(){ f.birds.value=8;f.size.value='standard';f.access.value='1';f.grow.value='0';f.shape.value='1.5';calc(); });
  $('copy').addEventListener('click',function(){
    var done=function(){$('copied').hidden=false;setTimeout(function(){$('copied').hidden=true},1800)};
    function fallback(){var t=document.createElement('textarea');t.value=last;document.body.appendChild(t);t.select();try{document.execCommand('copy');done()}catch(e){}document.body.removeChild(t)}
    if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(last).then(done,fallback)}else{fallback()}
  });
  calc();
})();
</script>'''

def build(page,header,footer,gear,faq_html):
    body='<div class="wrap">\n'+header('Poultry','How big does the chicken coop need to be?','Birds and breed in; coop floor, run, roost length, nest boxes, ventilation and bedding out, in the numbers extension poultry guides use.')+'\n'+CALC+'\n'+gear('Build it once','Most second coops get built because the first one was too small or a raccoon got in.',GEAR)+'\n'+ARTICLE+faq_html(FAQS)+'\n</article>\n'+footer('Space, roost and nest guidelines from the University of Kentucky, Penn State and Oregon State poultry extension programs.')+'\n'+TAIL
    return page('chicken-coop-size-calculator','Chicken Coop Size Calculator: Coop, Run, Roost and Nest Boxes | Back Forty Tools','Chicken Coop Size Calculator','Free chicken coop size calculator. Enter number of birds and breed to get coop square footage, run size, roost length, nest box count, ventilation and bedding, with suggested dimensions.',body,FAQS,'Chicken Coop Size Calculator')
