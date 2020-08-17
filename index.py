import base

products= base.getproducts()
base.header()

print('''
  <div class="container">
    <h1 class="text-center">products</h1>
    <hr>
    <div class="row">
''')
for product in products:
  base.createproducts()
print('''
    </div>
  </div>
''')
base.footer()