# Définir la fonction de suppression de valeurs aberrantes

def remove_outliers(dataframe, column_name):

    """
    Cette foncion permet de supprimer les valeurs aberrantes potentilles se trouvant
    dans un DataFrame et de renvoyer un nouveau DataFrame sans valeurs aberrantes

    Inputs:

    dataframe         : Le DataFrame avec sur lequel on souaite supprimer les valeurs aberrantes
    column_name: Le nom de la colonne qu'il faut vérifier les lignes des outliers potentiels

    Returns:

    Renvoyer le DatFrame (dataframe) qui ne contient aucune valeur aberrante

    """

    # Calculer le 1er et le 3ème quartiles
    quartile_1, quartile_3 = dataframe[column_name].quantile([0.25, 0.75])
    # Calculer l'écart interquartile (inter_quart_range)
    inter_quart_range = quartile_3 - quartile_1

    # Calculer les limites inférieures et supérieures
    lower_bound = quartile_1 - (1.5 * inter_quart_range)
    upper_bound = quartile_3 + (1.5 * inter_quart_range)
       
    # Supprimer les lignes qui contiennent les outliers potentiels
    # Des lignes se situant entre les limites inférieures et supérieures
    dataframe = dataframe[(dataframe[column_name] >= lower_bound)
                          & (dataframe[column_name] <= upper_bound)]

    # Renvoyer le DataFrame sans valeurs aberrantes
    return dataframe
    