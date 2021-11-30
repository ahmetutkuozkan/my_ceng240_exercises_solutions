def get_phone_number(person):
    phone_dict = {"Jerry Seinfeld":"+1 960-454-6956",
                  "George Constanza":"+1 844-833-4965",
                  "Elaine Benes":"+1 543-920-5729",
                  "Cosmo Kramer":"+1 556-673-6702",
                  "Jim Halpert":"+1 867-767-7664",
                  "Pam Beesly":"+1 410-570-7381",
                  "Michael Scott":"+1 657-220-6601",
                  "Dwight Schrute":"+1 940-573-6702",
                  "Rachel Green":"+1 813-856-3347",
                  "Monica Geller":"+1 527-324-1403",
                  "Ross Geller":"+1 687-801-6781",
                  "Phoebe Buffay":"+1 208-702-5161",
                  "Joey Tribbiani":"+1 908-665-3975",
                  "Chandler Bing":"+1 444-970-5300"}

    return phone_dict[person]
def send_sms(number):
    # sends message #
    print("Message is successfully sent to " + number)
    return True

def send_bulk_sms(Names):
    for name_in_names in Names:
        try:
            send_sms(get_phone_number(name_in_names))
        except KeyError:
            print("Customer is not found in the phone book: "+name_in_names)

