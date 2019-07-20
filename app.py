from flask import Flask, request
from connect import *
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/patientlist/<doctor_id>', methods = ['GET'])
def get_fetch_patient_list(doctor_id):
    list = select_patient_list(doctor_id)
    print(list)
    return json.dumps(list)



@app.route('/patientinfo/<patient_id>', methods = ['GET'])
def get_fetch_patient_info(patient_id):
    list = select_patient_info(patient_id)
    print(list)
    return json.dumps(list)


@app.route('/doctorinfo/<doctor_id>', methods = ['GET'])
def get_fetch_doctor_info(doctor_id):
    list = select_doctor_info(doctor_id)
    print(list)
    return json.dumps(list)



@app.route('/patientdoctorinfo/<patient_id>', methods = ['GET'])
def get_fetch_patient_doctor_info(patient_id):
    list = select_patient_doctor_info(patient_id)
    print(list)
    return json.dumps(list)


@app.route('/medicineInfo/<patient_id>', methods = ['GET'])
def get_fetch_medical_info(patient_id):
    list = select_medical_info(patient_id)
    print(list)
    return json.dumps(list)

@app.route('/lowpressurelist/<patient_id>', methods = ['GET'])
def get_fetch_lowpressure_list(patient_id):
    list = select_lowpressure_list(patient_id)
    print(list)
    return json.dumps(list)


@app.route('/highpressurelist/<patient_id>', methods = ['GET'])
def get_fetch_highpressure_list(patient_id):
    list = select_highpressure_list(patient_id)
    print(list)
    return json.dumps(list)


@app.route('/heartratelist/<patient_id>', methods = ['GET'])
def get_fetch_heartrate_list(patient_id):
    list = select_heartrate_list(patient_id)
    print(list)
    return json.dumps(list)



@app.route('/patientpassword', methods = ['POST'])
def get_fetch_patient_password_list():
    print(0)
    data = json.loads(request.data.decode('utf-8'))
    patient_id = data['id']
    password = data['password']
    return select_patient_password(patient_id, password)

@app.route('/doctorpassword', methods = ['POST'])
def get_fetch_doctor_password_list():
    data = json.loads(request.data.decode('utf-8'))
    doctor_id = data['id']
    password=data['password']
    return select_doctor_password(doctor_id, password)



@app.route('/register', methods = ['POST'])
def get_fetch_registerdata():
    # print(request.data.decode('utf-8'))
    list = json.loads(request.data.decode('utf-8'))
    print(list['id'])
    return ''


@app.route('/changeinfo', methods = ['POST'])
def get_change_patient_health_info():
    data = json.loads(request.data.decode('utf-8'))
    time = data['time']
    patient_id = data['id']
    heartrate = data['heartrate']
    highpressure = data['highpressure']
    lowpressure = data['lowpressure']
    return change_patient_health_info(time, patient_id, heartrate, highpressure, lowpressure)



@app.route('/insertmedicine', methods = ['POST'])
def insert_patient_medicine_info():
    data = json.loads(request.data.decode('utf-8'))
    patient_id = data['id']
    medicine = data['medicine']
    return add_patient_medicine(patient_id, medicine)

@app.route('/deletemedicinebyname', methods = ['POST'])
def delete_patient_medicine():
    data = json.loads(request.data.decode('utf-8'))
    patient_id = data['id']
    medicine = data['medicine_name']
    return delete_medicine_by_name(patient_id, medicine)


# deletemedicinebyname
@app.route('/addpatient', methods = ['POST'])
def add_patient_into_doctor_list():
    data = json.loads(request.data.decode('utf-8'))
    patient_id = data['patient_id']
    doctor_id = data['doctor_id']
    return add_patient(patient_id, doctor_id)


@app.route('/patientregister', methods = ['POST'])
def insert_into_patient_list():
    data = json.loads(request.data.decode('utf-8'))
    print(data)
    name = data['name']
    gender = data['gender']
    id = data['id']
    password = data['password']
    birthday = data['birthday']
    sickTime = data['sickTime']
    bloodType = data['bloodType']
    tel = data['tel']
    email = data['email']
    return register_patient(name, gender, id, password, birthday, sickTime, bloodType, tel, email)


@app.route('/doctorregister', methods = ['POST'])
def insert_into_doctor_list():
    data = json.loads(request.data.decode('utf-8'))
    print(data)
    name = data['name']
    gender = data['gender']
    id = data['id']
    password = data['password']
    birthday = data['birthday']
    professionalTime = data['professionalTime']
    tel = data['tel']
    email = data['email']
    return register_doctor(name, gender, id, password, birthday, professionalTime, tel, email)

if __name__ == '__main__':
    app.run()