with open('Emisiones_CO2.csv', 'rb') as file:

    header = list()
    body = list()
    
    for line, content in enumerate(file):
        
        content = content.decode('ISO-8859-1').split("|")

        for element, var in enumerate(content):

            var = var.replace("\r\n","").replace(".","").replace(",", ".")

            if line == 0:

                header.append(var)
            
            else:
                #Initialization of dictionaty values as list or append in case of exist list
                try:
                    new_var = body[element]
                except IndexError:
                    new_var = list()
                # Parse Data Type
                try:
                    if "." in var:
                        var = float(var)
                    else:
                        var = int(var)
                except:
                    pass

                # Ternary Operator for parse missing values
                new_var.append(var if var else None)
                body.append(new_var)

    # Create dictionary
    emisiones = dict(zip(header, body))

    # RESULTS
    print("Resumen")
    print(f"Numero de Variables: {len(emisiones.keys())}")
    for key, value in emisiones.items():

        print(f"{key} tiene {value.count(None)} datos faltantes")
    
    anio_to_find = 2010
    region_to_find = 'América Latina y Caribe'
    indexes = [i for i, x in enumerate(emisiones['Región']) if x == region_to_find]
    total_co2_emissions = 0
    for index in indexes:

        if emisiones['Año'][index]==anio_to_find:
            co2_emission = emisiones['CO2 (kt)'][index]
            if co2_emission:
                total_co2_emissions += emisiones['CO2 (kt)'][index]

    print(f"Emisiones Totales de CO2 (kt) para el Año {anio_to_find} en {region_to_find} fue de: {total_co2_emissions}")