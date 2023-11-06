import re
from robobrowser import RoboBrowser
print('123')
br = RoboBrowser()
br.open('https://college.astanait.edu.kz/login/index.php')
form = br.get_form()
form['username']='karakuzov'
form['password']='Kuanis2006$'
br.submit_form(form)
src=str(br.parsed())

