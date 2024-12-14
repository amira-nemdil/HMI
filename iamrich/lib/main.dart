import 'package:flutter/material.dart';

void main() {
  runApp(MaterialApp());
}
//theme: ThemeData(
//  colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
//  useMaterial3: false,
//
/*debugShowCheckedModeBanner: false,
      home: Scaffold(
        backgroundColor: Colors.lightBlue,
        appBar: AppBar(
          backgroundColor: Colors.blueGrey[900],
          title: const Center(
            child: Text(
              'I am rich',
              style: TextStyle(color: Colors.white),
            ),
          ),
        ),
        body: Center(
          child: Image.asset('image/Diamond1.jpg'),
        ),
      ),
    ),
  );
}*/
class MyApp extends StatelessWidget {
  const MyApp({super.key});

 
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: Scaffold(
        backgroundColor: Colors.red,
        body: Container(),

      ),
    );
  }
}
