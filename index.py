from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def home():
    title = 'Home Cipriano Escorche'
    return render_template('home.html',active='home',title=title)


@app.route('/about')
def about():
     title = 'About Cipriano Escorche'
     return render_template('about.html', active='about',title=title)

@app.route('/cursos')
def cursos():
     title = 'Cursos Cipriano Escorche'
     return render_template('cursos.html', active='cursos',title=title)

@app.route('/projects')
def projects():
     title = 'Projects Cipriano Escorche'
     return render_template('projects.html',active='projects',title=title)


if __name__ == '__main__':
    app.run(debug=True)

