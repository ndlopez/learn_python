//JSON.parse("http://localhost:8080/static/data/mystars.json");
//function to sort elems of an JSON-like array by property
function getAnySort(prop) {
    //function to sort inside elem of an object
    return function(a, b) {
	if (a[prop] > b[prop]) {
	    return 1;
	} else if (a[prop] < b[prop]) {
	    return -1;
	}
	return 0;
    }
}
var pStars=[];
var xhr=new XMLHttpRequest();
var my_data="http://localhost:8080/static/data/mystars.json";
xhr.onreadystatechange=function(){
    if(this.readyState==4 && this.status==200){
       pStars= JSON.parse(this.responseText);
	console.log(pStars);
	pStars.sort(getAnySort("firstN"));
	//pStars.reverse(getAnySort("weight"));
	//https://www.w3schools.com/howto/tryit.asp?filename=tryhow_css_four_columns_responsive
	//counting how many stars name starts with A, B, ...,Y
	var j,k=0;
	var vars=[];
	var texty="",text="<p class='p_sub'>";
	var fNames=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","P","R","S","T","V","Y"];
	for (let i=0; i< fNames.length;i++) {
	    j=0;
	    for (var xx in pStars){
		if (pStars[xx].firstN[0] == fNames[i]) {
		    j++;k++;
		}
	    }
	    vars[i]=j;//should be assoc with the firstN[0]
	    text+=fNames[i]+" ";
	}
	text+="</p>";
	text+="<p class='p_sub'>"+vars+"</p>";
	document.getElementById("numberOf").innerHTML=text;
	//document.getElementById("fNames_A").innerHTML="("+vars[0]+")";
	texty+="(" + k +")";
	document.getElementById("myCounter").innerHTML=texty;
	//filtering by class
	var zz=0;
	var firstName=["A","B","C","J","K","L","M","R","S"];
	var li_tex="";
	for (var xx in pStars) {
	    switch (pStars[xx].firstN[0]) {
		case "D":
		case "E":
		case "F":
			li_tex+="<div class='column start_DEF'>";
			dispStars(xx);
			li_tex+="</div>";
			break;
		case "G":
		case "H":
		case "I":
			li_tex+="<div class='column start_GHI'>";
			dispStars(xx);
			li_tex+="</div>";
			break;
		case "N":
		case "P":
		  li_tex+="<div class='column start_NP'>";
		  dispStars(xx);
		  li_tex+="</div>";
			break;
		case "T":
		case "V":
		case "Y":
			li_tex+="<div class='column start_TVY'>";
			dispStars(xx);
			li_tex+="</div>";
			break;
		default:
		  firstName.forEach((item,i) => {
		      if(pStars[xx].firstN[0] == item){
			  li_tex+="<div class='column start_" + item +"'>";
			  dispStars(xx);
			  li_tex+="</div>";
			  //if(vars[i])console.log(i,vars[i]);bug
		      }
		  });
	    }
	}
	document.getElementById("myStars").innerHTML = li_tex;
	function dispStars(value){
	    li_tex+="<div class='contain'>";
	    li_tex+="<img src='"+ pStars[value].photo + "' class='image' onclick=\"openNav('myNav" + value + "')\"></div>";
	    li_tex+="<div class='overlay whiteText'><h4>" + pStars[value].firstN + "</h4>";
	    li_tex+="<p class='p_sub'>"+ pStars[value].meas + "</p></div>";
	    return li_tex;
	}
	/*open and close modal -> Moved to filter-script.js*/
	//Modal page for every pStar
	function addDivs(_val){
	    var dob=pStars[_val].year;
	    var this_year=2022;
	    //var this_year=Date();
	    var mySec=document.createElement("SECTION");
	    mySec.id="myNav"+_val;
	    mySec.className="girl-stats";
	    mySec.innerHTML=`<a href='javascript:void(0)' class='closebtn tomatoText' onclick="closeNav('myNav${_val}')">&times;</a>`;
	    mySec.innerHTML+="<div><h2 class='mod-title tomatoText'>"+
		pStars[_val].firstN+" ("+ (this_year - dob) + ")</h2></div>"+
		"<div class='girl-stats-content'>"+
		"<div class='columns'><img class='imgcenter' src='"+
		pStars[_val].photo+"'><h3 class='twitter'>"+
		pStars[_val].twitter+"</h3></div>"+
		"<div class='columns'><ul class='stats-list'><li><div class='icon'><i class='ficon fas fa-birthday-cake'></i></div><span><strong>BIRTHDAY</strong><em>"+
		pStars[_val].born+"</em></span></li><li><div class='icon'><i class='fas fa-passport fa-2x'></i></div>" +
		"<span><strong>PLACE</strong><em>"+pStars[_val].country+
		"</em></span></li>"+
		"<li><div class='icon'><i class='fas fa-concierge-bell fa-2x'></i></div>" +
		"<span><strong>CUP SIZE</strong><em>"+pStars[_val].bra+"</em></span></li>"+
		"<li><div class='icon'><i class='fas fa-female fa-2x'></i></div><span>"+
		"<strong>BODY TYPE</strong><em>"+pStars[_val].type+"</em></span></li>"+
		"<li><div class='icon'><i class='fas fa-eye fa-2x'></i></div>" +
		"<span><strong>EYES-COLOR</strong><em>"+pStars[_val].eyes+
		"</em></span></li>"+
		"<li><div class='icon'><i class='fas fa-broom fa-2x'></i></div>" +
		"<span><strong>HAIR-COLOR</strong><em>"+pStars[_val].hair+
		"</em></span></li>"+
		"<li><div class='icon'><i class='fas fa-ruler-vertical fa-2x'></i></div>" +
		"<span><strong>HEIGHT</strong><em>"+pStars[_val].height+" m</em></span></li>"+
		"<li><div class='icon'><i class='fas fa-weight fa-2x'></i></div>" +
		"<span><strong>WEIGHT</strong><em>"+pStars[_val].weight+" kg</em></span></li>"+
		"<li><div class='icon'><i class='fas fa-venus fa-2x'></i></div>" +
		"<span><strong>PUBS</strong><em>"+pStars[_val].pubs +"</em></span></li>"+
		"<li><div class='icon'><i class='fas fa-apple-alt fa-2x'></i></div>" +
		"<span><strong>BUTT SIZE</strong><em>"+pStars[_val].meas.slice(-2)+
		" in</em></span></li>"+	"</ul></div></div>";
	    return mySec;
	}
	for(var z in pStars){
	    document.body.appendChild(addDivs(z));
	}
    }};
xhr.open("GET",my_data,true);
xhr.send();
console.log(pStars.type)

//Creating two JSON objects for d3js
/*var myObjW="[",myObjH="[";
for (var i in pStars) {
myObjW+='{firstN:"'+ pStars[i].firstN +'",weight:' +pStars[i].weight+"},";
myObjH+='{firstN:"'+ pStars[i].firstN +'",height:' +pStars[i].height+"},";
}
myObjW+="]";myObjH+="]";
console.log(myObjW);*/
