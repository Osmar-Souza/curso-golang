from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

# 1. Definir importacao de dados do csv (Pandas) ID consultar no mySQL qual o path do arquivo
# 2. getProfile = Retorna todos perfis
# 3. getDimensionsProperties = Retorna Dimensões e Properties de acordo com ID do Perfil informado
# 4. getStandard = Retorna Standards de acordo com ID do Perfil informado
# 5. getfy = Retorna fy de acordo com ID do Perfil informado
# 6. getResult = Retorna o resultado de acordo com ID do Perfil, Fy e Standard informados
# 7. getUtilizationRatio = Retorna o calculo

# Profile: id, description
# DimensionsProperties: id, H, Bf, D, t, A, Ixx, Iyy, Cw, J, xcg, Xs, ycg, Ys
# Standard: id, name
# fy: id, name
# Result: id, Description, Standard, fy, Lb, KxLx, KyLy, KzLz, lambdax, lambday, Nrd, Mrd

@app.route('/getProfile', methods=['GET'])
def get_profile():
    try:        
        file_properties = request.args.get('file_properties')        
        if file_properties is None:
            return jsonify({"error": "parameter required[file_properties]"}), 404 
        data = pd.read_csv(file_properties, sep=';', skiprows=[1])
        data = data.rename(columns=lambda x: x.strip())
        df = pd.DataFrame(data, columns=['ID', 'Description', 'H', 'Bf', 'D', 't', 'A', 'Ixx', 'Iyy', 'Cw', 'J', 'xcg', 'Xs', 'ycg', 'Ys'])

        lst_profile = df.values.tolist()
        profiles = []    

        for row in lst_profile:
            result_info = {"h": row[2], "bf": row[3], "d": row[4],
                           "t": row[5], "a": row[6], "ixx": row[7], "iyy": row[8], "cw": row[9], "j": row[10], "xcg": row[11], "xs": row[12], "ycg": row[13], "ys": row[14]}
            profile_info = {"id": row[0], "description": row[1], "dimensionsProperties" : result_info }
            profiles.append(profile_info)
            
        return jsonify(profiles)
    except FileNotFoundError:
        return jsonify({"error": "File not found"}), 404


@app.route('/getDimensionsProperties')
def get_dimensions_properties():
    try:
        id_profile = request.args.get('id_profile')
        if id_profile is None:
            return jsonify({"error": "parameter required[id_profile]"}), 404
        file_properties = request.args.get('file_properties')
        if file_properties is None:
            return jsonify({"error": "parameter required[file_properties]"}), 404 

        data = pd.read_csv(file_properties, sep=';', skiprows=[1])
        data = data.rename(columns=lambda x: x.strip())
        df = pd.DataFrame(data, columns=['ID', 'Description', 'H', 'Bf', 'D', 't', 'A', 'Ixx', 'Iyy', 'Cw', 'J', 'xcg', 'Xs', 'ycg', 'Ys']).query('ID ==' + id_profile).drop_duplicates()

        lst_dimensions_properties = df.values.tolist()
        results = []

        for row in lst_dimensions_properties:
            result_info = {"id": row[0], "description": row[1], "h": row[2], "bf": row[3], "d": row[4],
                           "t": row[5], "a": row[6], "ixx": row[7], "iyy": row[8], "cw": row[9], "j": row[10], "xcg": row[11], "xs": row[12], "ycg": row[13], "ys": row[14]}
            results.append(result_info)
        return jsonify(results)
    except FileNotFoundError:
        return jsonify({"error": "File not found"}), 404
        
@app.route('/getStandard')
def get_standard():
    try:
        id_profile = request.args.get('id_profile')
        if id_profile is None:
            return jsonify({"error": "parameter required[id_profile]"}), 404
        file_results = request.args.get('file_results')
        if file_results is None:
            return jsonify({"error": "parameter required[file_results]"}), 404               

        data = pd.read_csv(file_results, sep = ';', skiprows=[1])
        data = data.rename(columns=lambda x: x.strip())
        df= pd.DataFrame(data, columns=['Index', 'ID', 'Standard']).query('ID ==' + id_profile).drop_duplicates() 
        
        lst_standards = df.values.tolist()        
        standards = []
        
        for row in lst_standards:
        
                standard_info = {"id": row[1], "description": row[2]}
                standards.append(standard_info)

        return jsonify(standards)
    except FileNotFoundError:
        return jsonify({"error": "File not found"}), 404

@app.route('/getFY')
def get_fy():
    try:
        id_profile = request.args.get('id_profile')
        if id_profile is None:
            return jsonify({"error": "parameter required[id_profile]"}), 404
        file_results = request.args.get('file_results')
        if file_results is None:
            return jsonify({"error": "parameter required[file_results]"}), 404               

        data = pd.read_csv(file_results, sep = ';', skiprows=[1])
        data = data.rename(columns=lambda x: x.strip())
        df= pd.DataFrame(data, columns=['Index', 'ID', 'fy']).query('ID ==' + id_profile).drop_duplicates() 
        
        lst_fys = df.values.tolist()        
        fys = []
        
        for row in lst_fys:
        
                fy_info = {"id": row[1], "description": row[2]}
                fys.append(fy_info)

        return jsonify(fys)
    except FileNotFoundError:
        return jsonify({"error": "File not found"}), 404

@app.route('/getResult')
def get_result():
    try:
        id_profile = request.args.get('id_profile')
        if id_profile is None:
            return jsonify({"error": "parameter required[id_profile]"}), 404
        file_results = request.args.get('file_results')
        if file_results is None:
            return jsonify({"error": "parameter required[file_results]"}), 404     
        standard = request.args.get('standard')
        if standard is None:
            return jsonify({"error": "parameter required[standard]"}), 404 
        fy = request.args.get('fy')
        if fy is None:
            return jsonify({"error": "parameter required[fy]"}), 404                      

        print("standard:'" +standard +"'")
        print("fy:'" +fy +"'")   
        data = pd.read_csv(file_results, sep = ';', skiprows=[1])
        data = data.rename(columns=lambda x: x.strip())
        df= pd.DataFrame(data, columns=['Index', 'ID', 'Standard', 'fy', 'Lb', 'KxLx', 'KyLy', 'KzLz', 'Nrd', 'Mrd', 'lambdax', 'lambday']).query("ID ==" + id_profile + " & Standard=='" + standard + "'").drop_duplicates() #+ ' & Standard=="' + standard + '" & fy=="' + fy +'"'        
        
        lst_results = df.values.tolist()        
        results = []
        
        for row in lst_results:
        
                result_info = {"id": row[1], "standard": row[2], "fy": row[3], "lb": row[4], "kxlx": row[5], "kyly": row[6], "kzlz": row[7], "nrd": row[8], "mrd": row[9], "lambdax": row[10], "lambday": row[11]}
                results.append(result_info)


        if len(results)>0:
            return jsonify(results)
        else:
            return jsonify({"error": "Item not found"}), 404
    except FileNotFoundError:
        return jsonify({"error": "File not found"}), 404


@app.route('/getUtilizationRatio')
def get_UtilizationRatio():
    try:
        result_N_Nrd = 0
        N = request.args.get('n')
        Nrd = request.args.get('nrd')
        M = request.args.get('m')
        Mrd = request.args.get('mrd')
        if (N is None or Nrd is None) and (M is None or Mrd is None):
            return jsonify({"error": "required parameters[(N and Nrd) or (M and Mrd)]"}), 404

        
        if N is not None and Nrd is not None:
            N = float(request.args.get('n'))
            Nrd = float(request.args.get('nrd'))
            result_N_Nrd = N/Nrd
            
        result_M_Mrd = 0            
        if M is not None and Mrd is not None:
            M = float(request.args.get('m'))
            Mrd = float(request.args.get('mrd'))
            result_M_Mrd = M/Mrd
            
        result_M_Mrd = "{:.3f}".format(result_M_Mrd)
        result_N_Nrd = "{:.3f}".format(result_N_Nrd)
        # result_M_Mrd = math.trunc(result_M_Mrd)
        # result_N_Nrd = math.trunc(result_N_Nrd)
        utilization_ration = []
        result_info = {"n_nrd":result_N_Nrd, "m_mrd":result_M_Mrd}
        utilization_ration.append(result_info)
        return jsonify(utilization_ration)

    except FileNotFoundError:
        return jsonify({"error": "File not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)