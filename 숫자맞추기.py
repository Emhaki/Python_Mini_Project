from random import randint

logo = """
  ______                                                __    __                          __                           
 /      \                                              /  \  /  |                        /  |                          
/$$$$$$  |  ______   __    __   _______  _______       $$  \ $$ | __    __  _____  ____  $$ |____    ______    ______  
$$ | _$$/  /      \ /  |  /  | /       |/       |      $$$  \$$ |/  |  /  |/     \/    \ $$      \  /      \  /      \ 
$$ |/    | $$$$$$  |$$ |  $$ |/$$$$$$$//$$$$$$$/       $$$$  $$ |$$ |  $$ |$$$$$$ $$$$  |$$$$$$$  |/$$$$$$  |/$$$$$$  |
$$ |$$$$ | /    $$ |$$ |  $$ |$$      \$$      \       $$ $$ $$ |$$ |  $$ |$$ | $$ | $$ |$$ |  $$ |$$    $$ |$$ |  $$/ 
$$ \__$$ |/$$$$$$$ |$$ \__$$ | $$$$$$  |$$$$$$  |      $$ |$$$$ |$$ \__$$ |$$ | $$ | $$ |$$ |__$$ |$$$$$$$$/ $$ |      
$$    $$/ $$    $$ |$$    $$/ /     $$//     $$/       $$ | $$$ |$$    $$/ $$ | $$ | $$ |$$    $$/ $$       |$$ |      
 $$$$$$/   $$$$$$$/  $$$$$$/  $$$$$$$/ $$$$$$$/        $$/   $$/  $$$$$$/  $$/  $$/  $$/ $$$$$$$/   $$$$$$$/ $$/       
                                                                                                                       
                                                                                                                       
                                                                                                                       """


answer = randint(1, 100)
# number 리스트에 1~100까지 번호 삽입

easy_life = 10
hard_life = 5


def game():
    print("숫자 맞추기 게임에 오신걸 환영합니다!\n1~100까지 숫자를 맞춰보세요!")

    def check_answer(guess, answer, turns):
        """checks answer against guess. Returns the number of turns remaining"""
        if guess > answer:
            print("숫자가 너무 큽니다.")
            return turns - 1
        elif guess < answer:
            print("숫자가 너무 작습니다.")
            return turns - 1
        else:
            print(f"정답입니다! 정답은 {answer}였습니다.")

    def set_difficulty():
        level = input("난이도를 고를 수 있습니다. '쉬움' or '어려움': ")
        if level == "쉬움":
            return easy_life
        else:
            return hard_life

    # 리스트에 담긴 결과값을 랜덤으로 선택해서 result에 할당
    # 쉬우면 목숨 10개
    # 어려우면 목숨 5개

    turns = set_difficulty()
    guess = 0
    while guess != answer:
        guess = int(input(f"목숨이 {turns}개 남았어요. 숫자를 맞춰보세요:"))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("숫자 맞추기에 실패했습니다~\n정답은 {answer}였습니다.")
            return


game()
