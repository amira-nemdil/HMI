// Demonstrates basic mathematical operations
import 'dart:math';

void demoMathOperations() {
  print("Cosine of 135 degrees: ${cos(135 * pi / 180)}");
  print("Square root of 4: ${sqrt(4)}");
  print("Maximum of 0 and 2: ${max(0, 2)}");
  print("Minimum of 2 and 4: ${min(2, 4)}");

  int integer = 100;
  double decimal = 12.5;
  integer = decimal.toInt(); // Convert decimal to integer
  print("Converted decimal to integer: $integer");
}
void main() {
  demoMathOperations();
}