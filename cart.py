import base
import cgi
import json

form=cgi.FieldStorage()
p_id=form.getvalues("p_id")

file=open("../products.json")
products=json.load(file)
print(products)

base.header()

print('''
  <div class="container">
    <h1 class="text-center">products</h1>
    <hr>
    <div class="row">
''')

print('''
    </div>
  </div>
''')
base.footer()