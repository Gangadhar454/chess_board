

# Chess Valid Moves

## Table of Contents

- [Introduction](#introduction)
- [Requirements](#requirements)
- [Getting Started](#gettingstarted)

## Introduction
This application provides an API endpoint that determines the valid moves for a given chess piece on a chessboard. The
chessboard contains pieces such as Rook, Queen, Bishop, and Knight, and their positions are provided as input and returns the valid moves for that piece.
![Screenshot from 2024-02-17 23-59-06](https://github.com/Gangadhar454/chess_board/assets/36883246/0e5e3a59-10be-4597-8541-7bf2423c3c31)

### How the API calculates the valid Moves
1. First it will calculate all the possible moves of all the 4 pieces. For Example Bishop can move either in straigth line or diagnol, so the possible moves of bishop is straight moves + diagonal moves
2. Then it will substract the possible moves of other 3 pieces from slug's moves i.e (slug's moves - remaining 3 pieces moves)
3. the second step ensures that it removed the positions which can be attacked by other pieces.


## Requirements
1. Latest version of `docker` and `docker compose` [Link](https://docs.docker.com/engine/install/ubuntu/)
2. After installing `docker` and `docker compose` , do post installation steps [Link](https://docs.docker.com/engine/install/ubuntu/)
3. `make` (sudo apt install make) for easy use

## Getting Started
1. Go to the main directory (where the make file exists)
2. build the backend services
   ```bash
   make build
3. if step-2 fails
   ```bash
   docker compose build
4. start the services
   ```bash
   make restart
5. if step-4 fails
   ```bash
   docker compose up

 ### API Endpoint
 #### Example:
 
  `POST` - http://localhost:8000/chess/knight/
    
  Payload:
  
  ```json
  {
      "positions" : {
          "Queen": "E7",
          "Bishop": "B7",
          "Rook": "G5",
          "Knight": "C3"
      }
  }
  ```
  Response:
  ```json
  {
      "valid_moves": [
          "A2",
          "D1",
          "B1",
          "A4"
      ]
  }
  ```
  ![Screenshot from 2024-02-18 00-06-59](https://github.com/Gangadhar454/chess_board/assets/36883246/b3496179-593e-4d28-b923-3c80fa5485f0)

  
