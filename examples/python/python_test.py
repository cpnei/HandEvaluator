import clr
clr.AddReference("HandEvaluator")
from HoldemHand import Hand
from System import Array, Double, String, Int64
import time
import numpy as np
import itertools

def CalcWinrate_hpoo(Pocket, Board):
    playerWins = Array[Double]([1.0]*9)
    opponentWins = Array[Double]([0.0]*9)
    Hand.HandPlayerOpponentOdds(Pocket, Board, playerWins, opponentWins)
    return sum(playerWins)
    
def CalcWinrate_mc(Pocket, Board):
    wr = Double(0)
    r = Hand.MCWinRate(Pocket, Board, "", 10, 1000000, wr)
    return r
    
def RandomTable():
    values = "23456789tjqka"
    types = "shdc"
    allcards = list(map("".join, itertools.product(values, types)))
    pickedcards = np.random.permutation(allcards)[:5]
    return " ".join(pickedcards[:3]), " ".join(pickedcards[3:5])

def test_hpoo1():
    playerWins = Array[Double]([1.0]*9)
    opponentWins = Array[Double]([0.0]*9)
    Pocket = "ac as"
    Board = "4d 5d 6c"

    print("===============================================================================")
    for Board in ["", "4d 5d 6c", "4d 5d 6c 7s", "4d 5d 6c 7s 8d"]:
        Hand.HandPlayerOpponentOdds(Pocket, Board, playerWins, opponentWins)
        print("Pocket:", Pocket)
        print("Board:", Board)
        #print(list(playerWins))
        print("playerWins:", sum(playerWins))
        print("High Card: %f%%"%      ( playerWins[int(Hand.HandTypes.HighCard)]*100.0))
        print("Pair: %f%%"%           ( playerWins[int(Hand.HandTypes.Pair)]*100.0))
        print("Two Pair: %f%%"%       ( playerWins[int(Hand.HandTypes.TwoPair)]*100.0))
        print("Three of Kind: %f%%"%  ( playerWins[int(Hand.HandTypes.Trips)]*100.0))
        print("Straight: %f%%"%       ( playerWins[int(Hand.HandTypes.Straight)]*100.0))
        print("Flush: %f%%"%          ( playerWins[int(Hand.HandTypes.Flush)]*100.0))
        print("Fullhouse: %f%%"%      ( playerWins[int(Hand.HandTypes.FullHouse)]*100.0))
        print("Four of a Kind: %f%%"% ( playerWins[int(Hand.HandTypes.FourOfAKind)]*100.0))
        print("Straight Flush: %f%%"% ( playerWins[int(Hand.HandTypes.StraightFlush)]*100.0))
        print("\n")
        #print(list(opponentWins))
        print("opponentWins:", sum(opponentWins))
        print("High Card: %f%%"%      ( opponentWins[int(Hand.HandTypes.HighCard)]*100.0))
        print("Pair: %f%%"%           ( opponentWins[int(Hand.HandTypes.Pair)]*100.0))
        print("Two Pair: %f%%"%       ( opponentWins[int(Hand.HandTypes.TwoPair)]*100.0))
        print("Three of Kind: %f%%"%  ( opponentWins[int(Hand.HandTypes.Trips)]*100.0))
        print("Straight: %f%%"%       ( opponentWins[int(Hand.HandTypes.Straight)]*100.0))
        print("Flush: %f%%"%          ( opponentWins[int(Hand.HandTypes.Flush)]*100.0))
        print("Fullhouse: %f%%"%      ( opponentWins[int(Hand.HandTypes.FullHouse)]*100.0))
        print("Four of a Kind: %f%%"% ( opponentWins[int(Hand.HandTypes.FourOfAKind)]*100.0))
        print("Straight Flush: %f%%"% ( opponentWins[int(Hand.HandTypes.StraightFlush)]*100.0))
        print("===============================================================================\n")

def test_hpoo2():
    playerWins = Array[Double]([1.0]*9)
    opponentWins = Array[Double]([0.0]*9)
    Pocket = "kc ks"
    Board = "8h 6c 4h"

    print("===============================================================================")
    for Pocket in ["kc ks", "7h 9h"]:
        Hand.HandPlayerOpponentOdds(Pocket, Board, playerWins, opponentWins)
        print("Pocket:", Pocket)
        print("Board:", Board)
        #print(list(playerWins))
        print("playerWins:", sum(playerWins))
        print("High Card: %f%%"%      ( playerWins[int(Hand.HandTypes.HighCard)]*100.0))
        print("Pair: %f%%"%           ( playerWins[int(Hand.HandTypes.Pair)]*100.0))
        print("Two Pair: %f%%"%       ( playerWins[int(Hand.HandTypes.TwoPair)]*100.0))
        print("Three of Kind: %f%%"%  ( playerWins[int(Hand.HandTypes.Trips)]*100.0))
        print("Straight: %f%%"%       ( playerWins[int(Hand.HandTypes.Straight)]*100.0))
        print("Flush: %f%%"%          ( playerWins[int(Hand.HandTypes.Flush)]*100.0))
        print("Fullhouse: %f%%"%      ( playerWins[int(Hand.HandTypes.FullHouse)]*100.0))
        print("Four of a Kind: %f%%"% ( playerWins[int(Hand.HandTypes.FourOfAKind)]*100.0))
        print("Straight Flush: %f%%"% ( playerWins[int(Hand.HandTypes.StraightFlush)]*100.0))
        print("\n")
        #print(list(opponentWins))
        print("opponentWins:", sum(opponentWins))
        print("High Card: %f%%"%      ( opponentWins[int(Hand.HandTypes.HighCard)]*100.0))
        print("Pair: %f%%"%           ( opponentWins[int(Hand.HandTypes.Pair)]*100.0))
        print("Two Pair: %f%%"%       ( opponentWins[int(Hand.HandTypes.TwoPair)]*100.0))
        print("Three of Kind: %f%%"%  ( opponentWins[int(Hand.HandTypes.Trips)]*100.0))
        print("Straight: %f%%"%       ( opponentWins[int(Hand.HandTypes.Straight)]*100.0))
        print("Flush: %f%%"%          ( opponentWins[int(Hand.HandTypes.Flush)]*100.0))
        print("Fullhouse: %f%%"%      ( opponentWins[int(Hand.HandTypes.FullHouse)]*100.0))
        print("Four of a Kind: %f%%"% ( opponentWins[int(Hand.HandTypes.FourOfAKind)]*100.0))
        print("Straight Flush: %f%%"% ( opponentWins[int(Hand.HandTypes.StraightFlush)]*100.0))
        print("===============================================================================\n")

def benchmark_hpoo():
    playerWins = Array[Double]([1.0]*9)
    opponentWins = Array[Double]([0.0]*9)
    Pocket = "ac as"
    repeat = 100
    
    Board = "4d 5d 6c 7s 8d"
    start_time = time.time()
    for i in range(repeat):
        Hand.HandPlayerOpponentOdds(Pocket, Board, playerWins, opponentWins)
    average = (time.time()-start_time)/float(repeat)
    print("average time (5+2 cards): ", average*1000, "ms")
    
    Board = "4d 5d 6c 7s"
    start_time = time.time()
    for i in range(repeat):
        Hand.HandPlayerOpponentOdds(Pocket, Board, playerWins, opponentWins)
    average = (time.time()-start_time)/float(repeat)
    print("average time (4+2 cards): ", average*1000, "ms")
    
    Board = "4d 5d 6c"
    start_time = time.time()
    for i in range(repeat):
        Hand.HandPlayerOpponentOdds(Pocket, Board, playerWins, opponentWins)
    average = (time.time()-start_time)/float(repeat)
    print("average time (3+2 cards): ", average*1000, "ms")
    
    repeat = 10000
    Board = ""
    start_time = time.time()
    for i in range(repeat):
        Hand.HandPlayerOpponentOdds(Pocket, Board, playerWins, opponentWins)
    average = (time.time()-start_time)/float(repeat)
    print("average time (0+2 cards): ", average*1000, "ms")
    
def test_HandOdds():
    pockets = Array[String](["ac as", "ad 2c"])
    board = "4d 5d 6c"
    dead = ""
    wins = Array[Int64]([0]*2)
    ties = Array[Int64]([0]*2)
    losses = Array[Int64]([0]*2)
    totalHands = Int64(0)
    
    Hand.HandOdds(pockets, board, dead, wins, ties, losses, totalHands)
    #print(totalHands)
    #print(list(wins))
    #print(list(ties))
    #print(list(losses))
    totalHands = float(wins[0]+ties[0]+losses[0]) # so far there is an issue that totalHands is always returned as zero #float(int(totalHands.ToString()))
    
    print("P1_win:")
    print(wins[0]/totalHands)
    print("P1_ties:")
    print(ties[0]/totalHands)
    print("P1_losses:")
    print(losses[0]/totalHands)
    
    print("P2_win:")
    print(wins[1]/totalHands)
    print("P2_ties:")
    print(ties[1]/totalHands)
    print("P2_losses:")
    print(losses[1]/totalHands)
    
def test_HandPotential():
    pp = Double(0)
    np = Double(0)
    Pocket = "ac as"
    Board = "4d 5d 6c"
    r = Hand.HandPotential(Pocket, Board, pp, np)
    print("Positive potential", pp)
    print("Negative potential", np)
    print(r)
    
def test_MCWinRate():
    wr = Double(0)
    
    start_time = time.time()
    Pocket = "ac as"
    Board = "4d 5d 6c"
    for i in [10, 100, 1000, 10000, 100000, 1000000]:
        r = Hand.MCWinRate(Pocket, Board, "", 10, i, wr)
        etime = (time.time()-start_time)
        print(i, r)
        print("elapsed time=", etime)
    
def compare_WinRate():
    for i in range(100):
        Board, Pocket = RandomTable()
        print(Board, Pocket, CalcWinrate_hpoo(Pocket, Board), CalcWinrate_mc(Pocket, Board))
    
if __name__ == "__main__":
    #test_hpoo1()
    #test_hpoo2()
    #test_HandOdds()
    #benchmark_hpoo()
    #test_HandPotential()
    test_MCWinRate()
    #compare_WinRate()
    