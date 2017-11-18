question = input('')
answers = {'hi' : 'hello', 'hru' : 'best', 'buy' : 'good buy'}
def get_answer(question) :
    return answers [question]
print(get_answer(question)) 
while True:
    question = input('')
    print(get_answer(question))



