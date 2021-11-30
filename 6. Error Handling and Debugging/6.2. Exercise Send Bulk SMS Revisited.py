def get_phone_number(person):
    customers = ["Jerry Seinfeld","George Constanza","Elaine Benes","Cosmo Kramer",
                 "Jim Halpert","Pam Beesly","Michael Scott","Dwight Schrute",
                 "Rachel Green", "Monica Geller", "Ross Geller", "Phoebe Buffay",
                 "Joey Tribbiani", "Chandler Bing"]
    numbers = ["+1 960-454-6956", "+1 844-833-4965", "+1 543-920-5729", "+1 556-673-6702",
               "+1 867-767-7664", "+1 410-570-7381", "+1 657-220-6601", "+1 940-573-6702",
               "+1 813-856-3347", "+1 527-324-1403", "+1 687-801-6781", "+1 208-702-5161",
               "+1 908-665-3975", "+1 444-970-5300"]

    return numbers[customers.index(person)]

def send_sms(number):
    # sends message #
    print("Message is successfully sent to " + number)
    return True

def send_bulk_sms(Names):
    for name_in_names in Names:
        try:
            send_sms(get_phone_number(name_in_names))
        except ValueError:
            print("Customer is not found in the phone book: "+name_in_names)

