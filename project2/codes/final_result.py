import fuzzification, inference, defuzzification

class ProvideResult(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(ProvideResult, cls).__new__(cls)
        return cls.instance

    @staticmethod
    def get_final_result(input_dict: dict) -> str:
        fuzzification_result = fuzzification.do_fuzzification(input_dict)
        inference_result = inference.do_inference(fuzzification_result)
        defuzzification_result = defuzzification.do_defuzzification(inference_result)
               
        return str(inference_result) + ' -----> {' + str(defuzzification_result)[:-1] + '}'