In this file we apply the mini-max algorithm to develope an AI game player for a modified version of the game called Teeko.

Teeko is a game between two players on a 5x5 board. Each player has four markers of either red or black. Beginning with black, they take turns placing markers (the "drop phase") until all markers are on the board, with the goal of getting four in a row horizontally, vertically, or diagonally, or in a 2x2 box as shown above.

If after the drop phase neither player has won, they continue taking turns moving one marker at a time -- to an adjacent space only! (Note this includes diagonals, not just left, right, up, and down one space.) -- until one player wins.

The Teeko2 rules are almost identical to those of Teeko but we will exchange a rule. Specifically, we remove the 2x2 box winning condition and replace it with a diamond winning condition. Any diamond is defined by an empty center position surrounded by 4 markers on the spaces above, below, to the right, and to the left of the center. Mathematically, if (i,j) is the center of a diamond, then it must be that (i,j) is empty and that there is a marker of the appropriate color on each of (i+1,j), (i-1,j), (i,j+1), and (i,j-1). Visually, this makes a diamond shape on the board.

In the inplementation we use heuristic game value to evaluate a state at a certain depth to guarantee efficiency.
