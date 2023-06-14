
Curriculum
Short Specializations
Average: 108.49%
0x08. Making Change
Algorithm
Python
 By: Carrie Ybay, Software Engineer at Holberton School
 Weight: 1
 Project will start Jun 12, 2023 3:00 AM, must end by Jun 16, 2023 3:00 AM
 Checker will be released at Jun 13, 2023 3:00 AM
 An auto review will be launched at the deadline
Requirements
General
Allowed editors: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/python3
A README.md file, at the root of the folder of the project, is mandatory
Your code should use the PEP 8 style (version 1.7.x)
All your files must be executable
Tasks
0. Change comes from within
mandatory
Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount total.

Prototype: def makeChange(coins, total)
Return: fewest number of coins needed to meet total
If total is 0 or less, return 0
If total cannot be met by any number of coins you have, return -1
coins is a list of the values of the coins in your possession
The value of a coin will always be an integer greater than 0
You can assume you have an infinite number of each denomination of coin in the list
Your solution’s runtime will be evaluated in this task

==============================================

Étant donné un tas de pièces de différentes valeurs, déterminez le plus petit nombre de pièces nécessaires pour atteindre un montant total donné.

Prototype : def makeChange(coins, total)
Return : le plus petit nombre de pièces nécessaires pour atteindre le total
Si le total est égal ou inférieur à 0, il renvoie 0
Si le total ne peut pas être atteint avec n'importe quel nombre de pièces que vous avez, renvoyez -1
pièces est une liste des valeurs des pièces en votre possession
La valeur d'une pièce sera toujours un nombre entier supérieur à 0.
Vous pouvez supposer que vous avez un nombre infini de chaque dénomination de pièce dans la liste.
La durée d'exécution de votre solution sera évaluée dans cette tâche


carrie@ubuntu:~/0x08-making_change$ cat 0-main.py
#!/usr/bin/python3
"""
Main file for testing
"""

makeChange = __import__('0-making_change').makeChange

print(makeChange([1, 2, 25], 37))

print(makeChange([1256, 54, 48, 16, 102], 1453))

carrie@ubuntu:~/0x08-making_change$
carrie@ubuntu:~/0x08-making_change$ ./0-main.py
7
-1
carrie@ubuntu:~/0x08-making_change$
Repo:

GitHub repository: alx-interview
Directory: 0x08-making_change
File: 0-making_change.py
 
Copyright © 2023 ALX, All rights reserved.