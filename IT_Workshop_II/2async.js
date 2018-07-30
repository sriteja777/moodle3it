//////////////////////////////////////////////////////////////////////////////////////////////////
//tests the nature of asynchronous functions
    function test_async(){
		var x = 4;
		var async = function(){
	    		setTimeout(function(){
	       		 x = x+20;
			console.log("In async:callback x="+ x); //x=27
	    		}, 3000) };

		async();
		x = x + 3;
		console.log("In test_async: x=" + x);
	}


