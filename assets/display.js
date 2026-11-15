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
