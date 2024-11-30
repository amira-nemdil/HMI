// Full Program

const global = 'hello world';

void main() {
  // Part 1: fullName Function
  print(fullName('Ray', 'We,derlich')); // Output: Ray We,derlich
  print(fullName('Albert', 'Einstein', 'Professor')); // Output: *Professor Albert Einstein

  // Part 2: withinTolerance Function
  print(withinTolerance(value: 5)); // true
  print(withinTolerance(value: 15)); // false
  print(withinTolerance(value: 9, max: 11)); // true

  // Part 3: add Function
  print(add(4, 6)); // Output: 10

  // Part 4: User Class Example
  User user = User();
  print('User ID: ${user.id}, Name: ${user.name}'); // Output: User ID: 0, Name: 

  // Part 5: Final Example
  String name = 'ew';
  int age = 12;

  final anotherUser = User()
    ..name = name
    ..id = age;

  print('User Details: Name: ${anotherUser.name}, Age: ${anotherUser.id}'); // Output: User Details: Name: ew, Age: 12
}

// Part 1: fullName Function
String fullName(String first, String last, [String? title]) {
  if (title != null) {
    return '*$title $first $last';
  } else {
    return '$first $last';
  }
}

// Part 2: withinTolerance Function
bool withinTolerance({
  required int value,
  int min = 0,
  int max = 10,
}) {
  return min <= value && value <= max;
}

// Part 3: add Function
int add(int a, int b) => a + b;

// Part 4 & 5: User Class
class User {
  int id = 0;
  String name = '';
}


// How it Works:
//fullName: Handles optional parameters for titles.
//withinTolerance: Checks if a value is within a given range.
//add: Simple function to return the sum of two integers.
//User Class: Represents a user with id and name. Demonstrates property setting using cascade notation.