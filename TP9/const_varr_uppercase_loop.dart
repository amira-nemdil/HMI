void main () {
  const deserts= ['gobi','sahara','arctic'];
  var bigDeserts =[
    'ARABIAN',
    for (var desert in deserts) desert.toUpperCase()
  ];
  print(bigDeserts);
}