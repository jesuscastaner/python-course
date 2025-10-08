# this is an example script
# it can run standalone or be imported

def favorite_food(food):
    print(f"Your favorite food is {food}")


def main():
    print("This is script1")
    favorite_food("pizza")
    print("Goodbye!")

# check if we are running this script directly
# if so, call the main() function
if __name__ == '__main__':
    main()
