# Jacob Novak
# DataMan - prototype - M4
# 11/24/2026

import logic

def main():

    choice = ""

    while choice != "3":

        print("\nWelcome to DataMan!")
        print("Let's have some fun with numbers!")

        print("\nPlease Select from the following Menu")
        print("1) Complete Activity")
        print("2) View Progress")
        print("3) Quit")

        choice = input("Choice?: ")

        if choice == "1":

            learner = input("Learner ID: ")
            activity = input("Activity ID: ")

            logic.complete_activity(learner, activity)

            print("Activity Complete!")

        elif choice == "2":

            learner = input("Learner ID: ")

            progress = logic.view_progress(learner)

            print("\nCompleted Activities")

            for activity in progress:
                print(activity)

        elif choice == "3":
            print("Goodbye!")


if __name__ == "__main__":
    main()
