void main() {

  final drinks = <String>{};
  drinks.add('cola');
  drinks.add('water');
  drinks.add('cola');
  drinks.remove('water');
  drinks.addAll(['juice','coffe','milk']);

  print(drinks);

  for (final drink in drinks) {
    print("I'm drinking $drink");
    final beverges=drinks;
  print(drinks);
  print(beverges);

  }

}