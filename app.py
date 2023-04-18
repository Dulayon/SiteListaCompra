from flask import Flask , request ,render_template
from Lista_compra import Lista


app = Flask(__name__)

def salvar():
	txt = open("Lista_compra.py","w")
	txt.write(f"Lista = {Lista}")
	txt.close()


@app.route("/")
def pagina_inicial():
	em_processo = False
	if len(Lista) == False:
		em_processo = True
	return render_template("inicial.html",lista=Lista,ativo=em_processo)
	
@app.route("/registrar",methods=["GET","POST"])
def registro():
	output = request.form.to_dict()
	saida = list(output.values())[0]
	Lista.append(saida)
	salvar()
	return render_template("inicial.html",lista=Lista)
	
@app.route("/atualizar",methods=["GET","POST"])
def ver():
	em_processo = False
	output = request.form.to_dict()
	for x in list(output.keys()):	
		Lista.remove(x)
		salvar()
	if len(Lista) == False:
		em_processo = True
	return render_template("inicial.html",lista=Lista,ativo=em_processo)
	
app.run(debug=True)
