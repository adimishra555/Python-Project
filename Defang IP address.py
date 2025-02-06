def ip_address(address):
    new_address=" "
    split_address=address.split(".")
    separator="[.]"
    new_address=separator.join(split_address)
    return new_address
ipaddress=ip_address("1.1.2.3")
print(ipaddress)


#------------------------------ To Find public IP address
import requests

def get_public_ip():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        ip_data = response.json()
        return ip_data['ip']
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    public_ip = get_public_ip()
    print(f"Your public IP address is: {public_ip}")
