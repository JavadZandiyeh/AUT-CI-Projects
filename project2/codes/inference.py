def do_inference(input_dict: dict) -> dict:
    inf_dic = {}
    inf_dic['healthy'] = round(healthy_rules(input_dict), 2)
    inf_dic['sick_1'] = round(sick_1_rules(input_dict), 2)
    inf_dic['sick_2'] = round(sick_2_rules(input_dict), 2)
    inf_dic['sick_3'] = round(sick_3_rules(input_dict), 2)
    inf_dic['sick_4'] = round(sick_4_rules(input_dict), 2)

    return inf_dic

def healthy_rules(input_dict: dict) -> float:
    # healthy -> rules (11, 18, 23, 29, 34, 40, 45, 50)
    healthy = 0
        # rule 11:
    rule_output = input_dict['chest_pain']['typical_anginal']
    healthy = max(healthy, rule_output)
        # rule 18:
    rule_output = input_dict['blood_pressure']['low']
    healthy = max(healthy, rule_output)
        # rule 23:
    rule_output = input_dict['cholesterol']['low']
    healthy = max(healthy, rule_output)
        # rule 29
    rule_output = input_dict['ECG']['normal']
    healthy = max(healthy, rule_output)
        # rule 34
    rule_output = input_dict['maximum_heart_rate']['low']
    healthy = max(healthy, rule_output)
        # rule 40
    rule_output = input_dict['old_peak']['low']
    healthy = max(healthy, rule_output)
        # rule 45
    rule_output = input_dict['thallium']['normal']
    healthy = max(healthy, rule_output)
        # rule 50
    rule_output = input_dict['age']['young']
    healthy = max(healthy, rule_output)
    
    return healthy

def sick_1_rules(input_dict: dict) -> float:
    # sick_1 -> rules (9, 10, 12, 16, 19, 24, 30, 35, 41, 46, 51)
    sick_1 = 0
        # rule 9
    rule_output = max(input_dict['chest_pain']['asymptomatic'], input_dict['age']['very_old'])
    sick_1 = max(sick_1, rule_output)
        # rule 10
    rule_output = max(input_dict['blood_pressure']['high'], input_dict['maximum_heart_rate']['low'])
    sick_1 = max(sick_1, rule_output)
        # rule 12
    rule_output = input_dict['chest_pain']['atypical_anginal']
    sick_1 = max(sick_1, rule_output)
        # rule 16 
    rule_output = input_dict['sex']['female']
    sick_1 = max(sick_1, rule_output)
        # rule 19
    rule_output = input_dict['blood_pressure']['medium']
    sick_1 = max(sick_1, rule_output)
        # rule 24
    rule_output = input_dict['cholesterol']['medium']
    sick_1 = max(sick_1, rule_output)
        # rule 30
    rule_output = input_dict['ECG']['normal']
    sick_1 = max(sick_1, rule_output)
        # rule 35 (maximum_heart_rate IS medium)
    rule_output = input_dict['maximum_heart_rate']['medium']
    sick_1 = max(sick_1, rule_output)
        # rule 41
    rule_output = input_dict['old_peak']['low']
    sick_1 = max(sick_1, rule_output)
        # rule 46
    rule_output = input_dict['thallium']['normal']
    sick_1 = max(sick_1, rule_output)
        # rule 51
    rule_output = input_dict['age']['mild']
    sick_1 = max(sick_1, rule_output)

    return sick_1

def sick_2_rules(input_dict: dict) -> float:
    # sick_2 -> rules (4, 6, 8, 13, 17, 20, 25, 28, 31, 36, 39, 42, 47, 52)
    sick_2 = 0
        # rule 4
    rule_output = min(input_dict['sex']['female'], input_dict['maximum_heart_rate']['medium'])
    sick_2 = max(sick_2, rule_output)
        # rule 6
    rule_output = min(input_dict['chest_pain']['typical_anginal'], input_dict['maximum_heart_rate']['medium'])
    sick_2 = max(sick_2, rule_output)
        # rule 8
    rule_output = min(input_dict['blood_sugar']['false'], input_dict['blood_pressure']['very_high'])
    sick_2 = max(sick_2, rule_output)
        # rule 13
    rule_output = input_dict['chest_pain']['non_aginal_pain']
    sick_2 = max(sick_2, rule_output)
        # rule 17
    rule_output = input_dict['sex']['male']
    sick_2 = max(sick_2, rule_output)
        # rule 20
    rule_output = input_dict['blood_pressure']['high']
    sick_2 = max(sick_2, rule_output)
        # rule 25
    rule_output = input_dict['cholesterol']['high']
    sick_2 = max(sick_2, rule_output)
        # rule 28
    rule_output = input_dict['blood_sugar']['true']
    sick_2 = max(sick_2, rule_output)
        # rule 31
    rule_output = input_dict['ECG']['abnormal']
    sick_2 = max(sick_2, rule_output)
        # rule 36
    rule_output = input_dict['maximum_heart_rate']['medium']
    sick_2 = max(sick_2, rule_output)
        # rule 39
    rule_output = input_dict['exercise']['true']
    sick_2 = max(sick_2, rule_output)
        # rule 42
    rule_output = input_dict['old_peak']['terrible']
    sick_2 = max(sick_2, rule_output)
        # rule 47
    rule_output = input_dict['thallium']['medium']
    sick_2 = max(sick_2, rule_output)
        # rule 52
    rule_output = input_dict['age']['old']
    sick_2 = max(sick_2, rule_output)

    return sick_2

def sick_3_rules(input_dict: dict) -> float:
    # sick_3 -> rules (3, 5, 7, 14, 21, 26, 32, 37, 43, 48, 53)
    sick_3 = 0
        # rule 3
    rule_output = min(input_dict['sex']['male'], input_dict['maximum_heart_rate']['medium'])
    sick_3 = max(sick_3, rule_output) 
        # rule 5
    rule_output = min(input_dict['chest_pain']['non_aginal_pain'], input_dict['blood_pressure']['high'])
    sick_3 = max(sick_3, rule_output) 
        # rule 7
    rule_output = min(input_dict['blood_sugar']['true'], input_dict['age']['mild'])
    sick_3 = max(sick_3, rule_output) 
        # rule 14
    rule_output = input_dict['chest_pain']['asymptomatic']
    sick_3 = max(sick_3, rule_output) 
        # rule 21
    rule_output = input_dict['blood_pressure']['high']
    sick_3 = max(sick_3, rule_output) 
        # rule 26
    rule_output = input_dict['cholesterol']['high']
    sick_3 = max(sick_3, rule_output) 
        # rule 32
    rule_output = input_dict['ECG']['hypertrophy']
    sick_3 = max(sick_3, rule_output) 
        # rule 37
    rule_output = input_dict['maximum_heart_rate']['high']
    sick_3 = max(sick_3, rule_output) 
        # rule 43
    rule_output = input_dict['old_peak']['terrible']
    sick_3 = max(sick_3, rule_output) 
        # rule 48
    rule_output = input_dict['thallium']['high']
    sick_3 = max(sick_3, rule_output) 
        # rule 53
    rule_output = input_dict['age']['old']
    sick_3 = max(sick_3, rule_output) 

    return sick_3

def sick_4_rules(input_dict: dict) -> float:
    # sick_4 -> rules (1, 2, 15, 22, 27, 33, 38, 44, 49, 54)
    sick_4 = 0
        # rule 1
    rule_output = min(input_dict['age']['very_old'], input_dict['chest_pain']['atypical_anginal'])
    sick_4 = max(sick_4, rule_output) 
        # rule 2
    rule_output = min(input_dict['maximum_heart_rate']['high'], input_dict['age']['old'])
    sick_4 = max(sick_4, rule_output) 
        # rule 15
    rule_output = input_dict['chest_pain']['asymptomatic']
    sick_4 = max(sick_4, rule_output) 
        # rule 22
    rule_output = input_dict['blood_pressure']['very_high']
    sick_4 = max(sick_4, rule_output) 
        # rule 27
    rule_output = input_dict['cholesterol']['very_high']
    sick_4 = max(sick_4, rule_output) 
        # rule 33
    rule_output = input_dict['ECG']['hypertrophy']
    sick_4 = max(sick_4, rule_output) 
        # rule 38
    rule_output = input_dict['maximum_heart_rate']['high']
    sick_4 = max(sick_4, rule_output) 
        # rule 44
    rule_output = input_dict['old_peak']['risk']
    sick_4 = max(sick_4, rule_output) 
        # rule 49
    rule_output = input_dict['thallium']['high']
    sick_4 = max(sick_4, rule_output) 
        # rule 54
    rule_output = input_dict['age']['very_old']
    sick_4 = max(sick_4, rule_output) 
    
    return sick_4