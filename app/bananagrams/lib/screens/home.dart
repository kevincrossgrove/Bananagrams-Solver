import 'package:flutter/cupertino.dart';
import 'package:bananagrams/components/board.dart';
import 'package:flutter/material.dart';
import 'dart:io';
import 'package:dio/dio.dart';
import 'package:image_picker/image_picker.dart';
import 'package:bananagrams/api/firebase_ml_api.dart';

class Home extends StatefulWidget {
  @override
  _HomeState createState() => _HomeState();
}

class _HomeState extends State<Home> {
  List<List<String>> bananaBoard = [
  ["","","","","","","","","","","","","","",""],
  ["","","","","","","","","","","","","","",""],
  ["","","","S","","","","","","","","","","",""],
  ["","","","C","","","","","","","","","","",""],
  ["","","","A","","","","","","","","","","",""],
  ["","","","N","","L","E","T","T","E","R","S","","",""],
  ["","","","","","","","","","","","","","",""],
  ["","","","","","","","","","","","","","",""],
  ["","","","T","O","","S","T","A","R","T","","","",""],
  ["","","","","","","","","","","","","","",""],
  ["","","","","","","","","","","","","","",""]
  ];

  var lettersForm = TextEditingController(text: 'Currently no letters');

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.grey[700],
      body: Padding(
        padding: const EdgeInsets.all(10.0),
        child: ListView(
          children: [Column(
            children: [
              SizedBox(height: 40.0),
              Center(
                child: Container(
                  child: Text(
                    'Bananagrams Solver',
                    style: TextStyle(
                      color: Colors.black,
                      fontSize: 30.0,
                      letterSpacing: 2.0,
                      fontFamily: 'Bangers',
                    ),
                  ),
                  padding: EdgeInsets.all(15.0),
                  decoration: BoxDecoration(
                    color: Colors.amber,
                    borderRadius: BorderRadiusDirectional.circular(10.0),
                  ),
                ),
              ),
              SizedBox(height: 60.0),
              Container(
                  child: SingleChildScrollView(
                    scrollDirection: Axis.horizontal,
                    child: Row(
                        children: [
                          Board(boardData: bananaBoard),
                        ],
                      ),
                    ),
                  ),
              SizedBox(height: 40.0),
              ElevatedButton.icon(
                style: ElevatedButton.styleFrom(
                    primary: Colors.black,
                    padding: EdgeInsets.all(12.0)
                ),
                onPressed: () {
                  scanText();
                },
                icon: Icon(Icons.camera),
                label: Text(
                  'Scan Letters',
                  style: TextStyle(
                    fontSize: 20.0,
                    fontFamily: 'Bangers',
                    letterSpacing: 2.0,
                    color: Colors.amber,
                  ),
                ),
              ),
              SizedBox(height: 20.0),
              Container(
                  decoration: BoxDecoration(
                    color: Colors.grey[200],
                    borderRadius: BorderRadiusDirectional.circular(5.0),
                  ),
                  child: Padding(
                    padding: const EdgeInsets.fromLTRB(12.0, 8.0, 12.0, 8.0),
                    child: TextField(
                      maxLines: null,
                      controller: lettersForm,
                      style: TextStyle(
                        fontSize: 30.0,
                        fontFamily: 'Bangers',
                        letterSpacing: 3.0
                      ),
                    ),
                  ),
              ),
              SizedBox(height: 20.0),
              ElevatedButton.icon(
                style: ElevatedButton.styleFrom(
                    primary: Colors.black,
                    padding: EdgeInsets.all(12.0)
                ),
                onPressed: () {
                  getSolvedBoard(lettersForm.text);
                },
                icon: Icon(Icons.send_rounded),
                label: Text(
                  'Send Letters',
                  style: TextStyle(
                    fontSize: 20.0,
                    fontFamily: 'Bangers',
                    letterSpacing: 2.0,
                    color: Colors.green,
                  ),
                ),
              )
            ],
          )]
        ),
      ),
    );
  }

  Future scanText() async {
    final imageFile = await ImagePicker.platform.pickImage(
      preferredCameraDevice: CameraDevice.front,
      source: ImageSource.camera,
    );

    String text = await FirebaseMLApi.recogniseText(File(imageFile.path));

    setState(() {
      lettersForm.text = text;
    });
  }

  Future getSolvedBoard(String letters) async {
    List<List<String>> convertedBoard = [];
    String url = "http://192.168.1.205:9000/api/bananas/" + letters.toLowerCase() + '/true';

    final Dio dio = new Dio();

    try {
      var response = await dio.get(url);
      List<dynamic> boardData = response.data['data'];
      String remaining = response.data['remaining'];

      for (var row in boardData) {
        List<String> tempRow = [];
        for (var letter in row) {
          tempRow.add(letter);
        }
        convertedBoard.add(tempRow);
      }
      passDataToBoard(convertedBoard);
    } catch (error) {
      print('Uh oh stinky error alert');
      print(error);
    }
  }

  void passDataToBoard(List<List<String>> board) {
    setState(() {
      bananaBoard = board;
    });
  }
}
