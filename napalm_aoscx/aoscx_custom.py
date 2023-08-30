from aoscx import ArubaOSCXDriver
import napalm

#Custom class of type ArubaOSCXDriver
class CustomArubaOSCXDriver(ArubaOSCXDriver):
    #Custom Method to seach for mac addresses 
    def search_mac_addresses(self, *mac_addresses):
        mac_table = self.get_mac_address_table()

        #filter out only the mac addresses tat we are looing for and store in results variable
        results = [entry for entry in mac_table if entry['mac'] in mac_addresses and entry['interface_type'] == 'access']

        return results

    