
//First start the server by running the followng command
//python -m SimpleHTTPServer 8080
//Go to browser and type http://localhost:8080/ to see the directory structure
//pick a file to download

//////////////////////////////////////////////////////////////////////////////////////
//all browsers support onreadystatachange event

function myAsyncFunction(url){
	var xhttp = new XMLHttpRequest();
	xhttp.onreadystatechange = function() {
	    if (this.readyState == 4 && this.status == 200) {
	      // Typical action to be performed when the document is ready:
	       console.log(xhttp.responseText);
            }
	    else console.log(xhttp.statusText);
	};
	xhttp.open("GET", url, true);
	xhttp.send();
}
myAsyncFunction("http://localhost:8080/myfile.txt");

////////////////////////////////////////////////////////////////////////////////////////
//latest browsers support onload and onerror events
function myAsyncFunction2(url){
	var xhttp = new XMLHttpRequest();
	xhttp.onload = function() {
	       console.log(xhttp.responseText);
           };
	xhttp.onerror = function() {
	       console.log(xhttp.statusText);
           };
	
	xhttp.open("GET", url, true);
	xhttp.send();
}
myAsyncFunction2("http://localhost:8080/myfile.txt");
///////////////////////////////////////////////////////////////////////////////////////
//using promises to implement the above asynchronous function myAsyncFunction2
function myAsyncPromise(url) {
    var promise = new Promise((resolve, reject) => {
		    const xhr = new XMLHttpRequest();
		    xhr.open("GET", url);
		    xhr.onload = () => resolve(xhr.responseText);
		    xhr.onerror = () => reject(xhr.statusText);
		    xhr.send();
	  	});
	promise.then((response)=> console.log(response));
};
myAsyncPromise("http://localhost:8080/myfile.txt");


