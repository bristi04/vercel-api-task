import json
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all origins

# Imaginary data of marks for 100 students
students_marks = [{"name":"lZlSv","marks":22},{"name":"fUxKu","marks":80},{"name":"IDA27To","marks":92},{"name":"gB65","marks":70},{"name":"xzYQ3Zeki8","marks":90},{"name":"kKyLY","marks":92},{"name":"nj1o3N","marks":63},{"name":"hgv","marks":60},{"name":"3","marks":59},{"name":"Sm","marks":0},{"name":"g","marks":27},{"name":"3jnPwY9","marks":58},{"name":"m2dtRq","marks":70},{"name":"lqxPzbBBDy","marks":70},{"name":"wMwiMe","marks":61},{"name":"M5jTdaf1T2","marks":88},{"name":"XPcusAVFbH","marks":33},{"name":"q","marks":48},{"name":"3lF","marks":78},{"name":"DkObb5","marks":14},{"name":"6X8b0u4TF","marks":16},{"name":"A4mQSlwAW","marks":39},{"name":"70Y9","marks":0},{"name":"EVM9hT6JQ","marks":66},{"name":"u3qoW5hBB5","marks":6},{"name":"z18Z8lyi","marks":34},{"name":"5","marks":17},{"name":"R","marks":67},{"name":"GpwrT","marks":43},{"name":"QpVQ1Obn","marks":64},{"name":"ouIdNd","marks":63},{"name":"J0X","marks":55},{"name":"Vt","marks":37},{"name":"qh5bio","marks":96},{"name":"5NKwjvhO","marks":23},{"name":"UfVL","marks":91},{"name":"3RAq8","marks":67},{"name":"9OGwtq","marks":7},{"name":"4q","marks":66},{"name":"es","marks":21},{"name":"SBd1aOC","marks":62},{"name":"t","marks":3},{"name":"YP8oOGd6w","marks":5},{"name":"PL5H","marks":85},{"name":"HpOx","marks":18},{"name":"1b","marks":35},{"name":"tLMaGgLx","marks":38},{"name":"0","marks":84},{"name":"IOTD","marks":44},{"name":"up7sUO","marks":94},{"name":"lqrGyZ9D","marks":83},{"name":"oQngTQ","marks":32},{"name":"UwVEL","marks":17},{"name":"fkFmjVQ","marks":58},{"name":"vV8R8","marks":26},{"name":"B3QNtWAH","marks":77},{"name":"T1QIBoYgIo","marks":47},{"name":"axJ","marks":9},{"name":"sdCLG1","marks":0},{"name":"J","marks":88},{"name":"Qewu","marks":7},{"name":"wZ5CXTkcW1","marks":47},{"name":"UladiYBZ","marks":78},{"name":"j","marks":71},{"name":"2","marks":34},{"name":"CTBi","marks":24},{"name":"3xDRLmdJ","marks":46},{"name":"Ynwc5z","marks":35},{"name":"6btjrglz","marks":5},{"name":"F","marks":81},{"name":"AgBcet","marks":37},{"name":"WulfF9KmnV","marks":0},{"name":"QV","marks":96},{"name":"R0GuX","marks":88},{"name":"M","marks":16},{"name":"Ly4z64","marks":30},{"name":"3K","marks":3},{"name":"X","marks":71},{"name":"jGJlDmvuk","marks":64},{"name":"r20G","marks":64},{"name":"B0fa6l","marks":99},{"name":"Bt5st0gC8","marks":76},{"name":"8Gy4PrXQ5O","marks":18},{"name":"BTj","marks":39},{"name":"n6V4WG","marks":70},{"name":"LVw17CBcP","marks":96},{"name":"rP2","marks":52},{"name":"w6qW","marks":20},{"name":"MmUNbv6Fu","marks":56},{"name":"4rvAN","marks":42},{"name":"bEmJJ7m","marks":74},{"name":"Jd9IA","marks":21},{"name":"PKm","marks":94},{"name":"FcGPAi463","marks":53},{"name":"r2Vbd","marks":77},{"name":"Ry4","marks":74},{"name":"te","marks":16},{"name":"P6jp6P","marks":68},{"name":"q","marks":98},{"name":"6ei0CBZ","marks":24}]

@app.route('/api', methods=['GET'])
def get_marks():
    # Get the names from the query parameters
    names = request.args.getlist('name')
    
    # Retrieve the marks for each name
    marks = []
    for name in names:
        student = next((student for student in students_marks if student['name'] == name), None)
        if student:
            marks.append(student['marks'])
        else:
            marks.append('Student not found')
    
    # Return the marks in a JSON response
    return jsonify({'marks': marks})

if __name__ == '__main__':
    app.run(debug=True)

