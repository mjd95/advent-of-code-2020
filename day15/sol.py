from collections import defaultdict

starting_numbers = [1,0,18,10,19,6]

said = defaultdict(list)
turn = 1
last_said = None

# say the starting numbers
for n in starting_numbers:
    said[n].append(turn)
    last_said = n
    turn += 1

# now play the game
while turn <= 30000000:
    if len(said[last_said]) == 1:
        # that was the first time that number was said, so say 0
        said[0].append(turn)
        last_said = 0
    else:
        # we say the difference between the previous turn nubers
        to_say = said[last_said][-1] - said[last_said][-2]
        said[to_say].append(turn)
        last_said = to_say

    turn += 1
    if (turn % 1000000) == 0:
        print(last_said)
print(last_said)