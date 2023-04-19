# Filename: main.py

from datetime import datetime  # import datetime for epoch time conversion

List3 = [{"Elevator": "HIRISE1","ReportTime": 1666529999,"DoorOpenTimesTotal": 2626,"DoorReversalsTotal": 159,"RunCountTotal":2819},{"Elevator": "HIRISE1","ReportTime": 1666616399,"DoorOpenTimesTotal": 2188,"DoorReversalsTotal": 116,"RunCountTotal": 2334},{"Elevator": "HIRISE1","ReportTime": 1666702799,"DoorOpenTimesTotal": 1971,"DoorReversalsTotal": 101,"RunCountTotal": 2062},{"Elevator": "HIRISE1","ReportTime": 1666789199,"DoorOpenTimesTotal": 1951,"DoorReversalsTotal": 94,"RunCountTotal":2094 ,},{"Elevator": "HIRISE1","ReportTime": 1666875599,"DoorOpenTimesTotal": 2302,"DoorReversalsTotal": 136,"RunCountTotal": 2471,},{"Elevator": "HIRISE1","ReportTime": 1666961999,"DoorOpenTimesTotal": 2289,"DoorReversalsTotal": 130,"RunCountTotal": 2446,},{"Elevator": "HIRISE1","ReportTime": 1667048399,"DoorOpenTimesTotal": 2091,"DoorReversalsTotal": 127,"RunCountTotal": 2276,},{"Elevator": "HIRISE2","ReportTime": 1666529999,"DoorOpenTimesTotal": 475,"DoorReversalsTotal": 38,"RunCountTotal":1316 ,},{"Elevator": "HIRISE2","ReportTime": 1666616399,"DoorOpenTimesTotal": 816,"DoorReversalsTotal": 67,"RunCountTotal": 1529,},{"Elevator": "HIRISE2","ReportTime": 1666702799,"DoorOpenTimesTotal": 952,"DoorReversalsTotal": 97,"RunCountTotal": 1620,},{"Elevator": "HIRISE2","ReportTime": 1666789199,"DoorOpenTimesTotal": 846,"DoorReversalsTotal": 88,"RunCountTotal":1506,},{"Elevator": "HIRISE2","ReportTime": 1666875599,"DoorOpenTimesTotal": 921,"DoorReversalsTotal": 103,"RunCountTotal": 1605,},{"Elevator": "HIRISE2","ReportTime": 1666961999,"DoorOpenTimesTotal":594,"DoorReversalsTotal": 94,"RunCountTotal": 1382,},{"Elevator": "HIRISE2","ReportTime": 1667048399,"DoorOpenTimesTotal": 0,"DoorReversalsTotal": 0,"RunCountTotal": 1093,},{"Elevator": "HIRISE3","ReportTime": 1666529999,"DoorOpenTimesTotal": 2702,"DoorReversalsTotal": 631,"RunCountTotal":2769 ,},{"Elevator": "HIRISE3","ReportTime": 1666616399,"DoorOpenTimesTotal": 2289,"DoorReversalsTotal": 387,"RunCountTotal": 2352,},{"Elevator": "HIRISE3","ReportTime": 1666702799,"DoorOpenTimesTotal": 1966,"DoorReversalsTotal": 279,"RunCountTotal": 2147,},{"Elevator": "HIRISE3","ReportTime": 1666789199,"DoorOpenTimesTotal": 2075,"DoorReversalsTotal": 291,"RunCountTotal":2215 ,},{"Elevator": "HIRISE3","ReportTime": 1666875599,"DoorOpenTimesTotal": 1757,"DoorReversalsTotal": 284,"RunCountTotal": 1958,},{"Elevator": "HIRISE3","ReportTime": 1666961999,"DoorOpenTimesTotal":2366,"DoorReversalsTotal": 418,"RunCountTotal": 2563,},{"Elevator": "HIRISE3","ReportTime": 1667048399,"DoorOpenTimesTotal": 2292,"DoorReversalsTotal": 455,"RunCountTotal": 2531,},{"Elevator": "LORISE1","ReportTime": 1666529999,"DoorOpenTimesTotal": 26,"DoorReversalsTotal": 1,"RunCountTotal":21 ,},{"Elevator": "LORISE1","ReportTime": 1666616399,"DoorOpenTimesTotal": 404,"DoorReversalsTotal": 6,"RunCountTotal": 373,},{"Elevator": "LORISE1","ReportTime": 1666702799,"DoorOpenTimesTotal": 489,"DoorReversalsTotal": 7,"RunCountTotal": 448,},{"Elevator": "LORISE1","ReportTime": 1666789199,"DoorOpenTimesTotal": 461,"DoorReversalsTotal": 4,"RunCountTotal":429 ,},{"Elevator": "LORISE1","ReportTime": 1666875599,"DoorOpenTimesTotal": 449,"DoorReversalsTotal": 11,"RunCountTotal": 403,},{"Elevator": "LORISE1","ReportTime": 1666961999,"DoorOpenTimesTotal":516,"DoorReversalsTotal": 11,"RunCountTotal": 456,},{"Elevator": "LORISE1","ReportTime": 1667048399,"DoorOpenTimesTotal": 25,"DoorReversalsTotal": 1,"RunCountTotal": 18,},{"Elevator": "LORISE2","ReportTime": 1666529999,"DoorOpenTimesTotal": 60,"DoorReversalsTotal": 0,"RunCountTotal":44 ,},{"Elevator": "LORISE2","ReportTime": 1666616399,"DoorOpenTimesTotal": 378,"DoorReversalsTotal":11,"RunCountTotal": 313,},{"Elevator": "LORISE2","ReportTime": 1666702799,"DoorOpenTimesTotal": 294,"DoorReversalsTotal": 9,"RunCountTotal": 232,},{"Elevator": "LORISE2","ReportTime": 1666789199,"DoorOpenTimesTotal": 429, "DoorReversalsTotal": 20,"RunCountTotal":352 ,},{"Elevator": "LORISE2","ReportTime": 1666875599,"DoorOpenTimesTotal": 299,"DoorReversalsTotal": 9,"RunCountTotal": 245,},{"Elevator": "LORISE2","ReportTime": 1666961999,"DoorOpenTimesTotal":404,"DoorReversalsTotal": 10,"RunCountTotal": 319,},{"Elevator": "LORISE2","ReportTime": 1667048399,"DoorOpenTimesTotal": 150,"DoorReversalsTotal": 5,"RunCountTotal": 116,},]

AlarmList = [{"Elevator": "LORISE1","ReportTime": 1666701000,"Type": "Stop",},{"Elevator": "HIRISE1","ReportTime": 16667041000,"Type": "Stop",},{"Elevator": "HIRISE2","ReportTime": 16667041000,"Type": "SlowDoor",},]

ElevatorWatch = {"LORISE1", "LORISE2"}


def elevator_id_list():  # menu item 1
    elevator_id_set = set()  # create an empty set to store unique elevator IDs
    for daily_report in List3:  # iterate through each report in the list
        elevator_id_set.add(daily_report["Elevator"])  # add the elevator ID to the set
    print(sorted(elevator_id_set))  # display the unique elevator IDs in alphabetical order


def elevator_list_with_runs():  # menu item 2
    for daily_report in List3:  # iterate through each report in the list
        date = daily_report["ReportTime"]  # store the epoch time in a variable
        datetime_obj = datetime.fromtimestamp(date)  # convert the date to a readable timestamp
        datetime_string = datetime_obj.strftime("%m-%d-%Y")  # format the timestamp to mm/dd/yyy
        print(daily_report["Elevator"], " ", datetime_string, " ", daily_report["RunCountTotal"])  # display the elevator ID, date, and run total for each report


def elevator_total_runs_7_days():  # menu item 3
    weekly_total = dict()  # create an empty dictionary to store 7-day run totals for each elevator
    for daily_report in List3:  # iterate through each report in the list
        if daily_report["Elevator"] in weekly_total:  # check if the elevator is already in the dictionary
            weekly_total[daily_report["Elevator"]] += daily_report["RunCountTotal"]  # increment the elevator's 7-day run total
        else:  # elevator is not yet in the dictionary
            weekly_total[daily_report["Elevator"]] = daily_report["RunCountTotal"]  # add the elevator and its initial run count to the dictionary
    for key in weekly_total.keys():  # iterate through each elevator in the dictionary
        print(key, weekly_total[key])  # print the elevator and its 7-day run total


def elevator_date_excessive_reversals():  # menu item 4
    for daily_report in List3:  # iterate through each report in the list
        elevator_id = daily_report["Elevator"]  # store the elevator ID in a variable
        date = daily_report["ReportTime"]  # store the epoch time in a variable
        datetime_obj = datetime.fromtimestamp(date)  # convert the date to a readable timestamp
        datetime_string = datetime_obj.strftime("%m-%d-%Y")  # format the timestamp to mm/dd/yyy
        reversals = daily_report["DoorReversalsTotal"]  # store the total door reversals in a variable
        openings = daily_report["DoorOpenTimesTotal"]  # store the total door opens in a variable
        if openings == 0:  # check if it had zero openings
            continue  # ensure there are no "divide by zero" errors by ignoring reports with 0 openings
        else:
            percent_reversals = reversals / openings * 100  # calculate the percent reversals
            if percent_reversals > 10:  # check if percent reversals is greater than 10
                print(elevator_id, " ", datetime_string, " ", reversals, "/", openings, "=", round(percent_reversals, 1), "%")  # display the elevator ID, date, and reversals for each report


def check_watch_list():  # menu item 5
    set_less = set()  # create an empty set to store unique elevator IDs from reports with less than 100 runs
    set_stop = set()  # create an empty set to store unique elevator IDs from reports with a Stop alarm
    for daily_report in List3:  # iterate through each report in the list
        if daily_report["RunCountTotal"] < 100:  # check if total runs is less than 100
            set_less.add(daily_report["Elevator"])  # add the elevator ID to set_less
    for daily_report in AlarmList:  # iterate through each report in the list
        if daily_report["Type"] == "Stop":  # check if there was a Stop alarm
            set_stop.add(daily_report["Elevator"])  # add the elevator ID to set_stop
    set_matches_all = set_less & set_stop & ElevatorWatch  # create a set of unique elevator IDs that appear in all three sets
    print("Less than 100 runs =", sorted(set_less))  # display alphabetical list of elevator IDs in set_less
    print("Stop alarm =",  sorted(set_stop))  # display alphabetical list of elevator IDs in set_stop
    print("Watch list =", sorted(ElevatorWatch))  # display alphabetical list of elevator IDs in ElevatorWatch
    print("Matches all criteria = ", sorted(set_matches_all))  # display alphabetical list of elevator IDs in set_matches_all


def exit_program():  # menu item 0
    print("---\nPROGRAM CLOSED\n---")  # display a message confirming exit


def display_the_menu():  # display the menu
    print("---\nMENU\n---")
    print("1. Elevator List")
    print("2. Elevator List with Runs")
    print("3. Elevator Total Runs 7 days")
    print("4. Elevator Date when Excessive Reversals")
    print("5. Check Watch List with Alarms or Runs < 100")

    menu_selection = input("Enter Request (0 to Exit): ")  # take menu selection

    while not menu_selection.isdigit():  # show error message until entry is a digit
        menu_selection = input("Entry not valid. Please select from the menu: ")

    while float(menu_selection) < 0 or float(menu_selection) > 5:  # show error message until entry is a number between 0 and 5
        menu_selection = input("Entry not valid. Please select from the menu: ")

    while float(menu_selection) % 1 != 0:  # show error message until entry is a whole number
        menu_selection = input("Entry not valid. Please select from the menu: ")

    run_menu_item_function(menu_selection)  # run the function for that menu item


def run_menu_item_function(menu_selection):  # run function based on menu selection
    if menu_selection == '1':
        elevator_id_list()

    elif menu_selection == '2':
        elevator_list_with_runs()

    elif menu_selection == '3':
        elevator_total_runs_7_days()

    elif menu_selection == '4':
        elevator_date_excessive_reversals()

    elif menu_selection == '5':
        check_watch_list()

    if menu_selection == "0":
        exit_program()

    else:
        loop_the_menu()  # offer to re-display menu or exit


def loop_the_menu():

    x = input("Press 'm' for Menu or '0' to Exit: ")  # take input to re-display menu or exit

    while x != 'm' and x != '0':
        x = input("Press 'm' for Menu or '0' to Exit: ")  # show error message for invalid entry

    if x == 'm':
        display_the_menu()  # re-display the menu

    if x == '0':
        exit_program()  # exit the program


display_the_menu()  # display the menu to start the program



# Test Case 1:
# Enter '12' as the menu item selection
# Expected result: Shows invalid entry message
# Actual result: Shows invalid entry message
# Pass

# Test Case 2:
# Select menu item 2
# Expected result: The first line of data is 'HIRISE1  10-23-2022  2819'
# Actual result: The first line of data is 'HIRISE1  10-23-2022  2819'
# Pass

# Test Case 3:
# Select menu item 5
# Expected result: LORISE1 is the only elevator that matches all criteria
# Actual result: LORISE1 is the only elevator that matches all criteria
# Pass
