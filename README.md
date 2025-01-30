# Gomoku Game AI

This repository contains an implementation of the Gomoku game with an AI opponent. Gomoku, also known as Five in a Row, is a classic strategy board game where two players take turns placing stones on a grid, aiming to be the first to align five consecutive stones horizontally, vertically, or diagonally.

## Features

- **Game Modes**:
  - Human vs. AI: Play against the computer.
  - Human vs. Human: Two players can play against each other.

- **Artificial Intelligence**:
  - The AI utilizes the Minimax algorithm with Alpha-Beta Pruning to determine optimal moves.

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/lilswapnil/Gomuku-Game-AI.git
   ```

2. **Navigate to the Project Directory**:

   ```bash
   cd Gomuku-Game-AI
   ```

3. **Install Dependencies**:

   Ensure you have Python 3.x installed. Install the required packages using pip:

   ```bash
   pip install numpy
   ```

## Usage

1. **Run the Game**:

   ```bash
   python main.py
   ```

2. **Follow On-Screen Instructions**:

   - Choose the game mode.
   - If playing against the AI, select your desired difficulty level.
   - Make your moves by selecting the coordinates on the board.

## How It Works

The AI component is designed to evaluate possible moves and predict outcomes using the Minimax algorithm enhanced with Alpha-Beta Pruning. This approach allows the AI to effectively assess the game state and make strategic decisions.

## Contributing

Contributions are welcome! If you'd like to improve the game or fix any issues, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

This project was inspired by various Gomoku AI implementations, including:

- [ZitongMao/gomoku-ai](https://github.com/ZitongMao/gomoku-ai)
- [YoniAnk/Gomoku-Ai-Player](https://github.com/YoniAnk/Gomoku-Ai-Player)
- [anyaschukin/Gomoku](https://github.com/anyaschukin/Gomoku)

These repositories provided valuable insights into the development of Gomoku AI strategies.

Enjoy playing Gomoku! 
