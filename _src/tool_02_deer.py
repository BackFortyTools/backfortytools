# Deer meat yield calculator
CALC = r'''<section class="calc" aria-label="Deer meat yield calculator">
  <form class="panel" id="deerform" autocomplete="off">
    <h2>Your deer</h2>
    <div class="grid">
      <label>What did you weigh?
        <select id="wtype">
          <option value="fd" selected>Field-dressed weight (guts out)</option>
          <option value="live">Live weight (whole deer)</option>
          <option value="girth">I only have chest girth</option>
        </select>
      </label>
      <label id="wrap-weight">Weight <small>pounds</small>
        <input id="weight" type="number" min="20" max="400" step="1" value="130" inputmode="numeric">
      </label>
      <label id="wrap-girth" hidden>Chest girth <small>inches, just behind the front legs</small>
        <input id="girth" type="number" min="20" max="60" step="0.5" value="36" inputmode="decimal">
      </label>
      <label>Shot placement <small>sets meat lost to damage</small>
        <select id="shot">
          <option value="0" selected>Behind the shoulder / neck / head — little loss</option>
          <option value="8">One shoulder — about 8% lost</option>
          <option value="15">Both shoulders or hindquarter — about 15% lost</option>
          <option value="5">Gut shot, recovered quickly — about 5% lost</option>
        </select>
      </label>
      <label>How it'll be cut
        <select id="style">
          <option value="std" selected>Steaks, roasts and ground</option>
          <option value="ground">Mostly ground and sausage</option>
          <option value="bonein">Bone-in cuts (chops, shanks)</option>
        </select>
      </label>
      <label>Pork fat added to sausage/ground <small>% of batch, 0 if none</small>
        <input id="fat" type="number" min="0" max="40" step="5" value="0" inputmode="numeric">
      </label>
      <label>Processor fee <small>$ per deer, 0 if you do it yourself</small>
        <input id="fee" type="number" min="0" step="5" value="110" inputmode="numeric">
      </label>
    </div>
  </form>

  <aside class="panel results" aria-live="polite">
    <div class="tag">
      <div class="lbl">Meat in the freezer</div>
      <div class="big" id="r-meat">—</div>
      <div class="sub" id="r-range">—</div>
    </div>
    <dl class="rows">
      <dt>Live weight</dt><dd id="r-live">—</dd>
      <dt>Field-dressed weight</dt><dd id="r-fd">—</dd>
      <dt>Hanging carcass (skinned, head off)</dt><dd id="r-carc">—</dd>
      <dt>Lost to shot damage</dt><dd id="r-loss">—</dd>
      <dt class="total">Backstraps + tenderloins</dt><dd class="total" id="r-back">—</dd>
      <dt>Hindquarter steaks and roasts</dt><dd id="r-hind">—</dd>
      <dt>Front shoulders</dt><dd id="r-front">—</dd>
      <dt>Neck, flank and trim (ground)</dt><dd id="r-ground">—</dd>
      <dt class="total">Freezer space</dt><dd class="total" id="r-freezer">—</dd>
      <dt>One-pound packages</dt><dd id="r-pkgs">—</dd>
      <dt>Meals (3 people per lb)</dt><dd id="r-meals">—</dd>
      <dt class="total">Cost per pound</dt><dd class="total cost" id="r-cost">—</dd>
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
  <p>Wildlife biologists and university meat labs have weighed enough deer to settle the ratios. We use them in the order a deer actually comes apart.</p>
  <div class="formula">live × 0.78 = field-dressed &nbsp;·&nbsp; field-dressed × 0.75 = hanging carcass &nbsp;·&nbsp; carcass × 0.55 ≈ boneless meat</div>
  <p>Put together, a deer gives back about <strong>40% of its field-dressed weight</strong> as boneless, trimmed venison. A 130-pound field-dressed buck is roughly 52 pounds of meat in the freezer. Hunters who do their own cutting and save every scrap of trim can push that toward 45–50%. A shoulder-shot deer that sat overnight before it was found can drop under 35%.</p>

  <h2>Field-dressed weight from live weight (and back)</h2>
  <p>Field dressing removes about 22% of a whitetail: the gut pile, heart, lungs and blood. So a 165-pound live deer dresses to about 130 pounds. Skinning, removing the head and lower legs takes another 25%, leaving a hanging carcass near 97 pounds. Bone is roughly 45% of that carcass, which is why boneless yield lands where it does.</p>

  <h2>Estimating weight from chest girth</h2>
  <p>No scale in deer camp is normal. A tape measure around the chest, right behind the front legs, gets you close. These figures come from the Penn State and Mississippi State whitetail charts and the calculator uses the same table.</p>
  <div class="tbl"><table>
    <thead><tr><th>Chest girth</th><th>Live weight</th><th>Field-dressed</th><th>Boneless meat</th></tr></thead>
    <tbody>
      <tr><td>28 in</td><td>92 lb</td><td>72 lb</td><td>29 lb</td></tr>
      <tr><td>32 in</td><td>120 lb</td><td>94 lb</td><td>37 lb</td></tr>
      <tr><td>36 in</td><td>155 lb</td><td>121 lb</td><td>48 lb</td></tr>
      <tr><td>40 in</td><td>197 lb</td><td>154 lb</td><td>61 lb</td></tr>
      <tr><td>44 in</td><td>245 lb</td><td>191 lb</td><td>76 lb</td></tr>
    </tbody>
  </table></div>

  <h2>Where the meat is on a deer</h2>
  <p>Of the boneless meat, about 10% is backstrap and tenderloin, 35% comes off the hindquarters as steaks and roasts, 20% is the front shoulders, and the remaining 35% is neck, flank, shank and trim that ends up as ground or sausage. If you tell a processor "all ground," you'll get the same total pounds, just in one shape. If you add pork fat to the ground, the package count goes up but the venison didn't.</p>

  <h2>Freezer space</h2>
  <p>Packed venison runs about 35 pounds per cubic foot. A single average deer takes 1.5 cubic feet; a 5-cubic-foot chest freezer holds three deer with room for the ice cream. Vacuum-sealed packages stack tighter and last two years instead of six months.</p>

  <h2>Processing costs</h2>
  <p>In Georgia and most of the Southeast, basic processing (skin, cut, wrap, ground) runs $90 to $140 per deer in 2026, with sausage, jerky and cubed steak extra. On a 50-pound deer that is about $2.20 a pound before your tag, gas and gear. Do it yourself with a $150 grinder and a $100 vacuum sealer and the gear pays for itself on the second deer.</p>

  <h2>Frequently asked</h2>
'''

FAQS=[
("How much meat do you get from a 150 lb deer?","If 150 pounds is the field-dressed weight, expect about 60 pounds of boneless venison with a clean shot. If it is the live weight, field-dressed will be around 117 pounds and the meat about 47 pounds."),
("How much meat from a 100 lb doe?","A 100-pound field-dressed doe yields roughly 40 pounds of boneless meat. Does are often the better-eating deer because they carry more fat and no rut stress."),
("What percentage of a deer is meat?","About 40% of field-dressed weight, or about 31% of live weight, ends up as boneless trimmed venison. Bone-in cuts raise the number to around 50% of field-dressed weight."),
("How many pounds of meat does a deer processor give back?","Reputable processors return 38 to 45 pounds per 100 pounds field-dressed. If you are consistently getting back less than 35%, ask whether you are getting your own deer back."),
("How much freezer space does a deer take?","About 1.5 cubic feet for an average 50-pound yield. Plan on 35 pounds of packaged meat per cubic foot of freezer."),
]

GEAR=[
("Electric meat grinder, ½ HP or larger","The single purchase that turns one deer into a full freezer of burger, sausage and jerky. Pays for itself the second season.","https://www.amazon.com/s?k=meat+grinder+electric+1%2F2+hp","Shop grinders"),
("Vacuum sealer + bags","Doubles freezer life and stops the freezer burn that ruins the last ten pounds every spring.","https://www.amazon.com/s?k=vacuum+sealer+for+game+meat","Shop vacuum sealers"),
("Gambrel and hoist","Hang the deer at working height and skinning takes ten minutes instead of forty.","https://www.tractorsupply.com/tsc/search/deer%20hoist%20gambrel","Shop hoists"),
("Breathable game bags","Keep flies and dirt off the carcass while it cools. Cheap insurance for the meat you just calculated.","https://www.amazon.com/s?k=deer+game+bags","Shop game bags"),
]

TAIL = r'''</div>
<script>
(function(){
  var $=function(id){return document.getElementById(id)};
  var f={wtype:$('wtype'),weight:$('weight'),girth:$('girth'),shot:$('shot'),style:$('style'),fat:$('fat'),fee:$('fee')};
  var fmt=function(n,d){return n.toLocaleString('en-US',{maximumFractionDigits:d==null?0:d,minimumFractionDigits:d==null?0:d})};
  // girth(in) -> live weight (lb), from Penn State / MSU whitetail charts
  var G=[[26,77],[28,92],[30,105],[32,120],[34,137],[36,155],[38,175],[40,197],[42,220],[44,245],[46,270],[48,297],[50,325]];
  function girthToLive(g){ if(g<=G[0][0])return G[0][1]; for(var i=1;i<G.length;i++){ if(g<=G[i][0]){var a=G[i-1],b=G[i];return a[1]+(b[1]-a[1])*(g-a[0])/(b[0]-a[0]);} } return G[G.length-1][1]*(g/G[G.length-1][0]); }
  var last='';
  function calc(){
    var t=f.wtype.value, live, fd;
    if(t==='girth'){ live=girthToLive(+f.girth.value||0); fd=live*0.78; }
    else if(t==='live'){ live=+f.weight.value||0; fd=live*0.78; }
    else { fd=+f.weight.value||0; live=fd/0.78; }
    var carcass=fd*0.75;
    var boneless=carcass*0.55;          // ~41% of FD
    var shotLoss=boneless*((+f.shot.value||0)/100);
    var meat=boneless-shotLoss;
    var lo=meat*0.9, hi=meat*1.15;
    var style=f.style.value;
    var fat=(+f.fat.value||0)/100;
    var back=meat*0.10, hind=meat*0.35, front=meat*0.20, ground=meat*0.35;
    var pkgMeat=meat;
    if(style==='ground'){ hind=0; front=0; ground=meat-back; }
    if(style==='bonein'){ pkgMeat=meat*1.22; }
    var groundOut=ground/(1-fat);        // fat adds to the ground batch
    pkgMeat=pkgMeat+(groundOut-ground);
    var freezer=pkgMeat/35;
    var pkgs=Math.ceil(pkgMeat);
    var meals=Math.round(pkgMeat*3);
    var fee=+f.fee.value||0;
    var cpl=fee>0?fee/meat:null;
    $('r-meat').textContent=fmt(meat)+' lb';
    $('r-range').textContent='boneless venison, likely '+fmt(lo)+'–'+fmt(hi)+' lb';
    $('r-live').textContent=fmt(live)+' lb'+(t==='live'?'':' (est.)');
    $('r-fd').textContent=fmt(fd)+' lb'+(t==='fd'?'':' (est.)');
    $('r-carc').textContent=fmt(carcass)+' lb';
    $('r-loss').textContent='− '+fmt(shotLoss)+' lb';
    $('r-back').textContent=fmt(back,1)+' lb';
    $('r-hind').textContent=hind?fmt(hind)+' lb':'ground';
    $('r-front').textContent=front?fmt(front)+' lb':'ground';
    $('r-ground').textContent=fmt(groundOut)+' lb'+(fat?' incl. fat':'');
    $('r-freezer').textContent=fmt(freezer,1)+' cu ft';
    $('r-pkgs').textContent=fmt(pkgs);
    $('r-meals').textContent='~'+fmt(meals);
    $('r-cost').textContent=cpl==null?'DIY':'$'+cpl.toFixed(2)+'/lb';
    $('r-note').textContent=(style==='bonein'?'Bone-in cuts weigh about 22% more than boneless; the meat is the same. ':'')+'Yield assumes the deer was cooled within a few hours. Add 10% if you save every scrap of trim yourself.';
    last='Deer yield: field-dressed '+fmt(fd)+' lb → carcass '+fmt(carcass)+' lb → about '+fmt(meat)+' lb boneless venison ('+fmt(lo)+'–'+fmt(hi)+'). Backstraps '+fmt(back,1)+', hind '+fmt(hind)+', front '+fmt(front)+', ground '+fmt(groundOut)+'. Freezer '+fmt(freezer,1)+' cu ft, ~'+pkgs+' lb packages'+(cpl!=null?', $'+cpl.toFixed(2)+'/lb processed':'')+'.';
  }
  f.wtype.addEventListener('change',function(){ var g=f.wtype.value==='girth'; $('wrap-girth').hidden=!g; $('wrap-weight').hidden=g; if(f.wtype.value==='live'&&+f.weight.value<140)f.weight.value=165; if(f.wtype.value==='fd'&&+f.weight.value>=160)f.weight.value=130; calc(); });
  Object.keys(f).forEach(function(k){ f[k].addEventListener('input',calc); });
  $('deerform').addEventListener('submit',function(e){e.preventDefault();calc();});
  $('reset').addEventListener('click',function(){ f.wtype.value='fd';$('wrap-girth').hidden=true;$('wrap-weight').hidden=false;f.weight.value=130;f.girth.value=36;f.shot.value='0';f.style.value='std';f.fat.value=0;f.fee.value=110;calc(); });
  $('copy').addEventListener('click',function(){
    var done=function(){$('copied').hidden=false;setTimeout(function(){$('copied').hidden=true},1800)};
    function fallback(){var t=document.createElement('textarea');t.value=last;document.body.appendChild(t);t.select();try{document.execCommand('copy');done()}catch(e){}document.body.removeChild(t)}
    if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(last).then(done,fallback)}else{fallback()}
  });
  calc();
})();
</script>'''

def build(page,header,footer,gear,faq_html):
    body='<div class="wrap">\n'+header('Hunting & processing','How much meat will your deer yield?','Enter the weight you have (or just a chest girth) and where you hit it. We work it down from live weight to the pounds of venison you\'ll actually wrap, cut by cut.')+'\n'+CALC+'\n'+gear('Gear that gets more of that meat into the freezer','The yield above assumes the deer was cooled fast and cut clean. These are the four things that make that happen.',GEAR)+'\n'+ARTICLE+faq_html(FAQS)+'\n</article>\n'+footer('Dressing and carcass ratios from Penn State Extension, Mississippi State Deer Lab and the University of Wisconsin meat science program.')+'\n'+TAIL
    return page('deer-meat-yield-calculator','Deer Meat Yield Calculator: How Much Venison From Your Deer? | Back Forty Tools','Deer Meat Yield Calculator','Free deer meat yield calculator. Enter live weight, field-dressed weight or chest girth and get pounds of boneless venison, cut-by-cut breakdown, freezer space and cost per pound.',body,FAQS,'Deer Meat Yield Calculator')
