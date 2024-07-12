def runMatch():
    num=int(input("enter the number between 1 and 6: "))

    match num:
        case 1 | 2:
            print("one or two")

        case 3 | 4:
            print("three or four")

        case 5 | 6:
            print("five or six")

        case _:
            print("number not between 1 to 6")

runMatch()