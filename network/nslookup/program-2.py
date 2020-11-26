#
# @author       : Muhammad Hanif
# @email        : moehammadhanif@gmail.com
# @home page    : https://hanifmu.com
# @create date  : 2020-11-27 05:59:15
# @modify date  : 2020-11-27 05:59:15
#

from nslookup import Nslookup

domain = "hanifmu.com"
dns_servers = ["1.1.1.1"]

dns_query = Nslookup(dns_servers)

# SOA record lookup
soa_record = dns_query.soa_lookup(domain)

print(soa_record.response_full)
print(soa_record.answer)
