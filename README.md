Install dependencies:
Make sure you have Python 3.x installed on your system. Install the required Python libraries by running the following command:

bash
Copy code
pip install -r requirements.txt
3. Install Stockfish 🧑‍💻:
You need Stockfish, the powerful chess engine, to evaluate positions. The tool relies on Stockfish to provide accurate analysis.

Option 1: Download Stockfish and set it up manually
Create a Binaries directory inside the src folder. Your directory structure should look like this:

css
Copy code
ChessAnalyzer/
├── src/
│   ├── Binaries/
│   │   ├── Linux/
│   │   ├── Mac/
│   │   ├── Windows/
Download Stockfish for your OS:

Linux: Download Stockfish for Linux from Stockfish for Linux
Mac: Download Stockfish for Mac from Stockfish for Mac
Windows: Download Stockfish for Windows from Stockfish for Windows
Once downloaded, place the corresponding Stockfish binary inside the relevant folder:

src/Binaries/Linux/ for Linux
src/Binaries/Mac/ for macOS
src/Binaries/Windows/ for Windows
Option 2: Download Stockfish from the web
Alternatively, you can download Stockfish directly from the official site: Stockfish Download. After downloading, place the appropriate Stockfish binary into the corresponding folder in your project directory.

4. Run the application 🎮:
Once Stockfish is set up and dependencies are installed, you can run the Chess Analyzer by executing:

bash
Copy code
python ChessAnalyzer.py
Usage 🧑‍💻
Select an input method:
You can input a PGN file (a standard format for chess games) or a FEN string (representing a specific chess position) for analysis.

Set the analysis depth:
The tool lets you adjust the analysis depth (default is 12). A higher depth means a more detailed analysis, but it will take more time.

Choose the player's perspective:
You can select to analyze the game from the White or Black player's perspective.

Start the analysis:
Once the file or position is selected and settings are configured, simply click the "Analyze Game" button. The analysis will begin, and the results will be displayed once completed.

Example Usage 🔧
1. Analyzing a PGN file:
You can run the tool from the command line to analyze a PGN file. Here's an example:

bash
Copy code
python ChessAnalyzer.py gamefile.pgn white 12
This will analyze the game in gamefile.pgn from the White player's perspective at an analysis depth of 12.

2. Analyzing a position using a FEN string:
You can also analyze a chess position directly using a FEN string. A FEN (Forsyth-Edwards Notation) string represents a specific position on the chessboard.

For example, to analyze a position using a FEN string, run the following command:

bash
Copy code
python ChessAnalyzer.py "rnbqkbnr/pppppppp/..." black 12
This will analyze the position described by the FEN string, from the Black player's perspective, at an analysis depth of 12.

Credits 🙏
Stockfish: The powerful chess engine that provides the evaluations. Stockfish is one of the strongest chess engines in the world and is used for analyzing positions and games.
Aditya Kharmale: The developer of this tool. It took some time to realize that Stockfish is way smarter than me! 😅
