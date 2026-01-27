import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
length = len(friends)
random_no = random.randint(0 , length - 1)

print(f"Today's unlucky person is {friends[random_no]} ,"
      f" who is going to pay the bill for all of us. :(")