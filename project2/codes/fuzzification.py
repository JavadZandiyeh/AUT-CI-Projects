def do_fuzzification(input_dict: dict) -> dict:
    fuzz_dict = {}
    fuzz_dict['chest_pain'] = chest_pain(int(input_dict['chest_pain']))
    fuzz_dict['blood_pressure'] = blood_pressure(int(input_dict['blood_pressure']))
    fuzz_dict['cholesterol'] = cholesterol(int(input_dict['cholestrol']))
    fuzz_dict['blood_sugar'] = blood_sugar(int(input_dict['blood_sugar']))
    fuzz_dict['ECG'] = ECG(float(input_dict['ecg']))
    fuzz_dict['maximum_heart_rate'] = maximum_heart_rate(int(input_dict['heart_rate']))
    fuzz_dict['exercise'] = exercise(int(input_dict['exercise']))
    fuzz_dict['old_peak'] = old_peak(float(input_dict['old_peak']))
    fuzz_dict['thallium'] = thallium(int(input_dict['thallium_scan']))
    fuzz_dict['sex'] = sex(int(input_dict['sex']))
    fuzz_dict['age'] = age(int(input_dict['age']))

    return fuzz_dict

def chest_pain(cp: int) -> dict:
    cp_dict = {'typical_anginal': 0, 'atypical_anginal': 0, 'non_aginal_pain': 0, 'asymptomatic': 0}
    
    if cp == 1:
        cp_dict['typical_anginal'] = 1
    elif cp == 2:
        cp_dict['atypical_anginal'] = 1
    elif cp == 3:
        cp_dict['non_aginal_pain'] = 1
    elif cp == 4:
        cp_dict['asymptomatic'] = 1
    
    return cp_dict

def blood_pressure(bp: int) -> dict:
    bp_dict = {'low': 0, 'medium': 0, 'high': 0, 'very_high': 0}
    
    if bp < 111:
        bp_dict['low'] = 1
    if 111 <= bp < 134:
        bp_dict['low'] = (134-bp)/23

    if 127 <= bp < 139:
        bp_dict['medium'] = (bp-127)/12
    if 139 <= bp < 153:
        bp_dict['medium'] = (153-bp)/14

    if 142 <= bp < 157:
        bp_dict['high'] = (bp-142)/15
    if 157 <= bp < 172:
        bp_dict['high'] = (172-bp)/15

    if 154 <= bp < 171:
        bp_dict['very_high'] = (bp-154)/17
    if 171 <= bp:
        bp_dict['very_high'] = 1

    return bp_dict

def cholesterol(ch: int) -> dict:
    ch_dict = {'low': 0, 'medium': 0, 'high': 0, 'very_high': 0}
    
    if ch < 151:
        ch_dict['low'] = 1
    if 151 <= ch < 197:
        ch_dict['low'] = (197-ch)/46

    if 188 <= ch < 215:
        ch_dict['medium'] = (ch-188)/27
    if 215 <= ch < 250:
        ch_dict['medium'] = (250-ch)/35

    if 217 <= ch < 263:
        ch_dict['high'] = (ch-217)/46
    if 263 <= ch < 307:
        ch_dict['high'] = (307-ch)/44

    if 281 <= ch < 347:
        ch_dict['very_high'] = (ch-281)/66
    if 347 <= ch:
        ch_dict['very_high'] = 1

    return ch_dict

def blood_sugar(bs: int) -> dict:
    bs_dict = {'false': 0, 'true': 0}

    if bs <= 120:
        bs_dict['false'] = (bs-105)/15
    if 120 <= bs:
        bs_dict['true'] = 1

    return bs_dict

def ECG(ecg: float) -> dict:
    ecg_dict = {'normal': 0, 'abnormal': 0, 'hypertrophy': 0}

    if ecg < 0:
        ecg_dict['normal'] = 1
    if 0 <= ecg < 0.4:
        ecg_dict['normal'] = (0.4-ecg)/0.4

    if 0.2 <= ecg < 1:
        ecg_dict['abnormal'] = (ecg-0.2)/0.8
    if 1 <= ecg < 1.8:
        ecg_dict['abnormal'] = (1.8-ecg)/0.8

    if 1.4 <= ecg < 1.9:
        ecg_dict['hypertrophy'] = (ecg-1.4)/0.5
    if 1.9 <= ecg:
        ecg_dict['hypertrophy'] = 1

    return ecg_dict

def maximum_heart_rate(mhr: int) -> dict:
    mhr_dict = {'low': 0, 'medium': 0, 'high': 0}

    if mhr < 100:
        mhr_dict['low'] = 1
    if 100 <= mhr < 141:
        mhr_dict['low'] = (141-mhr)/41

    if 111 <= mhr < 152:
        mhr_dict['medium'] = (mhr-111)/41
    if 152 <= mhr < 194:
        mhr_dict['medium'] = (194-mhr)/42

    if 152 <= mhr < 210:
        mhr_dict['high'] = (210-mhr)/58
    if 210 <= mhr:
        mhr_dict['high'] = 1

    return mhr_dict

def exercise(ex: int) -> dict:
    ex_dict = {'false': 0, 'true': 0}

    if ex == 0:
        ex_dict['false'] = 1
    elif ex == 1:
        ex_dict['true'] = 1

    return ex_dict

def old_peak(op: float) -> dict:
    op_dict = {'low': 0, 'risk': 0, 'terrible': 0}

    if op < 1:
        op_dict['low'] = 1
    if 1 <= op < 2:
        op_dict['low'] = (op-1)/1
    
    if 1.5 <= op < 2.8:
        op_dict['risk'] = (op-1.5)/1.3
    if 2.8 <= op < 4.2:
        op_dict['risk'] = (4.2-op)/1.4

    if 2.5 <= op < 4:
        op_dict['terrible'] = (op-2.5)/1.5
    if 4 <= op:
        op_dict['terrible'] = 1

    return op_dict

def thallium(th: int) -> dict:
    th_dict = {'normal': 0, 'medium': 0, 'high': 0}
    
    if th == 3:
        th_dict['normal'] = 1
    elif th == 6:
        th_dict['medium'] = 1
    elif th == 7:
        th_dict['high'] = 1

    return th_dict

def sex(se: int) -> dict:
    sex_dict = {'male': 0, 'female': 0}

    if se == 0:
        sex_dict['male'] = 1
    elif se == 1:
        sex_dict['female'] = 1

    return sex_dict

def age(ag: int) -> dict:
    age_dict = {'young': 0, 'mild': 0, 'old': 0, 'very_old': 0}

    if ag < 29:
        age_dict['young'] = 1
    if 29 <= ag < 38:
        age_dict['young'] = (38-ag)/9

    if 33 <= ag < 38:
        age_dict['mild'] = (ag-33)/5
    if 38 <= ag < 45:
        age_dict['mild'] = (45-ag)/7
    
    if 40 <= ag < 48:
        age_dict['old'] = (ag-40)/8
    if 48 <= ag < 58:
        age_dict['old'] = (58-ag)/10
    
    if 52 <= ag < 60:
        age_dict['very_old'] = (ag-52)/8
    if 60 <= ag:
        age_dict['very_old'] = 1

    return age_dict