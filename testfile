var http = require('http');
var crypto = require('crypto');


var OOapiSecretKey = "329b5b204d0f11e0a2d060334bfffe90ab18xqh5";
var httpMethod = 'GET';
var route = "/v2/players/HbxJK";
var api_key = ""

var sha256 = crypto.createHash("sha256");


http.createServer(function (req, res) {

        res.writeHead(200, {'Content-Type': 'text/plain'});
        res.end(result);

}).listen(8080, '178.62.100.67');

sha256.update(OOapiSecretKey, "utf8");

var result = sha256.digest("base64");


console.log(result);
console.log('Server running at http://178.62.100.67:8080/');
console.log(OOapiSecretKey+httpMethod+route);
