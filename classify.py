NOT_FIT = 1         # кандидатка не подходит
FIT = 2             # кандидатка подходит


def classify(X):
    answer = 0
    iq_level, articles_count, has_education, ratio = X

    # TODO: пользуясь информацией, выведенной на экран в процессе построения
    # дерева решений, запрограммируте классификатор, реализующий логику
    # дерева решений. Используйте для этого простые конструкции if-elif-else, а также
    # конструкции if-elif-else, вложенные одна в другую там, где это необходимо.
    # Пример:
    # if iq_level <= 70:
    #     answer = NOT_FIT
    # else:
    #     ...

    if iq_level <= 70:
        answer = NOT_FIT
    else:
        if articles_count <= 5:
            if has_education == 1:
                answer = FIT
            else:
                answer = NOT_FIT
        else:
            if ratio <= 0.1:
                answer = NOT_FIT
            else:
                answer = FIT

    return answer
