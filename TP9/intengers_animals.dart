void main() {
  final integers = [32, 73, 2, 343, 7, 10, 1];
  integers.sort();
  print(integers);
  final smallest = integers[0];
  print(smallest);

  final lastIndex = integers.length - 1;
  final largest = integers[lastIndex];
  print(largest);

  final animals = ['zebra', 'dog', 'alligator', 'cat'];
  animals.sort();
  print(animals);
}