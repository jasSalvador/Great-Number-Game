from flask import Flask, render_template, request, redirect, session
import random #importar numero aleatorio

app = Flask(__name__)
app.secret_key='secret' #llave session creada


random = random.randint(1, 100) #numero aleatorio entre 1 y 100

#ruta para el numero aleatorio/ guardar en sesion /imprimirlo/redirigir/ se usa metodo get para enviar el numero
@app.route('/', methods=['GET'])
def numero():
    if "random" not in session:
        session["random"] = random
    print(random)
    return render_template('index.html', adivina=None, random=random)


#ruta con la funcion a realizar cuando se ingrese un numero
@app.route('/adivinar', methods=['POST'])
def adivinar():

    if request.form['adivina'] == "":
        return render_template('index.html', adivina=None, random=random)

    else:
        adivina=int(request.form['adivina'])

        if adivina == random:
            print("win")
            return render_template("index.html", adivina=adivina, random=random)

        elif adivina > random:
            print("Too high")
            return render_template("index.html", adivina=adivina, random=random)


        elif adivina < random:
            print("Too low")
            return render_template("index.html", adivina=adivina, random=random)

        else:
            return render_template("index.html")



@app.route('/reset')
def reset():
    session.clear()
    return render_template('index.html', adivina=None, random=random)



if __name__=="__main__":
    app.run(debug=True)