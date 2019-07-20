import pymysql
# conn = pymysql.connect(host='127.0.0.1', user='root', passwd="wu*ke225", db='testDB')
# conn.close()
lock = False
import time

def select_patient_list(doctor_id):
    conn = pymysql.connect(host='127.0.0.1', user='root', passwd="wu*ke225", db='testDB')
    cur = conn.cursor()
    print('doctor-id' +doctor_id)
    # cur.execute("USE testDB")
    cur.execute("SELECT * FROM patient_list WHERE doctor_id='{}'".format(doctor_id))
    # cur.execute("SELECT * FROM patient_list WHERE doctor_id='wuxinke'")
    list = []
    for r in cur:
        print(r)
        list.append({
            "name": r[0],
            "gender": int.from_bytes(r[1], byteorder='big'),
            "patient_id": r[2],
            "password": r[3],
            "birthday": r[4].strftime("%Y-%m-%d"),
            "sick_time": r[5].strftime("%Y-%m-%d"),
            "doctor_id": r[6],
            "tel": r[7],
            "email": r[8],
            "blood_type": r[9]

        })

    # print('list' + list[0])
    cur.close()
    conn.close()
    return list



def select_patient_info(patient_id):
    conn = pymysql.connect(host='127.0.0.1', user='root', passwd="wu*ke225", db='testDB')
    cur = conn.cursor()
    # cur.execute("USE testDB")
    cur.execute("SELECT * FROM patient_list WHERE patient_id='{}'".format(patient_id))
    list = []
    for r in cur:
        # print(r)
        list.append({
            "name": r[0],
            "gender": int.from_bytes(r[1], byteorder='big'),
            "patient_id": r[2],
            "password": r[3],
            "birthday": r[4].strftime("%Y-%m-%d"),
            "sick_time": r[5].strftime("%Y-%m-%d"),
            "doctor_id": r[6],
            "tel": r[7],
            "email": r[8],
            "blood_type": r[9]

        })

    cur.close()
    conn.close()
    return list



def select_doctor_info(doctor_id):
    conn = pymysql.connect(host='127.0.0.1', user='root', passwd="wu*ke225", db='testDB')
    cur = conn.cursor()
    # cur.execute("USE testDB")
    cur.execute("SELECT * FROM doctor_list WHERE doctor_id='{}'".format(doctor_id))
    list = []
    for r in cur:
        # print(r)
        list.append({
            "name": r[0],
            "gender": int.from_bytes(r[1], byteorder='big'),
            "doctor_id": r[2],
            "password": r[3],
            "birthday": r[4].strftime("%Y-%m-%d"),
            "professional_time": r[5].strftime("%Y-%m-%d"),
            "tel": r[6],
            "email": r[7]

        })

    cur.close()
    conn.close()
    return list


def select_medical_info(patient_id):
    conn = pymysql.connect(host='127.0.0.1', user='root', passwd="wu*ke225", db='testDB')
    # global lock
    # while lock == True:
    #     print(patient_id, 'medicalinfo')
    #     time.sleep(100)
    # lock = True
    cur = conn.cursor()
    cur.execute("SELECT medicine_name FROM medicine_list WHERE medicine_id IN (SELECT medicine_id FROM relationship_pat_medicine WHERE patient_id='{}')".format(patient_id)),
    list = []
    for r in cur:
        list.append({
            "medicine_name": r[0]
        })
    cur.close()
    conn.close()
    # lock = False
    return list


def select_lowpressure_list(patient_id):
    conn = pymysql.connect(host='127.0.0.1', user='root', passwd="wu*ke225", db='testDB')
    # global lock
    # while lock == True:
    #     print(patient_id, 'lowpressure')
    #     time.sleep(100)
    # lock = True
    cur = conn.cursor()
    cur.execute("SELECT lowpressure FROM pressure_heartrate_list WHERE patient_id='{}'".format(patient_id))
    print(cur)
    list = []
    for r in cur:
        list.append({
            "low_pressure": r[0]
        })
    cur.close()
    conn.close()
    # lock = False
    return list


def select_highpressure_list(patient_id):
    conn = pymysql.connect(host='127.0.0.1', user='root', passwd="wu*ke225", db='testDB')
    cur = conn.cursor()
    cur.execute("SELECT highpressure FROM pressure_heartrate_list WHERE patient_id='{}'".format(patient_id))
    print(cur)
    list = []
    for r in cur:
        list.append({
            "high_pressure": r[0]
        })
    cur.close()
    conn.close()
    return list

def select_heartrate_list(patient_id):
    conn = pymysql.connect(host='127.0.0.1', user='root', passwd="wu*ke225", db='testDB')
    cur = conn.cursor()
    cur.execute("SELECT heartrate FROM pressure_heartrate_list WHERE patient_id='{}'".format(patient_id))
    print(cur)
    list = []
    for r in cur:
        list.append({
            "heartrate": r[0]
        })
    cur.close()
    conn.close()
    return list


def select_patient_password(patient_id, password):
    conn = pymysql.connect(host='127.0.0.1', user='root', passwd="wu*ke225", db='testDB')
    cur = conn.cursor()
    cur.execute("SELECT password FROM patient_list WHERE patient_id='{}'".format(patient_id))
    # cur.execute("SELECT password FROM patient_list WHERE patient_id='c'")
    print(12)
    for r in cur:
        print(2)
        if r[0]==password:
            print(r[0])
            cur.close()
            conn.close()
            return '1'
    cur.close()
    conn.close()
    return '0'


def select_doctor_password(doctor_id, password):
    conn = pymysql.connect(host='127.0.0.1', user='root', passwd="wu*ke225", db='testDB')
    cur = conn.cursor()
    cur.execute("SELECT password FROM doctor_list WHERE doctor_id='{}'".format(doctor_id))
    # print(cur[0][0])
    for r in cur:
        if r[0]==password:
            print(r[0])
            cur.close()
            conn.close()
            return '1'
    cur.close()
    conn.close()
    return '0'

def select_patient_doctor_info(patient_id):
    conn = pymysql.connect(host='127.0.0.1', user='root', passwd="wu*ke225", db='testDB')
    cur = conn.cursor()
    list=[];
    cur.execute("SELECT * FROM doctor_list WHERE doctor_id IN (SELECT doctor_id FROM patient_list WHERE patient_id='{}')".format(patient_id))
    for r in cur:
        print(r)
        list.append({
            "name": r[0],
            "gender": int.from_bytes(r[1], byteorder='big'),
            "doctor_id": r[2],
            "password": r[3],
            "birthday": r[4].strftime("%Y-%m-%d"),
            "professional_time": r[5].strftime("%Y-%m-%d"),
            "tel": r[6],
            "email": r[7]

        })
    cur.close()
    conn.close()
    return list

def change_patient_health_info(time, patient_id, heartrate, highpressure, lowpressure):
    conn = pymysql.connect(host='127.0.0.1', user='root', passwd="wu*ke225", db='testDB')
    cur = conn.cursor()
    print(time, patient_id, heartrate, highpressure, lowpressure)
    cur.execute("insert ignore into pressure_heartrate_list values('{}','{}', {}, {}, {})".format(time, patient_id, heartrate, highpressure, lowpressure))
    conn.commit()
    cur.close()
    conn.close()
    return '1'


def add_patient_medicine(patient_id, medicine):
    conn = pymysql.connect(host='127.0.0.1', user='root', passwd="wu*ke225", db='testDB')
    cur = conn.cursor()
    print(patient_id, medicine)
    cur.execute("insert ignore into relationship_pat_medicine values('{}','{}')".format(patient_id, medicine))
    conn.commit()
    cur.close()
    conn.close()
    return'1'

def delete_medicine_by_name(patient_id, medicine):
    conn = pymysql.connect(host='127.0.0.1', user='root', passwd="wu*ke225", db='testDB')
    cur = conn.cursor()
    print(patient_id, medicine)
    cur.execute("DELETE from relationship_pat_medicine WHERE patient_id='{}' AND medicine_id IN (select medicine_id from medicine_list where medicine_name = '{}')".format(patient_id, medicine))
    conn.commit()
    cur.close()
    conn.close()
    return'1'


def add_patient(patient_id, doctor_id):
    conn = pymysql.connect(host='127.0.0.1', user='root', passwd="wu*ke225", db='testDB')
    cur = conn.cursor()
    print(patient_id, doctor_id)
    # cur.execute("select count(*) from patient_list where doctor_id='{}' and patient_id='{}'".format(doctor_id, patient_id))
    cur.execute("update patient_list set doctor_id='{}' where patient_id='{}'".format(doctor_id, patient_id))
    conn.commit()
    cur.close()
    conn.close()
    return '1'


def register_patient(name, gender, id, password, birthday, sickTime, bloodType, tel, email):
    conn = pymysql.connect(host='127.0.0.1', user='root', passwd="wu*ke225", db='testDB')
    cur = conn.cursor()
    cur.execute("insert into patient_list values('{}', {}, '{}', '{}', '{}', '{}', '0', '{}', '{}', '{}')".format(name, gender, id, password, birthday, sickTime, tel, email, bloodType))
    conn.commit()
    cur.close()
    conn.close()
    return '1'


def register_doctor(name, gender, id, password, birthday, professionalTime, tel, email):
    conn = pymysql.connect(host='127.0.0.1', user='root', passwd="wu*ke225", db='testDB')
    cur = conn.cursor()
    cur.execute("insert into doctor_list values('{}', {}, '{}', '{}', '{}', '{}', '{}', '{}')".format(name, gender, id, password, birthday, professionalTime, tel, email))
    conn.commit()
    cur.close()
    conn.close()
    return '1'





