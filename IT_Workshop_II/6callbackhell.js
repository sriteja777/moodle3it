/////////////////////////////// call back style - deep nesting ////////////////////////////////
function callbackhell() {
	setTimeout(function() {
    	console.log('1. First thing setting up second thing');
	    	setTimeout(function() {
      		console.log('2. Second thing setting up third thing');
      			setTimeout(function() {
       			 console.log('3. Third thing setting up fourth thing');
				setTimeout(function() {
       	 			console.log('4. fourth thing setting up fifth thing');
         				setTimeout(function() {
          				console.log('5. Fifth thing');
        				}, 2000); //5
      				}, 2000); //4
    			}, 2000); //3
  		}, 2000); //2
	}, 2000); //1
};

callbackhell();

/////////////////////////////// promises style - flat coding - chaining promises ////////////////////////////////
function breakthehell(){
	var promise1 = new Promise(function(resolve, reject){
				setTimeout(resolve, 2000);
			});
        promise1.then(function(){console.log('1. promise:First thing setting up second thing'); 
                                return new Promise (function(resolve, reject){
				                    setTimeout(resolve, 2000);
			})}) //1
                  .then(function(){console.log('2. promise:Second thing setting up third thing'); 
                                return new Promise (function(resolve, reject){
				                    setTimeout(resolve, 2000);
			})}) //2
		 .then(function(){console.log('3. promise:Third thing setting up fourth thing'); 
				                return new Promise (function(resolve, reject){
								    setTimeout(resolve, 2000);
			})}) //3
		 .then(function(){console.log('4. promise:Fouth thing setting up fifththing'); 
				                return new Promise (function(resolve, reject){
								    setTimeout(resolve, 2000);
			})}) //4
		 .then(function(){console.log('5. promise:fifth thing');
                         }); //5

}

breakthehell();
