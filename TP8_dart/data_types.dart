// Demonstrates data type declarations and constants
void demoDataTypes() {
  // Declaring variables with specific types
  int number = 10;
  print("Integer number: $number");

  double myFloat = 4.33333;
  print("Rounded double: ${myFloat.round()}");

  // Using `num` for both integer and float values
  num myNumber = 22;
  print("Num value: $myNumber");
  myNumber = 3.73738;
  print("Num value changed: $myNumber");

  // Using `const` and `final` for constants
  const constantValue = 10;
  print("Constant value: $constantValue");

  final hoursSinceMidnight = DateTime.now().hour;
  print("Hours since midnight: $hoursSinceMidnight");
}
void main() {
  demoDataTypes();
}
