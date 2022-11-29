$("#json-export, #csv-export, #xlsx-export ").click(function(){
	var e,r;
	(t.exporting.data.length=0,t.exporting.dataExport)?(r=t.exporting.data).push.apply(r,h(t.exporting.dataExport)):(e=t.exporting.data).push.apply(e,h(window.exchangeRate.dataExport));
	"uk"===document.documentElement.lang?t.exporting.dataFields={date:c.a.date,time:c.a.time,r030:c.a.codeDigital,cc:c.a.codeCurrency,units:c.a.unitsNumber,txt:c.a.nameCurrency,rate:c.a.officialRate+", "+c.a.UAH}:t.exporting.dataFields={date:c.a.date,time:c.a.time,r030:c.a.codeDigital,cc:c.a.codeCurrency,units:c.a.unitsNumber,enname:c.a.nameCurrency,rate:c.a.officialRate+", "+c.a.UAH}
})