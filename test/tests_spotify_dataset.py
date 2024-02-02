import os
import unittest

import numpy as np
import pandas as pd

from functions.contract_pre_post import ContractsPrePost
from helpers.enumerations import Belong, Operator, Closure
from helpers.logger import print_and_log


class ContractWithDatasetTests(unittest.TestCase):
    """
    Class to test the contracts with simple test cases

    Attributes:
    pre_post (ContractsPrePost): instance of the class ContractsPrePost
    dataDictionary (pd.DataFrame): dataframe with the external dataset. It must be loaded in the __init__ method

    Methods:
    execute_CheckFieldRange_Tests: execute the simple tests of the function checkFieldRange
    execute_CheckFixValueRangeString_Tests: execute the simple tests of the function checkFixValueRangeString
    execute_CheckFixValueRangeFloat_Tests: execute the simple tests of the function checkFixValueRangeFloat
    execute_CheckFixValueRangeDateTime_Tests: execute the simple tests of the function checkFixValueRangeDateTime
    """
    def __init__(self):
        """
        Constructor of the class

        Attributes:
        pre_post (ContractsPrePost): instance of the class ContractsPrePost
        dataDictionary (pd.DataFrame): dataframe with the external dataset. It must be loaded in the __init__ method
        """
        self.pre_post = ContractsPrePost()

        # Obtiene la ruta del directorio actual del script
        directorio_actual = os.path.dirname(os.path.abspath(__file__))
        # Construye la ruta al archivo CSV
        ruta_csv = os.path.join(directorio_actual, '../test_datasets/spotify_songs/spotify_songs.csv')
        # Crea el dataframe a partir del archivo CSV
        self.data_dictionary = pd.read_csv(ruta_csv)

        print_and_log("")
        print_and_log("--------------------------------------------------")
        print_and_log("---------- STARTING DATASET TEST CASES -----------")
        print_and_log("--------------------------------------------------")
        print_and_log("")

    def executeAll_DatasetTests(self):
        """
        Execute all the tests of the dataset
        """
        self.execute_CheckFieldRange_Tests()
        self.execute_CheckFixValueRangeString_Tests()
        self.execute_CheckFixValueRangeFloat_Tests()
        self.execute_CheckFixValueRangeDateTime_Tests()
        self.execute_checkIntervalRangeFloat_Tests()
        self.execute_CheckMissingRange_Tests()
        self.execute_CheckInvalidValues_Tests()

    def execute_CheckFieldRange_Tests(self):
        """
        Execute the datasets_tests of the checkFieldRange function
        """
        print_and_log("Testing CheckFieldRange Function")
        print_and_log("")

        print_and_log("Casos de test con dataset añadidos:")

        # Case 1 of checkFieldRange
        # Check that fields 'c1' and 'c2' belong to the data dictionary. It must return True
        fields = ['track_id', 'loudness', 'playlist_id']
        belong = 0
        result = self.pre_post.checkFieldRange(fields=fields, dataDictionary=self.data_dictionary, belongOp=Belong(belong))
        assert result is True, "Test Case 1 Failed: Expected True, but got False"
        print_and_log("Test Case 1 Passed: Expected True, got True")

        # Case 2 of checkFieldRange
        # Check that fields 'c2' and 'c3' belong to the data dictionary. It must return False as 'c3' does not belong
        fields = ['track_id', 'loudness', 'c3']
        belong = 0
        result = self.pre_post.checkFieldRange(fields=fields, dataDictionary=self.data_dictionary, belongOp=Belong(belong))
        assert result is False, "Test Case 2 Failed: Expected False, but got True"
        print_and_log("Test Case 2 Passed: Expected False, got False")

        # Case 3 of checkFieldRange
        # Check that fields 'c2' and 'c3' don't belong to the data dictionary.It must return True as 'c2' doesn't belong
        fields = ['c2', 'track_id', 'loudness']
        belong = 1
        result = self.pre_post.checkFieldRange(fields=fields, dataDictionary=self.data_dictionary, belongOp=Belong(belong))
        assert result is True, "Test Case 3 Failed: Expected True, but got False"
        print_and_log("Test Case 3 Passed: Expected True, got True")

        print_and_log("")
        print_and_log("Casos Básicos añadidos:")

        # Case 4 of checkFieldRange
        # Check that fields 'c1' and 'c2' don't belong to the data dictionary. It must return False as both belong
        fields = ['track_id', 'loudness', 'valence']
        belong = 1
        result = self.pre_post.checkFieldRange(fields=fields, dataDictionary=self.data_dictionary, belongOp=Belong(belong))
        assert result is False, "Test Case 4 Failed: Expected False, but got True"
        print_and_log("Test Case 4 Passed: Expected False, got False")
        print_and_log("")
        print_and_log("-----------------------------------------------------------")
        print_and_log("")

    def execute_CheckFixValueRangeString_Tests(self):
        """
        Execute the simple tests of the function checkFixValueRange
        """
        print_and_log("Testing CheckFixValueRangeString Function")

        print_and_log("")
        print_and_log("Casos de test con dataset añadidos:")

        # Example 13 of checkFixValueRange
        # Check that value None belongs to the data dictionary in field 'c1' and that
        # it appears less or equal than 30% of the times
        value = None
        belongOp = 0  # Belong
        field = 'track_artist'
        quant_op = 2  # lessEqual
        quant_rel = 0.3
        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=self.data_dictionary,
                                                        belongOp=Belong(belongOp), field=field, quant_rel=quant_rel,
                                                        quant_op=Operator(quant_op))
        assert result is True, "Test Case 13 Failed: Expected True, but got False"
        print_and_log("Test Case 13 Passed: Expected True, got True")

        # Example 14 of checkFixValueRange
        # Check that value None belongs to the data dictionary in field 'c1' and that
        # it appears less or equal than 30% of the times
        value = None
        belongOp = 0  # Belong
        field = 'track_name'
        quant_op = 1  # greater
        quant_rel = 0.3
        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=self.data_dictionary,
                                                        belongOp=Belong(belongOp), field=field, quant_rel=quant_rel,
                                                        quant_op=Operator(quant_op))
        assert result is False, "Test Case 14 Failed: Expected False, but got True"
        print_and_log("Test Case 14 Passed: Expected False, got False")

        # Example 18 of checkFixValueRange
        # Check that value 1 doesn't belong to the data dictionary in field 'c1'
        value = 'Una cancion'
        belongOp = 1  # NotBelong
        field = 'track_name'
        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=self.data_dictionary,
                                                        belongOp=Belong(belongOp), field=field)
        assert result is True, "Test Case 18 Failed: Expected True, but got False"
        print_and_log("Test Case 18 Passed: Expected True, got True")

        # Example 14.5 of checkFixValueRange
        # CASO DE QUE NO SE PUEDEN PROPORCIONAR QUANT_REL Y QUANT_ABS A LA VEZ??? VALUERROR
        value = None
        belongOp = 0  # Belong
        field = 'track_name'
        quant_op = 2  # lessEqual
        quant_rel = 0.4
        quant_abs = 50
        expected_exception = ValueError
        with self.assertRaises(expected_exception) as context:
            self.pre_post.checkFixValueRange(value=value, dataDictionary=self.data_dictionary,
                                                   belongOp=Belong(belongOp), field=field, quant_rel=quant_rel,
                                                   quant_abs=quant_abs, quant_op=Operator(quant_op))
        print_and_log("Test Case 14.5 Passed: Expected ValueError, got ValueError")

        # --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        print_and_log("")
        print_and_log("Casos añadidos:")

        # Example 1 of checkFixValueRange
        value = 'Maroon 5'
        belongOp = 0  # Belong
        field = None  # None
        quant_op = None  # None
        quant_rel = 0.3
        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=self.data_dictionary,
                                                        belongOp=Belong(belongOp), field=field, quant_rel=quant_rel,
                                                        quant_op=quant_op)
        assert result is True, "Test Case 1 Failed: Expected True, but got False"
        print_and_log("Test Case 1 Passed: Expected True, got True")

        # Example 2 of checkFixValueRange
        value = 'Maroon 4'
        belongOp = 0  # Belong
        field = None  # None
        quant_op = None  # None
        quant_rel = 0.3
        # Ejecutar la función y verificar que devuelve False
        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=self.data_dictionary,
                                                        belongOp=Belong(belongOp), field=field, quant_rel=quant_rel,
                                                        quant_op=quant_op)
        assert result is False, "Test Case 2 Failed: Expected False, but got True"
        print_and_log("Test Case 2 Passed: Expected False, got False")

        # Example 3 of checkFixValueRange
        value = 'Maroon 5'
        belongOp = 0  # Belong
        field = None
        quant_op = 2  # lessEqual
        quant_rel = 0.3

        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=self.data_dictionary,
                                                        belongOp=Belong(belongOp), field=field, quant_rel=quant_rel,
                                                        quant_op=Operator(quant_op))
        assert result is True, "Test Case 3 Failed: Expected True, but got False"
        print_and_log("Test Case 3 Passed: Expected True, got True")

        # Example 4 of checkFixValueRange
        value = 'Maroon 5'
        belongOp = 0  # Belong
        field = None
        quant_op = 1  # greater
        quant_rel = 0.4

        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=self.data_dictionary,
                                                        belongOp=Belong(belongOp), field=field, quant_rel=quant_rel,
                                                        quant_op=Operator(quant_op))
        assert result is False, "Test Case 4 Failed: Expected False, but got True"
        print_and_log("Test Case 4 Passed: Expected False, got False")

        # Example 5 of checkFixValueRange
        value = 'Maroon 5'
        belongOp = 0  # Belong
        field = None
        quant_op = 1  # greater
        quant_abs = 30

        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=self.data_dictionary,
                                                        belongOp=Belong(belongOp), field=field, quant_abs=quant_abs,
                                                        quant_op=Operator(quant_op))
        assert result is True, "Test Case 5 Failed: Expected True, but got False"
        print_and_log("Test Case 5 Passed: Expected True, got True")

        # Example 6 of checkFixValueRange
        value = None
        belongOp = 0  # Belong
        field = None
        quant_op = 2  # lessEqual
        quant_abs = 50

        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=self.data_dictionary,
                                                        belongOp=Belong(belongOp), field=field, quant_abs=quant_abs,
                                                        quant_op=Operator(quant_op))
        assert result is False, "Test Case 6 Failed: Expected False, but got True"
        print_and_log("Test Case 6 Passed: Expected False, got False")

        # Example 8 of checkFixValueRange
        value = '3'
        belongOp = 1  # Not Belong
        # # Ejecutar la función y verificar que devuelve False
        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=self.data_dictionary,
                                                        belongOp=Belong(belongOp))
        assert result is True, "Test Case 8 Failed: Expected True, but got False"
        print_and_log("Test Case 8 Passed: Expected True, got True")

        # Example 9 of checkFixValueRange
        value = 'Avicii'
        belongOp = 1  # Not Belong
        # # Ejecutar la función y verificar que devuelve False
        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=self.data_dictionary,
                                                        belongOp=Belong(belongOp))
        assert result is False, "Test Case 9 Failed: Expected False, but got True"
        print_and_log("Test Case 9 Passed: Expected False, got False")

        # Example 11 of checkFixValueRange
        value = 'Katy Perry'
        belongOp = 0  # Belong
        field = 'track_artist'
        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=self.data_dictionary, field=field,
                                                  belongOp=Belong(belongOp))
        assert result is True, "Test Case 11 Failed: Expected True, but got False"
        print_and_log("Test Case 11 Passed: Expected True, got True")

        # Example 12 of checkFixValueRange
        value = 'Bad Bunny'
        belongOp = 0  # Belong
        field = 'track_name'
        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=self.data_dictionary, field=field,
                                                  belongOp=Belong(belongOp))
        assert result is False, "Test Case 12 Failed: Expected False, but got True"
        print_and_log("Test Case 12 Passed: Expected False, got False")

        # Example 15 of checkFixValueRange
        value = None
        belongOp = 0  # Belong
        field = 'track_artist'
        quant_op = 1  # greater
        quant_abs = 2
        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=self.data_dictionary, field=field,
                                                  quant_abs=quant_abs, quant_op=Operator(quant_op),
                                                  belongOp=Belong(belongOp))
        assert result is True, "Test Case 15 Failed: Expected True, but got False"
        print_and_log("Test Case 15 Passed: Expected True, got True")

        # Example 16 of checkFixValueRange
        value = 'Poison'
        belongOp = 0  # Belong
        field = 'track_name'
        quant_op = 1  # greater
        quant_abs = 30
        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=self.data_dictionary, field=field,
                                                  quant_abs=quant_abs, quant_op=Operator(quant_op),
                                                  belongOp=Belong(belongOp))
        assert result is False, "Test Case 16 Failed: Expected False, but got True"
        print_and_log("Test Case 16 Passed: Expected False, got False")

        # Example 18 of checkFixValueRange
        value = 'Maroon 4'
        belongOp = 1  # Not Belong
        field = 'track_artist'
        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=self.data_dictionary, field=field,
                                                  belongOp=Belong(belongOp))
        assert result is True, "Test Case 18 Failed: Expected True, but got False"
        print_and_log("Test Case 18 Passed: Expected True, got True")

        # Example 19 of checkFixValueRange
        value = "Maroon 5"
        belongOp = 1  # Not Belong
        field = 'track_artist'
        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=self.data_dictionary, field=field,
                                                  belongOp=Belong(belongOp))
        assert result is False, "Test Case 19 Failed: Expected False, but got True"
        print_and_log("Test Case 19 Passed: Expected False, got False")

        # --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        # Casos de error añadidos
        print_and_log("")
        print_and_log("Casos de error añadidos:")

        # Example 4.5 of checkFixValueRange
        # CASO DE QUE quant_rel y quant_abs NO SEAN None A LA VEZ (existen los dos) VALUERROR
        value = None
        belongOp = 0  # Belong
        field = None
        quant_op = 2  # lessEqual
        quant_rel = 0.4
        quant_abs = 50
        expected_exception = ValueError
        with self.assertRaises(expected_exception) as context:
            self.pre_post.checkFixValueRange(value=value, dataDictionary=self.data_dictionary,
                                                   belongOp=Belong(belongOp), field=field, quant_rel=quant_rel,
                                                   quant_abs=quant_abs, quant_op=Operator(quant_op))

        print_and_log(f"Test Case 4.5 Passed: Expected ValueError, got ValueError")
        # Example 7 of checkFixValueRange
        # CASO DE QUE no existan ni quant_rel ni quant_abs cuando belongOp es BELONG Y quant_op no es None VALUERROR
        value = "Katy Perry"
        belongOp = 0  # Belong
        field = None
        quant_op = 2  # lessEqual
        expected_exception = ValueError
        with self.assertRaises(expected_exception) as context:
            result = self.pre_post.checkFixValueRange(value=value, dataDictionary=self.data_dictionary,
                                                      belongOp=Belong(belongOp), field=field,
                                                      quant_op=Operator(quant_op))
        print_and_log("Test Case 7 Passed: Expected ValueError, got ValueError")

        # # Example 10 of checkFixValueRange
        value = 'Martin Garrix'
        belongOp = 1  # Not Belong
        quant_op = 3
        expected_exception = ValueError
        with self.assertRaises(expected_exception) as context:
            result = self.pre_post.checkFixValueRange(value=value, dataDictionary=self.data_dictionary,
                                                      belongOp=Belong(belongOp), quant_op=Operator(quant_op))
        print_and_log("Test Case 10 Passed: Expected ValueError, got ValueError")
        print_and_log("")
        print_and_log("-----------------------------------------------------------")
        print_and_log("")

    def execute_CheckFixValueRangeFloat_Tests(self):
        """
        Execute the simple tests of the function checkFixValueRange
        """
        print_and_log("Testing CheckFixValueRangeString Function")

        print_and_log("")
        print_and_log("Casos de test con dataset añadidos:")

        # Example 13 of checkFixValueRange
        # Check that value None belongs to the data dictionary in field 'c1' and that
        # it appears less or equal than 30% of the times
        value = None
        belongOp = 0  # Belong
        field = 'key'
        quant_op = 2  # lessEqual
        quant_rel = 0.3
        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=self.data_dictionary,
                                                        belongOp=Belong(belongOp), field=field, quant_rel=quant_rel,
                                                        quant_op=Operator(quant_op))
        assert result is True, "Test Case 13 Failed: Expected True, but got False"
        print_and_log("Test Case 13 Passed: Expected True, got True")

        # Example 14 of checkFixValueRange
        # Check that value None belongs to the data dictionary in field 'c1' and that
        # it appears less or equal than 30% of the times
        value = None
        belongOp = 0  # Belong
        field = 'key'
        quant_op = 1  # greater
        quant_rel = 0.3
        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=self.data_dictionary,
                                                        belongOp=Belong(belongOp), field=field, quant_rel=quant_rel,
                                                        quant_op=Operator(quant_op))
        assert result is False, "Test Case 14 Failed: Expected False, but got True"
        print_and_log("Test Case 14 Passed: Expected False, got False")

        # Example 18 of checkFixValueRange
        # Check that value 1 doesn't belong to the data dictionary in field 'c1'
        value = 45.8
        belongOp = 1  # NotBelong
        field = 'key'
        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=self.data_dictionary,
                                                        belongOp=Belong(belongOp), field=field)
        assert result is True, "Test Case 18 Failed: Expected True, but got False"
        print_and_log("Test Case 18 Passed: Expected True, got True")

        # Example 14.5 of checkFixValueRange
        # CASO DE QUE NO SE PUEDEN PROPORCIONAR QUANT_REL Y QUANT_ABS A LA VEZ??? VALUERROR
        value = None
        belongOp = 0  # Belong
        field = 'key'
        quant_op = 2  # lessEqual
        quant_rel = 0.4
        quant_abs = 50
        expected_exception = ValueError
        with self.assertRaises(expected_exception) as context:
            self.pre_post.checkFixValueRange(value=value, dataDictionary=self.data_dictionary,
                                                   belongOp=Belong(belongOp), field=field, quant_rel=quant_rel,
                                                   quant_abs=quant_abs, quant_op=Operator(quant_op))
        print_and_log("Test Case 14.5 Passed: Expected ValueError, got ValueError")

        # --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        print_and_log("")
        print_and_log("Casos añadidos:")

        # Example 1 of checkFixValueRange
        value = 2
        belongOp = 0  # Belong
        field = None  # None
        quant_op = None  # None
        quant_rel = 0.3
        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=self.data_dictionary,
                                                        belongOp=Belong(belongOp), field=field, quant_rel=quant_rel,
                                                        quant_op=quant_op)
        assert result is True, "Test Case 1 Failed: Expected True, but got False"
        print_and_log("Test Case 1 Passed: Expected True, got True")

        # Example 2 of checkFixValueRange
        value = 400
        belongOp = 0  # Belong
        field = None  # None
        quant_op = None  # None
        quant_rel = 0.3
        # Ejecutar la función y verificar que devuelve False
        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=self.data_dictionary,
                                                        belongOp=Belong(belongOp), field=field, quant_rel=quant_rel,
                                                        quant_op=quant_op)
        assert result is False, "Test Case 2 Failed: Expected False, but got True"
        print_and_log("Test Case 2 Passed: Expected False, got False")

        # Example 3 of checkFixValueRange
        value = 1
        belongOp = 0  # Belong
        field = None
        quant_op = 2  # lessEqual
        quant_rel = 0.3

        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=self.data_dictionary,
                                                        belongOp=Belong(belongOp), field=field, quant_rel=quant_rel,
                                                        quant_op=Operator(quant_op))
        assert result is True, "Test Case 3 Failed: Expected True, but got False"
        print_and_log("Test Case 3 Passed: Expected True, got True")

        # Example 4 of checkFixValueRange
        value = 1
        belongOp = 0  # Belong
        field = None
        quant_op = 1  # greater
        quant_rel = 0.4

        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=self.data_dictionary,
                                                        belongOp=Belong(belongOp), field=field, quant_rel=quant_rel,
                                                        quant_op=Operator(quant_op))
        assert result is False, "Test Case 4 Failed: Expected False, but got True"
        print_and_log("Test Case 4 Passed: Expected False, got False")

        # Example 5 of checkFixValueRange
        value = 1
        belongOp = 0  # Belong
        field = None
        quant_op = 1  # greater
        quant_abs = 30

        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=self.data_dictionary,
                                                        belongOp=Belong(belongOp), field=field, quant_abs=quant_abs,
                                                        quant_op=Operator(quant_op))
        assert result is True, "Test Case 5 Failed: Expected True, but got False"
        print_and_log("Test Case 5 Passed: Expected True, got True")

        # Example 6 of checkFixValueRange
        value = None
        belongOp = 0  # Belong
        field = None
        quant_op = 2  # lessEqual
        quant_abs = 50

        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=self.data_dictionary,
                                                        belongOp=Belong(belongOp), field=field, quant_abs=quant_abs,
                                                        quant_op=Operator(quant_op))
        assert result is False, "Test Case 6 Failed: Expected False, but got True"
        print_and_log("Test Case 6 Passed: Expected False, got False")

        # Example 8 of checkFixValueRange
        value = 804.8
        belongOp = 1  # Not Belong
        # # Ejecutar la función y verificar que devuelve False
        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=self.data_dictionary,
                                                        belongOp=Belong(belongOp))
        assert result is True, "Test Case 8 Failed: Expected True, but got False"
        print_and_log("Test Case 8 Passed: Expected True, got True")

        # Example 9 of checkFixValueRange
        value = 3
        belongOp = 1  # Not Belong
        # # Ejecutar la función y verificar que devuelve False
        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=self.data_dictionary,
                                                        belongOp=Belong(belongOp))
        assert result is False, "Test Case 9 Failed: Expected False, but got True"
        print_and_log("Test Case 9 Passed: Expected False, got False")

        # Example 11 of checkFixValueRange
        value = 4
        belongOp = 0  # Belong
        field = 'key'
        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=self.data_dictionary, field=field,
                                                  belongOp=Belong(belongOp))
        assert result is True, "Test Case 11 Failed: Expected True, but got False"
        print_and_log("Test Case 11 Passed: Expected True, got True")

        # Example 12 of checkFixValueRange
        value = 0.146
        belongOp = 0  # Belong
        field = 'key'
        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=self.data_dictionary, field=field,
                                                  belongOp=Belong(belongOp))
        assert result is False, "Test Case 12 Failed: Expected False, but got True"
        print_and_log("Test Case 12 Passed: Expected False, got False")

        # Example 15 of checkFixValueRange
        value = None
        belongOp = 0  # Belong
        field = 'key'
        quant_op = 1  # greater
        quant_abs = 2
        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=self.data_dictionary, field=field,
                                                  quant_abs=quant_abs, quant_op=Operator(quant_op),
                                                  belongOp=Belong(belongOp))
        assert result is True, "Test Case 15 Failed: Expected True, but got False"
        print_and_log("Test Case 15 Passed: Expected True, got True")

        # Example 16 of checkFixValueRange
        value = 1
        belongOp = 0  # Belong
        field = 'track_name'
        quant_op = 1  # greater
        quant_abs = 3000
        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=self.data_dictionary, field=field,
                                                  quant_abs=quant_abs, quant_op=Operator(quant_op),
                                                  belongOp=Belong(belongOp))
        assert result is False, "Test Case 16 Failed: Expected False, but got True"
        print_and_log("Test Case 16 Passed: Expected False, got False")

        # Example 18 of checkFixValueRange
        value = 15
        belongOp = 1  # Not Belong
        field = 'key'
        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=self.data_dictionary, field=field,
                                                  belongOp=Belong(belongOp))
        assert result is True, "Test Case 18 Failed: Expected True, but got False"
        print_and_log("Test Case 18 Passed: Expected True, got True")

        # Example 19 of checkFixValueRange
        value = 8
        belongOp = 1  # Not Belong
        field = 'key'
        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=self.data_dictionary, field=field,
                                                  belongOp=Belong(belongOp))
        assert result is False, "Test Case 19 Failed: Expected False, but got True"
        print_and_log("Test Case 19 Passed: Expected False, got False")

        # --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        # Casos de error añadidos
        print_and_log("")
        print_and_log("Casos de error añadidos:")

        # Example 4.5 of checkFixValueRange
        # CASO DE QUE quant_rel y quant_abs NO SEAN None A LA VEZ (existen los dos) VALUERROR
        value = None
        belongOp = 0  # Belong
        field = None
        quant_op = 2  # lessEqual
        quant_rel = 0.4
        quant_abs = 50
        expected_exception = ValueError
        with self.assertRaises(expected_exception) as context:
            self.pre_post.checkFixValueRange(value=value, dataDictionary=self.data_dictionary,
                                             belongOp=Belong(belongOp), field=field, quant_rel=quant_rel,
                                             quant_abs=quant_abs, quant_op=Operator(quant_op))

        print_and_log(f"Test Case 4.5 Passed: Expected ValueError, got ValueError")
        # Example 7 of checkFixValueRange
        # CASO DE QUE no existan ni quant_rel ni quant_abs cuando belongOp es BELONG Y quant_op no es None VALUERROR
        value = 3
        belongOp = 0  # Belong
        field = None
        quant_op = 2  # lessEqual
        expected_exception = ValueError
        with self.assertRaises(expected_exception) as context:
            result = self.pre_post.checkFixValueRange(value=value, dataDictionary=self.data_dictionary,
                                                      belongOp=Belong(belongOp), field=field,
                                                      quant_op=Operator(quant_op))
        print_and_log("Test Case 7 Passed: Expected ValueError, got ValueError")

        # # Example 10 of checkFixValueRange
        value = 5
        belongOp = 1  # Not Belong
        quant_op = 3
        expected_exception = ValueError
        with self.assertRaises(expected_exception) as context:
            result = self.pre_post.checkFixValueRange(value=value, dataDictionary=self.data_dictionary,
                                                      belongOp=Belong(belongOp), quant_op=Operator(quant_op))
        print_and_log("Test Case 10 Passed: Expected ValueError, got ValueError")
        print_and_log("")
        print_and_log("-----------------------------------------------------------")
        print_and_log("")


    def execute_CheckFixValueRangeDateTime_Tests(self):     #TODO: hacer de la misma forma que los anteriores
        """
        Execute the simple tests of the function checkFixValueRange
        """
        print_and_log("Testing CheckFixValueRangeDateTime Function")
        print_and_log("")
        print_and_log("Casos de test con dataset añadidos:")

        # Eliminar los guiones de la columna 'track_album_release_date'
        # dataDictionary['track_album_release_date']=dataDictionary['track_album_release_date'].str.replace('-', '')
        # Convertir la columna 'track_album_release_date' a tipo timestamp
        preprocessed_data_dictionary = self.data_dictionary.copy()
        preprocessed_data_dictionary['track_album_release_date'] = pd.to_datetime(preprocessed_data_dictionary['track_album_release_date'], errors='coerce')


        # Example 13 of checkFixValueRange
        # Check that value None belongs to the data dictionary in field 'track_album_release_date' and that
        # it appears less or equal than 30% of the times
        value = pd.Timestamp('20180310')
        belongOp = 0  # Belong
        field = 'track_album_release_date'
        quant_op = 2  # lessEqual
        quant_rel = 0.3
        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=preprocessed_data_dictionary,
                                                        belongOp=Belong(belongOp), field=field, quant_rel=quant_rel,
                                                        quant_op=Operator(quant_op))
        assert result is True, "Test Case 13 Failed: Expected True, but got False"
        print_and_log("Test Case 13 Passed: Expected True, got True")

        # Example 14 of checkFixValueRange
        # Check that value None belongs to the data dictionary in field 'c1' and that
        # it appears less or equal than 30% of the times
        value = None
        belongOp = 0  # Belong
        field = 'track_album_release_date'
        quant_op = 1  # greater
        quant_rel = 0.3
        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=preprocessed_data_dictionary,
                                                        belongOp=Belong(belongOp), field=field, quant_rel=quant_rel,
                                                        quant_op=Operator(quant_op))
        assert result is False, "Test Case 14 Failed: Expected False, but got True"
        print_and_log("Test Case 14 Passed: Expected False, got False")

        # Example 18 of checkFixValueRange
        # Check that value 1 doesn't belong to the data dictionary in field 'track_album_release_date'
        value = pd.Timestamp('20250310')
        belongOp = 1  # NotBelong
        field = 'track_album_release_date'
        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=preprocessed_data_dictionary,
                                                        belongOp=Belong(belongOp), field=field)
        assert result is True, "Test Case 18 Failed: Expected True, but got False"
        print_and_log("Test Case 18 Passed: Expected True, got True")

        # Example 14.5 of checkFixValueRange
        # CASO DE QUE NO SE PUEDEN PROPORCIONAR QUANT_REL Y QUANT_ABS A LA VEZ --> VALUERROR
        value = None
        belongOp = 0  # Belong
        field = 'track_album_release_date'
        quant_op = 2  # lessEqual
        quant_rel = 0.4
        quant_abs = 50
        expected_exception = ValueError
        with self.assertRaises(expected_exception) as context:
            self.pre_post.checkFixValueRange(value=value, dataDictionary=preprocessed_data_dictionary,
                                                   belongOp=Belong(belongOp), field=field, quant_rel=quant_rel,
                                                   quant_abs=quant_abs, quant_op=Operator(quant_op))
        print_and_log("Test Case 14.5 Passed: Expected ValueError, got ValueError")

        # --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        print_and_log("")
        print_and_log("Casos añadidos:")

        # Example 1 of checkFixValueRange
        value = pd.Timestamp('20180721')
        belongOp = 0  # Belong
        field = None  # None
        quant_op = None  # None
        quant_rel = 0.3
        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=preprocessed_data_dictionary,
                                                        belongOp=Belong(belongOp), field=field, quant_rel=quant_rel,
                                                        quant_op=quant_op)
        assert result is True, "Test Case 1 Failed: Expected True, but got False"
        print_and_log("Test Case 1 Passed: Expected True, got True")

        # Example 2 of checkFixValueRange
        value = pd.Timestamp('20000721')
        belongOp = 0  # Belong
        field = None  # None
        quant_op = None  # None
        quant_rel = 0.3
        # Ejecutar la función y verificar que devuelve False
        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=preprocessed_data_dictionary,
                                                        belongOp=Belong(belongOp), field=field, quant_rel=quant_rel,
                                                        quant_op=quant_op)
        assert result is False, "Test Case 2 Failed: Expected False, but got True"
        print_and_log("Test Case 2 Passed: Expected False, got False")

        # Example 3 of checkFixValueRange
        value = pd.Timestamp('20180310')
        belongOp = 0  # Belong
        field = None
        quant_op = 2  # lessEqual
        quant_rel = 0.3

        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=preprocessed_data_dictionary,
                                                        belongOp=Belong(belongOp), field=field, quant_rel=quant_rel,
                                                        quant_op=Operator(quant_op))
        assert result is True, "Test Case 3 Failed: Expected True, but got False"
        print_and_log("Test Case 3 Passed: Expected True, got True")

        # Example 4 of checkFixValueRange
        value = pd.Timestamp('20180721')
        belongOp = 0  # Belong
        field = None
        quant_op = 1  # greater
        quant_rel = 0.4

        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=preprocessed_data_dictionary,
                                                        belongOp=Belong(belongOp), field=field, quant_rel=quant_rel,
                                                        quant_op=Operator(quant_op))
        assert result is False, "Test Case 4 Failed: Expected False, but got True"
        print_and_log("Test Case 4 Passed: Expected False, got False")

        # Example 5 of checkFixValueRange
        value = pd.Timestamp('2001-01-01')
        belongOp = 0  # Belong
        field = None
        quant_op = 1  # greater
        quant_abs = 30

        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=preprocessed_data_dictionary,
                                                        belongOp=Belong(belongOp), field=field, quant_abs=quant_abs,
                                                        quant_op=Operator(quant_op))
        assert result is True, "Test Case 5 Failed: Expected True, but got False"
        print_and_log("Test Case 5 Passed: Expected True, got True")

        # Example 6 of checkFixValueRange
        value = None
        belongOp = 0  # Belong
        field = None
        quant_op = 2  # lessEqual
        quant_abs = 50

        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=preprocessed_data_dictionary,
                                                        belongOp=Belong(belongOp), field=field, quant_abs=quant_abs,
                                                        quant_op=Operator(quant_op))
        assert result is False, "Test Case 6 Failed: Expected False, but got True"
        print_and_log("Test Case 6 Passed: Expected False, got False")

        # Example 8 of checkFixValueRange
        value = pd.Timestamp('20251215')
        belongOp = 1  # Not Belong
        # # Ejecutar la función y verificar que devuelve False
        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=preprocessed_data_dictionary,
                                                        belongOp=Belong(belongOp))
        assert result is True, "Test Case 8 Failed: Expected True, but got False"
        print_and_log("Test Case 8 Passed: Expected True, got True")

        # Example 9 of checkFixValueRange
        value = pd.Timestamp('20150721')
        belongOp = 1  # Not Belong
        # # Ejecutar la función y verificar que devuelve False
        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=preprocessed_data_dictionary,
                                                        belongOp=Belong(belongOp))
        assert result is False, "Test Case 9 Failed: Expected False, but got True"
        print_and_log("Test Case 9 Passed: Expected False, got False")

        # Example 11 of checkFixValueRange
        value = pd.Timestamp('20150721')
        belongOp = 0  # Belong
        field = 'track_album_release_date'
        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=preprocessed_data_dictionary, field=field,
                                                  belongOp=Belong(belongOp))
        assert result is True, "Test Case 11 Failed: Expected True, but got False"
        print_and_log("Test Case 11 Passed: Expected True, got True")

        # Example 12 of checkFixValueRange
        value = pd.Timestamp('20250721')
        belongOp = 0  # Belong
        field = 'track_album_release_date'
        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=preprocessed_data_dictionary, field=field,
                                                  belongOp=Belong(belongOp))
        assert result is False, "Test Case 12 Failed: Expected False, but got True"
        print_and_log("Test Case 12 Passed: Expected False, got False")

        # Example 15 of checkFixValueRange
        value = None
        belongOp = 0  # Belong
        field = 'track_album_release_date'
        quant_op = 1  # greater
        quant_abs = 2
        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=preprocessed_data_dictionary, field=field,
                                                  quant_abs=quant_abs, quant_op=Operator(quant_op),
                                                  belongOp=Belong(belongOp))
        assert result is True, "Test Case 15 Failed: Expected True, but got False"
        print_and_log("Test Case 15 Passed: Expected True, got True")

        # Example 16 of checkFixValueRange
        value = pd.Timestamp('20180721')
        belongOp = 0  # Belong
        field = 'track_album_release_date'
        quant_op = 1  # greater
        quant_abs = 3000
        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=preprocessed_data_dictionary, field=field,
                                                  quant_abs=quant_abs, quant_op=Operator(quant_op),
                                                  belongOp=Belong(belongOp))
        assert result is False, "Test Case 16 Failed: Expected False, but got True"
        print_and_log("Test Case 16 Passed: Expected False, got False")

        # Example 18 of checkFixValueRange
        value = pd.Timestamp('20250721')
        belongOp = 1  # Not Belong
        field = 'track_album_release_date'
        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=preprocessed_data_dictionary, field=field,
                                                  belongOp=Belong(belongOp))
        assert result is True, "Test Case 18 Failed: Expected True, but got False"
        print_and_log("Test Case 18 Passed: Expected True, got True")

        # Example 19 of checkFixValueRange
        value = pd.Timestamp('20180721')
        belongOp = 1  # Not Belong
        field = 'track_album_release_date'
        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=preprocessed_data_dictionary, field=field,
                                                  belongOp=Belong(belongOp))
        assert result is False, "Test Case 19 Failed: Expected False, but got True"
        print_and_log("Test Case 19 Passed: Expected False, got False")

        # --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        # Casos de error añadidos
        print_and_log("")
        print_and_log("Casos de error añadidos:")

        # Example 4.5 of checkFixValueRange
        # CASO DE QUE quant_rel y quant_abs NO SEAN None A LA VEZ (existen los dos) VALUERROR
        value = None
        belongOp = 0  # Belong
        field = None
        quant_op = 2  # lessEqual
        quant_rel = 0.4
        quant_abs = 50
        expected_exception = ValueError
        with self.assertRaises(expected_exception) as context:
            self.pre_post.checkFixValueRange(value=value, dataDictionary=preprocessed_data_dictionary,
                                             belongOp=Belong(belongOp), field=field, quant_rel=quant_rel,
                                             quant_abs=quant_abs, quant_op=Operator(quant_op))

        print_and_log(f"Test Case 4.5 Passed: Expected ValueError, got ValueError")
        # Example 7 of checkFixValueRange
        # CASO DE QUE no existan ni quant_rel ni quant_abs cuando belongOp es BELONG Y quant_op no es None VALUERROR
        value = pd.Timestamp('20180721')
        belongOp = 0  # Belong
        field = None
        quant_op = 2  # lessEqual
        expected_exception = ValueError
        with self.assertRaises(expected_exception) as context:
            result = self.pre_post.checkFixValueRange(value=value, dataDictionary=preprocessed_data_dictionary,
                                                      belongOp=Belong(belongOp), field=field,
                                                      quant_op=Operator(quant_op))
        print_and_log("Test Case 7 Passed: Expected ValueError, got ValueError")

        # # Example 10 of checkFixValueRange
        value = pd.Timestamp('20180721')
        belongOp = 1  # Not Belong
        quant_op = 3
        expected_exception = ValueError
        with self.assertRaises(expected_exception) as context:
            result = self.pre_post.checkFixValueRange(value=value, dataDictionary=preprocessed_data_dictionary,
                                                      belongOp=Belong(belongOp), quant_op=Operator(quant_op))
        print_and_log("Test Case 10 Passed: Expected ValueError, got ValueError")
        print_and_log("")
        print_and_log("-----------------------------------------------------------")
        print_and_log("")

    def execute_checkIntervalRangeFloat_Tests(self):
        """
        Execute the simple tests of the function checkIntervalRangeFloat
        """
        print_and_log("Testing checkIntervalRangeFloat Function")
        print_and_log("")
        print_and_log("Casos de test con dataset añadidos:")

        #field = None
        field = None
        #belongOp = 0
        belongOp = 0
        
        #Example 0 of checkIntervalRangeFloat
        #Check that the left margin is not bigger than the right margin
        left0=20
        right0=15
        closure = 0  # OpenOpen
        expected_exception = ValueError
        with self.assertRaises(expected_exception) as context:
            result = self.pre_post.checkIntervalRangeFloat(left_margin=left0, right_margin=right0,
                                                       dataDictionary=self.data_dictionary, closureType=Closure(closure),
                                                       belongOp=Belong(belongOp))
        print_and_log("Test Case 0 Passed: Expected ValueError, got ValueError")

        # Example 1 of checkIntervalRangeFloat
        # Check that the data in the whole dictionary belongs to the interval (0, 1)
        left = 0
        right = 1
        closure = 0  # OpenOpen
        result = self.pre_post.checkIntervalRangeFloat(left_margin=left, right_margin=right,
                                                       dataDictionary=self.data_dictionary, closureType=Closure(closure),
                                                       belongOp=Belong(belongOp))
        assert result is False, "Test Case 1 Failed: Expected False, but got True"
        print_and_log("Test Case 1 Passed: Expected False, got False")

        # Example 2 of checkIntervalRangeFloat
        # Check that the data in the whole dictionary belongs to the interval (-46.448, 517810)
        left = -47.30
        right = 518000
        closure = 0  # OpenOpen
        result = self.pre_post.checkIntervalRangeFloat(left_margin=left, right_margin=right,
                                                       dataDictionary=self.data_dictionary, closureType=Closure(closure),
                                                       belongOp=Belong(belongOp))
        assert result is True, "Test Case 2 Failed: Expected True, but got False"
        print_and_log("Test Case 2 Passed: Expected True, got True")

        # Example 3 of checkIntervalRangeFloat
        # Check that the data in the whole dictionary belongs to the interval (-46.448, 517810]
        left = -47.30
        right = 517810
        closure = 1  # OpenClosed
        result = self.pre_post.checkIntervalRangeFloat(left_margin=left, right_margin=right,
                                                       dataDictionary=self.data_dictionary, closureType=Closure(closure),
                                                       belongOp=Belong(belongOp))
        assert result is True, "Test Case 3 Failed: Expected True, but got False"
        print_and_log("Test Case 3 Passed: Expected True, got True")

        # Example 4 of checkIntervalRangeFloat
        # Check that the data in the whole dictionary belongs to the interval (-46.448, 517810]
        left = -47.30
        right = 517809.99
        closure = 1  # OpenClosed
        result = self.pre_post.checkIntervalRangeFloat(left_margin=left, right_margin=right,
                                                       dataDictionary=self.data_dictionary, closureType=Closure(closure),
                                                       belongOp=Belong(belongOp))
        assert result is False, "Test Case 4 Failed: Expected False, but got True"
        print_and_log("Test Case 4 Passed: Expected False, got False")

        # Example 5 of checkIntervalRangeFloat
        # Check that the data in the whole dictionary belongs to the interval [-46.448, 517810)
        left = -46.448
        right = 517811
        closure = 2  # ClosedOpen
        result = self.pre_post.checkIntervalRangeFloat(left_margin=left, right_margin=right,
                                                       dataDictionary=self.data_dictionary, closureType=Closure(closure),
                                                       belongOp=Belong(belongOp))
        assert result is True, "Test Case 5 Failed: Expected True, but got False"
        print_and_log("Test Case 5 Passed: Expected True, got True")

        # Example 6 of checkIntervalRangeFloat
        # Check that the data in the whole dictionary belongs to the interval [-46.448, 517810)
        left = -46.448
        right = 517810.0
        belongOp = 0
        closure = 2  # ClosedOpen
        result = self.pre_post.checkIntervalRangeFloat(left_margin=left, right_margin=right,
                                                       dataDictionary=self.data_dictionary, closureType=Closure(closure),
                                                       belongOp=Belong(belongOp))
        assert result is False, "Test Case 6 Failed: Expected False, but got True"
        print_and_log("Test Case 6 Passed: Expected False, got False")

        # Example 7 of checkIntervalRangeFloat
        # Check that the data in the whole dictionary belongs to the interval [-46.448, 517810]
        left = -46.448
        right = 517810
        closure = 3  # ClosedClosed
        result = self.pre_post.checkIntervalRangeFloat(left_margin=left, right_margin=right,
                                                       dataDictionary=self.data_dictionary, closureType=Closure(closure),
                                                       belongOp=Belong(belongOp))
        assert result is True, "Test Case 7 Failed: Expected True, but got False"
        print_and_log("Test Case 7 Passed: Expected True, got True")

        # Example 8 of checkIntervalRangeFloat
        # Check that the data in the whole dictionary belongs to the interval [-46.448, 517810]
        left = -46.447
        right = 517810.0
        closure = 3  # ClosedClosed
        result = self.pre_post.checkIntervalRangeFloat(left_margin=left, right_margin=right,
                                                       dataDictionary=self.data_dictionary, closureType=Closure(closure),
                                                       belongOp=Belong(belongOp))
        assert result is False, "Test Case 8 Failed: Expected False, but got True"
        print_and_log("Test Case 8 Passed: Expected False, got False")

        #belongOp = 1
        belongOp = 1

        # Example 9 of checkIntervalRangeFloat
        # Check that the data in the whole dictionary belongs to the interval (-46.448, 517810)
        left = -46.448
        right = 517811
        closure = 0  # OpenOpen
        result = self.pre_post.checkIntervalRangeFloat(left_margin=left, right_margin=right,
                                                       dataDictionary=self.data_dictionary, closureType=Closure(closure),
                                                       belongOp=Belong(belongOp))
        assert result is True, "Test Case 9 Failed: Expected True, but got False"
        print_and_log("Test Case 9 Passed: Expected True, got True")

        # Example 10 of checkIntervalRangeFloat
        # Check that the data in the whole dictionary belongs to the interval (-46.448, 517810)
        left = -46.449
        right = 517810.1
        closure = 0  # OpenOpen
        result = self.pre_post.checkIntervalRangeFloat(left_margin=left, right_margin=right,
                                                       dataDictionary=self.data_dictionary, closureType=Closure(closure),
                                                       belongOp=Belong(belongOp))
        assert result is False, "Test Case 10 Failed: Expected False, but got True"
        print_and_log("Test Case 10 Passed: Expected False, got False")

        # Example 11 of checkIntervalRangeFloat
        # Check that the data in the whole dictionary belongs to the interval (-46.448, 517810]
        left = -46.449
        right = 517810
        closure = 1  # OpenClosed
        result = self.pre_post.checkIntervalRangeFloat(left_margin=left, right_margin=right,
                                                       dataDictionary=self.data_dictionary, closureType=Closure(closure),
                                                       belongOp=Belong(belongOp))
        assert result is False, "Test Case 11 Failed: Expected False, but got True"
        print_and_log("Test Case 11 Passed: Expected False, got False")

        # Example 12 of checkIntervalRangeFloat
        # Check that the data in the whole dictionary belongs to the interval (-46.448, 517810]
        left = -46.448
        right = 517810
        closure = 1  # OpenClosed
        result = self.pre_post.checkIntervalRangeFloat(left_margin=left, right_margin=right,
                                                       dataDictionary=self.data_dictionary, closureType=Closure(closure),
                                                       belongOp=Belong(belongOp))
        assert result is True, "Test Case 12 Failed: Expected True, but got False"
        print_and_log("Test Case 12 Passed: Expected True, got True")

        # Example 13 of checkIntervalRangeFloat
        # Check that the data in the whole dictionary belongs to the interval [-46.448, 517810)
        left = -46.448
        right = 517810.01
        closure = 2  # ClosedOpen
        result = self.pre_post.checkIntervalRangeFloat(left_margin=left, right_margin=right,
                                                       dataDictionary=self.data_dictionary, closureType=Closure(closure),
                                                       belongOp=Belong(belongOp))
        assert result is False, "Test Case 13 Failed: Expected False, but got True"
        print_and_log("Test Case 13 Passed: Expected False, got False")

        # Example 14 of checkIntervalRangeFloat
        # Check that the data in the whole dictionary belongs to the interval [-46.448, 517810)
        left = -46.448
        right = 517810
        closure = 2  # ClosedOpen
        result = self.pre_post.checkIntervalRangeFloat(left_margin=left, right_margin=right,
                                                       dataDictionary=self.data_dictionary, closureType=Closure(closure),
                                                       belongOp=Belong(belongOp))
        assert result is True, "Test Case 14 Failed: Expected True, but got False"
        print_and_log("Test Case 14 Passed: Expected True, got True")

        # Example 15 of checkIntervalRangeFloat
        # Check that the data in the whole dictionary belongs to the interval [-46.448, 517810]
        left = -46.448
        right = 517810
        closure = 3  # ClosedClosed
        result = self.pre_post.checkIntervalRangeFloat(left_margin=left, right_margin=right,
                                                       dataDictionary=self.data_dictionary, closureType=Closure(closure),
                                                       belongOp=Belong(belongOp))
        assert result is False, "Test Case 15 Failed: Expected False, but got True"
        print_and_log("Test Case 15 Passed: Expected False, got False")

        # Example 16 of checkIntervalRangeFloat
        # Check that the data in the whole dictionary belongs to the interval [-46.448, 517810]
        left = -46.448
        right = 517809.9
        closure = 3  # ClosedClosed
        result = self.pre_post.checkIntervalRangeFloat(left_margin=left, right_margin=right,
                                                       dataDictionary=self.data_dictionary, closureType=Closure(closure),
                                                       belongOp=Belong(belongOp))
        assert result is True, "Test Case 16 Failed: Expected True, but got False"
        print_and_log("Test Case 16 Passed: Expected True, got True")

        #field = 'loudness'
        field = 'loudness'
        #belongOp = 0
        belongOp = 0

        # Example 17 of checkIntervalRangeFloat
        # Check that the data in the whole dictionary belongs to the interval (-46.448, 1.275)
        left = -46.448
        right = 1.275
        closure = 0  # OpenOpen
        result = self.pre_post.checkIntervalRangeFloat(left_margin=left, right_margin=right,
                                                       dataDictionary=self.data_dictionary, closureType=Closure(closure),
                                                       belongOp=Belong(belongOp),field=field)
        assert result is False, "Test Case 17 Failed: Expected False, but got True"
        print_and_log("Test Case 17 Passed: Expected False, got False")

        # Example 18 of checkIntervalRangeFloat
        # Check that the data in the whole dictionary belongs to the interval (-46.448, 1.275)
        left = -46.449
        right = 1.276
        closure = 0  # OpenOpen
        result = self.pre_post.checkIntervalRangeFloat(left_margin=left, right_margin=right,
                                                       dataDictionary=self.data_dictionary, closureType=Closure(closure),
                                                       belongOp=Belong(belongOp),field=field)
        assert result is True, "Test Case 18 Failed: Expected True, but got False"
        print_and_log("Test Case 18 Passed: Expected True, got True")

        # Example 19 of checkIntervalRangeFloat
        # Check that the data in the whole dictionary belongs to the interval (-46.448, 1.275]
        left = -46.449
        right = 1.275
        closure = 1  # OpenClosed
        result = self.pre_post.checkIntervalRangeFloat(left_margin=left, right_margin=right,
                                                       dataDictionary=self.data_dictionary, closureType=Closure(closure),
                                                       belongOp=Belong(belongOp),field=field)
        assert result is True, "Test Case 19 Failed: Expected True, but got False"
        print_and_log("Test Case 19 Passed: Expected True, got True")

        # Example 20 of checkIntervalRangeFloat
        # Check that the data in the whole dictionary belongs to the interval (-46.448, 1.275]
        left = -46.448
        right = 1.275
        closure = 1  # OpenClosed
        result = self.pre_post.checkIntervalRangeFloat(left_margin=left, right_margin=right,
                                                       dataDictionary=self.data_dictionary, closureType=Closure(closure),
                                                       belongOp=Belong(belongOp),field=field)
        assert result is False, "Test Case 20 Failed: Expected False, but got True"
        print_and_log("Test Case 20 Passed: Expected False, got False")

        # Example 21 of checkIntervalRangeFloat
        # Check that the data in the whole dictionary belongs to the interval [-46.448, 1.275)
        left = -46.448
        right = 1.276
        closure = 2  # ClosedOpen
        result = self.pre_post.checkIntervalRangeFloat(left_margin=left, right_margin=right,
                                                       dataDictionary=self.data_dictionary, closureType=Closure(closure),
                                                       belongOp=Belong(belongOp),field=field)
        assert result is True, "Test Case 21 Failed: Expected True, but got False"
        print_and_log("Test Case 21 Passed: Expected True, got True")

        # Example 22 of checkIntervalRangeFloat
        # Check that the data in the whole dictionary belongs to the interval [-46.448, 1.275)
        left = -46.448
        right = 1.275
        closure = 2  # ClosedOpen
        result = self.pre_post.checkIntervalRangeFloat(left_margin=left, right_margin=right,
                                                       dataDictionary=self.data_dictionary, closureType=Closure(closure),
                                                       belongOp=Belong(belongOp),field=field)
        assert result is False, "Test Case 22 Failed: Expected False, but got True"
        print_and_log("Test Case 22 Passed: Expected False, got False")

        # Example 23 of checkIntervalRangeFloat
        # Check that the data in the whole dictionary belongs to the interval [-46.448, 1.275]
        left = -46.448
        right = 1.275
        closure = 3  # ClosedClosed
        result = self.pre_post.checkIntervalRangeFloat(left_margin=left, right_margin=right,
                                                       dataDictionary=self.data_dictionary, closureType=Closure(closure),
                                                       belongOp=Belong(belongOp),field=field)
        assert result is True, "Test Case 23 Failed: Expected True, but got False"
        print_and_log("Test Case 23 Passed: Expected True, got True")

        # Example 24 of checkIntervalRangeFloat
        # Check that the data in the whole dictionary belongs to the interval [-46.448, 1.275]
        left = -46.448
        right = 1.274
        closure = 3  # ClosedClosed
        result = self.pre_post.checkIntervalRangeFloat(left_margin=left, right_margin=right,
                                                       dataDictionary=self.data_dictionary, closureType=Closure(closure),
                                                       belongOp=Belong(belongOp),field=field)
        assert result is False, "Test Case 24 Failed: Expected False, but got True"
        print_and_log("Test Case 24 Passed: Expected False, got False")

        #belongOp = 1
        belongOp = 1

        # Example 25 of checkIntervalRangeFloat
        # Check that the data in the whole dictionary belongs to the interval (-46.448, 1.275)
        left = -46.448
        right = 1.276
        closure = 0  # OpenOpen
        result = self.pre_post.checkIntervalRangeFloat(left_margin=left, right_margin=right,
                                                       dataDictionary=self.data_dictionary, closureType=Closure(closure),
                                                       belongOp=Belong(belongOp),field=field)
        assert result is True, "Test Case 25 Failed: Expected True, but got False"
        print_and_log("Test Case 25 Passed: Expected True, got True")

        # Example 26 of checkIntervalRangeFloat
        # Check that the data in the whole dictionary belongs to the interval (-46.448, 1.275)
        left = -46.449
        right = 1.276
        closure = 0  # OpenOpen
        result = self.pre_post.checkIntervalRangeFloat(left_margin=left, right_margin=right,
                                                       dataDictionary=self.data_dictionary, closureType=Closure(closure),
                                                       belongOp=Belong(belongOp),field=field)
        assert result is False, "Test Case 26 Failed: Expected False, but got True"
        print_and_log("Test Case 26 Passed: Expected False, got False")

        # Example 27 of checkIntervalRangeFloat
        # Check that the data in the whole dictionary belongs to the interval (-46.448, 1.275]
        left = -46.449
        right = 1.275
        closure = 1  # OpenClosed
        result = self.pre_post.checkIntervalRangeFloat(left_margin=left, right_margin=right,
                                                       dataDictionary=self.data_dictionary, closureType=Closure(closure),
                                                       belongOp=Belong(belongOp),field=field)
        assert result is False, "Test Case 27 Failed: Expected False, but got True"
        print_and_log("Test Case 27 Passed: Expected False, got False")

        # Example 28 of checkIntervalRangeFloat
        # Check that the data in the whole dictionary belongs to the interval (-46.448, 1.275]
        left = -46.448
        right = 1.275
        closure = 1  # OpenClosed
        result = self.pre_post.checkIntervalRangeFloat(left_margin=left, right_margin=right,
                                                       dataDictionary=self.data_dictionary, closureType=Closure(closure),
                                                       belongOp=Belong(belongOp),field=field)
        assert result is True, "Test Case 28 Failed: Expected True, but got False"
        print_and_log("Test Case 28 Passed: Expected True, got True")

        # Example 29 of checkIntervalRangeFloat
        # Check that the data in the whole dictionary belongs to the interval [-46.448, 1.275)
        left = -46.448
        right = 1.276
        closure = 2  # ClosedOpen
        result = self.pre_post.checkIntervalRangeFloat(left_margin=left, right_margin=right,
                                                       dataDictionary=self.data_dictionary, closureType=Closure(closure),
                                                       belongOp=Belong(belongOp),field=field)
        assert result is False, "Test Case 29 Failed: Expected False, but got True"
        print_and_log("Test Case 29 Passed: Expected False, got False")

        # Example 30 of checkIntervalRangeFloat
        # Check that the data in the whole dictionary belongs to the interval [-46.448, 1.275)
        left = -46.448
        right = 1.275
        closure = 2  # ClosedOpen
        result = self.pre_post.checkIntervalRangeFloat(left_margin=left, right_margin=right,
                                                       dataDictionary=self.data_dictionary, closureType=Closure(closure),
                                                       belongOp=Belong(belongOp),field=field)
        assert result is True, "Test Case 30 Failed: Expected True, but got False"
        print_and_log("Test Case 30 Passed: Expected True, got True")

        # Example 31 of checkIntervalRangeFloat
        # Check that the data in the whole dictionary belongs to the interval [-46.448, 1.275]
        left = -46.448
        right = 1.275
        closure = 3  # ClosedClosed
        result = self.pre_post.checkIntervalRangeFloat(left_margin=left, right_margin=right,
                                                       dataDictionary=self.data_dictionary, closureType=Closure(closure),
                                                       belongOp=Belong(belongOp),field=field)
        assert result is False, "Test Case 31 Failed: Expected False, but got True"
        print_and_log("Test Case 31 Passed: Expected False, got False")

        # Example 32 of checkIntervalRangeFloat
        # Check that the data in the whole dictionary belongs to the interval [-46.448, 1.275]
        left = -46.447
        right = 1.275
        closure = 3  # ClosedClosed
        result = self.pre_post.checkIntervalRangeFloat(left_margin=left, right_margin=right,
                                                       dataDictionary=self.data_dictionary, closureType=Closure(closure),
                                                       belongOp=Belong(belongOp),field=field)
        assert result is True, "Test Case 32 Failed: Expected True, but got False"
        print_and_log("Test Case 32 Passed: Expected True, got True")

        # Example 33 of checkIntervalRangeFloat
        field='playlist_name'
        closure = 3  # ClosedClosed
        expected_exception = ValueError
        with self.assertRaises(expected_exception) as context:
            result = self.pre_post.checkIntervalRangeFloat(left_margin=left, right_margin=right,
                                                           dataDictionary=self.data_dictionary, closureType=Closure(closure),
                                                           belongOp=Belong(belongOp),field=field)
        print_and_log("Test Case 33 Passed: Expected ValueError, got ValueError")
        print_and_log("")
        print_and_log("-----------------------------------------------------------")
        print_and_log("")


    def execute_CheckMissingRange_Tests(self):
        """
        Execute the simple tests of the function checkInvalidValues
        """
        print_and_log("Testing checkMissingRange Function")
        print_and_log("")
        print_and_log("Casos de test con dataset añadidos:")

        preprocessed_data_dictionary = self.data_dictionary.copy()
        string_replacement = 'No es nulo'
        numeric_replacement = 33.33  # You can choose any numeric value

        # Identify columns with string and numeric data types
        string_columns = preprocessed_data_dictionary.select_dtypes(include='object').columns
        numeric_columns = preprocessed_data_dictionary.select_dtypes(exclude='object').columns

        # Replace null values in string columns
        preprocessed_data_dictionary[string_columns] = preprocessed_data_dictionary[string_columns].fillna(
            string_replacement)

        # Replace null values in numeric columns
        preprocessed_data_dictionary[numeric_columns] = preprocessed_data_dictionary[numeric_columns].fillna(
            numeric_replacement)

        # Caso 1 Solicitado (Caso 20)

        belong = 0
        field = 'track_name'
        quant_op = 2 # lessEqual
        quant_rel = 0.5
        result = self.pre_post.checkMissingRange(dataDictionary=self.data_dictionary, field=field,
                                                 belongOp=Belong(belong), quant_op=Operator(quant_op),
                                                 quant_rel=quant_rel)
        assert result is True, "Test Case 20 Failed: Expected True, but got False"
        print_and_log("Test Case 20 Passed: Expected True, got True")

        # Caso 2 Solicitado (Caso 20 también)
        belong = 0
        field = 'track_artist'
        missing_values = [-1]
        quant_op = 2  # lessEqual
        quant_rel = 0.5
        result = self.pre_post.checkMissingRange(dataDictionary=self.data_dictionary, field=field,
                                                 belongOp=Belong(belong), quant_op=Operator(quant_op),
                                                 quant_rel=quant_rel, missing_values=missing_values)
        assert result is True, "Test Case 20 Failed: Expected True, but got False"
        print_and_log("Test Case 20 Passed: Expected True, got True")

        # Caso 3 Solicitado (Caso 23)
        belong = 0
        field = 'track_artist'
        missing_values = [-1]
        quant_op = 2 # lessEqual
        quant_abs = 50
        result = self.pre_post.checkMissingRange(dataDictionary=self.data_dictionary, field=field,
                                                 belongOp=Belong(belong), quant_op=Operator(quant_op),
                                                 quant_abs=quant_abs, missing_values=missing_values)
        assert result is True, "Test Case 23 Failed: Expected True, but got False"
        print_and_log("Test Case 23 Passed: Expected True, got True")

        #Casos añadidos

        #Caso 1
        field = None
        belong = 0
        missing_values = [-1]
        result=self.pre_post.checkMissingRange(dataDictionary=self.data_dictionary, field=field,missing_values=missing_values,
                                                 belongOp=Belong(belong))
        assert result is True, "Test Case 1 Failed: Expected True, but got False"
        print_and_log("Test Case 1 Passed: Expected True, got True")

        #Caso 2
        belong = 0
        field = None
        missing_values= ['Nulo', -8]
        quant_op = 2  # lessEqual
        quant_rel = 0.5
        result = self.pre_post.checkMissingRange(dataDictionary=self.data_dictionary, field=field, missing_values=missing_values,
                                                 belongOp=Belong(belong), quant_op=Operator(quant_op),
                                                 quant_rel=quant_rel)
        assert result is True, "Test Case 2 Failed: Expected True, but got False"
        print_and_log("Test Case 2 Passed: Expected True, got True")

        #Caso 3
        belong = 0
        field = None
        missing_values= ['Nul', 'Mandarina']
        result = self.pre_post.checkMissingRange(dataDictionary=preprocessed_data_dictionary, field=field, missing_values=missing_values,
                                                 belongOp=Belong(belong))
        assert result is False, "Test Case 3 Failed: Expected False, but got True"
        print_and_log("Test Case 3 Passed: Expected False, got False")

        #Caso 4
        belong = 0
        field = None
        missing_values= None
        result = self.pre_post.checkMissingRange(dataDictionary=preprocessed_data_dictionary, field=field, missing_values=missing_values,
                                                 belongOp=Belong(belong))
        assert result is False, "Test Case 4 Failed: Expected False, but got True"
        print_and_log("Test Case 4 Passed: Expected False, got False")

        #Caso 5
        belong = 0
        field = None
        quant_op = 2 # lessEqual
        quant_rel = 0.5
        result = self.pre_post.checkMissingRange(dataDictionary=self.data_dictionary, field=field,
                                                 belongOp=Belong(belong), quant_op=Operator(quant_op),
                                                 quant_rel=quant_rel)
        assert result is True, "Test Case 5 Failed: Expected True, but got False"
        print_and_log("Test Case 5 Passed: Expected True, got True")

        #Caso 6
        belong = 0
        field = None
        quant_op = 2 # lessEqual
        quant_rel = 0.5
        result = self.pre_post.checkMissingRange(dataDictionary=preprocessed_data_dictionary, field=field,
                                                 belongOp=Belong(belong), quant_op=Operator(quant_op),
                                                 quant_rel=quant_rel)
        assert result is False, "Test Case 6 Failed: Expected False, but got True"
        print_and_log("Test Case 6 Passed: Expected False, got False")

        #Caso 8
        belong = 0
        field = None
        quant_op = 0 # greaterEqual
        missing_values = ['Poison']
        quant_abs = 2
        result = self.pre_post.checkMissingRange(dataDictionary=preprocessed_data_dictionary, field=field,
                                                 belongOp=Belong(belong), quant_op=Operator(quant_op),
                                                 quant_abs=quant_abs, missing_values=missing_values)
        assert result is True, "Test Case 8 Failed: Expected True, but got False"
        print_and_log("Test Case 8 Passed: Expected True, got True")

        #Caso 9
        belong = 0
        field = None
        quant_op = 0 # greaterEqual
        missing_values = ['Mandarina']
        quant_abs = 2
        result = self.pre_post.checkMissingRange(dataDictionary=preprocessed_data_dictionary, field=field,
                                                 belongOp=Belong(belong), quant_op=Operator(quant_op),
                                                 quant_abs=quant_abs, missing_values=missing_values)
        assert result is False, "Test Case 9 Failed: Expected False, but got True"
        print_and_log("Test Case 9 Passed: Expected False, got False")

        #Caso 11
        belong = 1
        field = None
        missing_values = ['Mandarina']
        result = self.pre_post.checkMissingRange(dataDictionary=preprocessed_data_dictionary, field=field,
                                                 belongOp=Belong(belong), missing_values=missing_values)
        assert result is True, "Test Case 11 Failed: Expected True, but got False"
        print_and_log("Test Case 11 Passed: Expected True, got True")

        #Caso 12
        belong = 1
        field = None
        missing_values = ['Poison']
        result = self.pre_post.checkMissingRange(dataDictionary=preprocessed_data_dictionary, field=field,
                                                 belongOp=Belong(belong), missing_values=missing_values)
        assert result is False, "Test Case 12 Failed: Expected False, but got True"
        print_and_log("Test Case 12 Passed: Expected False, got False")

        #Caso 13
        belong = 1
        field = None
        result = self.pre_post.checkMissingRange(dataDictionary=preprocessed_data_dictionary, field=field,
                                                 belongOp=Belong(belong))
        assert result is True, "Test Case 13 Failed: Expected True, but got False"
        print_and_log("Test Case 13 Passed: Expected True, got True")

        #Caso 13.1
        belong = 1
        field = None
        result = self.pre_post.checkMissingRange(dataDictionary=self.data_dictionary, field=field,
                                                 belongOp=Belong(belong))
        assert result is False, "Test Case 13.1 Failed: Expected False, but got True"
        print_and_log("Test Case 13.1 Passed: Expected False, got False")

        # Caso 16
        belong = 0
        field = 'track_name'
        quant_op = None
        result = self.pre_post.checkMissingRange(dataDictionary=self.data_dictionary, field=field,
                                                    belongOp=Belong(belong), quant_op=quant_op)
        assert result is True, "Test Case 16 Failed: Expected True, but got False"
        print_and_log("Test Case 16 Passed: Expected True, got True")

        # Caso 17
        belong = 0
        field = 'track_name'
        quant_op = None
        missing_values = ['Poison', 'Mandarina']
        result = self.pre_post.checkMissingRange(dataDictionary=preprocessed_data_dictionary, field=field,
                                                 belongOp=Belong(belong), quant_op=quant_op,
                                                 missing_values=missing_values)
        assert result is True, "Test Case 17 Failed: Expected True, but got False"
        print_and_log("Test Case 17 Passed: Expected True, got True")

        # Caso 18
        belong = 0
        field = 'track_name'
        quant_op = None
        missing_values = ['Mandarina', 'Mandarino']
        result = self.pre_post.checkMissingRange(dataDictionary=preprocessed_data_dictionary, field=field,
                                                 belongOp=Belong(belong), quant_op=quant_op,
                                                 missing_values=missing_values)
        assert result is False, "Test Case 18 Failed: Expected False, but got True"
        print_and_log("Test Case 18 Passed: Expected False, got False")


        # Caso 19
        belong = 0
        field = 'track_name'
        quant_op = None
        missing_values = None
        result = self.pre_post.checkMissingRange(dataDictionary=preprocessed_data_dictionary, field=field,
                                                 belongOp=Belong(belong), quant_op=quant_op,
                                                 missing_values=missing_values)
        assert result is False, "Test Case 19 Failed: Expected False, but got True"
        print_and_log("Test Case 19 Passed: Expected False, got False")

        # Caso 21
        belong = 0
        field = 'track_artist'
        missing_values = ['Martin Garrix', 'Maroon 5']
        quant_op = 1  # greater
        quant_rel = 0.2
        result = self.pre_post.checkMissingRange(dataDictionary=preprocessed_data_dictionary, field=field,
                                                 belongOp=Belong(belong), quant_op=Operator(quant_op),
                                                 quant_rel=quant_rel, missing_values=missing_values)
        assert result is False, "Test Case 21 Failed: Expected False, but got True"
        print_and_log("Test Case 21 Passed: Expected False, got False")

        # Caso 24
        belong = 0
        field = 'key'
        missing_values = [1,5]
        quant_op = 2  # lessEqual
        quant_abs = 400
        result = self.pre_post.checkMissingRange(dataDictionary=preprocessed_data_dictionary, field=field,
                                                 belongOp=Belong(belong), quant_op=Operator(quant_op),
                                                 quant_abs=quant_abs, missing_values=missing_values)
        assert result is False, "Test Case 24 Failed: Expected False, but got True"
        print_and_log("Test Case 24 Passed: Expected False, got False")

        # Caso 26
        belong = 1
        field = 'track_artist'
        missing_values = [-1, np.NaN]
        result = self.pre_post.checkMissingRange(dataDictionary=preprocessed_data_dictionary, field=field,
                                                 belongOp=Belong(belong), missing_values=missing_values)
        assert result is True, "Test Case 26 Failed: Expected True, but got False"
        print_and_log("Test Case 26 Passed: Expected True, got True")

        # Caso 27
        belong = 1
        field = 'track_artist'
        missing_values = [np.NaN,'Maroon 5']
        result = self.pre_post.checkMissingRange(dataDictionary=self.data_dictionary, field=field,
                                                 belongOp=Belong(belong), missing_values=missing_values)
        assert result is False, "Test Case 27 Failed: Expected False, but got True"
        print_and_log("Test Case 27 Passed: Expected False, got False")

        # Caso 28
        belong = 1
        field = 'track_name'
        result = self.pre_post.checkMissingRange(dataDictionary=preprocessed_data_dictionary, field=field,
                                                 belongOp=Belong(belong))
        assert result is True, "Test Case 28 Failed: Expected True, but got False"
        print_and_log("Test Case 28 Passed: Expected True, got True")

        # Caso 29
        belong = 1
        field = 'track_artist'
        result = self.pre_post.checkMissingRange(dataDictionary=self.data_dictionary, field=field,
                                                 belongOp=Belong(belong))
        assert result is False, "Test Case 29 Failed: Expected False, but got True"
        print_and_log("Test Case 29 Passed: Expected False, got False")


        print_and_log("")
        print_and_log("Casos de error añadidos:")

        # Caso 7
        belong = 0
        field = None
        quant_op = 2  # lessEqual
        quant_rel = 0.5
        quant_abs = 2
        expected_exception = ValueError
        with self.assertRaises(expected_exception) as context:
            result = self.pre_post.checkMissingRange(dataDictionary=self.data_dictionary, field=field,
                                                     belongOp=Belong(belong), quant_op=Operator(quant_op),
                                                     quant_rel=quant_rel, quant_abs=quant_abs)
        print_and_log("Test Case 7 Passed: Expected ValueError, got ValueError")

        # Caso 10
        belong = 0
        field = None
        quant_op = 2  # lessEqual
        expected_exception = ValueError
        with self.assertRaises(expected_exception) as context:
            result = self.pre_post.checkMissingRange(dataDictionary=self.data_dictionary, field=field,
                                                     belongOp=Belong(belong), quant_op=Operator(quant_op))
        print_and_log("Test Case 10 Passed: Expected ValueError, got ValueError")

        # Caso 14
        belong = 1
        quan_abs = 5
        field = None
        expected_exception = ValueError
        with self.assertRaises(expected_exception) as context:
            result = self.pre_post.checkMissingRange(dataDictionary=self.data_dictionary, field=field, quant_abs=quan_abs,
                                                     belongOp=Belong(belong), quant_op=Operator(quant_op))
        print_and_log("Test Case 14 Passed: Expected ValueError, got ValueError")

        # Caso 15
        belong = 0
        field = 'colours'  # Error due to the inexistent field
        quant_op = 2  # lessEqual
        quant_rel = 0.5
        expected_exception = ValueError
        with self.assertRaises(expected_exception) as context:
            result = self.pre_post.checkMissingRange(dataDictionary=self.data_dictionary, field=field,
                                                     belongOp=Belong(belong), quant_op=Operator(quant_op),
                                                     quant_rel=quant_rel)
        print_and_log("Test Case 15 Passed: Expected ValueError, got ValueError")

        # Caso 22
        belong = 0
        field = 'colour'
        missing_values = [-1]
        quant_op = 2  # lessEqual
        quant_rel = 0.5
        quant_abs = 2
        expected_exception = ValueError  # Error due to quant_abs and quant_op are not None at the same time
        with self.assertRaises(expected_exception) as context:
            result = self.pre_post.checkMissingRange(dataDictionary=self.data_dictionary, field=field,
                                                     belongOp=Belong(belong), quant_op=Operator(quant_op),
                                                     quant_rel=quant_rel, quant_abs=quant_abs,
                                                     missing_values=missing_values)
        print_and_log("Test Case 22 Passed: Expected ValueError, got ValueError")

        # Caso 25
        belong = 0
        field = 'colour'
        missing_values = [-1]
        quant_op = 2  # lessEqual
        expected_exception = ValueError  # Error due to quant_op is not None and quant_abs/quant_rel are both None
        with self.assertRaises(expected_exception) as context:
            result = self.pre_post.checkMissingRange(dataDictionary=self.data_dictionary, field=field,
                                                     belongOp=Belong(belong), quant_op=Operator(quant_op),
                                                     missing_values=missing_values)
        print_and_log("Test Case 25 Passed: Expected ValueError, got ValueError")

        # Caso 30
        belong = 1
        field = 'colour'
        missing_values = [-1]
        quant_abs = 2
        quant_op = 0  # greaterEqual
        expected_exception = ValueError  # Error due to quant_abs, quant_op or quant_rel are not None when belongOp is 1
        with self.assertRaises(expected_exception) as context:
            result = self.pre_post.checkMissingRange(dataDictionary=self.data_dictionary, field=field,
                                                     belongOp=Belong(belong), missing_values=missing_values,
                                                     quant_abs=quant_abs, quant_op=Operator(quant_op))
        print_and_log("Test Case 30 Passed: Expected ValueError, got ValueError")




        print_and_log("")
        print_and_log("-----------------------------------------------------------")
        print_and_log("")




    # TODO: Hacer los test de checkInvalidValues
    def execute_CheckInvalidValues_Tests(self):
        """
        Execute the simple tests of the function checkInvalidValues
        """
        print_and_log("Testing checkInvalidValues Function")
        print_and_log("")
        print_and_log("Casos de test con dataset añadidos:")

        print_and_log("")
        print_and_log("-----------------------------------------------------------")
        print_and_log("")




