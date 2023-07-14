def do_defuzzification(input_dict: dict) -> str:
    c_sick_1 = 1
    c_sick_2 = 2
    c_sick_3 = 3
    c_sick_4 = 4

    x_star = (c_sick_1*input_dict['healthy']) + (c_sick_2*input_dict['sick_1']) + (c_sick_3*input_dict['sick_3']) + (c_sick_4*input_dict['sick_4'])
    x_star = x_star/(input_dict['healthy'] + input_dict['sick_1'] + input_dict['sick_2'] + input_dict['sick_3'] + input_dict['sick_4'])
    x_star = round(x_star, 2)
    
    output_result = ''
    if x_star < 1.78:
        output_result += ' Healthy &'
    if 1 <= x_star < 2.51:
        output_result += ' Sick(s1) &'
    if 1.78 <= x_star < 3.25:
        output_result += ' Sick(s2) &'
    if 1.5 <= x_star < 4.5:
        output_result += ' Sick(s3) &'
    if 3.25 < x_star:
        output_result += ' Sick(s4) &'
    
    
    return  str(x_star) + ' : ' + output_result 