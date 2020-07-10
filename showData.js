var LIST = ["PROPERTY TYPE", "ADDRESS", "ZIP CODE", 
				  "PRICE", "BEDS", "BATHS", 
				  "LOCATION", "SQUARE FEET", 
				  "LOT SIZE", "YEAR BUILT", 
				  "DAYS ON MARKET", "$/SQUARE FEET", 
				  "HOA", "URL"];
var NORTHWOOD = ["92620", "92618"]
var data = JSON.parse(test)
               .sort((a, b) => b["ZIP CODE"] - a["ZIP CODE"])
               .filter((elem) => NORTHWOOD.includes(elem["ZIP CODE"]));
var container = document.getElementById('propertyContainer');

for (var i = 1; i < data.length; i++) {
	var a = document.createElement("property-card");
	a.setAttribute("price", data[i]["PRICE"]);
	a.setAttribute("type", data[i]["PROPERTY TYPE"]);
	a.setAttribute("url", data[i]["URL"]);
	a.setAttribute("location", data[i]["LOCATION"]);
	container.appendChild(a);
}