# Importing libraries
import unittest
import numpy as np
import pandas as pd
from tqdm import tqdm

# Importing functions and classes from packages
from functions.contract_invariants import ContractsInvariants
from helpers.enumerations import Belong, Operator, Closure, DataType, DerivedType, SpecialType, Operation
from helpers.logger import print_and_log


class InvariantSimpleTest(unittest.TestCase):
    """
    Class to test the contracts with simple test cases

    Attributes:
    pre_post (InvariantSimpleTest): instance of the class InvariantSimpleTest

    Methods:
    """

    def __init__(self):
        """
        Constructor of the class

        Attributes:
        invariants (InvariantSimpleTest): instance of the class InvariantSimpleTest
        """
        self.invariants = ContractsInvariants()

    def execute_All_SimpleTests(self):
        """
        Method to execute all simple tests of the functions of the class
        """
        simple_test_methods = [
            self.execute_CheckInv_FixValue_FixValue,
            self.execute_checkInv_FixValue_DerivedValue,
            self.execute_CheckInv_FixValue_NumOp,
            self.execute_CheckInv_Interval_FixValue,
            self.execute_CheckInv_Interval_DerivedValue,
            self.execute_CheckInv_Interval_NumOp,
            self.execute_CheckInv_SpecialValue_FixValue,
            self.execute_CheckInv_SpecialValue_DerivedValue,
            self.execute_CheckInv_SpecialValue_NumOp
        ]

        print_and_log("")
        print_and_log("--------------------------------------------------")
        print_and_log("------ STARTING INVARIANT SIMPLE TEST CASES ------")
        print_and_log("--------------------------------------------------")
        print_and_log("")

        for simple_test_method in tqdm(simple_test_methods, desc="Running Simple Tests", unit="test"):
            simple_test_method()

        print_and_log("")
        print_and_log("--------------------------------------------------")
        print_and_log("- SIMPLE INVARIANT TEST CASES EXECUTION FINISHED -")
        print_and_log("--------------------------------------------------")
        print_and_log("")

    def execute_CheckInv_FixValue_FixValue(self):
        """
        Execute the simple tests of the function CheckInv_FixValue_FixValue
        """
        print_and_log("Testing CheckInv_FixValue_FixValue Function")
        print_and_log("")
        print_and_log("Casos Básicos añadidos:")

        # Caso 1
        # Comprobar la invariante: cambiar el valor fijo 2 por el valor fijo 999
        # Crear un DataFrame de prueba
        df = pd.DataFrame({'A': [0, 1, 2, 3, 4], 'B': [5, 4, 3, 2, 1]})
        # Definir el valor fijo y la condición para el cambio
        fixValueOutput = 999
        # Aplicar la invariante
        result_df = self.invariants.checkInv_FixValue_FixValue(df, dataTypeInput=DataType(2), fixValueInput=2,
                                                               dataTypeOutput=DataType(6),
                                                               fixValueOutput=fixValueOutput)
        # Definir el resultado esperado
        expected_df = pd.DataFrame({'A': [0, 1, fixValueOutput, 3, 4], 'B': [5, 4, 3, fixValueOutput, 1]})
        # Verificar si el resultado obtenido coincide con el esperado
        pd.testing.assert_frame_equal(result_df, expected_df)
        print("Test Case 1 Passed: the function returned the expected dataframe")

        # Caso 2
        # Comprobar la invariante: cambiar el valor fijo 'Clara' por el valor fijo de fecha 2021-01-01
        # Crear un DataFrame de prueba
        df = pd.DataFrame({'A': ['Clara', 'Ana', 'Clara', 'Clara', 'Clara'], 'B': ['Clara', 'Clara', 'Ana', 'Ana', 'Ana']})
        # Definir el valor fijo y la condición para el cambio
        fixValueOutput = pd.to_datetime('2021-01-01')
        # Aplicar la invariante
        result_df = self.invariants.checkInv_FixValue_FixValue(df, dataTypeInput=DataType(0), fixValueInput='Clara',
                                                               dataTypeOutput=DataType(3),
                                                               fixValueOutput=fixValueOutput)
        # Definir el resultado esperado
        expected_df = pd.DataFrame({'A': [fixValueOutput, 'Ana', fixValueOutput, fixValueOutput, fixValueOutput],
                                    'B': [fixValueOutput, fixValueOutput, 'Ana', 'Ana', 'Ana']})
        # Verificar si el resultado obtenido coincide con el esperado
        pd.testing.assert_frame_equal(result_df, expected_df)
        print("Test Case 2 Passed: the function returned the expected dataframe")

        # Caso 3
        # Comprobar la invariante: cambiar el valor fijo de tipo TIME 2021-01-01 por el valor fijo de tipo boolean True
        # Crear un DataFrame de prueba
        df = pd.DataFrame({'A': [pd.to_datetime('2021-01-01'), pd.to_datetime('2021-09-01'), pd.to_datetime('2021-01-01'), pd.to_datetime('2021-01-01'), pd.to_datetime('2021-01-01')],
                           'B': [pd.to_datetime('2021-01-01'), pd.to_datetime('2021-01-01'), pd.to_datetime('2021-01-01'), pd.to_datetime('2021-01-01'), pd.to_datetime('2021-08-01')]})
        # Definir el valor fijo y la condición para el cambio
        fixValueOutput = True
        # Aplicar la invariante
        result_df = self.invariants.checkInv_FixValue_FixValue(df, dataTypeInput=DataType(1), fixValueInput=pd.to_datetime('2021-01-01'),
                                                                dataTypeOutput=DataType(4),
                                                                fixValueOutput=fixValueOutput)
        # Definir el resultado esperado
        expected_df = pd.DataFrame({'A': [True, pd.to_datetime('2021-09-01'), True, True, True],
                                    'B': [True, True, True, True, pd.to_datetime('2021-08-01')]})
        # Verificar si el resultado obtenido coincide con el esperado
        pd.testing.assert_frame_equal(result_df, expected_df)
        print("Test Case 3 Passed: the function returned the expected dataframe")

        # Caso 4
        # Comprobar la invariante: cambiar el valor fijo string 'Clara' por el valor fijo de tipo FLOAT 3.0
        # Crear un DataFrame de prueba
        df = pd.DataFrame({'A': ['Clara', 'Ana', 'Clara', 'Clara', np.NaN], 'B': ['Clara', 'Clara', 'Ana', '8', None]})
        # Definir el valor fijo y la condición para el cambio
        fixValueOutput = 3.0
        # Aplicar la invariante
        result_df = self.invariants.checkInv_FixValue_FixValue(df, dataTypeInput=DataType(0), fixValueInput='Clara',
                                                                dataTypeOutput=DataType(6),
                                                                fixValueOutput=fixValueOutput)
        # Definir el resultado esperado
        expected_df = pd.DataFrame({'A': [3.0, 'Ana', 3.0, 3.0, np.NaN], 'B': [3.0, 3.0, 'Ana', '8', None]})
        # Verificar si el resultado obtenido coincide con el esperado
        pd.testing.assert_frame_equal(result_df, expected_df)
        print("Test Case 4 Passed: the function returned the expected dataframe")

        # Caso 5
        # Comprobar la invariante: cambiar el valor fijo de tipo FLOAT 3.0 por el valor fijo de tipo STRING 'Clara'
        # Crear un DataFrame de prueba
        df = pd.DataFrame({'A': [3.0, 2.0, 3.0, 3.0, 3.0], 'B': [3.0, 3.0, 2.0, 2.0, 2.0]})
        # Definir el valor fijo y la condición para el cambio
        fixValueOutput = 'Clara'
        # Aplicar la invariante
        result_df = self.invariants.checkInv_FixValue_FixValue(df, fixValueInput=3.0, fixValueOutput=fixValueOutput)
        # Definir el resultado esperado
        expected_df = pd.DataFrame({'A': ['Clara', 2.0, 'Clara', 'Clara', 'Clara'], 'B': ['Clara', 'Clara', 2.0, 2.0, 2.0]})
        # Verificar si el resultado obtenido coincide con el esperado
        pd.testing.assert_frame_equal(result_df, expected_df)
        print("Test Case 5 Passed: the function returned the expected dataframe")

        print_and_log("")
        print_and_log("-----------------------------------------------------------")
        print_and_log("")

    def execute_checkInv_FixValue_DerivedValue(self):
        """
        Execute the simple tests of the function checkInv_FixValue_DerivedValue
        """
        """
        DerivedTypes:
            0: Most Frequently
            1: Previous
            2: Next
        axis_param:
            0: Columns
            1: Rows
            None: All
        """
        print_and_log("Testing checkInv_FixValue_DerivedValue Function")
        print_and_log("")
        print_and_log("Casos Básicos añadidos:")

        # Caso 1
        # Comprobar la invariante: cambiar el valor fijo 0 por el valor derivado 0 (Most Frequently)
        # Crear un DataFrame de prueba
        datadic = pd.DataFrame({'A': [0, 2, 3, 5, 5], 'B': [1, 2, 4, 4, 5], 'C': [1, 2, 3, 4, 3]})
        # Aplicar la invariante
        result = self.invariants.checkInv_FixValue_DerivedValue(dataDictionary=datadic, dataTypeInput=DataType(2), fixValueInput=0,
                                                                derivedTypeOutput=DerivedType(0), axis_param=None)
        # Definir el resultado esperado
        expected = pd.DataFrame({'A': [2, 2, 3, 5, 5], 'B': [1, 2, 4, 4, 5], 'C': [1, 2, 3, 4, 3]})
        # Verificar si el resultado obtenido coincide con el esperado
        pd.testing.assert_frame_equal(result, expected)
        print_and_log("Test Case 1 Passed: the function returned the expected dataframe")

        # Caso 2
        # Comprobar la invariante: cambiar el valor fijo 5 por el valor derivado 2 (Previous) a nivel de columna
        # Crear un DataFrame de prueba
        datadic = pd.DataFrame({'A': [0, 2, 3, 5, 5], 'B': [1, 8, 4, 4, 5], 'C': [1, 2, 3, 4, 3]})
        # Aplicar la invariante
        result = self.invariants.checkInv_FixValue_DerivedValue(dataDictionary=datadic, dataTypeInput=DataType(2), fixValueInput=5,
                                                                derivedTypeOutput=DerivedType(1), axis_param=0)
        # Definir el resultado esperado
        expected = pd.DataFrame({'A': [0, 2, 3, 3, 5], 'B': [1, 8, 4, 4, 4], 'C': [1, 2, 3, 4, 3]})
        # Verificar si el resultado obtenido coincide con el esperado
        pd.testing.assert_frame_equal(result, expected)
        print_and_log("Test Case 2 Passed: the function returned the expected dataframe")

        # Caso 3
        # Comprobar la invariante: cambiar el valor fijo 0 por el valor derivado 3 (Next) a nivel de fila
        # Crear un DataFrame de prueba
        datadic = pd.DataFrame({'A': [0, 2, 3, 4, 5], 'B': [2, 3, 6, 0, 5], 'C': [1, 2, 3, 4, 5]})
        # Aplicar la invariante
        result = self.invariants.checkInv_FixValue_DerivedValue(dataDictionary=datadic, dataTypeInput=DataType(2), fixValueInput=0,
                                                                derivedTypeOutput=DerivedType(2), axis_param=1)
        # Definir el resultado esperado
        expected = pd.DataFrame({'A': [2, 2, 3, 4, 5], 'B': [2, 3, 6, 4, 5], 'C': [1, 2, 3, 4, 5]})
        # Verificar si el resultado obtenido coincide con el esperado
        pd.testing.assert_frame_equal(result, expected)
        print_and_log("Test Case 3 Passed: the function returned the expected dataframe")

        # Caso 4
        # Comprobar la invariante: cambiar el valor fijo 5 por el valor más frecuente a nivel de columna
        # Crear un DataFrame de prueba
        datadic = pd.DataFrame({'A': [0, 2, 3, 3, 5], 'B': [1, 8, 4, 4, 5], 'C': [1, 2, 3, 4, 3]})
        # Aplicar la invariante
        result = self.invariants.checkInv_FixValue_DerivedValue(dataDictionary=datadic, dataTypeInput=DataType(2), fixValueInput=5,
                                                                derivedTypeOutput=DerivedType(0), axis_param=0)
        # Definir el resultado esperado
        expected = pd.DataFrame({'A': [0, 2, 3, 3, 3], 'B': [1, 8, 4, 4, 4], 'C': [1, 2, 3, 4, 3]})
        # Verificar si el resultado obtenido coincide con el esperado
        pd.testing.assert_frame_equal(result, expected)
        print_and_log("Test Case 4 Passed: the function returned the expected dataframe")

        # Caso 5
        # Comprobar la invariante: cambiar el valor fijo 5 por el valor más frecuente a nivel de fila
        # Crear un DataFrame de prueba
        datadic = pd.DataFrame({'A': [0, 2, 3, 3, 5], 'B': [1, 8, 4, 4, 3], 'C': [1, 2, 3, 4, 8], 'D': [4, 5, 6, 7, 8]})
        # Aplicar la invariante
        result = self.invariants.checkInv_FixValue_DerivedValue(dataDictionary=datadic, dataTypeInput=DataType(2), fixValueInput=5,
                                                                derivedTypeOutput=DerivedType(0), axis_param=1)
        # Definir el resultado esperado
        expected = pd.DataFrame({'A': [0, 2, 3, 3, 8], 'B': [1, 8, 4, 4, 3], 'C': [1, 2, 3, 4, 8], 'D': [4, 2, 6, 7, 8]})
        # Verificar si el resultado obtenido coincide con el esperado
        pd.testing.assert_frame_equal(result, expected)
        print_and_log("Test Case 5 Passed: the function returned the expected dataframe")

        # Caso 6
        # Comprobar la invariante: cambiar el valor fijo 5 por el valor previo a nivel de fila
        # Crear un DataFrame de prueba
        datadic = pd.DataFrame({'A': [0, 2, 3, 3, 5], 'B': [1, 8, 5, 4, 3], 'C': [1, 2, 3, 4, 8], 'D': [4, 5, 6, 5, 8]})
        # Aplicar la invariante
        result = self.invariants.checkInv_FixValue_DerivedValue(dataDictionary=datadic, dataTypeInput=DataType(2), fixValueInput=5,
                                                                derivedTypeOutput=DerivedType(1), axis_param=1)
        # Definir el resultado esperado
        expected = pd.DataFrame({'A': [0, 2, 3, 3, 5], 'B': [1, 8, 3, 4, 3], 'C': [1, 2, 3, 4, 8], 'D': [4, 2, 6, 4, 8]})
        # Verificar si el resultado obtenido coincide con el esperado
        pd.testing.assert_frame_equal(result, expected)
        print_and_log("Test Case 6 Passed: the function returned the expected dataframe")

        # Caso 7
        # Comprobar la invariante: cambiar el valor fijo 5 por el valor siguiente a nivel de columna
        # Crear un DataFrame de prueba
        datadic = pd.DataFrame({'A': ["0", 2, 3, 3, 5], 'B': [1, 8, 5, 4, 3], 'C': [1, 2, 3, 4, 8], 'D': [4, 5, 6, 5, 8]})
        # Aplicar la invariante
        result = self.invariants.checkInv_FixValue_DerivedValue(dataDictionary=datadic, dataTypeInput=DataType(2), fixValueInput=5,
                                                                derivedTypeOutput=DerivedType(2), axis_param=0)
        # Definir el resultado esperado
        expected = pd.DataFrame({'A': ["0", 2, 3, 3, 5], 'B': [1, 8, 4, 4, 3], 'C': [1, 2, 3, 4, 8], 'D': [4, 6, 6, 8, 8]})
        # Verificar si el resultado obtenido coincide con el esperado
        pd.testing.assert_frame_equal(result, expected)
        print_and_log("Test Case 7 Passed: the function returned the expected dataframe")

        # Caso 8
        # Comprobar la invariante: cambiar el valor fijo 5 por el valor siguiente a nivel de columna
        # Crear un DataFrame de prueba
        datadic = pd.DataFrame({'A': [0, 2, "Ainhoa", "Ainhoa", 5], 'B': [1, 8, "Ainhoa", 4, 3], 'C': [1, 2, 3, 4, "Ainhoa"], 'D': [4, 5, 6, 5, 8]})
        # Aplicar la invariante
        result = self.invariants.checkInv_FixValue_DerivedValue(dataDictionary=datadic, dataTypeInput=DataType(0), fixValueInput="Ainhoa",
                                                                derivedTypeOutput=DerivedType(2), axis_param=0)
        # Definir el resultado esperado
        expected = pd.DataFrame({'A': [0, 2, "Ainhoa", 5, 5], 'B': [1, 8, 4, 4, 3], 'C': [1, 2, 3, 4, "Ainhoa"], 'D': [4, 5, 6, 5, 8]})
        expected = expected.astype({
            'A': 'object',  # Convertir A a object
            'B': 'object',  # Convertir B a int64
            'C': 'object',  # Convertir C a object
            'D': 'int64'  # Convertir D a object
        })
        # Verificar si el resultado obtenido coincide con el esperado
        pd.testing.assert_frame_equal(result, expected)
        print_and_log("Test Case 8 Passed: the function returned the expected dataframe")

        # Caso 9
        # Comprobar la invariante: cambiar el valor fijo "Ana" por el valor más frecuente a nivel de columna
        # Crear un DataFrame de prueba
        datadic = pd.DataFrame({'A': [0, pd.to_datetime('2021-01-01'), "Ainhoa", "Ana", pd.to_datetime('2021-01-01')], 'B': [pd.to_datetime('2021-01-01'), 8, "Ainhoa", 4, pd.to_datetime('2021-01-01')], 'C': [1, pd.to_datetime('2021-01-01'), 3, 4, "Ainhoa"], 'D': [pd.to_datetime('2021-01-01'), 5, "Ana", 5, 8]})
        # Aplicar la invariante
        result = self.invariants.checkInv_FixValue_DerivedValue(dataDictionary=datadic, dataTypeInput=DataType(0), fixValueInput="Ana",
                                                                derivedTypeOutput=DerivedType(0), axis_param=0)
        # Definir el resultado esperado
        expected = pd.DataFrame({'A': [0, pd.to_datetime('2021-01-01'), "Ainhoa", pd.to_datetime('2021-01-01'), pd.to_datetime('2021-01-01')], 'B': [pd.to_datetime('2021-01-01'), 8, "Ainhoa", 4, pd.to_datetime('2021-01-01')], 'C': [1, pd.to_datetime('2021-01-01'), 3, 4, "Ainhoa"], 'D': [pd.to_datetime('2021-01-01'), 5, 5, 5, 8]})
        # Verificar si el resultado obtenido coincide con el esperado
        pd.testing.assert_frame_equal(result, expected)
        print_and_log("Test Case 9 Passed: the function returned the expected dataframe")

        print_and_log("")
        print_and_log("-----------------------------------------------------------")
        print_and_log("")

    # TODO: Implement the simples tests
    def execute_CheckInv_FixValue_NumOp(self):
        """
        Execute the simple tests of the function checkInv_FixValue_NumOp
        """
        """
        Operation:
            0: Interpolation
            1: Mean
            2: Median
            3: Closest
        Axis:
            0: Columns
            1: Rows
            None: All
        """
        print_and_log("Testing checkInv_FixValue_NumOp Function")
        print_and_log("")
        print_and_log("Casos Básicos añadidos:")

        # Caso 1
        # Comprobar la invariante: cambiar el valor fijo 0 por el valor de operación 0 (Interpolación) a nivel de columna
        # Crear un DataFrame de prueba
        datadic = pd.DataFrame({'A': [0, 2, 3, 4, 5], 'B': [2, 3, 6, 0, 5], 'C': [1, 2, 3, 4, 5]})
        # Aplicar la invariante
        result = self.invariants.checkInv_FixValue_NumOp(dataDictionary=datadic, dataTypeInput=DataType(2),
                                                          fixValueInput=0, numOpOutput=Operation(0), axis_param=0)
        # Definir el resultado esperado
        expected = pd.DataFrame({'A': [2, 2, 3, 4, 5], 'B': [2, 3, 6, 5.5, 5], 'C': [1, 2, 3, 4, 5]})
        expected = expected.astype({
            'A': 'float64',  # Convertir A a float64
            'B': 'float64',  # Convertir B a float64
            'C': 'int64'  # Convertir C a float64
        })
        # Verificar si el resultado obtenido coincide con el esperado
        pd.testing.assert_frame_equal(result, expected)
        print_and_log("Test Case 1 Passed: the function returned the expected dataframe")

        # Case 2
        # Comprobar la invariante: cambiar el valor fijo 0 por el valor de operación 0 (Interpolación) a nivel de fila
        # Crear un DataFrame de prueba
        datadic = pd.DataFrame({'A': [0, 2, 3, 4, 5], 'B': [2, 0, 6, 0, 5], 'C': [1, 2, 3, 4, 5]})
        # Aplicar la invariante
        result = self.invariants.checkInv_FixValue_NumOp(dataDictionary=datadic, dataTypeInput=DataType(2),
                                                            fixValueInput=0, numOpOutput=Operation(0), axis_param=1)
        # Definir el resultado esperado
        expected = pd.DataFrame({'A': [2, 2, 3, 4, 5], 'B': [2, 2, 6, 4, 5], 'C': [1, 2, 3, 4, 5]})
        expected = expected.astype({
            'A': 'float64',  # Convertir A a float64
            'B': 'float64',  # Convertir B a float64
            'C': 'float64'  # Convertir C a float64
        })
        # Verificar si el resultado obtenido coincide con el esperado
        pd.testing.assert_frame_equal(result, expected)
        print_and_log("Test Case 2 Passed: the function returned the expected dataframe")

        # Caso 3
        # Comprobar la invariante: cambiar el valor fijo 0 por el valor de operación 1 (Mean) a nivel de columna
        # Crear un DataFrame de prueba
        datadic = pd.DataFrame({'A': [0, 2, 3, 4, 5], 'B': [2, 3, 6, 0, 5], 'C': [1, 0, 3, 4, 5]})
        # Aplicar la invariante
        result = self.invariants.checkInv_FixValue_NumOp(dataDictionary=datadic, dataTypeInput=DataType(2),
                                                            fixValueInput=0, numOpOutput=Operation(1), axis_param=0)
        # Definir el resultado esperado
        expected = pd.DataFrame({'A': [(0+ 2+ 3+ 4 + 5) / 5, 2, 3, 4, 5], 'B': [2, 3, 6, (2+ 3+ 6+ 5+0) / 5, 5], 'C': [1, (1+ 0+ 3+ 4 + 5) / 5, 3, 4, 5]})
        expected = expected.astype({
            'A': 'float64',  # Convertir A a float64
            'B': 'float64',  # Convertir B a float64
            'C': 'float64'  # Convertir C a float64
        })
        # Verificar si el resultado obtenido coincide con el esperado
        pd.testing.assert_frame_equal(result, expected)
        print_and_log("Test Case 3 Passed: the function returned the expected dataframe")

        # Caso 4
        # Comprobar la invariante: cambiar el valor fijo 0 por el valor de operación 1 (Mean) a nivel de fila
        # Crear un DataFrame de prueba
        datadic = pd.DataFrame({'A': [0, 2, 3, 4, 5], 'B': [2, 0, 6, 0, 5], 'C': [1, 2, 3, 4, 0]})
        # Aplicar la invariante
        result = self.invariants.checkInv_FixValue_NumOp(dataDictionary=datadic, dataTypeInput=DataType(2),
                                                            fixValueInput=0, numOpOutput=Operation(1), axis_param=1)
        # Definir el resultado esperado
        expected = pd.DataFrame({'A': [(2+ 1) / 3, 2, 3, 4, 5], 'B': [2, (2+2)/3, 6, (4+4)/3, 5], 'C': [1, 2, 3, 4, (5+5)/3]})
        expected = expected.astype({
            'A': 'float64',  # Convertir A a float64
            'B': 'float64',  # Convertir B a float64
            'C': 'float64'  # Convertir C a float64
        })
        # Verificar si el resultado obtenido coincide con el esperado
        pd.testing.assert_frame_equal(result, expected)
        print_and_log("Test Case 4 Passed: the function returned the expected dataframe")

        # Caso 5
        # Comprobar la invariante: cambiar el valor fijo 0 por el valor de operación 2 (Median) a nivel de columna
        # Crear un DataFrame de prueba
        datadic = pd.DataFrame({'A': [0, 2, 3, 4, 5], 'B': [2, 3, 6, 0, 5], 'C': [1, 0, 3, 4, 5]})
        # Aplicar la invariante
        result = self.invariants.checkInv_FixValue_NumOp(dataDictionary=datadic, dataTypeInput=DataType(2),
                                                            fixValueInput=0, numOpOutput=Operation(2), axis_param=0)
        # Definir el resultado esperado
        expected = pd.DataFrame({'A': [3, 2, 3, 4, 5], 'B': [2, 3, 6, 3, 5], 'C': [1, 3, 3, 4, 5]})
        expected = expected.astype({
            'A': 'float64',  # Convertir A a float64
            'B': 'float64',  # Convertir B a float64
            'C': 'float64'  # Convertir C a float64
        })
        # Verificar si el resultado obtenido coincide con el esperado
        pd.testing.assert_frame_equal(result, expected)
        print_and_log("Test Case 5 Passed: the function returned the expected dataframe")



        # Caso 8
        # Comprobar la invariante: cambiar el valor fijo 0 por el valor de operación 3 (Closest) a nivel de fila
        # Crear un DataFrame de prueba
        datadic = pd.DataFrame({'A': [0, 2, 3, 4, 5], 'B': [2, 3, 6, 0, 5], 'C': [1, 2, 3, 4, 5]})
        # Aplicar la invariante
        result = self.invariants.checkInv_FixValue_NumOp(dataDictionary=datadic, dataTypeInput=DataType(2),
                                                            fixValueInput=0, numOpOutput=Operation(3), axis_param=1)
        # Definir el resultado esperado
        expected = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [2, 3, 6, 4, 5], 'C': [1, 2, 3, 4, 5]})
        # Verificar si el resultado obtenido coincide con el esperado
        pd.testing.assert_frame_equal(result, expected)
        print_and_log("Test Case 2 Passed: the function returned the expected dataframe")

        print_and_log("")
        print_and_log("-----------------------------------------------------------")
        print_and_log("")

    # TODO: Implement the simples tests
    def execute_CheckInv_Interval_FixValue(self):
        """
        Execute the simple tests of the function checkInv_Interval_FixValue
        """
        print_and_log("Testing checkInv_Interval_FixValue Function")
        print_and_log("")
        print_and_log("Casos Básicos añadidos:")

        # Caso 1
        # Comprobar la invariante: cambiar el rango de valores [0, 5) por el valor fijo 'Suspenso'
        # Crear un DataFrame de prueba
        datadic = pd.DataFrame({'A': [0, 2, 3, 4, 5], 'B': [2, 3, 6, 0, 5], 'C': [1, 2, 3, 4, 5]})
        # Aplicar la invariante
        result = self.invariants.checkInv_Interval_FixValue(dataDictionary=datadic, leftMargin=0, rightMargin=5,
                                                            closureType=Closure(2), dataTypeOutput=DataType(0), fixValueOutput='Suspenso')
        # Definir el resultado esperado
        expected = pd.DataFrame({'A': ['Suspenso', 'Suspenso', 'Suspenso', 'Suspenso', 5],
                                 'B': ['Suspenso', 'Suspenso', 6, 'Suspenso', 5],
                                 'C': ['Suspenso', 'Suspenso', 'Suspenso', 'Suspenso', 5]})
        # Verificar si el resultado obtenido coincide con el esperado
        pd.testing.assert_frame_equal(result, expected)
        print_and_log("Test Case 1 Passed: the function returned the expected dataframe")



        print_and_log("")
        print_and_log("-----------------------------------------------------------")
        print_and_log("")

    # TODO: Implement the simples tests
    def execute_CheckInv_Interval_DerivedValue(self):
        """
        Execute the simple tests of the function checkInv_Interval_DerivedValue
        """
        print_and_log("Testing checkInv_Interval_DerivedValue Function")
        print_and_log("")
        print_and_log("Casos Básicos añadidos:")

        # Caso 1
        # Comprobar la invariante: cambiar el rango de valores (0, 5] por el valor derivado 1 (Previous) a nivel de columna
        # Crear un DataFrame de prueba
        datadic = pd.DataFrame({'A': [0, 2, 3, 4, 5], 'B': [2, 3, 6, 0, 5], 'C': [1, 2, 3, 4, 5]})
        # Aplicar la invariante
        result = self.invariants.checkInv_Interval_DerivedValue(dataDictionary=datadic, leftMargin=0, rightMargin=5, closureType=Closure(1),
                                                                derivedTypeOutput=DerivedType(1), axis_param=0)
        # Definir el resultado esperado
        expected = pd.DataFrame({'A': [0, 0, 2, 3, 4], 'B': [2, 2, 6, 0, 0], 'C': [1, 1, 2, 3, 4]})
        # Verificar si el resultado obtenido coincide con el esperado
        pd.testing.assert_frame_equal(result, expected)
        print_and_log("Test Case 1 Passed: the function returned the expected dataframe")

        # Caso 2
        # Comprobar la invariante: cambiar el rango de valores (0, 5] por el valor derivado 1 (Previous) a nivel de fila
        # Crear un DataFrame de prueba
        datadic = pd.DataFrame({'A': [0, 2, 3, 4, 5], 'B': [2, 3, 6, 0, 5], 'C': [1, 2, 3, 4, 5]})
        # Aplicar la invariante
        result = self.invariants.checkInv_Interval_DerivedValue(dataDictionary=datadic, leftMargin=0, rightMargin=5, closureType=Closure(1),
                                                                derivedTypeOutput=DerivedType(1), axis_param=1)
        # Definir el resultado esperado
        expected = pd.DataFrame({'A': [0, 2, 3, 4, 5], 'B': [0, 2, 6, 0, 5], 'C': [2, 3, 6, 0, 5]})
        # Verificar si el resultado obtenido coincide con el esperado
        pd.testing.assert_frame_equal(result, expected)
        print_and_log("Test Case 2 Passed: the function returned the expected dataframe")


        print_and_log("")
        print_and_log("-----------------------------------------------------------")
        print_and_log("")

    # TODO: Implement the simples tests
    def execute_CheckInv_Interval_NumOp(self):
        """
        Execute the simple tests of the function checkInv_Interval_NumOp
        """
        print_and_log("Testing checkInv_Interval_NumOp Function")
        print_and_log("")
        print_and_log("Casos Básicos añadidos:")

        # Caso 1
        # Comprobar la invariante: cambiar el rango de valores (2, 4] por el valor de operación 0 (Interpolación) a nivel de columna
        # Crear un DataFrame de prueba
        datadic = pd.DataFrame({'A': [0, 2, 3, 4, 5], 'B': [2, 3, 6, 0, 5], 'C': [1, 2, 3, 4, 5]})
        # Aplicar la invariante
        result = self.invariants.checkInv_Interval_NumOp(dataDictionary=datadic, leftMargin=2, rightMargin=4,
                                                            closureType=Closure(1), numOpOutput=Operation(0), axis_param=0)
        # Definir el resultado esperado
        expected = pd.DataFrame({'A': [0, 2, 3, 4, 5], 'B': [2, 4, 6, 0, 5], 'C': [1, 2, 3, 4, 5]})
        expected = expected.astype({
            'A': 'float64',  # Convertir A a float64
            'B': 'float64',  # Convertir B a float64
            'C': 'float64'  # Convertir C a float64
        })
        # Verificar si el resultado obtenido coincide con el esperado
        pd.testing.assert_frame_equal(result, expected)
        print_and_log("Test Case 1 Passed: the function returned the expected dataframe")



        print_and_log("")
        print_and_log("-----------------------------------------------------------")
        print_and_log("")

    # TODO: Implement the simples tests
    def execute_CheckInv_SpecialValue_FixValue(self):
        """
        Execute the simple tests of the function checkInv_SpecialValue_FixValue
        """
        print_and_log("Testing checkInv_SpecialValue_FixValue Function")
        print_and_log("")
        print_and_log("Casos Básicos añadidos:")

        # Caso 1
        # Comprobar la invariante: cambiar el valor especial 2 (Outliers) a nivel de fila por el valor fijo 999
        # Crear un DataFrame de prueba
        datadic = pd.DataFrame({'A': [0, 2, 3, 4, 1], 'B': [2, 3, 4, 6, 10], 'C': [1, 10, 3, 4, 1], 'D': [2, 3, 4, 6, 10], 'E': [1, 10, 3, 4, 1]})
        # Aplicar la invariante
        result = self.invariants.checkInv_SpecialValue_FixValue(dataDictionary=datadic, specialTypeInput=SpecialType(2),
                                                                dataTypeOutput=DataType(2), fixValueOutput=999, axis_param=1)
        # Definir el resultado esperado
        expected = pd.DataFrame({'A': [0, 2, 3, 4, 1], 'B': [2, 3, 4, 6, 999], 'C': [1, 10, 3, 4, 1], 'D': [2, 3, 4, 6, 999], 'E': [1, 10, 3, 4, 1]})
        # Verificar si el resultado obtenido coincide con el esperado
        pd.testing.assert_frame_equal(result, expected)
        print_and_log("Test Case 1 Passed: the function returned the expected dataframe")


        print_and_log("")
        print_and_log("-----------------------------------------------------------")
        print_and_log("")

    # TODO: Implement the simples tests
    def execute_CheckInv_SpecialValue_DerivedValue(self):
        """
        Execute the simple tests of the function checkInv_SpecialValue_DerivedValue
        """
        print_and_log("Testing checkInv_SpecialValue_DerivedValue Function")
        print_and_log("")
        print_and_log("Casos Básicos añadidos:")

        # Caso 1
        # Comprobar la invariante: cambiar el valor especial 1 (Invalid) a nivel de columna por el valor derivado 0 (Most Frequent)
        # Crear un DataFrame de prueba
        datadic = pd.DataFrame({'A': [0, None, 3, 4, 1], 'B': [2, 3, 4, 12, 12], 'C': [10, 0, 3, 3, 2], 'D': [1, 8, 8, 1, 2]})
        # Definir la lista de valores invalidos
        missing_values = [1, 3, 4]
        # Aplicar la invariante
        result = self.invariants.checkInv_SpecialValue_DerivedValue(dataDictionary=datadic, specialTypeInput=SpecialType(1),
                                                                    derivedTypeOutput=DerivedType(0), missing_values=missing_values,
                                                                    axis_param=0)
        # Definir el resultado esperado
        expected = pd.DataFrame({'A': [0, None, 0, 0, 0], 'B': [2, 12, 12, 12, 12], 'C': [10, 0, 3, 3, 2], 'D': [1, 8, 8, 1, 2]})
        # Verificar si el resultado obtenido coincide con el esperado
        pd.testing.assert_frame_equal(result, expected)
        print_and_log("Test Case 1 Passed: the function returned the expected dataframe")

        print_and_log("")
        print_and_log("-----------------------------------------------------------")
        print_and_log("")

    # TODO: Implement the simples tests
    def execute_CheckInv_SpecialValue_NumOp(self):
        """
        Execute the simple tests of the function checkInv_SpecialValue_NumOp
        """
        """
        SpecialTypes:
            0: Missing
            1: Invalid
            2: Outlier
        Operation:
            0: Interpolation
            1: Mean
            2: Median
            3: Closest
        Axis:
            0: Columns
            1: Rows
            None: All
        """
        print_and_log("Testing checkInv_SpecialValue_NumOp Function")
        print_and_log("")
        print_and_log("Casos Básicos añadidos:")

        print_and_log("")
        print_and_log("-----------------------------------------------------------")
        print_and_log("")

        # Caso 1
        datadic = pd.DataFrame(
            {'A': [0, 2, 3, 4, 1], 'B': [2, 3, 4, 6, 12], 'C': [10, 1, 3, 3, 0], 'D': [1, 8.2, 6, 1, 2]})
        missing_values = [1, 3, 4]
        expected_df = pd.DataFrame(
            {'A': [0, 2, 2, 2.0, 2], 'B': [2, 2 + 4/3, 2 + 8/3, 6, 12], 'C': [10, 7.5, 5, 2.5, 0], 'D': [8.2, 8.2, 6, 4, 2]})
        result_df = self.invariants.checkInv_SpecialValue_NumOp(dataDictionary=datadic, specialTypeInput=SpecialType(0),
                                                             numOpOutput=Operation(0), missing_values=missing_values,
                                                             axis_param=0)
        pd.testing.assert_frame_equal(expected_df, result_df)
        print_and_log("Test Case 1 Passed: the function returned the expected dataframe")

        # Caso 2
        # Probamos a aplicar la operación closest sobre un dataframe con missing values (existen valores nulos)
        datadic = pd.DataFrame(
            {'A': [0, 2, 3, 4, 1], 'B': [2, 3, 4, 6, 12], 'C': [10, None, 3, 3, 0], 'D': [1, 8.2, np.NaN, 1, 2]})
        missing_values = [1, 3, 4]
        expected_exception = ValueError
        with self.assertRaises(expected_exception) as context:
            result = self.invariants.checkInv_SpecialValue_NumOp(dataDictionary=datadic, specialTypeInput=SpecialType(0),
                                                             numOpOutput=Operation(3), missing_values=missing_values,
                                                             axis_param=0)
        print_and_log("Test Case 2 Passed: Expected ValueError, got ValueError")













