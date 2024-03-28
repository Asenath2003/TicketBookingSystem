while True:
    ticket_type = input("Enter the type of ticket (Silver/Gold/Diamond): ")

    if ticket_type == "Exit":
        print("Exiting..")
        break
    tickets = int(input("Enter the number of tickets: "))
    if ticket_type == "Silver":
        price = 50.00
    elif ticket_type == "Gold":
        price = 100.00
    elif ticket_type == "Diamond":
        price = 150.00
    else:
        print("Invalid option!!")
        continue

    total_cost = price * tickets
    print(f"Total cost for {tickets} {ticket_type} tickets: {total_cost:.2f}")
