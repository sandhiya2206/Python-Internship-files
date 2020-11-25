Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> set1={100,200,300,400,500,600,700,800}
>>> set2={100,200,300,400,500,900}
>>> set3=set1.intersection(set2)
>>> set3
{100, 200, 300, 400, 500}
>>> set3.remove(500)
>>> set3
{100, 200, 300, 400}
>>> set3.remove(400)
>>> set3
{100, 200, 300}
>>> set3.remove(200)
>>> set3
{100, 300}
>>> set3.remove(300)
>>> set3
{100}
>>> set3.remove(100)
>>> set3
set()
>>> 