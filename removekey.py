Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> customer_details={"cid":1122,"cname":"sandhiya","caddress":"chennai"}
>>> del customer_details["cname"]
>>> customer_details
{'cid': 1122, 'caddress': 'chennai'}
>>> del customer_details["caddress"]
>>> customer_details
{'cid': 1122}
>>> students_dic={1001:"Raju",1002:"Ramya",1003:"sandhiya",1004:"nandhini",1005:"gomathi"}
>>> students_dic
{1001: 'Raju', 1002: 'Ramya', 1003: 'sandhiya', 1004: 'nandhini', 1005: 'gomathi'}
>>> del students_dic[1003]
>>> students_dic
{1001: 'Raju', 1002: 'Ramya', 1004: 'nandhini', 1005: 'gomathi'}
>>> 