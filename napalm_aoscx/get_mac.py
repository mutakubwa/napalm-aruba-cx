import getpass
from aoscx_custom import CustomArubaOSCXDriver

#fnction to connect to switch by definition of driver details
def connect_to_switch(hostname, username, password ):
    driver = CustomArubaOSCXDriver(hostname=hostname, username=username, password=password)
    driver.open()
    return driver

#main method
def main():
    department_switches = {
        'HR': ['SW1','SW2'],
        'Finance': ['SW3','SW4'],
    }

    department = input("Enter a department (options: HR,Finance)")
    switches = department_switches.get(department,[])

    if not switches:
        print("unknown Department:")
        return
    
    username = input("Enter Switch username: ")# Get user input for username
    password = getpass.getpass("Enter password for user: ")# Get user input for password without displaying it

    mac_addresses = input("Enter mac addresses separated by commas: ").split(',')# Get MAC addresses to search for comma separated

    #connect to switch with details retrieved from user
    for switch in switches:
        connection  = connect_to_switch(switch, username, password)
        results = connection.search_mac_addresses(*mac_addresses)
        if results:
            print(f"In Switch {switch}, found mac addresses on: ")
            for entry in results:
                print(f" - interface{entry{interface}}")
        connection.close()


if __name__ == "__main__":
    main()


    
