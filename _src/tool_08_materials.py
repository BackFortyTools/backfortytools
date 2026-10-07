# Bulk material calculator: gravel, dirt, sand, concrete, mulch
CALC = r'''<section class="calc" aria-label="Gravel, dirt and concrete calculator">
  <form class="panel" id="bmform" autocomplete="off">
    <h2>Your project</h2>
    <div class="grid">
      <label>Material
        <select id="mat">
          <optgroup label="Gravel and stone">
            <option value="1.40" data-cat="gravel" selected>Crusher run / #57 gravel (1.40 t/yd³)</option>
            <option value="1.35" data-cat="gravel">Pea gravel / river rock (1.35)</option>
            <option value="1.25" data-cat="gravel">Limestone #3 / rip rap (1.25)</option>
            <option value="1.50" data-cat="gravel">Granite screenings / M10 dust (1.50)</option>
          </optgroup>
          <optgroup label="Dirt and sand">
            <option value="1.10" data-cat="dirt">Topsoil, loose (1.10)</option>
            <option value="1.30" data-cat="dirt">Fill dirt / clay (1.30)</option>
            <option value="1.35" data-cat="dirt">Sand, masonry or concrete (1.35)</option>
            <option value="0.80" data-cat="dirt">Garden soil / compost mix (0.80)</option>
          </optgroup>
          <optgroup label="Concrete">
            <option value="2.0" data-cat="concrete">Concrete, ready-mix or bags</option>
          </optgroup>
          <optgroup label="Mulch and bedding">
            <option value="0.40" data-cat="mulch">Hardwood mulch (0.40)</option>
            <option value="0.30" data-cat="mulch">Pine straw / bark nuggets (0.30)</option>
          </optgroup>
        </select>
      </label>
      <label>Shape
        <select id="shape">
          <option value="rect" selected>Rectangle (pad, driveway, bed)</option>
          <option value="circle">Circle (fire pit, round pad)</option>
          <option value="tri">Triangle</option>
        </select>
      </label>
      <label id="w-l">Length <small>feet</small><input id="L" type="number" min="0" step="1" value="60" inputmode="decimal"></label>
      <label id="w-w">Width <small>feet</small><input id="W" type="number" min="0" step="1" value="12" inputmode="decimal"></label>
      <label id="w-d" hidden>Diameter <small>feet</small><input id="D" type="number" min="0" step="1" value="12" inputmode="decimal"></label>
      <label>Depth <small>inches</small><input id="depth" type="number" min="0.5" step="0.5" value="4" inputmode="decimal"></label>
      <label>Compaction / settling allowance <small>%; gravel 15, dirt 20, concrete 5</small>
        <input id="waste" type="number" min="0" max="50" step="5" value="15" inputmode="numeric">
      </label>
      <label>Price <small id="pl">$ per ton delivered</small>
        <input id="price" type="number" min="0" step="1" value="38" inputmode="decimal">
      </label>
      <label>Truck size <small>tons per load</small>
        <input id="truck" type="number" min="1" step="1" value="18" inputmode="numeric">
      </label>
    </div>
  </form>

  <aside class="panel results" aria-live="polite">
    <div class="tag">
      <div class="lbl">Order this much</div>
      <div class="big" id="r-main">—</div>
      <div class="sub" id="r-sub">—</div>
    </div>
    <dl class="rows">
      <dt>Area</dt><dd id="r-area">—</dd>
      <dt>Volume, exact</dt><dd id="r-vol">—</dd>
      <dt>With allowance</dt><dd id="r-volw">—</dd>
      <dt class="total">Cubic yards</dt><dd class="total" id="r-yd">—</dd>
      <dt id="l-tons">Tons</dt><dd id="r-tons">—</dd>
      <dt id="l-bags">Bags</dt><dd id="r-bags">—</dd>
      <dt>Truckloads</dt><dd id="r-loads">—</dd>
      <dt>Pickup loads (½ ton, ~¾ yd³)</dt><dd id="r-pickup">—</dd>
      <dt class="total">Estimated cost</dt><dd class="total cost" id="r-cost">—</dd>
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
  <p>Every bulk material is sold by the cubic yard or the ton, and the quarry converts between them with a density. We do the same.</p>
  <div class="formula">length × width × (depth ÷ 12) ÷ 27 = cubic yards &nbsp;·&nbsp; cubic yards × density = tons</div>
  <p>A 60 by 12 foot driveway topped with 4 inches of crusher run is 240 cubic feet, or 8.9 cubic yards. Crusher run weighs about 1.4 tons a yard, so that is 12.4 tons before compaction. Gravel packs down 10 to 20 percent when you run a plate compactor or just drive on it, so order 14 to 15 tons. That is one full tandem dump truck, and at $38 a ton delivered it comes to about $550.</p>

  <h2>Weight per cubic yard</h2>
  <div class="tbl"><table>
    <thead><tr><th>Material</th><th>Tons per yd³</th><th>Pounds per yd³</th></tr></thead>
    <tbody>
      <tr><td>Crusher run, #57, #67 gravel</td><td>1.35–1.45</td><td>2,700–2,900</td></tr>
      <tr><td>Pea gravel, river rock</td><td>1.30–1.40</td><td>2,600–2,800</td></tr>
      <tr><td>Granite screenings, M10</td><td>1.45–1.55</td><td>2,900–3,100</td></tr>
      <tr><td>Sand, damp</td><td>1.30–1.40</td><td>2,600–2,800</td></tr>
      <tr><td>Topsoil, loose</td><td>1.00–1.20</td><td>2,000–2,400</td></tr>
      <tr><td>Fill dirt, clay, damp</td><td>1.25–1.40</td><td>2,500–2,800</td></tr>
      <tr><td>Concrete, cured</td><td>2.0</td><td>4,000</td></tr>
      <tr><td>Hardwood mulch</td><td>0.35–0.45</td><td>700–900</td></tr>
    </tbody>
  </table></div>

  <h2>How deep?</h2>
  <p>A gravel driveway on firm ground wants 4 inches of base; on soft or clay ground, 6 to 8 inches, ideally in two lifts with the bigger stone (#3 or #4) on the bottom. A barn pad or parking area that will see trucks: 6 inches minimum. Walkways and patios, 2 to 3 inches over compacted base. For concrete, a sidewalk is 4 inches, a driveway or shop slab 5 to 6, and anything that will carry a tractor or a loaded trailer 6 inches with rebar.</p>

  <h2>Concrete: bags or a truck?</h2>
  <p>An 80-pound bag of concrete mix yields 0.6 cubic feet; it takes 45 bags to make a yard. Under about a yard, bags make sense. Above that, call a ready-mix plant: most charge $140 to $180 a yard in 2026 with a short-load fee under 4 or 5 yards. A 12 by 12 slab at 4 inches is 1.8 yards, which is 80 bags of mixing by hand or one short truck. The truck wins.</p>

  <h2>Truckloads</h2>
  <p>A single-axle dump truck carries 8 to 10 tons; a tandem 15 to 20; a tri-axle 22 to 25. Most quarries and landscape yards deliver by the full load or charge the same delivery fee for a partial, so sizing a project to fill a truck saves money. A half-ton pickup can haul about three quarters of a yard of gravel (1 ton) safely, which is why a driveway takes a dump truck and a flower bed takes a pickup.</p>

  <h2>Frequently asked</h2>
'''

FAQS=[
("How many tons of gravel do I need for a driveway?","For a 4-inch layer, multiply length × width in feet by 0.0173 to get tons of crusher run, then add 15% for compaction. A 100 × 12 foot driveway needs about 24 tons."),
("How much does a cubic yard of gravel weigh?","About 2,800 pounds, or 1.4 tons, for crusher run and #57 stone. Pea gravel is slightly lighter; screenings and stone dust slightly heavier."),
("How many cubic yards in a dump truck?","A tandem dump truck holds 10 to 14 cubic yards of gravel, which is 15 to 20 tons. A single-axle holds 5 to 7 yards. Ask your supplier what their truck carries; it varies."),
("How many 80 lb bags of concrete make a yard?","45 bags. Each 80-pound bag yields 0.6 cubic feet and a cubic yard is 27 cubic feet. A 60-pound bag yields 0.45 cubic feet, so 60 of those."),
("How much topsoil do I need to cover 1,000 square feet?","At 2 inches deep, 6.2 cubic yards, which is about 7 tons loose. At 4 inches, 12.4 yards. Order 10 to 20 percent extra; topsoil settles."),
]

GEAR=[
("Plate compactor (rent or buy)","Gravel that isn't compacted is gravel you'll re-order next year. A rental runs $70 a day.","https://www.amazon.com/s?k=plate+compactor","Shop plate compactors"),
("Landscape rake, 36-inch","Spreads a dump-truck load evenly without renting a skid steer.","https://www.tractorsupply.com/tsc/search/landscape%20rake","Shop landscape rakes"),
("Geotextile fabric","Under the gravel on soft ground. Stops the stone from sinking into the clay, which is where half of all driveway gravel goes.","https://www.amazon.com/s?k=driveway+geotextile+fabric","Shop driveway fabric"),
("Concrete float and edger set","For the slab work the calculator just sized. Cheap tools, big difference in the finish.","https://www.amazon.com/s?k=concrete+finishing+tool+set","Shop finishing tools"),
]

TAIL = r'''</div>
<script>
(function(){
  var $=function(id){return document.getElementById(id)};
  var f={mat:$('mat'),shape:$('shape'),L:$('L'),W:$('W'),D:$('D'),depth:$('depth'),waste:$('waste'),price:$('price'),truck:$('truck')};
  var fmt=function(n,d){return n.toLocaleString('en-US',{maximumFractionDigits:d==null?0:d,minimumFractionDigits:d==null?0:d})};
  var usd=function(n){return '$'+fmt(n,0)};
  var last='';
  function cat(){return f.mat.options[f.mat.selectedIndex].getAttribute('data-cat')}
  function showShape(){ var s=f.shape.value; $('w-d').hidden=s!=='circle'; $('w-l').hidden=s==='circle'; $('w-w').hidden=s==='circle'; }
  function matChanged(){
    var c=cat();
    var def={gravel:[15,38,'$ per ton delivered'],dirt:[20,30,'$ per ton delivered'],concrete:[5,160,'$ per cubic yard, ready-mix'],mulch:[10,35,'$ per cubic yard']}[c];
    f.waste.value=def[0]; f.price.value=def[1]; $('pl').textContent=def[2];
  }
  function calc(){
    var s=f.shape.value, area;
    if(s==='circle'){var r=(+f.D.value||0)/2; area=Math.PI*r*r;}
    else if(s==='tri'){area=(+f.L.value||0)*(+f.W.value||0)/2;}
    else area=(+f.L.value||0)*(+f.W.value||0);
    var depth=+f.depth.value||0, waste=(+f.waste.value||0)/100, dens=+f.mat.value, price=+f.price.value||0, truck=+f.truck.value||18;
    var c=cat();
    var cf=area*depth/12;
    var yd=cf/27;
    var ydw=yd*(1+waste);
    var tons=ydw*dens;
    var main,sub,bags,bagsLabel,cost,loads;
    if(c==='concrete'){
      bags=Math.ceil(ydw*45); bagsLabel='80-lb bags (45/yd³)';
      cost=ydw*price; loads=Math.ceil(ydw/10);
      main=fmt(ydw,2)+' yd³'; sub='ready-mix, or '+fmt(bags)+' 80-lb bags';
      $('l-tons').textContent='Weight when cured'; $('r-tons').textContent=fmt(tons,1)+' tons';
    } else if(c==='mulch'){
      bags=Math.ceil(ydw*13.5); bagsLabel='2-cu-ft bags';
      cost=ydw*price; loads=Math.ceil(ydw/12);
      main=fmt(ydw,1)+' yd³'; sub='bulk, or '+fmt(bags)+' 2-cu-ft bags';
      $('l-tons').textContent='Weight'; $('r-tons').textContent=fmt(tons,1)+' tons';
    } else {
      bags=Math.ceil(ydw*54); bagsLabel='0.5-cu-ft bags (54/yd³)';
      cost=tons*price; loads=Math.ceil(tons/truck);
      main=fmt(tons,1)+' tons'; sub=fmt(ydw,1)+' cubic yards with '+Math.round(waste*100)+'% allowance';
      $('l-tons').textContent='Tons'; $('r-tons').textContent=fmt(tons,1);
    }
    $('r-main').textContent=main; $('r-sub').textContent=sub;
    $('r-area').textContent=fmt(area)+' sq ft';
    $('r-vol').textContent=fmt(cf)+' cu ft = '+fmt(yd,2)+' yd³';
    $('r-volw').textContent=fmt(ydw,2)+' yd³';
    $('r-yd').textContent=fmt(ydw,1);
    $('l-bags').textContent=bagsLabel; $('r-bags').textContent=fmt(bags);
    $('r-loads').textContent=c==='concrete'?fmt(loads)+' mixer truck'+(loads===1?'':'s'):fmt(loads)+' @ '+truck+' tons';
    $('r-pickup').textContent=c==='concrete'?'—':fmt(Math.ceil(ydw/0.75));
    $('r-cost').textContent=price>0?usd(cost):'—';
    $('r-note').textContent=c==='concrete'?'Under 1 yard, bags are fine. Over that, call for a truck; most plants charge a short-load fee under 4–5 yards.':'Suppliers round to the half ton. Ask what one truckload is before you order a partial.';
    last='Material: '+f.mat.options[f.mat.selectedIndex].text+', '+fmt(area)+' sq ft × '+depth+' in = '+fmt(yd,2)+' yd³, +'+Math.round(waste*100)+'% = '+fmt(ydw,2)+' yd³'+(c==='gravel'||c==='dirt'?' = '+fmt(tons,1)+' tons':'')+'. '+bags+' '+bagsLabel+', '+loads+' truckloads'+(price>0?', ≈ '+usd(cost):'')+'.';
  }
  f.mat.addEventListener('change',function(){matChanged();calc();});
  f.shape.addEventListener('change',function(){showShape();calc();});
  Object.keys(f).forEach(function(k){ f[k].addEventListener('input',calc); });
  $('bmform').addEventListener('submit',function(e){e.preventDefault();calc();});
  $('reset').addEventListener('click',function(){ f.mat.selectedIndex=0;matChanged();f.shape.value='rect';showShape();f.L.value=60;f.W.value=12;f.D.value=12;f.depth.value=4;f.truck.value=18;calc(); });
  $('copy').addEventListener('click',function(){
    var done=function(){$('copied').hidden=false;setTimeout(function(){$('copied').hidden=true},1800)};
    function fallback(){var t=document.createElement('textarea');t.value=last;document.body.appendChild(t);t.select();try{document.execCommand('copy');done()}catch(e){}document.body.removeChild(t)}
    if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(last).then(done,fallback)}else{fallback()}
  });
  showShape(); calc();
})();
</script>'''

def build(page,header,footer,gear,faq_html):
    body='<div class="wrap">\n'+header('Grading & projects','How much gravel, dirt, sand or concrete do you need?','Measure the area, pick the material, set the depth. Get cubic yards, tons, bags, truckloads and a cost, with compaction already added so you don\'t come up short.')+'\n'+CALC+'\n'+gear('Make the first load the only load','Most second orders happen because the base wasn\'t compacted or the gravel sank into soft ground.',GEAR)+'\n'+ARTICLE+faq_html(FAQS)+'\n</article>\n'+footer('Material densities from the National Stone, Sand and Gravel Association and USDA NRCS engineering tables; prices from 2026 Southeastern quarry and ready-mix averages.')+'\n'+TAIL
    return page('gravel-dirt-concrete-calculator','Gravel, Dirt, Sand and Concrete Calculator: Yards, Tons and Cost | Back Forty Tools','Gravel, Dirt and Concrete Calculator','Free bulk material calculator for gravel, crusher run, topsoil, fill dirt, sand, concrete and mulch. Enter area and depth to get cubic yards, tons, bags, truckloads and cost, with compaction allowance.',body,FAQS,'Gravel, Dirt and Concrete Calculator')
