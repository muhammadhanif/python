#
# @author       : Muhammad Hanif
# @email        : moehammadhanif@gmail.com
# @home page    : https://hanifmu.com
# @create date  : 2020-11-26 08:02:51
# @modify date  : 2020-11-26 08:02:51
#

import pydig

# CNAME record lookup
print(pydig.query('www.hanifmu.com', 'CNAME'))
