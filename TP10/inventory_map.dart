void main () {
  final inventory = {
    'cakes': 20,
    'pies' : 14,
    'donuts' : 37,
    'cookies':141,
  };

  final numberOfCakes =inventory['cakes'];
  print(numberOfCakes);
  inventory['brownies']=3;
  print(inventory);
  inventory['cakes']=1;
  inventory.remove('cookies');
  print(inventory);

  inventory.isEmpty ;
  inventory.isNotEmpty;
  inventory.length;

  print(inventory.containsKey('pies')); //true
  print(inventory.containsValue(42)); //false

  for (var key in inventory.keys) {
    print(inventory[key]);
  }

  for (final entry in inventory.entries) {
    print('${entry.key} -> ${entry.value}');
  }

  //inventory.isEmpty //False 
  //inventory.isNotEmpty //True


  
  }
