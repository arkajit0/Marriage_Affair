from flask import Flask, render_template, request
import pickle

app = Flask(__name__, template_folder='../templates')

@app.route('/', methods=['GET'])
def base():
    return render_template('index.html')

@app.route('/predict', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        marriage_rate = {'very poor': 1, 'poor': 2, 'fair': 3, 'good': 4, 'very good': 5}
        religious_dict = {'not': 1, 'mildly': 2, 'fairly': 3, 'strongly': 4}
        educ_dict = {'grade school': 9, 'high school': 12, 'college UG': 14, 'college graduate': 16,
                     'some graduate school': 17, 'advanced degree': 20}
        occ_dict = {'student': 1, 'farming': 2, 'unskilled': 2, 'white colloar': 3, 'skilled worker': 4, 'business': 5,
                    'professional': 6}
        result = {0: "will not have an affair", 1: "will have an affair"}
        occ = [0,0,0,0,0]

        rate_marriage = marriage_rate[request.form['rate_marriage']]
        children = float(request.form['children'])
        religious = religious_dict[request.form['religious']]
        educ = educ_dict[request.form['educ']]
        married_age = float(request.form['married age'])
        occ_wife = occ_dict[request.form['occ_wife']]
        occ_husb = occ_dict[request.form['occ_husb']]

        if occ_wife == 1:
            occ_2, occ_3, occ_4, occ_5, occ_6 = occ
        else:
            occ[occ_wife-2] = 1
            occ_2, occ_3, occ_4, occ_5, occ_6 = occ

        if occ_husb == 1:
            occ_2_husb, occ_3_husb, occ_4_husb, occ_5_husb, occ_6_husb = occ
        else:
            occ[occ_husb-2] = 1
            occ_2_husb, occ_3_husb, occ_4_husb, occ_5_husb, occ_6_husb = occ

        model = pickle.load(open('final_model_v1.pkl', 'rb'))
        scale = pickle.load(open('final_scale_v1.pkl', 'rb'))

        predicted_value = model.predict(scale.transform([[occ_2, occ_3, occ_4, occ_5, occ_6,
                                                      occ_2_husb, occ_3_husb, occ_4_husb, occ_5_husb, occ_6_husb,
                                                          rate_marriage, children, religious, educ, married_age,]]))[0]


        return render_template("test.html", prediction=result[predicted_value])
        # return render_template("test.html")

if __name__ == '__main__':
    app.run(host="0.0.0.0")



