# Fence materials calculator
CALC = r'''<section class="calc" aria-label="Fence calculator">
  <form class="panel" id="fcform" autocomplete="off">
    <h2>Your fence line</h2>
    <div class="grid">
      <label>How do you know the length?
        <select id="mode">
          <option value="len" selected>I know the total feet</option>
          <option value="rect">Rectangle, length × width</option>
          <option value="acres">Square-ish field, I know the acres</option>
        </select>
      </label>
      <label id="w-len">Total fence length <small>feet</small>
        <input id="len" type="number" min="10" step="10" value="1320" inputmode="numeric">
      </label>
      <label id="w-l" hidden>Length <small>feet</small><input id="dl" type="number" min="10" step="10" value="400" inputmode="numeric"></label>
      <label id="w-w" hidden>Width <small>feet</small><input id="dw" type="number" min="10" step="10" value="250" inputmode="numeric"></label>
      <label id="w-ac" hidden>Acres<input id="ac" type="number" min="0.1" step="0.5" value="5" inputmode="decimal"></label>
      <label>Fence type
        <select id="type">
          <option value="woven" data-sp="10" data-str="1" data-ppf="1.10" selected>Woven wire / field fence</option>
          <option value="barbed" data-sp="12" data-str="5" data-ppf="0.11">Barbed wire, 5 strand</option>
          <option value="hitensile" data-sp="20" data-str="5" data-ppf="0.06">High-tensile electric, 5 strand</option>
          <option value="board" data-sp="8" data-str="4" data-ppf="1.60">Board fence, 4 rail</option>
          <option value="poly" data-sp="25" data-str="3" data-ppf="0.04">Polywire / temporary electric, 3 strand</option>
        </select>
      </label>
      <label>Post spacing <small>feet</small>
        <input id="spacing" type="number" min="4" max="40" step="1" value="10" inputmode="numeric">
      </label>
      <label>Corners and ends <small>each gets a braced H-assembly</small>
        <input id="corners" type="number" min="0" step="1" value="4" inputmode="numeric">
      </label>
      <label>Gates
        <input id="gates" type="number" min="0" step="1" value="2" inputmode="numeric">
      </label>
      <label>Line post price <small>$ each</small><input id="pp" type="number" min="0" step="0.5" value="6" inputmode="decimal"></label>
      <label>Corner/brace post price <small>$ each</small><input id="cp" type="number" min="0" step="0.5" value="22" inputmode="decimal"></label>
      <label>Wire or boards <small>$ per foot of fence, all strands</small><input id="wp" type="number" min="0" step="0.05" value="1.10" inputmode="decimal"></label>
      <label>Gate price <small>$ each, hung</small><input id="gp" type="number" min="0" step="5" value="160" inputmode="numeric"></label>
    </div>
  </form>

  <aside class="panel results" aria-live="polite">
    <div class="tag">
      <div class="lbl">Materials estimate</div>
      <div class="big" id="r-cost">—</div>
      <div class="sub" id="r-perft">—</div>
    </div>
    <dl class="rows">
      <dt>Fence length</dt><dd id="r-len">—</dd>
      <dt>Line posts</dt><dd id="r-posts">—</dd>
      <dt>Corner, end and brace posts</dt><dd id="r-cposts">—</dd>
      <dt>Brace rails</dt><dd id="r-rails">—</dd>
      <dt>Wire or boards</dt><dd id="r-wire">—</dd>
      <dt>Staples / clips / insulators</dt><dd id="r-hw">—</dd>
      <dt>Gates</dt><dd id="r-gates">—</dd>
      <dt class="total">Posts cost</dt><dd class="total" id="r-pc">—</dd>
      <dt>Wire cost</dt><dd id="r-wc">—</dd>
      <dt>Gates cost</dt><dd id="r-gc">—</dd>
      <dt>Hardware, 8%</dt><dd id="r-hc">—</dd>
      <dt class="total">Rough labor if hired</dt><dd class="total" id="r-labor">—</dd>
    </dl>
    <p class="note" id="r-note"></p>
    <div style="display:flex;gap:10px;flex-wrap:wrap;align-items:center">
      <button class="btn" type="button" id="copy">Copy list</button>
      <button class="btn ghost" type="button" id="reset">Reset</button>
      <span class="copied" id="copied" hidden>Copied</span>
    </div>
  </aside>
</section>'''

ARTICLE = r'''<article>
  <h2>How the calculator works</h2>
  <p>A fence is posts, something stretched between them, and the corners that hold the tension. The count is simple once you know the length.</p>
  <div class="formula">line posts = length ÷ spacing &nbsp;·&nbsp; each corner or end = 2 posts + 1 brace rail &nbsp;·&nbsp; wire = length × strands</div>
  <p>A quarter mile (1,320 feet) of woven wire at 10-foot spacing needs about 132 line posts, four braced corners (8 heavy posts and 4 rails), 1,320 feet of fence and roughly 1,500 staples. In 2026 that is about $2,400 in materials at farm-store prices, or $1.80 a foot. Barbed wire on the same line runs about $1.20 a foot; high-tensile electric about $0.90; four-board about $8 to $12.</p>

  <h2>Fence length by field size</h2>
  <p>A square field is the cheapest shape to fence. Long narrow fields can need half again as much.</p>
  <div class="tbl"><table>
    <thead><tr><th>Acres</th><th>Square, feet of fence</th><th>2:1 rectangle</th><th>4:1 rectangle</th></tr></thead>
    <tbody>
      <tr><td>1</td><td>835</td><td>885</td><td>1,045</td></tr>
      <tr><td>5</td><td>1,867</td><td>1,980</td><td>2,335</td></tr>
      <tr><td>10</td><td>2,640</td><td>2,800</td><td>3,300</td></tr>
      <tr><td>20</td><td>3,733</td><td>3,960</td><td>4,670</td></tr>
      <tr><td>40</td><td>5,280</td><td>5,600</td><td>6,600</td></tr>
    </tbody>
  </table></div>

  <h2>Post spacing by fence type</h2>
  <div class="tbl"><table>
    <thead><tr><th>Fence</th><th>Line post spacing</th><th>Strands / rails</th><th>Materials, $/ft (2026)</th></tr></thead>
    <tbody>
      <tr><td>Woven wire, 47-inch</td><td>8–12 ft</td><td>1 roll</td><td>$1.60–2.20</td></tr>
      <tr><td>Barbed wire, cattle</td><td>10–15 ft</td><td>4–5</td><td>$1.00–1.40</td></tr>
      <tr><td>High-tensile electric</td><td>20–30 ft</td><td>3–5</td><td>$0.70–1.10</td></tr>
      <tr><td>Board, 3 or 4 rail</td><td>8 ft</td><td>3–4</td><td>$8–14</td></tr>
      <tr><td>Polywire, temporary</td><td>25–50 ft step-ins</td><td>1–3</td><td>$0.15–0.35</td></tr>
    </tbody>
  </table></div>

  <h2>Corners are where fences fail</h2>
  <p>Every corner, end and gate opening needs a braced assembly: two 6- to 8-inch posts set 3 feet deep, a horizontal rail between them, and a diagonal brace wire. Skip the brace and the corner leans within two winters and the whole run goes slack. The calculator counts two heavy posts and one rail per corner, which is the standard single H-brace; long runs over 600 feet of high-tensile need a double.</p>

  <h2>Labor</h2>
  <p>Fence contractors in the Southeast charge roughly $2 to $4 a foot for barbed or woven wire installed, $6 to $10 for high-tensile with the energizer, and $15 to $25 for board. Hire out the corners and gates and drive your own line posts and you'll keep most of the savings with little of the frustration.</p>

  <h2>Frequently asked</h2>
'''

FAQS=[
("How many T-posts do I need for 1 acre?","A square acre is about 835 feet around. At 10-foot spacing that is 84 line posts, plus 8 wooden corner posts and 4 brace rails. Add a gate and 90 T-posts is a safe buy."),
("How much does it cost to fence 5 acres?","About 1,870 feet of fence for a square 5 acres. Materials run roughly $2,000 for barbed wire, $3,400 for woven wire, $1,700 for high-tensile electric or $18,000 for board fence. Installed, double those numbers."),
("How far apart should fence posts be?","8 to 12 feet for woven wire, 10 to 15 for barbed, 20 to 30 for high-tensile electric, and 8 feet for board fence. Closer on curves, hills and where livestock crowd a corner."),
("How many feet of fence is a quarter mile?","1,320 feet. A roll of barbed wire is 1,320 feet for a reason; a 330-foot roll of woven wire is a quarter of that."),
("How deep should a corner post be set?","One third of its length, minimum 3 feet, in a hole at least twice the post diameter. Tamp dry, or use concrete only below grade so the post doesn't rot at the collar."),
]

GEAR=[
("Post driver or post pounder","Drives a T-post in under a minute. Rent a gas one for a long run.","https://www.tractorsupply.com/tsc/search/t%20post%20driver","Shop post drivers"),
("Fence stretcher / come-along","Woven and high-tensile fence only works when it's tight. This is what gets it there.","https://www.tractorsupply.com/tsc/search/fence%20stretcher","Shop stretchers"),
("Brace wire and in-line strainers","The diagonal wire on every H-brace, plus strainers to re-tension high-tensile each spring.","https://www.tractorsupply.com/tsc/search/fence%20strainer","Shop strainers"),
("Fence pliers","One tool for staples, splices and twisting. Keep it on the four-wheeler.","https://www.amazon.com/s?k=fencing+pliers","Shop fence pliers"),
]

TAIL = r'''</div>
<script>
(function(){
  var $=function(id){return document.getElementById(id)};
  var f={mode:$('mode'),len:$('len'),dl:$('dl'),dw:$('dw'),ac:$('ac'),type:$('type'),spacing:$('spacing'),corners:$('corners'),gates:$('gates'),pp:$('pp'),cp:$('cp'),wp:$('wp'),gp:$('gp')};
  var fmt=function(n,d){return n.toLocaleString('en-US',{maximumFractionDigits:d==null?0:d,minimumFractionDigits:d==null?0:d})};
  var usd=function(n){return '$'+fmt(n,0)};
  var last='';
  function showMode(){ var m=f.mode.value; $('w-len').hidden=m!=='len'; $('w-l').hidden=m!=='rect'; $('w-w').hidden=m!=='rect'; $('w-ac').hidden=m!=='acres'; }
  function calc(){
    var m=f.mode.value, L;
    if(m==='len') L=+f.len.value||0;
    else if(m==='rect') L=2*((+f.dl.value||0)+(+f.dw.value||0));
    else L=4*Math.sqrt((+f.ac.value||0)*43560);
    var sp=+f.spacing.value||10, corners=+f.corners.value||0, gates=+f.gates.value||0;
    var o=f.type.options[f.type.selectedIndex]; var strands=+o.getAttribute('data-str'); var t=f.type.value;
    var netLen=Math.max(0,L-gates*12);
    var posts=Math.ceil(netLen/sp)-corners;  if(posts<0)posts=0;
    var cposts=corners*2+gates*2;
    var rails=corners+gates;
    var wireFt=netLen*strands;
    var hw= t==='board'? Math.ceil(posts*strands*2)+' screws/nails' : t==='hitensile'||t==='poly'? fmt(posts*strands)+' insulators' : fmt(posts*(t==='woven'?6:strands))+' staples';
    var pc=posts*(+f.pp.value||0)+cposts*(+f.cp.value||0)+rails*(+f.cp.value||0)*0.6;
    var wc=netLen*(+f.wp.value||0);
    var gc=gates*(+f.gp.value||0);
    var hc=(pc+wc)*0.08;
    var total=pc+wc+gc+hc;
    var laborRate= t==='board'?18: t==='hitensile'?7: t==='poly'?0.5:3;
    var labor=L*laborRate;
    $('r-cost').textContent=usd(total);
    $('r-perft').textContent='materials, '+ (L?('$'+(total/L).toFixed(2)+' per foot'):'');
    $('r-len').textContent=fmt(L)+' ft'+(m!=='len'?' (computed)':'');
    $('r-posts').textContent=fmt(posts)+' @ '+sp+' ft';
    $('r-cposts').textContent=fmt(cposts);
    $('r-rails').textContent=fmt(rails);
    $('r-wire').textContent= t==='woven'?fmt(netLen)+' ft ('+Math.ceil(netLen/330)+' rolls of 330)': t==='board'? fmt(wireFt)+' ft of board ('+Math.ceil(wireFt/16)+' 16-ft boards)': fmt(wireFt)+' ft ('+Math.ceil(wireFt/(t==='barbed'?1320:4000))+' rolls)';
    $('r-hw').textContent=hw;
    $('r-gates').textContent=fmt(gates);
    $('r-pc').textContent=usd(pc); $('r-wc').textContent=usd(wc); $('r-gc').textContent=usd(gc); $('r-hc').textContent=usd(hc);
    $('r-labor').textContent='+ '+usd(labor);
    $('r-note').textContent='Prices are yours to edit; defaults are 2026 farm-store averages. Buy 5% extra wire for splices and sag.';
    last='Fence: '+fmt(L)+' ft '+o.text+'. '+posts+' line posts @ '+sp+' ft, '+cposts+' corner/brace posts, '+rails+' rails, '+$('r-wire').textContent+', '+hw+', '+gates+' gates. Materials ≈ '+usd(total)+' ($'+(L?(total/L).toFixed(2):'0')+'/ft); hired labor ≈ '+usd(labor)+'.';
  }
  f.mode.addEventListener('change',function(){showMode();calc();});
  f.type.addEventListener('change',function(){ var o=f.type.options[f.type.selectedIndex]; f.spacing.value=o.getAttribute('data-sp'); f.wp.value=o.getAttribute('data-ppf'); calc(); });
  Object.keys(f).forEach(function(k){ f[k].addEventListener('input',calc); });
  $('fcform').addEventListener('submit',function(e){e.preventDefault();calc();});
  $('reset').addEventListener('click',function(){ f.mode.value='len';showMode();f.len.value=1320;f.dl.value=400;f.dw.value=250;f.ac.value=5;f.type.selectedIndex=0;f.spacing.value=10;f.corners.value=4;f.gates.value=2;f.pp.value=6;f.cp.value=22;f.wp.value=1.10;f.gp.value=160;calc(); });
  $('copy').addEventListener('click',function(){
    var done=function(){$('copied').hidden=false;setTimeout(function(){$('copied').hidden=true},1800)};
    function fallback(){var t=document.createElement('textarea');t.value=last;document.body.appendChild(t);t.select();try{document.execCommand('copy');done()}catch(e){}document.body.removeChild(t)}
    if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(last).then(done,fallback)}else{fallback()}
  });
  showMode(); calc();
})();
</script>'''

def build(page,header,footer,gear,faq_html):
    body='<div class="wrap">\n'+header('Fencing','How many posts, how much wire, what will it cost?','Length, fence type and spacing in; a shopping list and a materials total out. Prices are editable so the number matches your farm store.')+'\n'+CALC+'\n'+gear('The tools that make a fence last','Tight wire and braced corners are the whole difference between a 5-year fence and a 30-year fence.',GEAR)+'\n'+ARTICLE+faq_html(FAQS)+'\n</article>\n'+footer('Spacing and brace guidance from UGA Extension, Penn State Extension and the USDA NRCS fence standards; prices from 2026 farm-store averages.')+'\n'+TAIL
    return page('fence-calculator','Fence Calculator: Posts, Wire and Cost for Farm Fencing | Back Forty Tools','Farm Fence Calculator','Free farm fence calculator. Enter length (or acres), fence type and post spacing to get line posts, corner posts, brace rails, wire rolls, hardware, gates and a materials cost estimate.',body,FAQS,'Farm Fence Calculator')
