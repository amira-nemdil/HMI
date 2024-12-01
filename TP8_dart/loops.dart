// Demonstrates loops
void demoLoops() {
  print("Using while loop:");
  int sum = 1;
  while (sum < 10) {
    sum += 4;
    print(sum);
  }

  print("\nUsing do-while loop:");
  sum = 1;
  do {
    sum += 4;
    print(sum);
  } while (sum < 10);

  print("\nUsing for loop:");
  for (var i = 0; i < 5; i++) {
    if (i == 2) continue; // Skip the number 2
    print(i);
  }
}
void main() {
  demoLoops();
}