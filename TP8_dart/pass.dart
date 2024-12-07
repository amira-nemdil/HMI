import 'my_pass.dart';

void main() {
  print(withinTolelrence(5));
  print(withinTolelrence(10, min: 10, max: 20));

  User user = User(15,"raouf");
  User guest = User.guest();
  print(user);
  user.test = 10;
  user.miklo = "test";
  print(user);
  print(guest);

  final myObject = MyClass();
  final anotherObject = myObject;
  anotherObject.myProprety = 2;
  print(anotherObject.myProprety); // one in the same
  print(myObject.myProprety); // one in the same

  final password = Password();
  final text = password.getPlainText();
  final text2 = password.plainText;
  print('Text from getter: $text');
  print('Text from direct property access: $text2');
}

class MyClass {
  var myProprety = 1;
}

class User {
  User.guest(){
    test=0;
    miklo="guest";
  }

  // User(int test, String miklo ){
  //   this.test=id;
  //   this.miklo=miklo;
  // } long form constructor

   User(this.test, this.miklo);  //short form constuctor

  final id = 0;
  int test = 10;
  String miklo = " ";

  String toJson() {
    return ("the miklo $miklo test $test");
  }

  @override
  String toString() {
    return ("the miklo $miklo test $test");
  }
}

bool withinTolelrence(int value, {int min = 0, int max = 10}) {
  return min <= value && value <= max;
}

int add(int a, int b) => a + b;