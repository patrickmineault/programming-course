% Supplementary assignment I
% Programming for VR I
% Patrick Mineault
---
pandoc-latex-fontsize:
  - classes: [listing]
    size: scriptsize
  - classes: [footnote]
    size: tiny
---

# Goal

* Create a mini-game, hexagon ball
* https://youtu.be/5tMZaPQ0Xos 

# Elements

* hexagon
* turns with left and right keys
* ball
* ball moves toward the center
* the ball can either touch the hexagon or go through the gap
* when the ball goes through the gap, it returns to the side, scoring one point
* hitting the ball on the side of the hexagon ends the game, resetting the score to zero
* score in the top left

# Hint

* Use trigonometry to figure out whether ball is passing through the gap
* OR look at the pixel directly under the ball

# Assignment

* post on Github
* Due in two weeks
* Final score = max(exam, hexagon_ball)

