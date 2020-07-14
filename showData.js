var LIST = ["PROPERTY TYPE", "ADDRESS", "ZIP CODE", 
				  "PRICE", "BEDS", "BATHS", 
				  "LOCATION", "SQUARE FEET", 
				  "LOT SIZE", "YEAR BUILT", 
				  "DAYS ON MARKET", "$/SQUARE FEET", 
				  "HOA", "URL"];
var convertType = {"Single Family Residential": "Single Family",
                   "Condo/Co-op": "Condo", 
                   "Townhouse": "Townhouse"};
var NORTHWOOD = ["92620", "92618"];
var container = document.getElementById('container');
var data = JSON.parse(test)
               .sort((a, b) => b["ZIP CODE"] - a["ZIP CODE"])
               .filter((elem) => NORTHWOOD.includes(elem["ZIP CODE"]));

// setup HTML structure
for (let zip of NORTHWOOD) {
	let item = document.createElement('div');
	item.setAttribute("class", "menuItem");
	item.setAttribute("id", zip);

	let title = document.createElement("h2");
	title.innerHTML = '<button>' + zip + '</button>';
	item.appendChild(title);

	let list = document.createElement("div");
	list.setAttribute("class", "propertyContainer");
	item.appendChild(list);

	title.onclick = () => {
		if (list.style.display === "") {
			list.style.display = "flex";
		} else {
			list.style.display = "";
		}
	};

	container.appendChild(item);
}

for (var i = 1; i < data.length; i++) {
	// TODO: add HOA, year built
	var a = document.createElement("property-card");
	if (data[i]["ZIP CODE"] !== "92620") {
		a.style.backgroundColor = '#708090';
	}
	// TODO: convert to money format
	a.setAttribute("price", data[i]["PRICE"]);
	a.setAttribute("type", convertType[data[i]["PROPERTY TYPE"]] + ', ' + data[i]["BEDS"] + "B/" + data[i]["BATHS"] + "B");
	a.setAttribute("url", data[i]["URL"]);
	a.setAttribute("location", data[i]["LOCATION"]);
	a.setAttribute("onmarket", "On Market: " + data[i]["DAYS ON MARKET"] + " days");

	document.getElementById(data[i]["ZIP CODE"]).childNodes[1].appendChild(a);
}