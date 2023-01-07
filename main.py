import app.comments


def run():
    my_string = "apples, pears # and bananas\ngrapes\nbananas !apples"
    my_list = ["#", "!"]
    r = app.comments.strip_comments(my_string, my_list)
    print(r)


if __name__ == '__main__':
    run()