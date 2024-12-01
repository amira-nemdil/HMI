void main() {
  const drinks = ['water', 'milk', 'juice', 'soda'];
  print(drinks.first);
  print(drinks.last);
  for (int i = 0; i < drinks.length; i++) {
    final item = drinks[i];
    print('I like $item.');
  }
  for (final item in drinks) {
    print('I also like $item.');
  }
}