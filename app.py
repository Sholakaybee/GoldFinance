from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Remote',
        'salary': '$60,000'
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Remote'
    },
    {
        'id': 3,
        'title': 'Frontend Engineer',
        'location': 'Remote',
        'salary': '$65,000'
    },
    {
        'id': 4,
        'title': 'Backend Engineer',
        'location': 'Remote',
        'salary': '$75,000'
    }
]

@app.route("/")
def home():
    return render_template('home.html', jobs=JOBS)


if __name__ == '__main__':
    app.run(debug=True)