def cough_dec(func):
    def fun_wrapper():
#         Code before firing the function
        print("*Caugh*")
        func()
#         code after the function
        print("*Caugh*")
        print("--------------------------------------------------")
    return fun_wrapper

@cough_dec
def question():
    print("Can you give a discount?")

@cough_dec
def answer():
    print("It is only 50 Kenyan shillings only")
question()
answer()