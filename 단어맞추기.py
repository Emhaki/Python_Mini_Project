from dis import dis
import random
from turtle import pos
word_list = ["바나나", "파인애플", "사과", "복숭아", "청포도", "천도복숭아", "샤인머스켓"]

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6


display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess_word = input("글자를 맞춰봐:").lower()

    if guess_word in display:
        print(f"이미 {guess_word}를 말했었어")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess_word:
            display[position] = letter

    if guess_word not in chosen_word:
        lives -= 1
        print(
            f"너가 추리했던 {guess_word}은(는) 단어에 없어. 목숨 하나를 잃었어. 현재 목숨 {lives}")
        if lives == 0:
            print("넌 졌어")
            end_of_game = True

    print(f"{' '.join(display)}")

    # display 리스트에 "_"가 있는지 없는지 확인
    if "_" not in display:
        end_of_game = True
        print("너가 이겼어!")
