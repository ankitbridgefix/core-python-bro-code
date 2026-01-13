def Outer(func):
    print("Call Outer Func:")
    def wrapper(*args, **kwargs):
        print("Befor Call Function")
        d =func(*args, **kwargs)
        print("After Call Function")
        return d.upper(),d.lower()

    return wrapper

@Outer
def upperCase(text):
    return text

print(upperCase("Helloankit"))



