
// Demonstrates string manipulations and operations
 void demoStringOperations() {
  const name = 'Ray';
  const introduction = 'Hello, my name is $name'; // String interpolation
  print(introduction);

  const oneThird = 1 / 3;
  final sentence = 'One third is ${oneThird.toStringAsFixed(3)}.';
  print(sentence);

  const multiLineString = '''
  This is a string
  that spans multiple
  lines.''';
  print(multiLineString);

  const rawString = r'This is a raw string with no special character handling: \n $name';
  print(rawString);
}
void main() {
  demoStringOperations();
}