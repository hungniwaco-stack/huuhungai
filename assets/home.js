/* Trang chu: tim kiem, loc chu de, hien dan danh sach. Khong co JS thi hien toan bo bai. */
(function(){
  var EN=document.documentElement.lang==="en",PAGE=12;
  var $=function(s){return document.querySelector(s)},all=function(s){return Array.prototype.slice.call(document.querySelectorAll(s))};
  var cards=all(".article-card"),chips=all(".topic-chip"),q=$("#article-search"),status=$("#result-status"),empty=$("#empty-state"),more=$("#show-more"),start=$("#start");
  var topic="All Posts",limit=PAGE;
  function norm(v){return String(v||"").normalize("NFD").replace(/[̀-ͯ]/g,"").replace(/đ/g,"d").toLowerCase().trim()}
  function apply(){
    var term=norm(q.value),filtering=!!term||topic!=="All Posts",count=0,shown=0;
    cards.forEach(function(c){
      var ok=(topic==="All Posts"||c.dataset.topic===topic)&&(!term||c.dataset.search.indexOf(term)>=0);
      if(ok)count++;
      var show=ok&&count<=limit;c.style.display=show?"flex":"none";if(show)shown++});
    status.textContent=EN?"Showing "+shown+" of "+count+" "+(filtering?"matching ":"")+"article"+(count===1?"":"s")
                         :"Đang hiện "+shown+" trong "+count+" bài"+(filtering?" phù hợp":"");
    empty.style.display=count?"none":"block";more.hidden=shown>=count;start.hidden=filtering;
    chips.forEach(function(c){var on=c.dataset.filter===topic;c.classList.toggle("active",on);if(on)c.setAttribute("aria-current","true");else c.removeAttribute("aria-current")});
  }
  chips.forEach(function(c){c.addEventListener("click",function(e){e.preventDefault();topic=c.dataset.filter||"All Posts";limit=PAGE;apply()})});
  q.addEventListener("input",function(){limit=PAGE;apply()});
  $("#clear-search").addEventListener("click",function(){q.value="";topic="All Posts";limit=PAGE;apply();q.focus()});
  more.addEventListener("click",function(){
    var before=limit;limit+=PAGE;apply();
    var next=cards.filter(function(c){return c.style.display!=="none"})[before];if(next)next.focus({preventScroll:true})});
  apply();
})();
