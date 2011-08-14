var http = require('http'); // Var is not global

var s = http.createServer(function(req,resp) {
        resp.writeHead(200, {'content-type': 'text/plain'});
        resp.write('Hello ');

        setTimeout(function() {resp.end(" Node Sundar!!!!");
          }, 2000);

    });
s.listen(8000);
