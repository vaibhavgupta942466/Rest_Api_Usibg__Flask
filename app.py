from flask import Flask,jsonify,request,render_template


app = Flask(__name__,template_folder='templates')

courses = [
    {
        'id': 1,
        'name': 'Python',
        'price': 100
    },
    {
        'id': 2,
        'name': 'Java',
        'price': 200
    },
    {
        'id': 3,
        'name': 'C++',
        'price': 300
    },
    {
        'id': 4,
        'name': 'C#',
        'price': 400
    },
    {
        'id': 5,
        'name': 'Ruby',
        'price': 500
    }
]

# GET METHODS
@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        a = int(request.form['a'])
        if a < 0:
            return jsonify({
            'number': a,
            'result': 'Enter a positive number'
            })
        else:
            sum = 0
            for i in str(a):
                sum += int(i)**3
            if sum == a:
                return jsonify({
                    'number': a,
                    'result': 'Armstrong Number',\
                    'Armstrong Number': True
                    })
            else:
                return jsonify({
                    'number': a,
                    'result': 'Not an Armstrong Number',
                    'Armstrong Number': False
                    })
    return render_template('home.html')

@app.route('/courses')
def get_courses():
    return jsonify({'course': courses})

@app.route('/courses/<int:id>',methods=['GET'])
def get_course_by_id(id):
    return jsonify({'course': courses[id]})

@app.route('/aon/<int:a>',methods=['GET'])
def AoN(a):
    if a < 0:
        print("Enter a positive number")
    else:
        sum = 0
        for i in str(a):
            sum += int(i)**3
        if sum == a:
            return jsonify({
                'number': a,
                'result': 'Armstrong Number',\
                'Armstrong Number': True
                })
        else:
            return jsonify({
                'number': a,
                'result': 'Not an Armstrong Number',
                'Armstrong Number': False
                })


# POST METHODS
@app.route('/addcourse/' ,methods=['GET','POST'])
def add_course():
    if request.method == 'POST':
        course = {
            'id': courses[-1]['id'] + 1,
            'name': request.form['name'],
            'price': request.form['price']
        }
        courses.append(course)
        return jsonify({'course': course})
    return render_template('form.html')

# PUT METHODS
@app.route('/courses/<int:id>',methods=['PUT'])
def update_course(id):
    courses[id]['price'] = 100
    return jsonify({'course': courses})

# DELETE METHODS
@app.route('/courses/<int:id>',methods=['DELETE'])
def delete_course(id):
    courses.pop(id)
    return jsonify({'course': courses})

if __name__=="__main__":
    app.run(debug=True)