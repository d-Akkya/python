import random

def game():
    print("You are playing a game...")
    score = random.randint(1, 62)
    # fetch the highScore
    with open("F:/python/CHAPTER_9 - PS/Hi-score.txt") as f:
        highScore = f.read()
        if(highScore!=""):
            highScore = int(highScore)
        else:
            highScore = 0
        
    print(f"Your score: {score}")
    if(score>highScore):
        # write this highScore to the file
         with open("F:/python/CHAPTER_9 - PS/Hi-score.txt", "w") as f:
            f.write(str(score))

    return score

game()