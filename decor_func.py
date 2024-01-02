def decor(func):
    def wrap():
        print("============")
        func()
        print("============")
    return wrap
#We use the @ operator above the function which we want to use a decorator function
@decor
def print_text():
    print("Hello world!")

print_text();

#our function replacing the variable containing the function with a wrapped version.
# https://chat.openai.com/share/06da35be-6c73-4758-b73e-4498241c57cb
