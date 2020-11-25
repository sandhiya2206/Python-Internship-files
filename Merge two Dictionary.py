Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> MobilesDictionary1={1001:"iphone",1002:"SamsungGalaxy"}
>>> MobilesDictionary2={1003:"Lenovo",1004:"LG Mobile"}
>>> MobilesDictionary1
{1001: 'iphone', 1002: 'SamsungGalaxy'}
>>> MobilesDictionary2
{1003: 'Lenovo', 1004: 'LG Mobile'}
>>> MobilesDictionary1.update(MobilesDictionary2)
>>> MobilesDictionary1
{1001: 'iphone', 1002: 'SamsungGalaxy', 1003: 'Lenovo', 1004: 'LG Mobile'}
>>> dic1={1:"one",2:"two"}
>>> dic2={3:"three",4:"four"}
>>> dic3={**dic1,**dic2}
>>> dic3
{1: 'one', 2: 'two', 3: 'three', 4: 'four'}
>>> 