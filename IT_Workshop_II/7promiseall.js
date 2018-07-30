

/////////////////////////////// promises style - flat coding - chaining promises ////////////////////////////////
function parallelpromises(){
	var promises =[];
	for (let i = 0; i<10; i++)
        {
		promises[i] = new Promise(function(resolve, reject){
						setTimeout(resolve, 2000 + i * 1000);
						});
		promises[i].then(function(){console.log (i + "th promise fulfilled!");});
	}

        Promise.all(promises);

}

parallelpromises();
