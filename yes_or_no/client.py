from yes_or_no.game import Game
from yes_or_no.game_result import GameResult
from yes_or_no.game_status import GameStatus


def end_of_game_handler(result: GameResult):
    print(f'Questions asked: {result.questions_passed}. Mistakes made:{result.mistakes_made}')
    print(f'You won!' if result.won else 'You lost!')


game = Game('..\\yes_or_no\\data\\Questions.csv', end_of_game_handler, allowed_mistakes=3)

while game.game_status == GameStatus.IN_PROGRESS:
    # if game.is_last_question():
    #     print('no more question')
    #     break

    q = game.get_next_question()
    print('Do you believe in the next statement or question? Enter "y" or "n"')
    print(q.text)

    answer = input() == 'y'

    if q.is_true == answer:
        print('Good job! You are right!')
    else:
        print('Oops, actually you are mistaken. Here is the explanation:')
        print(q.explanation)

    game.give_answer(answer)
