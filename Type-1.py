""" Task Requirements
Use a for loop to go from 1 to 20.

Inside the loop:

If the number is a multiple of 5 → skip it using continue.

If the number equals 17 → stop the loop using break.

Print the numbers that remain. 
"""
# CODE BEGINS HERE

Num = 0
for Num in range (1 , 21):
    if Num %5 == 0:
        continue
    if Num == 17:
        break
    print(Num)
