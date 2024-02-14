# Importing libraries
import numpy as np
import pandas as pd

from helpers.auxiliar import cast_type_FixValue, find_closest_value
# Importing functions and classes from packages
from helpers.enumerations import Belong, Operator, Closure, DataType, DerivedType, Operation, SpecialType


class ContractsInvariants:
    # FixValue - FixValue, FixValue - DerivedValue, FixValue - NumOp
    # Interval - FixValue, Interval - DerivedValue, Interval - NumOp
    # SpecialValue - FixValue, SpecialValue - DerivedValue, SpecialValue - NumOp
    """

    """
    def checkInv_FixValue_FixValue(self, dataDictionary: pd.DataFrame, dataTypeInput: DataType, fixValueInput, dataTypeOutput: DataType, fixValueOutput) -> pd.DataFrame:
        """
        Check the invariant of the FixValue - FixValue relation
        params:
            dataDictionary: dataframe with the data
            dataTypeInput: data type of the input value
            FixValueInput: input value to check
            dataTypeOutput: data type of the output value
            FixValueOutput: output value to check
            axis_param: axis to check the invariant
        Returns:
            dataDictionary with the FixValueInput and FixValueOutput values changed to the type dataTypeInput and dataTypeOutput respectively
        """
        fixValueInput, fixValueOutput=cast_type_FixValue(dataTypeInput, fixValueInput, dataTypeOutput, fixValueOutput)
        #Función auxiliar que cambia los valores de FixValueInput y FixValueOutput al tipo de dato en DataTypeInput y DataTypeOutput respectivamente
        dataDictionary = dataDictionary.replace(fixValueInput, fixValueOutput)
        return dataDictionary

    def checkInv_FixValue_DerivedValue(self, dataDictionary: pd.DataFrame, dataTypeInput: DataType, fixValueInput, derivedTypeOutput: DerivedType, axis_param: int = None) -> pd.DataFrame:
        # Por defecto, si todos los valores son igual de frecuentes, se sustituye por el primer valor.
        # Comprobar si solo se debe hacer para filas y columnas o también para el dataframe completo.

        """
        Check the invariant of the FixValue - DerivedValue relation
        Sustituye el valor proporcionado por el usuario por el valor derivado en el eje que se especifique por parámetros
        params:
            dataDictionary: dataframe with the data
            dataTypeInput: data type of the input value
            FixValueInput: input value to check
            derivedTypeOutput: derived type of the output value
            axis_param: axis to check the invariant
        """
        fixValueInput, valorNulo=cast_type_FixValue(dataTypeInput, fixValueInput, None, None)
        #Función auxiliar que cambia el valor de FixValueInput al tipo de dato en DataTypeInput

        dataDictionary_copy = dataDictionary.copy()

        if derivedTypeOutput == DerivedType.MOSTFREQUENT:
            if axis_param == 1: # Aplica la función lambda a nivel de fila
                dataDictionary_copy = dataDictionary_copy.apply(lambda fila: fila.apply(
                    lambda value: dataDictionary_copy.loc[
                        fila.name].value_counts().idxmax() if value == fixValueInput else value), axis=axis_param)
            elif axis_param == 0: # Aplica la función lambda a nivel de columna
                dataDictionary_copy = dataDictionary_copy.apply(lambda columna: columna.apply(
                    lambda value: dataDictionary_copy[
                        columna.name].value_counts().idxmax() if value == fixValueInput else value), axis=axis_param)
            else: # Aplica la función lambda a nivel de dataframe
                # Asumiendo que 'dataDictionary_copy' es tu DataFrame y 'fixValueInput' el valor a reemplazar
                # En caso de empate de valor con más apariciones en el dataset, se toma el primer valor
                valor_mas_frecuente = dataDictionary_copy.stack().value_counts().idxmax()
                # Reemplaza 'fixValueInput' con el valor más frecuente en el DataFrame completo usando lambda
                dataDictionary_copy = dataDictionary_copy.apply(
                    lambda col: col.replace(fixValueInput, valor_mas_frecuente))

        elif derivedTypeOutput == DerivedType.PREVIOUS:
            # Aplica la función lambda a nivel de columna (axis=0) o a nivel de fila (axis=1)
            # Lambda que sustitutuye cualquier valor igual a FixValueInput del dataframe por el valor de la fila anterior en la misma columna

            dataDictionary_copy = dataDictionary_copy.apply(lambda x: x.where(x != fixValueInput,
                                                                                  other=x.shift(1)), axis=axis_param)
        elif derivedTypeOutput == DerivedType.NEXT:
            # Aplica la función lambda a nivel de columna (axis=0) o a nivel de fila (axis=1)
            dataDictionary_copy = dataDictionary_copy.apply(lambda x: x.where(x != fixValueInput,
                                                                                  other=x.shift(-1)), axis=axis_param)


        return dataDictionary_copy


    def checkInv_FixValue_NumOp(self, dataDictionary: pd.DataFrame, dataTypeInput: DataType, fixValueInput, numOpOutput: Operation, axis_param: int = None) -> pd.DataFrame:
        """
        Check the invariant of the FixValue - NumOp relation
        If the value of 'axis_param' is None, the operation mean or median is applied to the entire dataframe
        params:
            dataDictionary: dataframe with the data
            dataTypeInput: data type of the input value
            FixValueInput: input value to check
            numOpOutput: operation to check the invariant
            axis_param: axis to check the invariant
        Returns:
            dataDictionary with the FixValueInput values replaced by the result of the operation numOpOutput
        """
        fixValueInput, valorNulo=cast_type_FixValue(dataTypeInput, fixValueInput, None, None)

        #Función auxiliar que cambia el valor de FixValueInput al tipo de dato en DataTypeInput
        dataDictionary_copy = dataDictionary.copy()

        if numOpOutput == Operation.INTERPOLATION:
            if axis_param == 0 or axis_param == 1:
                # Aplicamos la interpolación lineal en el DataFrame
                if axis_param == 0:
                    for col in dataDictionary_copy.columns:
                        dataDictionary_copy[col] = dataDictionary_copy[col].apply(
                            lambda x: np.nan if x == fixValueInput else x).interpolate(method='linear', limit_direction='both')
                else:
                    dataDictionary_copy = dataDictionary_copy.apply(
                        lambda row: row.apply(lambda x: np.nan if x == fixValueInput else x).interpolate(
                            method='linear', limit_direction='both'), axis=axis_param)

        elif numOpOutput == Operation.MEAN:
            if axis_param == None:
                # Seleccionar solo columnas con datos numéricos, incluyendo todos los tipos numéricos (int, float, etc.)
                only_numbers_df = dataDictionary_copy.select_dtypes(include=[np.number])
                # Calcular la media de estas columnas numéricas
                mean_value = only_numbers_df.mean().mean()
                # Reemplaza 'fixValueInput' con la media del DataFrame completo usando lambda
                dataDictionary_copy = dataDictionary_copy.apply(
                    lambda col: col.replace(fixValueInput, mean_value))
            elif axis_param == 0 or axis_param == 1:
                # dataDictionary_copy = dataDictionary_copy.apply(lambda x: x.where(x != fixValueInput, other=x.mean()), axis=axis_param)
                dataDictionary_copy = dataDictionary_copy.apply(
                    lambda x: x.apply(
                        lambda y: y if not np.issubdtype(type(y), np.number) or y != fixValueInput
                        else x[x.apply(lambda z: np.issubdtype(type(z), np.number))].mean()), axis=axis_param)

        elif numOpOutput == Operation.MEDIAN:
            if axis_param == None:
                # Seleccionar solo columnas con datos numéricos, incluyendo todos los tipos numéricos (int, float, etc.)
                only_numbers_df = dataDictionary_copy.select_dtypes(include=[np.number])
                # Calcular la media de estas columnas numéricas
                median_value = only_numbers_df.median().median()
                # Reemplaza 'fixValueInput' con la mediana del DataFrame completo usando lambda
                dataDictionary_copy = dataDictionary_copy.apply(
                    lambda col: col.replace(fixValueInput, median_value))
            elif axis_param == 0 or axis_param == 1:
                # dataDictionary_copy = dataDictionary_copy.apply(lambda x: x.where(x != fixValueInput, other=x.mean()), axis=axis_param)
                dataDictionary_copy = dataDictionary_copy.apply(
                    lambda x: x.apply(
                        lambda y: y if not np.issubdtype(type(y), np.number) or y != fixValueInput
                        else x[x.apply(lambda z: np.issubdtype(type(z), np.number))].median()), axis=axis_param)

        elif numOpOutput == Operation.CLOSEST:
            if axis_param is None:
                dataDictionary_copy = dataDictionary_copy.apply(
                    lambda col: col.apply(lambda x: find_closest_value(dataDictionary_copy.stack(),
                                                                       fixValueInput) if x == fixValueInput else x))
            elif axis_param == 0 or axis_param == 1:
                # Reemplazar 'fixValueInput' por el valor numérico más cercano a lo largo de las columnas
                dataDictionary_copy = dataDictionary_copy.apply(
                    lambda col: col.apply(
                        lambda x: find_closest_value(col, fixValueInput) if x == fixValueInput else x), axis=axis_param)


        else:
            raise ValueError("No valid operator")

        return dataDictionary_copy








