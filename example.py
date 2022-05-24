users_detection = ['user1', 'user2']
user1 = {
        "get_api_v1_admin": [{"parameters": None, "response": "200"}],
        "get_api_v1_hospital_hospital_id_department_department_id": [{"parameters": ["hospital1","department1"], "response": "200" },
                                                                     {"parameters": ["hospital1", "department2"],"response": "200"},
                                                                     {"parameters": ["hospital2", "department1"], "response": "404"},
                                                                     {"parameters": ["hospital2", "department2"], "response": "404"}],
        "get_api_v1_hospital_hospital_id": [{"parameters": ["hospital1"], "response": "200"},
                                            {"parameters": ["hospital2"], "response": "200"},],
        "post_api_v1_patient": [{"parameters": ["patient1"], "response": "200"},
                                {"parameters": ["patient2"], "response": "200"}],
        "put_api_v1_patient": [{"parameters": ["patient1"], "response": "200"},
                               {"parameters": ["patient2"], "response": "200"}],
        "delete_api_v1_patient_patient_id": [{"parameters": ["patient1"], "response": "200"},
                                             {"parameters": ["patient2"], "response": "200"}],
        "get_api_v1_patient_patient_id": [{"parameters": ["patient1"], "response": "200"},],
        "get_api_v1_patient_patient_id_sensitive": [{"parameters": ["patient2"], "response": "200"},],
        "get_api_v1_user_user_id": [{"parameters": ["user1"], "response": "200"},
                                    {"parameters": ["user2"], "response": "401"}],
},
user2 = {
        "get_api_v1_admin": [{"parameters": None, "response": "200"}],
        "get_api_v1_hospital_hospital_id_department_department_id": [{"parameters": ["hospital1","department1"], "response": "200" },
                                                                     {"parameters": ["hospital1", "department2"],"response": "200"},
                                                                     {"parameters": ["hospital2", "department1"], "response": "404"},
                                                                     {"parameters": ["hospital2", "department2"], "response": "404"}],
},


