class IP_Address:
    def __init__(self, ip_address: str, CIDR_range: int):
        self.ip_address = ip_address
        self.CIDR_range = CIDR_range
        self.IP_as_bits = self.ip_address_to_bits(ip_address)
        self.mask = self.sub_net_mask()

    # Convert IP address in the form e.g. "192.168.2.1" to bits, e.g. "11000000101010000000001000000001"
    def ip_address_to_bits(self, ip_address: str):
        pass

    # Get the subnet mask in bits from the CIDR range, e.g. 24 -> "11111111111111111111111100000000"
    def sub_net_mask(self):
        pass

    # Perform a bitwise AND operation on two strings of bits, e.g. "11000000101010000000001000000001" and "11111111111111111111111100000000"
    def bitwise_and(self, bits1: str, bits2: str):
        pass

    # Get the network address from the given IP address and CIDR range as bit stream
    def network_address(self):
        pass

    # Transform a given bit stream to a human-readable (e.g. decimal representation) IP address
    def bits_to_ip_address(self, bits: str):
        pass

    # Check if a given IP address is in the same range as the current IP address. The other IP address is given in decimal format
    def is_ip_in_own_range(self, other_ip_address: str):
        pass


if __name__ == "__main__":
    ip_address = IP_Address("192.168.2.1", 24)
    print(ip_address.is_ip_in_own_range("192.168.2.12"))  # True
    print(ip_address.is_ip_in_own_range("10.2.1.4"))  # False