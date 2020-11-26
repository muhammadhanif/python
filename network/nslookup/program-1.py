#
# @author       : Muhammad Hanif
# @email        : moehammadhanif@gmail.com
# @home page    : https://hanifmu.com
# @create date  : 2020-11-27 05:54:44
# @modify date  : 2020-11-27 05:54:44
#

from nslookup import Nslookup

domain = "hanifmu.com"
dns_servers = ["1.1.1.1"]

dns_query = Nslookup(dns_servers)

# A record lookup
ips_record = dns_query.dns_lookup(domain)

print(ips_record.response_full)
print(ips_record.answer)
