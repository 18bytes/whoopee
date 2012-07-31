#import('dart:html');

class dart_tour {

  dart_tour() {
  }

  void run() {
    write("Hello Sundar!");
   
  }

  void write(String message) {
    // the HTML library defines a global "document" variable
    document.query('#status').innerHTML = message;
  }
}

void main() {
  print(Math.random());
  print(Math.random());
  print(Math.random());
}
