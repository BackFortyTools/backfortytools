# Brisket start-time planner
CALC = r'''<section class="calc" aria-label="Brisket smoking time calculator">
  <form class="panel" id="bkform" autocomplete="off">
    <h2>Your cook</h2>
    <div class="grid">
      <label>Brisket weight <small>pounds, after trimming</small>
        <input id="weight" type="number" min="2" max="25" step="0.5" value="12" inputmode="decimal">
      </label>
      <label>Cut
        <select id="cut">
          <option value="packer" selected>Whole packer (point + flat)</option>
          <option value="flat">Flat only</option>
          <option value="point">Point only</option>
        </select>
      </label>
      <label>Pit temperature
        <select id="pit">
          <option value="225">225°F — low and slow</option>
          <option value="250" selected>250°F — the usual</option>
          <option value="275">275°F — hot and fast</option>
          <option value="300">300°F — competition pace</option>
        </select>
      </label>
      <label>Wrap at the stall
        <select id="wrap">
          <option value="none">No wrap — bark first</option>
          <option value="paper" selected>Butcher paper</option>
          <option value="foil">Foil (Texas crutch)</option>
        </select>
      </label>
      <label>Rest before slicing <small>hours; 1 minimum, 2–4 in a cooler is better</small>
        <input id="rest" type="number" min="0.5" max="6" step="0.5" value="1.5" inputmode="decimal">
      </label>
      <label>Safety buffer <small>hours, for a stubborn stall</small>
        <input id="buffer" type="number" min="0" max="4" step="0.5" value="1" inputmode="decimal">
      </label>
      <label>When do you want to eat?
        <input id="serve" type="time" value="18:00">
      </label>
      <label>Smoker warm-up <small>minutes</small>
        <input id="preheat" type="number" min="0" max="120" step="5" value="45" inputmode="numeric">
      </label>
    </div>
  </form>

  <aside class="panel results" aria-live="polite">
    <div class="tag">
      <div class="lbl">Put the brisket on at</div>
      <div class="big" id="r-on">—</div>
      <div class="sub" id="r-cook">—</div>
    </div>
    <dl class="rows" id="timeline">
      <dt>Light the smoker</dt><dd id="t-light">—</dd>
      <dt>Brisket on, fat side up</dt><dd id="t-on">—</dd>
      <dt>Expect the stall (≈150–165°F)</dt><dd id="t-stall">—</dd>
      <dt id="t-wrap-l">Wrap</dt><dd id="t-wrap">—</dd>
      <dt>Start probing (195°F+)</dt><dd id="t-probe">—</dd>
      <dt>Pull at ~203°F, probe-tender</dt><dd id="t-pull">—</dd>
      <dt>Rest, wrapped, in a cooler</dt><dd id="t-rest">—</dd>
      <dt class="total">Slice and eat</dt><dd class="total" id="t-eat">—</dd>
    </dl>
    <p class="note" id="r-note"></p>
    <div style="display:flex;gap:10px;flex-wrap:wrap;align-items:center">
      <button class="btn" type="button" id="copy">Copy timeline</button>
      <button class="btn ghost" type="button" id="reset">Reset</button>
      <span class="copied" id="copied" hidden>Copied</span>
    </div>
  </aside>
</section>'''

ARTICLE = r'''<article>
  <h2>How the planner works</h2>
  <p>Every pitmaster has a rule of thumb, and they agree more than they admit. We use the middle of the range and then work backwards from your dinner time.</p>
  <div class="formula">hours ≈ pounds × (1.5 at 225°F · 1.25 at 250°F · 1 at 275°F · 0.8 at 300°F), minus about 20% if you wrap</div>
  <p>A 12-pound packer at 250°F is around 15 hours unwrapped and 12 wrapped in paper. Add an hour of rest and an hour of buffer and the meat goes on about 14 hours before you plan to eat. For a 6 p.m. dinner that is 4 a.m., which is why so many brisket cooks start the night before and hold the finished brisket in a cooler.</p>

  <h2>Brisket cook time by weight and temperature</h2>
  <p>Unwrapped, whole packer, hours to probe-tender. Wrapped cooks run about 20% shorter.</p>
  <div class="tbl"><table>
    <thead><tr><th>Trimmed weight</th><th>225°F</th><th>250°F</th><th>275°F</th><th>300°F</th></tr></thead>
    <tbody>
      <tr><td>6 lb flat</td><td>9 h</td><td>7.5 h</td><td>6 h</td><td>5 h</td></tr>
      <tr><td>10 lb packer</td><td>15 h</td><td>12.5 h</td><td>10 h</td><td>8 h</td></tr>
      <tr><td>12 lb packer</td><td>18 h</td><td>15 h</td><td>12 h</td><td>9.5 h</td></tr>
      <tr><td>14 lb packer</td><td>21 h</td><td>17.5 h</td><td>14 h</td><td>11 h</td></tr>
      <tr><td>16 lb packer</td><td>24 h</td><td>20 h</td><td>16 h</td><td>13 h</td></tr>
    </tbody>
  </table></div>

  <h2>The stall, and why we add a buffer</h2>
  <p>Somewhere around 150 to 165°F internal, the brisket stops climbing for two to four hours. Moisture evaporating off the surface cools it as fast as the pit heats it. It is normal, and it is the reason no calculator can promise a finish time to the minute. Wrapping in butcher paper or foil traps that moisture and pushes through the stall faster, at the cost of some bark. The buffer in the planner exists so that a long stall ruins nobody's dinner; a brisket that finishes early just rests longer, and a longer rest is better anyway.</p>

  <h2>Temperature is a guide; feel is the answer</h2>
  <p>Start checking at 195°F. A brisket is done when a probe slides into the flat like it is going into warm butter, usually between 200 and 205°F. The point is always done before the flat. If the flat is tender at 198°F, pull it; if it is still tight at 205°F, give it more time.</p>

  <h2>Resting and holding</h2>
  <p>Rest at least an hour, wrapped, so the juices settle back into the meat. A faux Cambro, which is a dry cooler with towels, holds a brisket safely above 140°F for four to six hours. If you have the time, a long rest at 150°F in a warming oven is what the famous Texas joints do, and it is the single biggest upgrade most backyard cooks can make.</p>

  <h2>Frequently asked</h2>
'''

FAQS=[
("How long does it take to smoke a brisket at 225?","About 1.5 hours per pound unwrapped, so a 12-pound packer takes around 18 hours. Wrapping at the stall cuts that to roughly 14 to 15 hours."),
("How long to smoke a 10 lb brisket at 250?","Plan on 12 to 13 hours unwrapped or about 10 hours wrapped, plus at least an hour of rest. Put it on about 13 hours before you want to eat."),
("When should I wrap my brisket?","When the bark is set and the internal temperature stalls, usually 150 to 165°F and about 5 to 6 hours into a 250°F cook. Paper keeps more bark; foil finishes faster."),
("What time should I start a brisket for dinner?","For a 6 p.m. dinner with a 12-pound packer at 250°F wrapped, light the smoker around 3 a.m. and put the meat on at about 4 a.m. If that sounds miserable, cook it the day before and hold it, or run 275°F and start at 7 a.m."),
("Can a brisket rest too long?","Not really, as long as it stays above 140°F. Four hours in a cooler is common; competition cooks hold even longer. Under an hour is where most dry brisket comes from."),
]

GEAR=[
("Leave-in dual-probe thermometer","One probe in the flat, one for the pit. Lets you sleep during the overnight part of this timeline.","https://www.amazon.com/s?k=wireless+meat+thermometer+dual+probe","Shop thermometers"),
("Pink butcher paper, 18-inch roll","The wrap that keeps bark. A roll lasts a season.","https://www.amazon.com/s?k=pink+butcher+paper+18+inch","Shop butcher paper"),
("Insulated cooler for the rest","Any good cooler works as a holding box. Wrap the brisket, stuff with towels, close the lid.","https://www.amazon.com/s?k=cooler+for+resting+brisket","Shop coolers"),
("Instant-read thermometer","For the probe test at the end. Feel is the answer, but you need to know when to start feeling.","https://www.amazon.com/s?k=instant+read+meat+thermometer","Shop instant-read"),
]

TAIL = r'''</div>
<script>
(function(){
  var $=function(id){return document.getElementById(id)};
  var f={weight:$('weight'),cut:$('cut'),pit:$('pit'),wrap:$('wrap'),rest:$('rest'),buffer:$('buffer'),serve:$('serve'),preheat:$('preheat')};
  var RATE={225:1.5,250:1.25,275:1.0,300:0.8};
  var WRAP={none:1,paper:0.82,foil:0.75};
  var last='';
  function clock(mins){ // mins may be negative = previous day
    var day=0; while(mins<0){mins+=1440;day--;} while(mins>=1440){mins-=1440;day++;}
    var h=Math.floor(mins/60), m=Math.round(mins%60); if(m===60){m=0;h=(h+1)%24;}
    var ap=h>=12?'PM':'AM'; var hh=h%12; if(hh===0)hh=12;
    return hh+':'+(m<10?'0':'')+m+' '+ap+(day<0?' (day before)':day>0?' (next day)':'');
  }
  function hrs(x){ var h=Math.floor(x), m=Math.round((x-h)*60); if(m===60){h++;m=0;} return h+' h'+(m?' '+m+' m':''); }
  function calc(){
    var w=+f.weight.value||0, pit=+f.pit.value, rate=RATE[pit]||1.25, wrap=f.wrap.value, cut=f.cut.value;
    var cutAdj= cut==='flat'?0.95: cut==='point'?1.05:1;
    var cook=w*rate*cutAdj*WRAP[wrap];
    var lo=cook*0.85, hi=cook*1.15;
    var rest=+f.rest.value||0, buffer=+f.buffer.value||0, pre=(+f.preheat.value||0)/60;
    var sv=f.serve.value||'18:00'; var p=sv.split(':'); var serve=(+p[0])*60+(+p[1]);
    var eat=serve;
    var restStart=eat-rest*60;
    var pull=restStart-buffer*60;
    var on=pull-cook*60;
    var light=on-pre*60;
    var stall=on+cook*60*0.42;
    var wrapAt=on+cook*60*0.5;
    var probe=pull-45;
    $('r-on').textContent=clock(on);
    $('r-cook').textContent='about '+hrs(cook)+' on the pit (likely '+hrs(lo)+' to '+hrs(hi)+')';
    $('t-light').textContent=clock(light);
    $('t-on').textContent=clock(on);
    $('t-stall').textContent=clock(stall);
    $('t-wrap-l').textContent=wrap==='none'?'Spritz, no wrap':'Wrap in '+(wrap==='paper'?'butcher paper':'foil');
    $('t-wrap').textContent=wrap==='none'?'—':clock(wrapAt);
    $('t-probe').textContent=clock(probe);
    $('t-pull').textContent=clock(pull);
    $('t-rest').textContent=clock(pull)+' → '+clock(restStart+ (buffer*60));
    $('t-eat').textContent=clock(eat);
    $('r-note').textContent='Buffer of '+hrs(buffer)+' is built in before the rest. If the brisket finishes early it simply rests longer, which is fine down to about 140°F internal.';
    last='Brisket plan: '+w+' lb '+cut+' at '+pit+'°F, '+(wrap==='none'?'unwrapped':'wrapped in '+wrap)+' ≈ '+hrs(cook)+'. Light '+clock(light)+', on '+clock(on)+', stall ~'+clock(stall)+(wrap!=='none'?', wrap ~'+clock(wrapAt):'')+', probe from '+clock(probe)+', pull ~'+clock(pull)+', rest, eat '+clock(eat)+'.';
  }
  Object.keys(f).forEach(function(k){ f[k].addEventListener('input',calc); f[k].addEventListener('change',calc); });
  $('bkform').addEventListener('submit',function(e){e.preventDefault();calc();});
  $('reset').addEventListener('click',function(){ f.weight.value=12;f.cut.value='packer';f.pit.value='250';f.wrap.value='paper';f.rest.value=1.5;f.buffer.value=1;f.serve.value='18:00';f.preheat.value=45;calc(); });
  $('copy').addEventListener('click',function(){
    var done=function(){$('copied').hidden=false;setTimeout(function(){$('copied').hidden=true},1800)};
    function fallback(){var t=document.createElement('textarea');t.value=last;document.body.appendChild(t);t.select();try{document.execCommand('copy');done()}catch(e){}document.body.removeChild(t)}
    if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(last).then(done,fallback)}else{fallback()}
  });
  calc();
})();
</script>'''

def build(page,header,footer,gear,faq_html):
    body='<div class="wrap">\n'+header('Smoking','What time do I put the brisket on?','Tell it the weight, the pit temperature and when you want to eat. It hands you the whole timeline, from lighting the fire to slicing, with room for the stall.')+'\n'+CALC+'\n'+gear('What makes the timeline hold','A brisket cook is mostly waiting. These make the waiting reliable.',GEAR)+'\n'+ARTICLE+faq_html(FAQS)+'\n</article>\n'+footer('Rates based on published guidance from Aaron Franklin, Texas A&M Meat Science and the AmazingRibs cooking-time research.')+'\n'+TAIL
    return page('brisket-smoking-time-calculator','Brisket Smoking Time Calculator: When to Start for Dinner | Back Forty Tools','Brisket Smoking Time Calculator','Free brisket smoking time calculator. Enter weight, pit temperature, wrap and dinner time; get the hour to light the smoker, put the meat on, wrap, pull and rest.',body,FAQS,'Brisket Smoking Time Calculator')
