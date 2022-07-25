import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler
import joblib
import pandas as pd
# 1 --- import model

path = "/content/ANN-4Dense.h5"
model = tf.keras.models.load_model(path)

# 2 --- set up scaler variables

scalerX = joblib.load("/content/ANN_4D_scalerXAtoB.save")
scalerY = joblib.load("/content/ANN_4D_scalerYAtoB.save")


def myMLPredictions3(area, u_value_walls_W_per_m2K, u_value_roof_W_per_m2K, u_value_basement_W_per_m2K, u_value_glass_W_per_m2K, g_value_glass_W_per_m2K, bdgcode ):

    # Create Input Array
    new_data = pd.DataFrame([[area, u_value_walls_W_per_m2K, u_value_roof_W_per_m2K, u_value_basement_W_per_m2K, u_value_glass_W_per_m2K, g_value_glass_W_per_m2K, bdgcode ]])

    # Scale Input to match the same format from the trained model
    scaled_input = scalerX.transform(new_data)

    # Generate Predictions from Scaled Input using model.predict

    # 01// predict
    out = model.predict(scaled_input)
    #02 // inverse scaling
    predictions = scalerY.inverse_transform(out)

    
    #Flatten predictions list to be readable for hops
    pred_list = predictions.tolist()
    flat_list = []

    for i in pred_list:
        flat_list += i

    # Set each prediction value to a variable
    Heating_energy = round(flat_list[0], 2)
    Cooling_energy = round(flat_list[1], 2)
    DHW_energy = round(flat_list[2], 2)
    total_energy = round(flat_list[3], 2)
   
   
    return Heating_energy, Cooling_energy, DHW_energy, total_energy
    #msg = ("Heating-energy-kWh/m2 is =", Heating_energy, "+ Cooling-energy-kWh/m2 is =" , Cooling_energy, "DHW-energy-kWh/m2 is =",DHW_energy, "total-energy is =",total_energy )
    
    #print(msg )


    #model.summary()