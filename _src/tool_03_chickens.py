# Backyard chicken cost calculator
CALC = r'''<section class="calc" aria-label="Backyard chicken cost calculator">
  <form class="panel" id="chxform" autocomplete="off">
    <h2>Your flock</h2>
    <div class="grid">
      <label>Laying hens
        <input id="hens" type="number" min="1" max="500" step="1" value="6" inputmode="numeric">
      </label>
      <label>Feed per hen per day <small>ounces; 4 is typical for layers</small>
        <input id="oz" type="number" min="1" max="10" step="0.5" value="4" inputmode="decimal">
      </label>
      <label>Feed price <small>$ per 50 lb bag</small>
        <input id="bag" type="number" min="1" step="0.5" value="20" inputmode="decimal">
      </label>
      <label>Free-range or kitchen scraps <small>% of feed they find themselves</small>
        <input id="forage" type="number" min="0" max="60" step="5" value="10" inputmode="numeric">
      </label>
      <label>Eggs per hen per week <small>5 in peak season, 3 for older hens or winter</small>
        <input id="eggs" type="number" min="0" max="7" step="0.5" value="4.5" inputmode="decimal">
      </label>
      <label>Bedding, grit, oyster shell, misc. <small>$ per month</small>
        <input id="misc" type="number" min="0" step="1" value="12" inputmode="numeric">
      </label>
      <label>Startup spent <small>$ coop, run, feeders, birds</small>
        <input id="startup" type="number" min="0" step="25" value="650" inputmode="numeric">
      </label>
      <label>Store price you'd otherwise pay <small>$ per dozen</small>
        <input id="store" type="number" min="0" step="0.25" value="4.50" inputmode="decimal">
      </label>
    </div>
  </form>

  <aside class="panel results" aria-live="polite">
    <div class="tag">
      <div class="lbl">Your cost per dozen</div>
      <div class="big" id="r-dozen">—</div>
      <div class="sub" id="r-vs">—</div>
    </div>
    <dl class="rows">
      <dt>Feed per month, whole flock</dt><dd id="r-feedlb">—</dd>
      <dt>Bags per month</dt><dd id="r-bags">—</dd>
      <dt>Feed cost per month</dt><dd id="r-feed">—</dd>
      <dt>Bedding and extras</dt><dd id="r-misc">—</dd>
      <dt class="total">Total per month</dt><dd class="total" id="r-month">—</dd>
      <dt>Per hen per month</dt><dd id="r-perhen">—</dd>
      <dt class="total">Eggs per month</dt><dd class="total" id="r-eggs">—</dd>
      <dt>Dozens per month</dt><dd id="r-doz">—</dd>
      <dt class="total">Yearly savings vs. store</dt><dd class="total cost" id="r-save">—</dd>
      <dt>Startup pays off in</dt><dd id="r-payback">—</dd>
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
  <p>Feed is 70 to 80 percent of what a laying flock costs once the coop is built, so the math starts there.</p>
  <div class="formula">hens × ounces per day × 30 ÷ 16 = pounds of feed per month, then ÷ 50 × bag price</div>
  <p>A laying hen eats about a quarter pound of feed a day, roughly 1.75 pounds a week or 7.5 pounds a month. Six hens go through 45 pounds a month, which is one 50-pound bag. At $20 a bag that is $20 in feed for about 115 eggs, or just under $2.10 a dozen before bedding and grit. Add those and most small flocks land between $2.50 and $3.50 a dozen, which beats pasture-raised eggs at the store and loses to the cheapest factory eggs.</p>

  <h2>What a hen really eats</h2>
  <div class="tbl"><table>
    <thead><tr><th>Bird</th><th>Feed per day</th><th>Per month</th><th>Notes</th></tr></thead>
    <tbody>
      <tr><td>Bantam hen</td><td>2 oz</td><td>3.75 lb</td><td>Small eggs, small appetite</td></tr>
      <tr><td>Standard layer (Leghorn, sex-link)</td><td>3.5–4 oz</td><td>6.5–7.5 lb</td><td>Most efficient converters</td></tr>
      <tr><td>Dual-purpose (Orpington, Rock, Wyandotte)</td><td>4–5 oz</td><td>7.5–9.5 lb</td><td>Bigger bird, eats more</td></tr>
      <tr><td>Meat bird (Cornish Cross)</td><td>6–8 oz</td><td>n/a</td><td>8 weeks to butcher</td></tr>
      <tr><td>Chick, 0–8 weeks</td><td>1–2 oz</td><td>about 10 lb total starter</td><td>Starter feed costs more per bag</td></tr>
    </tbody>
  </table></div>
  <p>Hens eat more in cold weather and when they are molting, and less when they free-range on good pasture. Feed waste from open trough feeders can run 20 percent or more; a treadle or hanging feeder with a lip pays for itself in a few months.</p>

  <h2>How many eggs to expect</h2>
  <p>A good production hen in her first year lays 250 to 300 eggs, about five a week. Heritage and dual-purpose breeds lay 180 to 220. Production drops roughly 15 to 20 percent each year after the first, and nearly all hens slow or stop for a few weeks during the fall molt and the short days of winter unless you add light. Over a hen's productive life, 4 eggs a week is a fair average to plan on.</p>

  <h2>Startup costs</h2>
  <p>A used or self-built coop with a run for six hens runs $200 to $500; a prefab kit $300 to $800; a built-to-last walk-in coop $1,000 and up. Chicks cost $4 to $7 each, started pullets $25 to $35. Add a feeder, waterer, heat lamp for the brooder and a bag of starter and most people are into a first flock of six for $500 to $900. The calculator spreads that over the eggs you collect so you can see when the coop has paid for itself.</p>

  <h2>Ways to bring the cost down</h2>
  <p>Buy feed by the bag from a farm store rather than a pet store, or split a pallet with a neighbor. Ferment the feed (soak it two to three days) and most people see 10 to 20 percent less consumption. Let the birds free-range an hour before dusk so they forage without wandering. Sell a few dozen a week to coworkers at $5 and the flock turns a small profit on paper.</p>

  <h2>Frequently asked</h2>
'''

FAQS=[
("How much does it cost to feed 6 chickens a month?","About one 50-pound bag of layer feed, $18 to $24 depending on brand and region. Add bedding and grit and six hens cost $30 to $40 a month to keep."),
("Is it cheaper to raise chickens or buy eggs?","Cheaper than pasture-raised or organic store eggs, more expensive than the cheapest conventional eggs. Most backyard flocks produce eggs for $2.50 to $3.50 a dozen in feed and supplies once the coop is paid off."),
("How many eggs will 6 chickens lay?","Around 25 to 30 eggs a week in the first year, roughly two dozen. Expect that to fall to 15 to 20 a week by year three."),
("How long does a chicken coop take to pay for itself?","A $600 setup with six hens saving $2 a dozen versus store eggs pays off in about two and a half years. Buying chicks instead of pullets and building the coop from scrap can cut that to a year."),
("How much feed does a chicken eat per day?","A standard laying hen eats about 4 ounces (a quarter pound) a day. Bantams eat half that; big dual-purpose breeds up to 5 ounces."),
]

GEAR=[
("Treadle or no-waste feeder","Stops the 20% that gets raked onto the ground and feeds the rats. Biggest single saving on this page.","https://www.tractorsupply.com/tsc/search/treadle%20chicken%20feeder","Shop feeders"),
("Automatic coop door","Opens at dawn, closes at dusk. Lets you leave for a weekend without a chicken sitter.","https://www.amazon.com/s?k=automatic+chicken+coop+door","Shop coop doors"),
("Heated waterer base","One frozen waterer in January costs more eggs than the base does.","https://www.tractorsupply.com/tsc/search/heated%20poultry%20waterer","Shop heated waterers"),
("Egg cartons, flats and date stamps","If you'll sell a few dozen, clean cartons are the difference between $3 and $5 a dozen.","https://www.amazon.com/s?k=egg+cartons+bulk","Shop egg cartons"),
]

TAIL = r'''</div>
<script>
(function(){
  var $=function(id){return document.getElementById(id)};
  var f={hens:$('hens'),oz:$('oz'),bag:$('bag'),forage:$('forage'),eggs:$('eggs'),misc:$('misc'),startup:$('startup'),store:$('store')};
  var fmt=function(n,d){return n.toLocaleString('en-US',{maximumFractionDigits:d==null?0:d,minimumFractionDigits:d==null?0:d})};
  var usd=function(n,d){return '$'+fmt(n,d==null?2:d)};
  var last='';
  function calc(){
    var hens=+f.hens.value||0, oz=+f.oz.value||0, bag=+f.bag.value||0, forage=(+f.forage.value||0)/100;
    var eggs=+f.eggs.value||0, misc=+f.misc.value||0, startup=+f.startup.value||0, store=+f.store.value||0;
    var feedLb=hens*oz*30.4/16*(1-forage);
    var bags=feedLb/50;
    var feedCost=bags*bag;
    var month=feedCost+misc;
    var eggsMo=hens*eggs*30.4/7;
    var doz=eggsMo/12;
    var perDoz=doz>0?month/doz:null;
    var yearSave=(store*doz-month)*12;
    var payback=yearSave>0?startup/yearSave*12:null;
    $('r-dozen').textContent=perDoz==null?'—':usd(perDoz);
    $('r-vs').textContent=perDoz==null?'no eggs, no dozen':(perDoz<store?usd(store-perDoz)+' less than the store':usd(perDoz-store)+' more than the store');
    $('r-feedlb').textContent=fmt(feedLb)+' lb';
    $('r-bags').textContent=fmt(bags,1);
    $('r-feed').textContent=usd(feedCost);
    $('r-misc').textContent=usd(misc);
    $('r-month').textContent=usd(month);
    $('r-perhen').textContent=hens?usd(month/hens):'—';
    $('r-eggs').textContent=fmt(eggsMo);
    $('r-doz').textContent=fmt(doz,1);
    $('r-save').textContent=(yearSave>=0?'+':'−')+usd(Math.abs(yearSave),0);
    $('r-payback').textContent=payback==null?'never at these prices':(payback<1?'under a month':fmt(payback,0)+' months');
    $('r-note').textContent='Running cost only; startup is used for the payback line. Add a bag of starter and a few months of no eggs if you begin with chicks.';
    last='Chicken cost: '+hens+' hens, '+fmt(feedLb)+' lb feed/mo ('+fmt(bags,1)+' bags @ '+usd(bag)+') = '+usd(feedCost)+' + '+usd(misc)+' extras = '+usd(month)+'/mo. '+fmt(eggsMo)+' eggs/mo = '+fmt(doz,1)+' dozen → '+(perDoz==null?'n/a':usd(perDoz))+'/dozen vs '+usd(store)+' store. Yearly '+(yearSave>=0?'savings ':'loss ')+usd(Math.abs(yearSave),0)+(payback?'; startup pays back in '+fmt(payback,0)+' months':'')+'.';
  }
  Object.keys(f).forEach(function(k){ f[k].addEventListener('input',calc); });
  $('chxform').addEventListener('submit',function(e){e.preventDefault();calc();});
  $('reset').addEventListener('click',function(){ f.hens.value=6;f.oz.value=4;f.bag.value=20;f.forage.value=10;f.eggs.value=4.5;f.misc.value=12;f.startup.value=650;f.store.value=4.50;calc(); });
  $('copy').addEventListener('click',function(){
    var done=function(){$('copied').hidden=false;setTimeout(function(){$('copied').hidden=true},1800)};
    function fallback(){var t=document.createElement('textarea');t.value=last;document.body.appendChild(t);t.select();try{document.execCommand('copy');done()}catch(e){}document.body.removeChild(t)}
    if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(last).then(done,fallback)}else{fallback()}
  });
  calc();
})();
</script>'''

def build(page,header,footer,gear,faq_html):
    body='<div class="wrap">\n'+header('Poultry','What do backyard chickens really cost?','Feed, bedding and your coop, turned into a cost per dozen and a payback date. Change any number and see what moves.')+'\n'+CALC+'\n'+gear('Where the money leaks out of a small flock','Most of the gap between a $2.50 dozen and a $4 dozen is feed on the ground and water that froze.',GEAR)+'\n'+ARTICLE+faq_html(FAQS)+'\n</article>\n'+footer('Feed intake and lay rates from Oklahoma State Extension, Tennessee State Extension and the University of Kentucky poultry program.')+'\n'+TAIL
    return page('chicken-cost-calculator','Backyard Chicken Cost Calculator: Cost Per Dozen Eggs | Back Forty Tools','Backyard Chicken Cost Calculator','Free backyard chicken cost calculator. Enter your hens, feed price and egg rate to get monthly cost, cost per dozen, yearly savings versus store eggs and when your coop pays for itself.',body,FAQS,'Backyard Chicken Cost Calculator')
