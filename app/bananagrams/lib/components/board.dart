import 'package:flutter/material.dart';

class Board extends StatefulWidget {
  final List<List<String>> boardData;

  Board({Key key, this.boardData}): super(key: key);

  @override
  _BoardState createState() => _BoardState();
}

class _BoardState extends State<Board> {
  int row = 10;
  int column = 10;

  List<List<String>> bananaBoard;

  void setUpBoard() {
    setState(() {
      bananaBoard = widget.boardData;
      print(widget.boardData);
    });
  }

  @override
  void initState() {
    super.initState();
    setUpBoard();
  }

  @override
  Widget build(BuildContext context) {
    bananaBoard = widget.boardData;
    return Column(
      children: bananaBoard.map((row) {
        return Row(
          mainAxisAlignment: MainAxisAlignment.center,
          children: row.map((tile) {
            return Container(
              height: 25.0,
              width: 25.0,
              margin: EdgeInsets.all(.5),
              child: Center(
                  child: Text(
                      tile,
                      style: TextStyle(
                        fontWeight: FontWeight.bold,
                      )
                  )
              ),
              decoration: BoxDecoration(
                color: tile == '' ? Colors.grey[600] : Colors.white,
                borderRadius: BorderRadiusDirectional.circular(1.0),
              ),
            );
          }).toList(),
        );
      }).toList(),
    );
  }


}
