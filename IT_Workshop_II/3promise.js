//The promise constructor takes one argument, a callback with two parameters, resolve and reject. Do something within the callback, perhaps async, then call resolve if everything worked, otherwise call reject.
//then() takes two arguments, a callback for a success case, and another for the failure case. Both are optional, so you can add a callback for the success or failure case only.

//tests the implementation of asynchronous function using Promise
     function test_promise(){
		var y = 4;

		function pasync(){
		  return new Promise((resolve, reject) => {
		    /*
		    TODO: try to do something asynchronously
		    and resolve or reject according to
		    operation result.
		    */
		    setTimeout(function(){resolve("success")}, 6000);
		  })
		};

		// Call pasync and receive a Promise as return
		let promise = pasync();

		promise.done = false;
		y = y + 3;
		console.log("In test_promise (before then): y="+ y + " promise.done=" + promise.done);

		// Wait for the promise to get resolved 
		// or 6 sec timeout to get over
		promise.then(response => { promise.done = true
					   y = y + 20;
					   console.log("In promise.then: y= " + y + " response= " + response + " promise.done=" + promise.done);
		})
		
		console.log("In test_promise (after then): y=" + y + " promise.done=" + promise.done);

	}
