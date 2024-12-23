import os
import platform  # Add this import
import chess.engine
import re

dir = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) + '/Binaries'

class AI():
    def __init__(self, depth):
        if platform.system() == "Darwin":
            stockfish_bin = dir + "/Stockfish/Mac/stockfish-11-bmi2"
        elif platform.system() == "Linux":
            stockfish_bin = dir + "/Stockfish/Linux/stockfish_20090216_x64_bmi2"
        else:
            stockfish_bin = dir + "/Stockfish/Windows/stockfish_20090216_x64_bmi2.exe"
            
        self.stockfish = chess.engine.SimpleEngine.popen_uci(stockfish_bin)
        self.depth = depth

    def getBestMove(self, Chessboard):
        try:
            best_move = str(self.stockfish.play(Chessboard, chess.engine.Limit(depth=self.depth)).move)
            return best_move
        except:
            return None

    def getScore(self, move, Chessboard):
        info = self.stockfish.analyse(Chessboard, chess.engine.Limit(depth=self.depth), root_moves=[move])
        score_str = str(info['score'])
        
        # Extract the numeric part from the PovScore string, e.g., 'PovScore(Cp(+31), WHITE)' -> '31'
        if 'Cp' in score_str:
            score_value = score_str.split('Cp(')[1].split(')')[0]
            score_value = score_value.strip('+-')  # Remove + or - sign if present
            return int(score_value)
        else:
            # If the score is not in the expected format, handle it (e.g., return a default value or raise an error)
            raise ValueError(f"Could not extract score from {score_str}")

    
    def compareMove(self, move, Chessboard):
        best_move = self.getBestMove(Chessboard)

        if best_move == move:  # Case move = best move
            return (move, best_move, "B")

        score_move = self.getScore(chess.Move.from_uci(move), Chessboard)
        score_best_move = self.getScore(chess.Move.from_uci(best_move), Chessboard)

        if score_best_move == score_move:  # Case score best move = score move
            return (move, best_move, "B")

        if score_move < 0 and score_best_move >= 0:  # Case score move < 0 and score best move >= 0
            return (str(move), best_move, "E")
        
        if score_best_move > 0:  # Case score move and best move same signs
            dist = score_move / score_best_move
        else:
            dist = abs(score_best_move) / abs(score_move)

        if dist > 0.7:
            return (str(move), best_move, "G")
        elif dist > 0.5:
            return (str(move), best_move, "P")
        else:
            return (str(move), best_move, "E")

    def quit(self):
        self.stockfish.quit()
