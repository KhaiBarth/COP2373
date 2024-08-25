#In this assignment, I am programming a ticket booth at a movie theater. There are 20 tickets, and the maximum amount per person is 4. I am making the code output how many purchases there are, and how many tickets remain until zero.
def sell_tickets():


    #This is the total number of tickets available for pre-sell.
    TOTAL_TICKETS = 20
    #Initializing formulas for the number of tickets and total buyers
    tickets_sold = 0
    number_of_buyers = 0

    while tickets_sold < TOTAL_TICKETS:
        #Calculate the remaining tickets purchased
        remaining_tickets = TOTAL_TICKETS - tickets_sold

        #Ask the user for the number of tickets they would like to buy, 4 being the max amount.
        try:
            desired_tickets = int(input(
               f"Tickets available: {remaining_tickets}. Enter how many tickets you would like to purchase. No more than 4 per purchase."
            ))

            #Check if the input is within the valid range of desired output
            if 1 <= desired_tickets <= 4:
                #ensure are enough tickets left
                if desired_tickets <= remaining_tickets:
                    #Update the number of tickets sold and the number of buyers until there are zero left
                    tickets_sold += desired_tickets
                    number_of_buyers += 1
                    print(f"Thank you! {desired_tickets} tickets purchased.")
                else:
                    print(f"Sorry, only {remaining_tickets} ticket(s) remaining.")
            else:
                print("Please enter between 1 and 4 tickets.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")

    #Display the total number of buyers
    print(f"All pre-sell tickets have sold.Totals: {number_of_buyers}")


#Run the ticket function
if __name__ == "__main__":
    sell_tickets()
