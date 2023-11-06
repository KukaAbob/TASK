import re
import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property
from robobrowser import RoboBrowser

br = RoboBrowser()
br.open('https://college.astanait.edu.kz/login/index.php')
form = br.get_form()
form['username']='karakuzov'
form['password']='Kuanis2006$'
br.submit_form(form)
src=str(br.parsed())
start='<h6 class="mb-0 pt-2">'
end ='</h6> </div>'
