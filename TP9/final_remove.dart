void main() {
  final integers = [34, 26, 98, 32, 87, 85];
  integers.sort();
  print(integers);
  final lastIndex = integers.length - 1;
  final largest = integers[lastIndex];
  print(largest);

  final animals = ['zebra', 'dog', 'alligator', 'cat'];
  animals.sort();
  print(animals);

  var desserts = ['cookies', 'cupcakes', 'donuts', 'pie'];
  desserts = [];
  desserts = ['cookies', 'cupcakes', 'donuts', 'pie'];
  // it is not allowed to modify a final or const value, but it is allowed to modify its components like a list.
}