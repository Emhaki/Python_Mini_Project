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
    if chosen_word == "바나나":
        print("열대 과일중에 나무에서 자라는 과일이야!, 3글자")
    if chosen_word == "파인애플":
        print("사과랑 비슷한 이름이지만 맛이 완전 달라!, 4글자")
    if chosen_word == "사과":
        print("가장 흔하게 먹을 수 잇는 과일 인 것 같아!, 2글자")
    if chosen_word == "복숭아":
        print("애벌레들이 가장 좋아하는 과일!, 3글자")
    if chosen_word == "청포도":
        print("꿀떡 삼킬 수 있는 과일!, 3글자")
    if chosen_word == "천도복숭아":
        print("매우 뜨거운 과일이라고도 불려!, 5글자")
    if chosen_word == "샤인머스켓":
        print("초록초록한게 식감이 아주 좋아!, 5글자")

    guess_word = input("한 글자씩 맞춰봐:").lower()

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
