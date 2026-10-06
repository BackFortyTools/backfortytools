# Firewood calculator
CALC = r'''<section class="calc" aria-label="Firewood calculator">
  <form class="panel" id="fwform" autocomplete="off">
    <h2>Your house and your stove</h2>
    <div class="grid">
      <label>Heated space <small>square feet</small>
        <input id="sqft" type="number" min="200" max="8000" step="50" value="1800" inputmode="numeric">
      </label>
      <label>Climate
        <select id="climate">
          <option value="1.5" selected>Southeast / Gulf (GA, AL, TN, Carolinas)</option>
          <option value="2.5">Mid-Atlantic / lower Midwest (VA, KY, MO, OH)</option>
          <option value="3.5">North / New England / upper Midwest</option>
          <option value="4.5">Far north / mountain (MN, ND, MT, northern ME)</option>
          <option value="1.0">Mild West Coast / Southwest</option>
        </select>
      </label>
      <label>Wood is your…
        <select id="use">
          <option value="1" selected>Primary heat</option>
          <option value="0.45">Supplemental (evenings, cold snaps)</option>
          <option value="0.12">Occasional fires</option>
        </select>
      </label>
      <label>Insulation
        <select id="insul">
          <option value="0.85">Tight, newer house</option>
          <option value="1" selected>Average</option>
          <option value="1.3">Drafty, old or uninsulated</option>
        </select>
      </label>
      <label>What you burn in
        <select id="stove">
          <option value="1" selected>EPA wood stove or insert (2015+)</option>
          <option value="1.3">Older stove or insert</option>
          <option value="1.15">Outdoor wood boiler</option>
          <option value="2.2">Open fireplace</option>
        </select>
      </label>
      <label>Wood species
        <select id="species">
          <option value="21" selected>Mixed hardwood</option>
          <option value="27">Hickory</option>
          <option value="24">Oak (red or white)</option>
          <option value="24">Sugar maple / beech</option>
          <option value="20">Ash / red maple</option>
          <option value="18">Cherry / elm</option>
          <option value="15">Pine / fir / spruce</option>
          <option value="13">Poplar / sweetgum / cottonwood</option>
        </select>
      </label>
      <label>Price per full cord <small>$ delivered; 0 if you cut your own</small>
        <input id="price" type="number" min="0" step="10" value="250" inputmode="numeric">
      </label>
      <label>Wood you already have <small>full cords</small>
        <input id="have" type="number" min="0" step="0.25" value="0" inputmode="decimal">
      </label>
    </div>
    <h2 style="margin-top:20px">Stack to cords</h2>
    <div class="grid">
      <label>Stack length <small>feet</small><input id="sl" type="number" min="0" step="0.5" value="16" inputmode="decimal"></label>
      <label>Stack height <small>feet</small><input id="sh" type="number" min="0" step="0.5" value="4" inputmode="decimal"></label>
      <label>Piece length <small>inches</small><input id="sw" type="number" min="8" max="48" step="1" value="16" inputmode="numeric"></label>
      <label>That stack is<input id="stack-out" type="text" readonly value="—"></label>
    </div>
  </form>

  <aside class="panel results" aria-live="polite">
    <div class="tag">
      <div class="lbl">Cords for the season</div>
      <div class="big" id="r-cords">—</div>
      <div class="sub" id="r-range">—</div>
    </div>
    <dl class="rows">
      <dt>Base for your size and climate</dt><dd id="r-base">—</dd>
      <dt>Adjusted for how you use it</dt><dd id="r-use">—</dd>
      <dt>Adjusted for house and stove</dt><dd id="r-adj">—</dd>
      <dt>Adjusted for wood species</dt><dd id="r-sp">—</dd>
      <dt class="total">Face cords (16-inch)</dt><dd class="total" id="r-face">—</dd>
      <dt>Pickup loads (½ ton, ~⅓ cord)</dt><dd id="r-loads">—</dd>
      <dt>Stack footprint, 4 ft high</dt><dd id="r-stack">—</dd>
      <dt class="total">Still need to buy or cut</dt><dd class="total" id="r-need">—</dd>
      <dt class="total">Cost for the season</dt><dd class="total cost" id="r-cost">—</dd>
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
  <p>The old rule is cords per thousand square feet, set by climate. We start there and then correct for the things that actually change the number: how much of your heat comes from wood, how tight the house is, how efficient the stove is, and how much heat is in the wood you burn.</p>
  <div class="formula">(sq ft ÷ 1,000) × climate cords × use × insulation × stove × (21 ÷ species BTU)</div>
  <p>An 1,800-square-foot house in north Georgia heated mostly with an EPA stove burning mixed hardwood needs about 2.7 cords. The same house in Vermont needs more than 6. Switch to seasoned oak and both numbers drop about 12 percent, because a cord of oak carries more heat than a cord of mixed wood.</p>

  <h2>Cords per 1,000 square feet by region</h2>
  <div class="tbl"><table>
    <thead><tr><th>Region</th><th>Primary heat</th><th>Supplemental</th></tr></thead>
    <tbody>
      <tr><td>Southeast and Gulf</td><td>1–2 cords</td><td>½–1 cord</td></tr>
      <tr><td>Mid-Atlantic, lower Midwest</td><td>2–3 cords</td><td>1–1½ cords</td></tr>
      <tr><td>Northeast, upper Midwest</td><td>3–4 cords</td><td>1½–2 cords</td></tr>
      <tr><td>Far north and mountain West</td><td>4–5 cords</td><td>2 cords</td></tr>
    </tbody>
  </table></div>

  <h2>What a cord actually is</h2>
  <p>A full cord is a stack 4 feet high, 4 feet deep and 8 feet long: 128 cubic feet, about 85 of it solid wood. A "face cord," "rick" or "rack" is one row of that stack, 4 by 8, and its depth is however long the pieces are cut. With 16-inch firewood a face cord is one third of a full cord. Sellers who quote a "cord" of 16-inch wood for a suspiciously low price are often selling a face cord. Ask for the stacked dimensions, then use the stack converter above.</p>

  <h2>Heat in a cord, by species</h2>
  <p>Seasoned hardwood at 20 percent moisture, millions of BTU per full cord.</p>
  <div class="tbl"><table>
    <thead><tr><th>Species</th><th>Million BTU / cord</th><th>Compared to mixed hardwood</th></tr></thead>
    <tbody>
      <tr><td>Hickory, black locust, osage orange</td><td>27–30</td><td>burns 25–40% longer</td></tr>
      <tr><td>White oak, red oak, sugar maple, beech</td><td>24–26</td><td>burns 15–20% longer</td></tr>
      <tr><td>Ash, red maple, black walnut</td><td>20–21</td><td>about the same</td></tr>
      <tr><td>Cherry, elm, sycamore</td><td>18–20</td><td>10% shorter</td></tr>
      <tr><td>Southern yellow pine, fir</td><td>15–17</td><td>25% shorter</td></tr>
      <tr><td>Poplar, sweetgum, cottonwood, willow</td><td>12–14</td><td>40% shorter</td></tr>
    </tbody>
  </table></div>

  <h2>Seasoning changes everything</h2>
  <p>Green wood is nearly half water by weight. Burning it spends a third of its heat boiling that water off and sends the rest up the chimney as creosote. Oak needs 12 to 24 months split and stacked off the ground; softer hardwoods and pine 6 to 12. A $20 moisture meter tells you where a split stands: under 20 percent is ready. If you are buying "seasoned" wood in October, assume it is not, and buy next winter's wood this year.</p>

  <h2>Frequently asked</h2>
'''

FAQS=[
("How many cords of wood do I need for winter?","Most homes heated primarily with wood burn 3 to 5 cords a season. In the Southeast, 1 to 2 cords per 1,000 square feet; in the North, 3 to 4. Supplemental burners need about half that."),
("How much wood is a face cord?","One third of a full cord when the pieces are cut 16 inches long: a stack 4 feet high by 8 feet long by 16 inches deep. A 12-inch face cord is a quarter cord."),
("How long does a cord of wood last?","Burning as primary heat in a cold climate, about a month. As supplemental evening heat in a mild climate, a full season. Most families with an EPA stove in the mid-South get 6 to 8 weeks of steady heating per cord."),
("How much does a cord of firewood cost?","In 2026, $200 to $350 delivered for seasoned mixed hardwood in most of the country, more near big cities and in the Northeast, less in rural areas with lots of timber. A face cord usually sells for $80 to $130."),
("How many pickup loads are in a cord?","A standard half-ton pickup with an 8-foot bed holds about a third of a cord stacked level, a bit more heaped. Three full loads is roughly one cord."),
]

GEAR=[
("Moisture meter","$20 settles every argument with a wood seller and tells you which stack is ready to burn.","https://www.amazon.com/s?k=firewood+moisture+meter","Shop moisture meters"),
("Firewood rack with cover","Off the ground and covered on top only, wood seasons in half the time and stays dry for the stove.","https://www.amazon.com/s?k=outdoor+firewood+rack+with+cover","Shop firewood racks"),
("Kindling splitter","The safe way to make kindling, and the thing that gets a cold stove drawing in five minutes.","https://www.amazon.com/s?k=kindling+splitter","Shop kindling splitters"),
("Stove thermometer","Shows the burn zone so you stop smoldering wood you worked hard to cut.","https://www.amazon.com/s?k=wood+stove+thermometer+magnetic","Shop stove thermometers"),
]

TAIL = r'''</div>
<script>
(function(){
  var $=function(id){return document.getElementById(id)};
  var f={sqft:$('sqft'),climate:$('climate'),use:$('use'),insul:$('insul'),stove:$('stove'),species:$('species'),price:$('price'),have:$('have'),sl:$('sl'),sh:$('sh'),sw:$('sw')};
  var fmt=function(n,d){return n.toLocaleString('en-US',{maximumFractionDigits:d==null?0:d,minimumFractionDigits:d==null?0:d})};
  var last='';
  function calc(){
    var sq=+f.sqft.value||0, cl=+f.climate.value, use=+f.use.value, ins=+f.insul.value, st=+f.stove.value, sp=+f.species.value||21;
    var price=+f.price.value||0, have=+f.have.value||0;
    var base=sq/1000*cl;
    var afterUse=base*use;
    var afterAdj=afterUse*ins*st;
    var cords=afterAdj*(21/sp);
    var lo=cords*0.8, hi=cords*1.25;
    var face=cords*3, loads=cords*3;
    var stackLen=cords*128/(4*4/3); // 4 ft high, 16 in deep -> length in feet
    var need=Math.max(0,cords-have);
    var cost=price>0?need*price:null;
    $('r-cords').textContent=fmt(cords,1)+(cords===1?' cord':' cords');
    $('r-range').textContent='full cords, likely '+fmt(lo,1)+' to '+fmt(hi,1);
    $('r-base').textContent=fmt(base,1);
    $('r-use').textContent=fmt(afterUse,1);
    $('r-adj').textContent=fmt(afterAdj,1);
    $('r-sp').textContent=fmt(cords,1);
    $('r-face').textContent=fmt(face,1);
    $('r-loads').textContent='~'+fmt(loads,0);
    $('r-stack').textContent=fmt(stackLen,0)+' ft long × 16 in deep';
    $('r-need').textContent=fmt(need,1)+' cords';
    $('r-cost').textContent=cost==null?'your labor':'$'+fmt(cost,0);
    $('r-note').textContent='Round up. A mild winter leaves you a head start on next year; a hard one with no wood in February costs double.';
    // stack converter
    var L=+f.sl.value||0,H=+f.sh.value||0,W=(+f.sw.value||0)/12;
    var sc=L*H*W/128;
    $('stack-out').value=sc>0?fmt(sc,2)+' cords ('+fmt(sc*3,1)+' face)':'—';
    last='Firewood: '+fmt(sq)+' sq ft, climate factor '+cl+', '+f.use.options[f.use.selectedIndex].text+', '+f.species.options[f.species.selectedIndex].text+' → about '+fmt(cords,1)+' full cords ('+fmt(lo,1)+'–'+fmt(hi,1)+'), '+fmt(face,1)+' face cords. Have '+have+', need '+fmt(need,1)+(cost!=null?' ≈ $'+fmt(cost,0):'')+'.';
  }
  Object.keys(f).forEach(function(k){ f[k].addEventListener('input',calc); f[k].addEventListener('change',calc); });
  $('fwform').addEventListener('submit',function(e){e.preventDefault();calc();});
  $('reset').addEventListener('click',function(){ f.sqft.value=1800;f.climate.value='1.5';f.use.value='1';f.insul.value='1';f.stove.value='1';f.species.selectedIndex=0;f.price.value=250;f.have.value=0;f.sl.value=16;f.sh.value=4;f.sw.value=16;calc(); });
  $('copy').addEventListener('click',function(){
    var done=function(){$('copied').hidden=false;setTimeout(function(){$('copied').hidden=true},1800)};
    function fallback(){var t=document.createElement('textarea');t.value=last;document.body.appendChild(t);t.select();try{document.execCommand('copy');done()}catch(e){}document.body.removeChild(t)}
    if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(last).then(done,fallback)}else{fallback()}
  });
  calc();
})();
</script>'''

def build(page,header,footer,gear,faq_html):
    body='<div class="wrap">\n'+header('Wood heat','How many cords of firewood do you need?','House size, climate, stove and species in; full cords, face cords, pickup loads and dollars out. Plus a stack converter so nobody sells you a face cord as a cord.')+'\n'+CALC+'\n'+gear('Burn less wood for the same heat','Dry wood in a hot stove is the whole game. These are the cheap tools that get you there.',GEAR)+'\n'+ARTICLE+faq_html(FAQS)+'\n</article>\n'+footer('Regional cord estimates from University of Maine Extension, Penn State Extension and the US Forest Service firewood BTU tables.')+'\n'+TAIL
    return page('firewood-calculator','Firewood Calculator: How Many Cords Do You Need? | Back Forty Tools','Firewood Calculator','Free firewood calculator. Enter square footage, climate, stove type and wood species to get full cords, face cords, pickup loads and cost for the season, plus a stack-to-cord converter.',body,FAQS,'Firewood Calculator')
