from OOP.diarys.Diary import Diary


def inputs(prompt):
    return inputs(prompt)


def print_output(prompt):
    print(prompt)


def main_app():
    Diary("Timi", "1111")

    display = """
            Welcome To App By TIMI
            Diary Display Icon...
            1 --> Create Diary
            2 --> Lock Diary
            3 --> Unlock Diary
            4 --> Find Entry By Id
            5 --> Add Entry
            6 --> Update Entry
            7 --> Delete Entry
            8 --> Exit App
            """
    choice = inputs(display + "Enter your choice: ")

    if choice == '1':
        create_diary()
    elif choice == '2':
        lock_diary()
    elif choice == '3':
        unlock_diary()
    elif choice == '4':
        find_entry_by_id()
    elif choice == '5':
        create_entry()
    elif choice == '6':
        update_entry()
    elif choice == '7':
        delete_entry()
    elif choice == '8':
        exit_app()
    else:
        main_app()


def delete_entry():
    Id = inputs("Kindly Enter The Unique Id Of The Entry: ")
    try:
        entry_id = int(Id)
        new_user.delete_entry(entry_id)
        print_output("Entry deleted successfully.")
    except ValueError:
        print_output("Invalid entry ID. Please enter a valid number.")
    except Exception as e:
        print_output(str(e))
    finally:
        main_app()


def update_entry():
    Id = inputs("Kindly Edit The Unique Id Of The Entry: ")
    title = inputs("Kindly Edit The Title Of The Entry: ")
    body = inputs("Kindly Edit The Body Of The Entry: ")
    try:
        entry_id = int(Id)
        new_user.update_entry(entry_id, title, body)
        print_output("Entry updated successfully.")
    except ValueError:
        print_output("Invalid entry ID. Please enter a valid number.")
    except Exception as e:
        print_output(str(e))
    finally:
        main_app()


def create_entry():
    Id = inputs("Kindly Enter The Unique Id Of The Entry: ")
    title = inputs("Kindly Enter The Title Of The Entry: ")
    body = inputs("Kindly Enter The Body Of The Entry: ")
    try:
        entry_id = int(Id)
        new_user.create_entry(entry_id, title, body)
        print_output("Entry created successfully.")
    except ValueError:
        print_output("Invalid entry ID. Please enter a valid number.")
    except Exception as e:
        print_output(str(e))
    finally:
        main_app()


def find_entry_by_id():
    Id = inputs("Kindly Enter The Unique Id Of The Entry: ")
    try:
        entry_id = int(Id)
        entry = new_user.find_entry(entry_id)
        print_output("Entry found successfully: \nTitle: {}\nBody: {}".format(entry['title'], entry['body']))
    except ValueError:
        print_output("Invalid entry ID. Please enter a valid number.")
    except Exception as e:
        print_output(str(e))
    finally:
        main_app()


def lock_diary():
    password = inputs("Enter password To Lock Diary: ")
    try:
        new_user.lock_diary(password)
        print_output("Diary locked successfully.")
    except Exception as e:
        print_output(str(e))
    finally:
        main_app()


def unlock_diary():
    password = inputs("Enter password To Unlock Diary: ")
    try:
        new_user.unlock_diary(password)
        print_output("Diary unlocked successfully.")
    except Exception as e:
        print_output(str(e))
    finally:
        main_app()


def create_diary():
    username = inputs("Kindly Enter A username Of Your Choice: ")
    password = inputs("Kindly Enter A password Of Your Choice: ")
    try:
        global new_user
        new_user = Diary(username, password)
        print_output("Diary Create successfully.")
    except Exception as e:
        print_output(str(e))
    finally:
        main_app()


def exit_app():
    print_output("Thanks for using App By TIMI")
    quit()


if __name__ == "__main__":
    main_app()
