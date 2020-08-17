def getproducts():
  return products=[
    {"p_id":101,
    "p_category":"kitchen_appliance",
    "p_name":" 2 Slice Panni Grill Sandwich Maker Grill, Toast ",
    "brand":"nova",
    "price":1695,
    "image":"https://rukminim1.flixcart.com/image/352/352/k0sgl8w0/sandwich-maker/c/e/4/nova-2-slice-panni-grill-sandwich-maker-original-imafkgcmggv7me6p.jpeg?q=70"
    },
    {"p_id":102,
    "p_category":"kitchen_appliance",
    "p_name":" Delight PRWO - 1.0 Electric Rice Cooker",
    "brand":"prestige",
    "price":1270,
    "image":"https://rukminim1.flixcart.com/image/416/416/j7hxmkw0/electric-cooker/b/h/6/prestige-delight-prwo-1-0-delight-prwo-1-0-original-imaexq4d7dr3sngb.jpeg?q=70"
    },
    {"p_id":103,
    "p_category":"kitchen_appliance",
    "p_name":"IC 1800 W Induction Cooktop",
    "brand":"pigion",
    "price":1399,
    "image":"https://rukminim1.flixcart.com/image/416/416/induction-cook-top/5/c/k/pigeon-favourite-ic-1800-w-favourite-ic-1800-w-original-imaenreqhefzd63h.jpeg?q=70"
    },
    {"p_id":104,
    "p_category":"purifiers",
    "p_name":"LIV-PEP-PRO-PLUS+ 7 L RO + UV + UF Water Purifier",
    "brand":"livepure",
    "price":9299,
    "image":"https://rukminim1.flixcart.com/image/416/416/j13vqfk0/water-purifier/8/n/7/livpure-pep-pro-original-imaesrgs2c2gtyvh.jpeg?q=70"
    },
    {"p_id":105,
    "p_category":"kitchen_appliance",
    "p_name":" 300 700 W Pop Up Toaster (Red) 700 W Pop Up Toaster",
    "brand":"cello",
    "price":1149,
    "image":"https://rukminim1.flixcart.com/image/416/416/jx3kn0w0/pop-up-toaster/h/v/s/cello-300-700-w-pop-up-toaster-red-original-imafhkuhkadfashw.jpeg?q=70"
    },
    {"p_id":106,
    "p_category":"(SKT 180 ASE) Electric Kettle",
    "p_name":"kitchen_appliance",
    "brand":"singer aroma",
    "price":632,
    "image":"https://rukminim1.flixcart.com/image/416/416/joonafk0/electric-kettle/y/7/b/singer-skt-180-ase-original-imafb38vsehjzq2s.jpeg?q=70"
    },
    {"p_id":107,
    "p_category":"purifiers",
    "p_name":"Ace Plus 8 L RO + UV + UF + TDS Water Purifier",
    "brand":"kent",
    "price":12999,
    "image":"https://rukminim1.flixcart.com/image/416/416/jxjahe80/water-purifier/y/g/7/kent-ace-plus-original-imafhzawerdykpeh.jpeg?q=70"
    },
    {"p_id":108,
    "p_category":"home_appliances",
    "p_name":"Plus 1100 w Amaze NI 10 1100 W Dry Iron",
    "brand":"nova",
    "price":382,
    "image":"https://rukminim1.flixcart.com/image/416/416/jf8khow0/iron/8/w/c/nova-plus-1100-w-amaze-ni-10-original-imaf3qxpabhhdwss.jpeg?q=70"
    },
    {"p_id":109,
    "p_category":"air_conditioners",
    "p_name":"MIDIEA BT-07 400MM 400 mm 3 Blade Table Fan ",
    "brand":"bajaj",
    "price":1849,
    "image":"https://rukminim1.flixcart.com/image/416/416/k7w8eq80/fan/r/g/h/bt-07-55-table-fan-400-bajaj-original-imafqf6enkdzqh3c.jpeg?q=70"
    },
    {"p_id":110,
    "p_category":"home_appliances",
    "p_name":"Analog 30 cm X 30 cm Wall Clock",
    "brand":"ajanta",
    "price":599,
    "image":"https://rukminim1.flixcart.com/image/416/416/kb3z2q80/wall-clock/b/y/s/aj-black-white-aj-black-white-analog-ajanta-original-imafsj4cjb5fe4ey.jpeg?q=70"
    },
    {"p_id":111,
    "p_category":"air_conditioners",
    "p_name":" 1.5 Ton 3 Star Split AC - White  (183 DZZ (R-32)",
    "brand":"voltas",
    "price":29999,
    "image":"https://rukminim1.flixcart.com/image/416/416/jxm5d3k0/air-conditioner-new/q/3/c/183-dzz-r-32-1-5-split-fixed-speed-voltas-original-imafgf6nndarub2k.jpeg?q=70"
    },
    {"p_id":112,
    "p_category":"air_conditioners",
    "p_name":" 2 Ton 3 Star Split Dual Inverter AC",
    "brand":"LG",
    "price":52999,
    "image":"https://rukminim1.flixcart.com/image/416/416/jri3jww0/air-conditioner-new/h/j/g/ks-q18ynza-1-5-split-lg-original-imafd4jdzgpwqgyu.jpeg?q=70"
    },
]
def getproducts():
def createproducts():  
 print(f'''
  <div class="col-lg-4 col-md-6 col-sm-6 col-xs-12">
    <div class="card {product["p_category"]} style="width: 95%; height: 33rem; margun-bottom:20px; padding:10px">
    <img src="{product["image"]}" class="card-img-top" alt="...">
    <div class="card-body">
      <h5 class="card-title">{product["brand"]}{product["p_name"]}</h5>
      <p class="card-text">price:{product["price"]}</p>
      <a href="cart.py" class="btn btn-primary">add to cart</a>
    </div>
  </div>
</div>
''')  
def header():
    print('''
<html>
<head>
    <title>title</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">
    <link rel="stylesheet" href="../design.css">
    <style>
      .card-img-top{
        align-self:center;
      }
      .card img{
        width: 210px;
      }
      body{
        background-image: ("https://img.freepik.com/free-vector/abstract-blue-geometric-shapes-background_1035-17545.jpg?size=626&ext=jpg")
      }
    </style>
</head>
<body>
<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <a class="navbar-brand" href="index.py">onlineshop</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>

  <div class="collapse navbar-collapse" id="navbarSupportedContent">
    <ul class="navbar-nav mr-auto">
      <li class="nav-item active">
        <a class="nav-link" href="index.py">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item active">
        <a class="nav-link" href="#">all products</a>
      </li>
      <li class="nav-item dropdown">
        <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
          Dropdown
        </a>
        <div class="dropdown-menu" aria-labelledby="navbarDropdown">
          <a class="dropdown-item" href="#">Action</a>
          <a class="dropdown-item" href="#">Another action</a>
          <div class="dropdown-divider"></div>
          <a class="dropdown-item" href="#">Something else here</a>
        </div>
      </li>
      <li class="nav-item">
        <a class="nav-link " href="#" tabindex="-1" aria-disabled="true">my cart</a>
      </li>
    </ul>
    <form class="form-inline my-2 my-lg-0" action="search.py">
      <input name="q" class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
      <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
    </form>
  </div>
</nav>
''')
def footer():
    print('''
        <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js" integrity="sha384-OgVRvuATP1z7JjHLkuOU7Xw704+h835Lr+6QL9UvYjZE3Ipu6Tp75j7Bh/kR0JKI" crossorigin="anonymous"></script>
    </body>
    </html>
    ''')

