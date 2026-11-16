(function(){
  var d=document.documentElement,nav=document.querySelector(".nav");
  if(!nav)return;
  var SIZES=["-1","0","1","2"];
  function get(k){try{return localStorage.getItem(k)}catch(e){return null}}
  function set(k,v){try{localStorage.setItem(k,v)}catch(e){}}
  function size(){var s=d.dataset.size||"0";return SIZES.indexOf(s)<0?"0":s}
  var box=document.createElement("div");box.className="disp";box.setAttribute("role","group");box.setAttribute("aria-label","Chế độ hiển thị");
  function btn(label,text,fn){var b=document.createElement("button");b.type="button";b.textContent=text;b.setAttribute("aria-label",label);b.title=label;b.onclick=fn;box.appendChild(b);return b}
  var theme=btn("Đổi giao diện sáng hoặc tối","",function(){
    var t=d.dataset.theme==="light"?"dark":"light";d.dataset.theme=t;set("hh-theme",t);sync()});
  var minus=btn("Giảm cỡ chữ","A−",function(){step(-1)});
  var plus=btn("Tăng cỡ chữ","A+",function(){step(1)});
  function step(n){var i=Math.max(0,Math.min(SIZES.length-1,SIZES.indexOf(size())+n));
    d.dataset.size=SIZES[i];set("hh-size",SIZES[i]);sync()}
  function sync(){
    theme.textContent=d.dataset.theme==="light"?"🌙":"☀";
    var i=SIZES.indexOf(size());minus.disabled=i===0;plus.disabled=i===SIZES.length-1}
  sync();nav.appendChild(box);
})();

(function(){
  function get(){try{return localStorage.getItem("hh-consent")}catch(e){return null}}
  function set(v){try{localStorage.setItem("hh-consent",v)}catch(e){}}
  function apply(v){if(typeof gtag==="function")gtag("consent","update",{analytics_storage:v});}
  var bar;
  function close(){if(bar){bar.remove();bar=null}}
  function choose(v){set(v);apply(v);close()}
  function show(){
    if(bar)return;
    bar=document.createElement("div");bar.className="consent";bar.setAttribute("role","dialog");bar.setAttribute("aria-label","Cookie");
    bar.innerHTML='<p>Trang dùng Google Analytics để đo lượng truy cập. Bạn đồng ý cho lưu cookie đo lường không? <a href="/quyen-rieng-tu.html">Chi tiết</a></p><div class="consent-btns"><button type="button" data-v="granted">Đồng ý</button><button type="button" data-v="denied">Từ chối</button></div>';
    bar.onclick=function(e){var v=e.target&&e.target.getAttribute&&e.target.getAttribute("data-v");if(v)choose(v)};
    document.body.appendChild(bar);
  }
  if(!get())show();
  var foot=document.querySelector(".site-foot");
  if(foot){var a=document.createElement("a");a.href="#";a.textContent="Cài đặt cookie";a.onclick=function(e){e.preventDefault();show()};foot.insertBefore(document.createTextNode(" · "),foot.firstChild);foot.insertBefore(a,foot.firstChild)}
})();
