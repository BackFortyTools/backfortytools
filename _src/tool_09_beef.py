# Beef yield calculator: whole, half, quarter
CALC = r'''<section class="calc" aria-label="Beef yield calculator">
  <form class="panel" id="bfform" autocomplete="off">
    <h2>The animal and your share</h2>
    <div class="grid">
      <label>Weight you know
        <select id="wtype">
          <option value="live" selected>Live weight</option>
          <option value="hang">Hanging (carcass) weight</option>
        </select>
      </label>
      <label>Weight <small>pounds</small>
        <input id="weight" type="number" min="200" max="2500" step="10" value="1250" inputmode="numeric">
      </label>
      <label>Breed / finish <small>sets dressing %</small>
        <select id="dress">
          <option value="0.60">Grass-finished, dairy cross (60%)</option>
          <option value="0.62" selected>Typical grain-finished beef (62%)</option>
          <option value="0.64">Well-finished Angus / Hereford (64%)</option>
        </select>
      </label>
      <label>Your share
        <select id="share">
          <option value="1">Whole</option>
          <option value="0.5" selected>Half</option>
          <option value="0.25">Quarter</option>
          <option value="0.125">Eighth</option>
        </select>
      </label>
      <label>How it's cut
        <select id="cut">
          <option value="0.63" selected>Mostly boneless, some bone-in steaks (63%)</option>
          <option value="0.70">Bone-in where possible (70%)</option>
          <option value="0.58">All boneless, trimmed lean (58%)</option>
        </select>
      </label>
      <label>Price to the farmer <small>$ per lb hanging weight</small>
        <input id="ppl" type="number" min="0" step="0.05" value="4.25" inputmode="decimal">
      </label>
      <label>Processing <small>$ per lb hanging weight</small>
        <input id="proc" type="number" min="0" step="0.05" value="0.95" inputmode="decimal">
      </label>
      <label>Kill / harvest fee <small>$ per whole animal</small>
        <input id="kill" type="number" min="0" step="5" value="110" inputmode="numeric">
      </label>
    </div>
  </form>

  <aside class="panel results" aria-live="polite">
    <div class="tag">
      <div class="lbl">Beef in your freezer</div>
      <div class="big" id="r-meat">—</div>
      <div class="sub" id="r-sharetxt">—</div>
    </div>
    <dl class="rows">
      <dt>Live weight</dt><dd id="r-live">—</dd>
      <dt>Hanging weight, whole</dt><dd id="r-hang">—</dd>
      <dt>Your share, hanging</dt><dd id="r-myhang">—</dd>
      <dt class="total">Ground beef (~45%)</dt><dd class="total" id="r-ground">—</dd>
      <dt>Steaks (~20%)</dt><dd id="r-steak">—</dd>
      <dt>Roasts (~25%)</dt><dd id="r-roast">—</dd>
      <dt>Ribs, stew, brisket, other (~10%)</dt><dd id="r-other">—</dd>
      <dt class="total">Freezer space</dt><dd class="total" id="r-freezer">—</dd>
      <dt>Paid to farmer</dt><dd id="r-farm">—</dd>
      <dt>Processing + kill fee</dt><dd id="r-proc">—</dd>
      <dt class="total">Total cost</dt><dd class="total" id="r-total">—</dd>
      <dt class="total">Per pound in the freezer</dt><dd class="total cost" id="r-cpl">—</dd>
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
  <p>Buying beef by the half is priced on a number most people have never seen: hanging weight. This tool walks the three weights so the invoice makes sense.</p>
  <div class="formula">live × dressing % = hanging &nbsp;·&nbsp; hanging × cutting yield = take-home &nbsp;·&nbsp; you pay on hanging, you eat take-home</div>
  <p>A 1,250-pound steer dresses at about 62 percent, so the carcass hangs at 775 pounds. Your half is 388 pounds hanging. After aging, boning and trimming you take home about 63 percent of that, which is 245 pounds of packaged beef. At $4.25 a pound hanging plus $0.95 processing and half a $110 kill fee, the half costs about $2,070, or $8.45 a pound for everything from ground beef to ribeyes.</p>

  <h2>The three weights, by animal size</h2>
  <div class="tbl"><table>
    <thead><tr><th>Live weight</th><th>Hanging (62%)</th><th>Take-home, whole (63%)</th><th>Take-home, half</th><th>Quarter</th></tr></thead>
    <tbody>
      <tr><td>1,000 lb</td><td>620 lb</td><td>390 lb</td><td>195 lb</td><td>98 lb</td></tr>
      <tr><td>1,200 lb</td><td>745 lb</td><td>470 lb</td><td>235 lb</td><td>117 lb</td></tr>
      <tr><td>1,300 lb</td><td>805 lb</td><td>510 lb</td><td>255 lb</td><td>127 lb</td></tr>
      <tr><td>1,400 lb</td><td>870 lb</td><td>550 lb</td><td>275 lb</td><td>137 lb</td></tr>
    </tbody>
  </table></div>

  <h2>Why take-home is less than hanging</h2>
  <p>The carcass hangs 10 to 21 days to age and loses 3 to 5 percent to evaporation. Then the bones come out (about 20 percent of the carcass), and the fat is trimmed (another 8 to 15 percent). Ask for bone-in cuts, T-bones, short ribs and shanks, and your yield climbs toward 70 percent, though some of that weight is bone. Ask for everything boneless and closely trimmed and it falls toward 58 percent, but every pound is meat.</p>

  <h2>What a half looks like in the freezer</h2>
  <p>Of the roughly 245 pounds in a typical half: 100 to 110 pounds of ground beef, 45 to 55 pounds of steaks (ribeye, strip, sirloin, T-bone, filet), 55 to 65 pounds of roasts (chuck, rump, round, brisket), and 15 to 25 pounds of short ribs, stew meat, soup bones and organ meat if you ask for it. It fills about 7 cubic feet, so a 7-cubic-foot chest freezer holds a half with nothing else in it.</p>

  <h2>What it costs in 2026</h2>
  <p>Farm price on hanging weight runs $3.75 to $5.00 a pound in the Southeast for grain-finished, $5.00 to $6.50 for grass-finished or certified programs. Processing is $0.85 to $1.20 a pound hanging plus a $75 to $150 kill fee. All in, most halves land between $7.50 and $10.50 per pound of take-home beef. Compare that to a grocery store where ground beef alone is $6 and ribeyes are $18.</p>

  <h2>Frequently asked</h2>
'''

FAQS=[
("How much meat do you get from half a cow?","About 220 to 260 pounds of packaged beef from a typical 1,200 to 1,300-pound steer: roughly 100 pounds of ground, 50 of steaks, 60 of roasts and 20 of ribs, stew and other cuts."),
("How much freezer space for half a cow?","7 to 8 cubic feet. A quarter needs 4; a whole beef needs 14 to 16, which is a full upright or a large chest freezer."),
("What is hanging weight?","The weight of the carcass after slaughter, with the hide, head, feet and organs removed, before aging and cutting. It is about 62 percent of live weight and it is what most farmers charge on."),
("How much does half a cow cost?","Usually $1,800 to $2,600 in 2026 including processing, which works out to $7.50 to $10.50 per pound of take-home beef. Grass-finished and certified programs run higher."),
("Why did I get less meat than the hanging weight I paid for?","Normal. About 37 percent of hanging weight is bone, trimmed fat and moisture lost during aging. If your take-home is under 55 percent of hanging, ask the processor for the cut sheet and the aged weight."),
]

GEAR=[
("Chest freezer, 7 cu ft","Exactly the size a half fits in. Cheaper to run than an upright and holds cold longer in an outage.","https://www.amazon.com/s?k=7+cu+ft+chest+freezer","Shop chest freezers"),
("Freezer inventory whiteboard","Sounds silly until you find the brisket from two halves ago in March.","https://www.amazon.com/s?k=magnetic+freezer+inventory+board","Shop inventory boards"),
("Vacuum sealer","If your processor paper-wraps, re-sealing the steaks you won't eat this year doubles their life.","https://www.amazon.com/s?k=vacuum+sealer+for+meat","Shop vacuum sealers"),
("Freezer alarm / thermometer","A $15 alarm has saved more half-cows than any other gadget on this page.","https://www.amazon.com/s?k=freezer+alarm+thermometer","Shop freezer alarms"),
]

TAIL = r'''</div>
<script>
(function(){
  var $=function(id){return document.getElementById(id)};
  var f={wtype:$('wtype'),weight:$('weight'),dress:$('dress'),share:$('share'),cut:$('cut'),ppl:$('ppl'),proc:$('proc'),kill:$('kill')};
  var fmt=function(n,d){return n.toLocaleString('en-US',{maximumFractionDigits:d==null?0:d,minimumFractionDigits:d==null?0:d})};
  var usd=function(n){return '$'+fmt(n,0)};
  var last='';
  function calc(){
    var w=+f.weight.value||0, d=+f.dress.value, sh=+f.share.value, cy=+f.cut.value;
    var live,hang;
    if(f.wtype.value==='hang'){hang=w;live=w/d;} else {live=w;hang=w*d;}
    var myHang=hang*sh;
    var meat=myHang*cy;
    var ground=meat*0.45, steak=meat*0.20, roast=meat*0.25, other=meat*0.10;
    var freezer=meat/35;
    var farm=myHang*(+f.ppl.value||0);
    var proc=myHang*(+f.proc.value||0)+(+f.kill.value||0)*sh;
    var total=farm+proc;
    var cpl=meat>0?total/meat:0;
    var shareName=f.share.options[f.share.selectedIndex].text.toLowerCase();
    $('r-meat').textContent=fmt(meat)+' lb';
    $('r-sharetxt').textContent='take-home from a '+shareName+', about '+fmt(meat*0.93)+'–'+fmt(meat*1.08)+' lb';
    $('r-live').textContent=fmt(live)+' lb'+(f.wtype.value==='hang'?' (est.)':'');
    $('r-hang').textContent=fmt(hang)+' lb'+(f.wtype.value==='live'?' (est.)':'');
    $('r-myhang').textContent=fmt(myHang)+' lb';
    $('r-ground').textContent=fmt(ground)+' lb'; $('r-steak').textContent=fmt(steak)+' lb'; $('r-roast').textContent=fmt(roast)+' lb'; $('r-other').textContent=fmt(other)+' lb';
    $('r-freezer').textContent=fmt(freezer,1)+' cu ft';
    $('r-farm').textContent=usd(farm); $('r-proc').textContent=usd(proc); $('r-total').textContent=usd(total);
    $('r-cpl').textContent='$'+cpl.toFixed(2)+'/lb';
    $('r-note').textContent='Cut shares are typical for a standard cut sheet. More steaks means fewer roasts; the total stays the same.';
    last='Beef: '+fmt(live)+' lb live → '+fmt(hang)+' lb hanging → '+shareName+' = '+fmt(myHang)+' lb hanging → '+fmt(meat)+' lb take-home (ground '+fmt(ground)+', steaks '+fmt(steak)+', roasts '+fmt(roast)+', other '+fmt(other)+'). Freezer '+fmt(freezer,1)+' cu ft. Cost '+usd(total)+' = $'+cpl.toFixed(2)+'/lb.';
  }
  f.wtype.addEventListener('change',function(){ if(f.wtype.value==='hang'&&+f.weight.value>1000)f.weight.value=775; if(f.wtype.value==='live'&&+f.weight.value<1000)f.weight.value=1250; calc(); });
  Object.keys(f).forEach(function(k){ f[k].addEventListener('input',calc); f[k].addEventListener('change',calc); });
  $('bfform').addEventListener('submit',function(e){e.preventDefault();calc();});
  $('reset').addEventListener('click',function(){ f.wtype.value='live';f.weight.value=1250;f.dress.value='0.62';f.share.value='0.5';f.cut.value='0.63';f.ppl.value=4.25;f.proc.value=0.95;f.kill.value=110;calc(); });
  $('copy').addEventListener('click',function(){
    var done=function(){$('copied').hidden=false;setTimeout(function(){$('copied').hidden=true},1800)};
    function fallback(){var t=document.createElement('textarea');t.value=last;document.body.appendChild(t);t.select();try{document.execCommand('copy');done()}catch(e){}document.body.removeChild(t)}
    if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(last).then(done,fallback)}else{fallback()}
  });
  calc();
})();
</script>'''

def build(page,header,footer,gear,faq_html):
    body='<div class="wrap">\n'+header('Butchering','How much meat is in half a cow, and what will it cost?','Live weight to hanging weight to the pounds you actually take home, with the cut breakdown, freezer space and the real price per pound.')+'\n'+CALC+'\n'+gear('Before the beef shows up','A half is 250 pounds of meat on one day. Have somewhere to put it.',GEAR)+'\n'+ARTICLE+faq_html(FAQS)+'\n</article>\n'+footer('Dressing and cutting yields from the University of Tennessee, South Dakota State and Oklahoma State meat science programs; prices from 2026 Southeastern direct-market averages.')+'\n'+TAIL
    return page('beef-yield-calculator','Half a Cow Calculator: How Much Meat and What It Costs | Back Forty Tools','Beef Yield Calculator (Whole, Half, Quarter)','Free beef yield calculator. Enter live or hanging weight and your share (whole, half, quarter) to get take-home pounds, ground/steak/roast breakdown, freezer space and true cost per pound.',body,FAQS,'Beef Yield Calculator')
