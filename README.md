# HandEvaluator
A partial porting of Keith Rule's "Fast, Texas Holdem Hand Evaluation and Analysis" on https://www.codeproject.com/Articles/12279/Fast-Texas-Holdem-Hand-Evaluation-and-Analysis.

To understand the algorithm behind the source code please refer to http://poker.cs.ualberta.ca/publications/davidson.msc.pdf section 3.3

## Introduction of interested functions
```C#
public static void HandPlayerOpponentOdds(string pocketcards, string boardcards, ref double[] player, ref double[] opponent)
```
Compute hand odds for one player againt an opponent with random pocket cards. The output is stored in 2 arrays:
* **player**: Arrary of size 9. Wining probability of player with each hand types.(refering of HoldemHand.Hand.HandTypes)
* **opponent**: Arrary of size 9. Wining probability of opponent with each hand types.
* sum(player) is the winning probability of player and sum(opponent) is the losing probability of player regardless of hand types.
* sum(player)+sum(opponent)=1

```C#
public static void HandOdds(string[] pockets, string board, string dead, long[] wins, long[] ties, long[] losses, ref long totalHands)
```
Given complete table information(pocket hands of each player, board cords.), calculate winning/tying/losing probability for each player.

## Build environment
The project was tested with VS2015 and .NET framework 4.0

Python example was tested with Python 3.6

## How to use in Python

* Install Python for .NET
```
pip install pythonnet
```
* Copy HandEvaluator.dll to the same folder with your python code
* Add reference to HandEvaluator in the python code and enjoy.(See examples\python\python_test.py for complete examples.)
```python
import clr
clr.AddReference("HandEvaluator")
from HoldemHand import Hand
from System import Array, Double, String, Int64

playerWins = Array[Double]([1.0]*9)
opponentWins = Array[Double]([0.0]*9)
Pocket = "ac as"
Board = "4d 5d 6c"
Hand.HandPlayerOpponentOdds(Pocket, Board, playerWins, opponentWins)
print("Win rate: ", sum(playerWins))
print("Lose rate: ", sum(opponentWins))
```

