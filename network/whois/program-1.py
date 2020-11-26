#
# @author       : Muhammad Hanif
# @email        : moehammadhanif@gmail.com
# @home page    : https://hanifmu.com
# @create date  : 2020-11-26 07:44:03
# @modify date  : 2020-11-26 07:44:03
#

import whois

domain = whois.query('hanifmu.com')

print(domain.__dict__)
print()
print(domain.name)
print(domain.expiration_date)
