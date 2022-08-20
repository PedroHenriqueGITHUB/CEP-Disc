from flask import *
import requests

server = Flask(__name__)

@server.route("/")
def input():
    return render_template("input.html")

@server.route("/get_cep", methods=["GET", "POST"])
def get_cep():
    cep = request.form["cep"]
    try:
        cep_json = requests.get("https://cep.awesomeapi.com.br/json/{}".format(cep)).json()
        adress = cep_json["address"]
        adress_name = cep_json["address_name"]
        adress_type = cep_json["address_type"]
        city = cep_json["city"] + "-" + cep_json["state"]
        city_ibge = cep_json["city_ibge"]
        ddd = cep_json["ddd"]
        district= cep_json["district"]
        lat = cep_json["lat"]
        lng = cep_json["lng"]
        return render_template("output.html", cep=cep, adress=adress, city=city, city_ibge=city_ibge, ddd=ddd, district=district, lat=lat, lng=lng)
    except:
        return render_template("erro.html", cep=cep)

server.run(debug=True)