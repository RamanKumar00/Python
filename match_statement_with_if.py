def rumMatch():
    num=int(input("enter a number: "))

    match num:

      case num if num>0:
        print("positive")

      case num if num<0:
        print("negative")

      case _:
        print("zero")

rumMatch()
