import requests

def post_api_login(jwt='', body=None):
     url = 'http://127.0.0.1:5000/api/login'
     headers = {'Authorization': 'Bearer ' + jwt}
     req = requests.post(url, headers=headers, json=body)
     return req.status_code, req.text


def get_api_v1_admin(jwt='', body=None):
     url = 'http://127.0.0.1:5000/api/v1/admin'
     headers = {'Authorization': 'Bearer ' + jwt}
     req = requests.get(url, headers=headers, json=body)
     return req.status_code, req.text


def get_api_v1_hospital_hospital_id(jwt='', body=None, hospital_id=None):
     url = 'http://127.0.0.1:5000/api/v1/hospital/' + hospital_id + ''
     headers = {'Authorization': 'Bearer ' + jwt}
     req = requests.get(url, headers=headers, json=body)
     return req.status_code, req.text


def get_api_v1_hospital_hospital_id_department_department_id(jwt='', body=None, hospital_id=None, department_id=None):
     url = 'http://127.0.0.1:5000/api/v1/hospital/' + hospital_id + '/department/' + department_id + ''
     headers = {'Authorization': 'Bearer ' + jwt}
     req = requests.get(url, headers=headers, json=body)
     return req.status_code, req.text


def post_api_v1_patient(jwt='', patient=None):
     url = 'http://127.0.0.1:5000/api/v1/patient'
     headers = {'Authorization': 'Bearer ' + jwt}
     req = requests.post(url, headers=headers, json=patient)
     return req.status_code, req.text


def put_api_v1_patient(jwt='', patient=None):
     url = 'http://127.0.0.1:5000/api/v1/patient'
     headers = {'Authorization': 'Bearer ' + jwt}
     req = requests.put(url, headers=headers, json=patient)
     return req.status_code, req.text


def delete_api_v1_patient_patient_id(jwt='', body=None, patient_id=None):
     url = 'http://127.0.0.1:5000/api/v1/patient/' + patient_id + ''
     headers = {'Authorization': 'Bearer ' + jwt}
     req = requests.delete(url, headers=headers, json=body)
     return req.status_code, req.text


def get_api_v1_patient_patient_id(jwt='', body=None, patient_id=None):
     url = 'http://127.0.0.1:5000/api/v1/patient/' + patient_id + ''
     headers = {'Authorization': 'Bearer ' + jwt}
     req = requests.get(url, headers=headers, json=body)
     return req.status_code, req.text


def get_api_v1_patient_patient_id_sensitive(jwt='', body=None, patient_id=None):
     url = 'http://127.0.0.1:5000/api/v1/patient/' + patient_id + '/sensitive'
     headers = {'Authorization': 'Bearer ' + jwt}
     req = requests.get(url, headers=headers, json=body)
     return req.status_code, req.text


def get_api_v1_user_user_id(jwt='', body=None, user_id=None):
     url = 'http://127.0.0.1:5000/api/v1/user/' + user_id + ''
     headers = {'Authorization': 'Bearer ' + jwt}
     req = requests.get(url, headers=headers, json=body)
     return req.status_code, req.text


