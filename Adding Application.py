#This program calls the adding_report() function which repeatedly takes positive integer input until the user quits and then sums the integers and prints a "report".
#The adding_report() function has 1 string parameter which indicates the type of report:
#"A" used as the argument to adding_report() results in printing of all of the input integers and the total
#"T" used as the argument results in printing only the total

def adding_report(report_type = "T"):
    total = 0
    items = ""
    while True:
        report_request = input ("Enter and integer or Q to quit: ")
        if report_request.isdigit():
            total += int(report_request)
            if report_type.startswith ("A"):
                items = items + "\n" + report_request
        elif report_request.upper().startswith("Q"):
            if report_type.startswith("A"):
                print ("\nItems:\n",items,"\n\nTotal:\n\n",total)
                break
            else:
                print ("\n\nTotal:\n\n",total)
                break
        else:
            print("Invalid input")
            
#Report choice
while True:
    report_type = input ("Choose report type A/T: ").upper()
    if report_type == "A":
        break
    elif report_type == "T":
        break
    else:
        print("Wrong report type")

adding_report(report_type)
