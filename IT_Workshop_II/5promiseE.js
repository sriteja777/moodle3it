////////////////////////////////////////////////////////////////////////////////////////
//using promises to implement asynchronous calls - handle rejected promises
function myAsyncPromiseE(url) {
    var promise = new Promise((resolve, reject) => {
		    const xhr = new XMLHttpRequest();
		    xhr.open("GET", url);
		    xhr.onload = function() { if (xhr.status == 200) {
						// Resolve the promise with the response text
						resolve(xhr.response);
					      }
					      else {
						// Otherwise reject with the status text which will hopefully be a meaningful error
						reject(Error(xhr.response));
					      }};
		    xhr.onerror = () => reject(Error("Network Error"));
		    xhr.send();
	  	});
	promise.then((response)=> console.log("In success callback:" + response), 
                    (errorobj)=>{console.log("In reject callback:"+ errorobj.toString()); throw "check URL";})
	       .catch(
                      // Log the rejection reason
                     (reason) => { console.log('In catch: ('+reason+') here.')});
}
//promise is fulfilled successfully
myAsyncPromiseE("http://localhost:8080/myfile.txt");

//promise is fulfilled succesfully even though response buffer is filled with details on error
myAsyncPromiseE("http://localhost:8080/myfile3.txt");

//then - onreject handles rejected promise due to unestablished connection
myAsyncPromiseE("http://localhost:8088/myfile3.txt");


