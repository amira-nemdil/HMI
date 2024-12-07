void main() {
  // Collection if
  const peanutAllergy = true;
  const sensitiveCandy = [
    'Junior Mints',
    'Twizzlers',
    // ignore: dead_code
    if (!peanutAllergy) 'Resses',
  ];
  print(sensitiveCandy);
  // collection for
  const deserts = ['gobi', 'sahara', 'arctic'];
  List<String> bigDesserts = [
    'ARABIAN',
    for (var desert in deserts) desert.toUpperCase(),
  ];
  print(bigDesserts);

  // const drinks = ['water', 'milk', 'juice', 'soda'];
  // const candy = ['Junior Mints', 'Twizzlers', 'MMs'];

  // const desserts = ['cookies', ...candy, ...drinks];
  // print(desserts);

  // print(drinks.first);
  // print(drinks.last);
  // for (int i = 0; i < drinks.length; i++) {
  //   final item = drinks[i];
  //   print('I like $item.');
  // }
  // for (final item in drinks) {
  //   print('I also like $item.');
  // 
  }