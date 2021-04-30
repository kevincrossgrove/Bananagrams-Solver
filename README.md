# Bananagrams-Solver
Flutter application that allows user to scan their Bananagrams letters and have a solved board generated using those letters. 

### How it works
1. Allows user to scan their letters use text recognition from **Firebase ML Kit**.
2. Allows users to edit the letters scanned in, and then send the letters to a **Flask Server**.
3. The flask server performs all the logic involved with solving the board.
4. The flash server returns the solved board as a **2D** array then can then be outputted in flutter

### Caveats
- To use on your machine, update the IP address used in the get request to your **IPV4**.
- If you are running the app on a physical phone, the phone must be on the **SAME** wifi network as the server.
- To run the server **Python** must be installed. ```cd server; python server.py```
- To run the app **Flutter** must be installed as well. ```cd app/bananagrams; flutter pub get```
- **Text recognition struggles with certain bananagrams tiles. For example I's. You likely will need to add any I's you have manually.**

#### Images

![bananagrams-pic-1](https://user-images.githubusercontent.com/58451014/116639210-f98c1480-a935-11eb-8b5e-bdf89c9fa4df.png)

![bananagrams-pic-2](https://user-images.githubusercontent.com/58451014/116639244-11639880-a936-11eb-84ed-9354aa660b1f.png)
