
# Importing libraries
import unittest
import numpy as np
import pandas as pd
from tqdm import tqdm

# Importing functions and classes from packages
from functions.contract_pre_post import ContractsPrePost
from helpers.enumerations import Belong, Operator, Closure
from helpers.logger import print_and_log


class ContractSimpleTest(unittest.TestCase):
    """
    Class to test the contracts with simple test cases

    Attributes:
    pre_post (ContractsPrePost): instance of the class ContractsPrePost

    Methods:
    execute_CheckFieldRange_Tests: execute the simple tests of the function checkFieldRange
    execute_CheckFixValueRangeString_Tests: execute the simple tests of the function checkFixValueRange
    execute_CheckFixValueRangeFloat_Tests: execute the simple tests of the function checkFixValueRange
    execute_CheckFixValueRangeDateTime_Tests: execute the simple tests of the function checkFixValueRange
    """

    def __init__(self):
        """
        Constructor of the class

        Attributes:
        pre_post (ContractsPrePost): instance of the class ContractsPrePost

        Functions:
        executeAll_SimpleTests: execute all the simple tests of the functions of the class
        execute_CheckFieldRange_SimpleTests: execute the simple tests of the function checkFieldRange
        execute_CheckFixValueRangeString_SimpleTests: execute the simple tests of the function checkFixValueRange
        execute_CheckFixValueRangeFloat_SimpleTests: execute the simple tests of the function checkFixValueRange
        execute_CheckFixValueRangeDateTime_SimpleTests: execute the simple tests of the function checkFixValueRange
        execute_CheckIntervalRangeFloat_SimpleTests: execute the simple tests of the function checkIntervalRange
        execute_CheckMissingRange_SimpleTests: execute the simple tests of the function checkMissingRange
        execute_CheckInvalidValues_SimpleTests: execute the simple tests of the function checkInvalidValues
        """
        self.pre_post = ContractsPrePost()

    def executeAll_SimpleTests(self):
        """
        Execute all the simple tests of the functions of the class
        """
        simple_test_methods = [
            self.execute_CheckFieldRange_SimpleTests,
            self.execute_CheckFixValueRangeString_SimpleTests,
            self.execute_CheckFixValueRangeFloat_SimpleTests,
            self.execute_CheckFixValueRangeDateTime_SimpleTests,
            self.execute_CheckIntervalRangeFloat_SimpleTests,
            self.execute_CheckMissingRange_SimpleTests,
            self.execute_CheckInvalidValues_SimpleTests,
            self.execute_CheckOutliers_SimpleTests
        ]

        print_and_log("")
        print_and_log("--------------------------------------------------")
        print_and_log("------- STARTING PRE-POST SIMPLE TEST CASES -------")
        print_and_log("--------------------------------------------------")
        print_and_log("")

        for simple_test_method in tqdm(simple_test_methods, desc="Running Simple Tests", unit="test"):
            simple_test_method()

        print_and_log("")
        print_and_log("--------------------------------------------------")
        print_and_log("-- SIMPLE PRE-POST TEST CASES EXECUTION FINISHED -")
        print_and_log("--------------------------------------------------")
        print_and_log("")

    def execute_CheckFieldRange_SimpleTests(self):
        """
        Execute the simple tests of the function checkFieldRange
        """
        print_and_log("Testing CheckFieldRange Function")
        print_and_log("")

        print_and_log("Casos Básicos solicitados en la especificación del contrato:")


        # Case 1 of checkFieldRange
        # Check that fields 'c1' and 'c2' belong to the data dictionary. It must return True
        fields = ['c1', 'c2']
        data_dictionary = pd.DataFrame(columns=['c1', 'c2'])
        belong = 0
        result = self.pre_post.checkFieldRange(fields=fields, dataDictionary=data_dictionary, belongOp=Belong(belong))
        assert result is True, "Test Case 1 Failed: Expected True, but got False"
        print_and_log("Test Case 1 Passed: Expected True, got True")

        # Case 2 of checkFieldRange
        # Check that fields 'c2' and 'c3' belong to the data dictionary. It must return False as 'c3' does not belong
        fields = ['c2', 'c3']
        data_dictionary = pd.DataFrame(columns=['c1', 'c2'])
        belong = 0
        result = self.pre_post.checkFieldRange(fields=fields, dataDictionary=data_dictionary, belongOp=Belong(belong))
        assert result is False, "Test Case 2 Failed: Expected False, but got True"
        print_and_log("Test Case 2 Passed: Expected False, got False")

        # Case 3 of checkFieldRange
        # Check that fields 'c2' and 'c3' don't belong to the data dictionary.It must return True as 'c3' doesn't belong
        fields = ['c2', 'c3']
        data_dictionary = pd.DataFrame(columns=['c1', 'c2'])
        belong = 1
        result = self.pre_post.checkFieldRange(fields=fields, dataDictionary=data_dictionary, belongOp=Belong(belong))
        assert result is True, "Test Case 3 Failed: Expected True, but got False"
        print_and_log("Test Case 3 Passed: Expected True, got True")

        print_and_log("")
        print_and_log("Casos Básicos añadidos:")

        # Case 4 of checkFieldRange
        # Check that fields 'c1' and 'c2' don't belong to the data dictionary. It must return False as both belong
        fields = ['c1', 'c2']
        data_dictionary = pd.DataFrame(columns=['c1', 'c2'])
        belong = 1
        result = self.pre_post.checkFieldRange(fields=fields, dataDictionary=data_dictionary, belongOp=Belong(belong))
        assert result is False, "Test Case 4 Failed: Expected False, but got True"
        print_and_log("Test Case 4 Passed: Expected False, got False")

        # Case 5 of checkFieldRange
        # Check that fields 'c2' and 'c1' belong to the data dictionary. It must return True as both belong
        fields = ['c2', 'c1']
        data_dictionary = pd.DataFrame(columns=['c1', 'c2'])
        belong = 0
        result = self.pre_post.checkFieldRange(fields=fields, dataDictionary=data_dictionary, belongOp=Belong(belong))
        assert result is True, "Test Case 5 Failed: Expected True, but got False"
        print_and_log("Test Case 5 Passed: Expected True, got True")
        print_and_log("")
        print_and_log("-----------------------------------------------------------")
        print_and_log("")

    def execute_CheckFixValueRangeString_SimpleTests(self):
        """
        Execute the simple tests of the function checkFixValueRange
        """
        print_and_log("Testing CheckFixValueRangeString Function")

        print_and_log("")
        print_and_log("Casos Básicos solicitados en la especificación del contrato:")

        # 23 Casos

        # Example 13 of checkFixValueRange
        # Check that value None belongs to the data dictionary in field 'c1' and that
        # it appears less or equal than 30% of the times
        value = None
        dataDictionary = pd.DataFrame(data={'c1': ['0', '0', '0', '0', '0', '0', '0', None, None, None]})
        belongOp = 0  # Belong
        field = 'c1'
        quant_op = 2  # lessEqual
        quant_rel = 0.3
        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=dataDictionary,
                                                  belongOp=Belong(belongOp), field=field, quant_rel=quant_rel,
                                                  quant_op=Operator(quant_op))
        assert result is True, "Test Case 13 Failed: Expected True, but got False"
        print_and_log("Test Case 13 Passed: Expected True, got True")

        # Example 14 of checkFixValueRange
        # Check that value None belongs to the data dictionary in field 'c1' and that
        # it appears less or equal than 30% of the times
        value = None
        dataDictionary = pd.DataFrame(data={'c1': ['0', '0', '0', '0', '0', '0', None, None, None, None]})
        belongOp = 0  # Belong
        field = 'c1'
        quant_op = 2  # lessEqual
        quant_rel = 0.3
        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=dataDictionary,
                                                  belongOp=Belong(belongOp), field=field, quant_rel=quant_rel,
                                                  quant_op=Operator(quant_op))
        assert result is False, "Test Case 14 Failed: Expected False, but got True"
        print_and_log("Test Case 14 Passed: Expected False, got False")

        # Example 18 of checkFixValueRange
        # Check that value 1 doesn't belong to the data dictionary in field 'c1'
        value = '1'
        dataDictionary = pd.DataFrame(data={'c1': ['0', '0', '0', '0', '0', '0', '0', None, None, None]})
        belongOp = 1  # NotBelong
        field = 'c1'
        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=dataDictionary,
                                                  belongOp=Belong(belongOp), field=field)
        assert result is True, "Test Case 18 Failed: Expected True, but got False"
        print_and_log("Test Case 18 Passed: Expected True, got True")

        # Example 14.5 of checkFixValueRange
        # ValueError if quant_rel and quant_abs are not None at the same time
        value = None
        dataDictionary = pd.DataFrame(data={'c1': ['0', '0', '0', '0', '0', '0', '0', None, None, None]})
        belongOp = 0  # Belong
        field = 'c1'
        quant_op = 2  # lessEqual
        quant_rel = 0.4
        quant_abs = 50
        expected_exception = ValueError
        with self.assertRaises(expected_exception) as context:
            self.pre_post.checkFixValueRange(value=value, dataDictionary=dataDictionary,
                                             belongOp=Belong(belongOp), field=field, quant_rel=quant_rel,
                                             quant_abs=quant_abs, quant_op=Operator(quant_op))
        print_and_log("Test Case 14.5 Passed: Expected ValueError, got ValueError")


        print_and_log("")
        print_and_log("Casos Básicos añadidos:")

        # Example 1 of checkFixValueRange
        value = '3'
        dataDictionary = pd.DataFrame(data={'c1': ['0', '0', '0', '3', '0', '0', '0', None, None, None]})
        belongOp = 0  # Belong
        field = None  # None
        quant_op = None  # None
        quant_rel = 0.3
        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=dataDictionary,
                                                  belongOp=Belong(belongOp), field=field, quant_rel=quant_rel,
                                                  quant_op=quant_op)
        assert result is True, "Test Case 1 Failed: Expected True, but got False"
        print_and_log("Test Case 1 Passed: Expected True, got True")

        # Example 2 of checkFixValueRange
        value = '3'
        dataDictionary = pd.DataFrame(data={'c1': ['0', '0', '0', '0', '0', '0', '0', None, None, None]})
        belongOp = 0  # Belong
        field = None  # None
        quant_op = None  # None
        quant_rel = 0.3
        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=dataDictionary,
                                                  belongOp=Belong(belongOp), field=field, quant_rel=quant_rel,
                                                  quant_op=quant_op)
        assert result is False, "Test Case 2 Failed: Expected False, but got True"
        print_and_log("Test Case 2 Passed: Expected False, got False")

        # Example 3 of checkFixValueRange
        value = '0'
        dataDictionary = pd.DataFrame(data={'c1': ['0', '0', '0', '0', '0', '0', '0', None, None, None]})
        belongOp = 0  # Belong
        field = None
        quant_op = 1  # greater
        quant_rel = 0.1
        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=dataDictionary,
                                                  belongOp=Belong(belongOp), field=field, quant_rel=quant_rel,
                                                  quant_op=Operator(quant_op))
        assert result is True, "Test Case 3 Failed: Expected True, but got False"
        print_and_log("Test Case 3 Passed: Expected True, got True")

        # Example 4 of checkFixValueRange
        value = '0'
        dataDictionary = pd.DataFrame(data={'c1': ['0', '0', '0', '0', '0', '0', '0', None, None, None]})
        belongOp = 0  # Belong
        field = None
        quant_op = 1  # greater
        quant_rel = 0.7
        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=dataDictionary,
                                                  belongOp=Belong(belongOp), field=field, quant_rel=quant_rel,
                                                  quant_op=Operator(quant_op))
        assert result is False, "Test Case 4 Failed: Expected False, but got True"
        print_and_log("Test Case 4 Passed: Expected False, got False")

        # Example 5 of checkFixValueRange
        value = '0'
        dataDictionary = pd.DataFrame(data={'c1': ['0', '0', '0', '0', '0', '0', '0', None, None, None]})
        belongOp = 0  # Belong
        field = None
        quant_op = 1  # greater
        quant_abs = 3
        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=dataDictionary,
                                                  belongOp=Belong(belongOp), field=field, quant_abs=quant_abs,
                                                  quant_op=Operator(quant_op))
        assert result is True, "Test Case 5 Failed: Expected True, but got False"
        print_and_log("Test Case 5 Passed: Expected True, got True")

        # Example 6 of checkFixValueRange
        value = None
        dataDictionary = pd.DataFrame(data={'c1': ['0', '0', '0', '0', '0', '0', '0', None, None, None]})
        belongOp = 0  # Belong
        field = None
        quant_op = 1  # greater
        quant_abs = 5
        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=dataDictionary,
                                                  belongOp=Belong(belongOp), field=field, quant_abs=quant_abs,
                                                  quant_op=Operator(quant_op))
        assert result is False, "Test Case 6 Failed: Expected False, but got True"
        print_and_log("Test Case 6 Passed: Expected False, got False")

        # Example 8 of checkFixValueRange
        value = '3'
        dataDictionary = pd.DataFrame(data={'c1': ['0', '0', '0', '0', '0', '0', '0', None, None, None]})
        belongOp = 1  # Not Belong
        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=dataDictionary,
                                                  belongOp=Belong(belongOp))
        assert result is True, "Test Case 8 Failed: Expected True, but got False"
        print_and_log("Test Case 8 Passed: Expected True, got True")

        # Example 9 of checkFixValueRange
        value = '0'
        dataDictionary = pd.DataFrame(data={'c1': ['0', '0', '0', '0', '0', '0', '0', None, None, None]})
        belongOp = 1  # Not Belong
        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=dataDictionary,
                                                  belongOp=Belong(belongOp))
        assert result is False, "Test Case 9 Failed: Expected False, but got True"
        print_and_log("Test Case 9 Passed: Expected False, got False")

        # Example 11 of checkFixValueRange
        value = '0'
        dataDictionary = pd.DataFrame(data={'c1': ['0', '0', '0', '0', '0', '0', '0', None, None, None]})
        belongOp = 0  # Belong
        field = 'c1'
        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=dataDictionary, field=field,
                                                  belongOp=Belong(belongOp))
        assert result is True, "Test Case 11 Failed: Expected True, but got False"
        print_and_log("Test Case 11 Passed: Expected True, got True")

        # Example 12 of checkFixValueRange
        value = '5'
        dataDictionary = pd.DataFrame(data={'c1': ['0', '0', '0', '0', '0', '0', '0', None, None, None]})
        belongOp = 0  # Belong
        field = 'c1'
        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=dataDictionary, field=field,
                                                  belongOp=Belong(belongOp))
        assert result is False, "Test Case 12 Failed: Expected False, but got True"
        print_and_log("Test Case 12 Passed: Expected False, got False")

        # Example 15 of checkFixValueRange
        value = '0'
        dataDictionary = pd.DataFrame(data={'c1': ['0', '0', '0', '0', '0', '0', '0', None, None, None]})
        belongOp = 0  # Belong
        field = 'c1'
        quant_op = 1  # greater
        quant_abs = 3
        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=dataDictionary, field=field,
                                                  quant_abs=quant_abs, quant_op=Operator(quant_op),
                                                  belongOp=Belong(belongOp))
        assert result is True, "Test Case 15 Failed: Expected True, but got False"
        print_and_log("Test Case 15 Passed: Expected True, got True")

        # Example 16 of checkFixValueRange
        value = '0'
        dataDictionary = pd.DataFrame(data={'c1': ['0', '0', '0', '0', '0', '0', '0', None, None, None]})
        belongOp = 0  # Belong
        field = 'c1'
        quant_op = 1  # greater
        quant_abs = 10
        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=dataDictionary, field=field,
                                                  quant_abs=quant_abs, quant_op=Operator(quant_op),
                                                  belongOp=Belong(belongOp))
        assert result is False, "Test Case 16 Failed: Expected False, but got True"
        print_and_log("Test Case 16 Passed: Expected False, got False")

        # Example 18 of checkFixValueRange
        value = '3'
        dataDictionary = pd.DataFrame(data={'c1': ['0', '0', '0', '0', '0', '0', '0', None, None, None]})
        belongOp = 1  # Not Belong
        field = 'c1'
        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=dataDictionary, field=field,
                                                  belongOp=Belong(belongOp))
        assert result is True, "Test Case 18 Failed: Expected True, but got False"
        print_and_log("Test Case 18 Passed: Expected True, got True")

        # Example 19 of checkFixValueRange
        value = '0'
        dataDictionary = pd.DataFrame(data={'c1': ['0', '0', '0', '0', '0', '0', '0', None, None, None]})
        belongOp = 1  # Not Belong
        field = 'c1'
        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=dataDictionary, field=field,
                                                  belongOp=Belong(belongOp))
        assert result is False, "Test Case 19 Failed: Expected False, but got True"
        print_and_log("Test Case 19 Passed: Expected False, got False")


        # Casos de error añadidos
        print_and_log("")
        print_and_log("Casos de error añadidos:")

        # Example 4.5 of checkFixValueRange
        value = None
        dataDictionary = pd.DataFrame(data={'c1': ['0', '0', '0', '0', '0', '0', '0', None, None, None]})
        belongOp = 0  # Belong
        field = None
        quant_op = 2  # lessEqual
        quant_rel = 0.4
        quant_abs = 50
        expected_exception = ValueError
        with self.assertRaises(expected_exception) as context:
            self.pre_post.checkFixValueRange(value=value, dataDictionary=dataDictionary,
                                             belongOp=Belong(belongOp), field=field, quant_rel=quant_rel,
                                             quant_abs=quant_abs, quant_op=Operator(quant_op))
        print_and_log(f"Test Case 4.5 Passed: Expected ValueError, got ValueError")

        # Example 7 of checkFixValueRange
        value = '0'
        dataDictionary = pd.DataFrame(data={'c1': ['0', '0', '0', '0', '0', '0', '0', None, None, None]})
        belongOp = 0  # Belong
        field = None
        quant_op = 2  # lessEqual
        expected_exception = ValueError
        with self.assertRaises(expected_exception) as context:
            self.pre_post.checkFixValueRange(value=value, dataDictionary=dataDictionary,
                                             belongOp=Belong(belongOp), field=field,
                                             quant_op=Operator(quant_op))
        print_and_log("Test Case 7 Passed: Expected ValueError, got ValueError")

        # # Example 10 of checkFixValueRange
        value = '0'
        dataDictionary = pd.DataFrame(data={'c1': ['0', '0', '0', '0', '0', '0', '0', None, None, None]})
        belongOp = 1  # Not Belong
        quant_op = 3 # less
        expected_exception = ValueError
        with self.assertRaises(expected_exception) as context:
            self.pre_post.checkFixValueRange(value=value, dataDictionary=dataDictionary,
                                             belongOp=Belong(belongOp), quant_op=Operator(quant_op))
        print_and_log("Test Case 10 Passed: Expected ValueError, got ValueError")

        # Example 17 of checkFixValueRange
        value = '0'
        dataDictionary = pd.DataFrame(data={'c1': ['0', '0', '0', '0', '0', '0', '0', None, None, None]})
        belongOp = 0  # Belong
        field = 'c1'
        quant_op = 2  # lessEqual
        expected_exception = ValueError
        with self.assertRaises(expected_exception) as context:
            self.pre_post.checkFixValueRange(value=value, dataDictionary=dataDictionary,
                                             belongOp=Belong(belongOp), field=field, quant_op=Operator(quant_op))
        print_and_log("Test Case 17 Passed: Expected ValueError, got ValueError")

        # Example 20 of checkFixValueRange
        value = '0'
        dataDictionary = pd.DataFrame(data={'c1': ['0', '0', '0', '0', '0', '0', '0', None, None, None]})
        belongOp = 1  # Not Belong
        field = 'c1'
        quant_op = 3 # less
        expected_exception = ValueError
        with self.assertRaises(expected_exception) as context:
            self.pre_post.checkFixValueRange(value=value, dataDictionary=dataDictionary, field=field,
                                             belongOp=Belong(belongOp), quant_op=Operator(quant_op))
        print_and_log("Test Case 20 Passed: Expected ValueError, got ValueError")
        print_and_log("")
        print_and_log("-----------------------------------------------------------")
        print_and_log("")

    def execute_CheckFixValueRangeFloat_SimpleTests(self):
        """
        Execute the simple tests of the function checkFixValueRange
        """
        print_and_log("Testing CheckFixValueRangeFloat Function")

        print_and_log("")
        print_and_log("Casos Básicos solicitados en la especificación del contrato:")

        # 23 Casos

        # Example 13 of checkFixValueRange
        # Check that value None belongs to the data dictionary in field 'c1' and that
        # it appears less or equal than 30% of the times
        value = None
        dataDictionary = pd.DataFrame(data={'c1': [0, 0, 0, 0, 0, 0, 0, None, None, None]})
        belongOp = 0  # Belong
        field = 'c1'
        quant_op = 2  # lessEqual
        quant_rel = 0.3
        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=dataDictionary,
                                                  belongOp=Belong(belongOp), field=field, quant_rel=quant_rel,
                                                  quant_op=Operator(quant_op))
        assert result is True, "Test Case 13 Failed: Expected True, but got False"
        print_and_log("Test Case 13 Passed: Expected True, got True")

        # Example 14 of checkFixValueRange
        # Check that value None belongs to the data dictionary in field 'c1' and that
        # it appears less or equal than 30% of the times
        value = None
        dataDictionary = pd.DataFrame(data={'c1': [0, 0, 0, 0, 0, 0, None, None, None, None]})
        belongOp = 0  # Belong
        field = 'c1'
        quant_op = 2  # lessEqual
        quant_rel = 0.3
        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=dataDictionary,
                                                  belongOp=Belong(belongOp), field=field, quant_rel=quant_rel,
                                                  quant_op=Operator(quant_op))
        assert result is False, "Test Case 14 Failed: Expected False, but got True"
        print_and_log("Test Case 14 Passed: Expected False, got False")

        # Example 18 of checkFixValueRange
        # Check that value 1 doesn't belong to the data dictionary in field 'c1'
        value = 1
        dataDictionary = pd.DataFrame(data={'c1': [0, 0, 0, 0, 0, 0, 0, None, None, None]})
        belongOp = 1  # NotBelong
        field = 'c1'
        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=dataDictionary,
                                                  belongOp=Belong(belongOp), field=field)
        assert result is True, "Test Case 18 Failed: Expected True, but got False"
        print_and_log("Test Case 18 Passed: Expected True, got True")

        # Example 14.5 of checkFixValueRange
        value = None
        dataDictionary = pd.DataFrame(data={'c1': [0, 0, 0, 0, 0, 0, 0, None, None, None]})
        belongOp = 0  # Belong
        field = 'c1'
        quant_op = 2  # lessEqual
        quant_rel = 0.4
        quant_abs = 50
        expected_exception = ValueError
        with self.assertRaises(expected_exception) as context:
            result = self.pre_post.checkFixValueRange(value=value, dataDictionary=dataDictionary,
                                                      belongOp=Belong(belongOp), field=field, quant_rel=quant_rel,
                                                      quant_abs=quant_abs, quant_op=Operator(quant_op))
        print_and_log("Test Case 14.5 Passed: Expected ValueError, got ValueError")


        print_and_log("")
        print_and_log("Casos Básicos añadidos:")

        # Example 1 of checkFixValueRange
        value = 3
        dataDictionary = pd.DataFrame(data={'c1': [0, 0, 0, 3, 0, 0, 0, None, None, None]})
        belongOp = 0  # Belong
        field = None  # None
        quant_op = None  # None
        quant_rel = 0.3
        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=dataDictionary,
                                                  belongOp=Belong(belongOp), field=field, quant_rel=quant_rel,
                                                  quant_op=quant_op)
        assert result is True, "Test Case 1 Failed: Expected True, but got False"
        print_and_log("Test Case 1 Passed: Expected True, got True")

        # Example 2 of checkFixValueRange
        value = 3.5
        dataDictionary = pd.DataFrame(data={'c1': [0, 0, 0, 0, 0, 0, 0, None, None, None]})
        belongOp = 0  # Belong
        field = None  # None
        quant_op = None  # None
        quant_rel = 0.3
        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=dataDictionary,
                                                  belongOp=Belong(belongOp), field=field, quant_rel=quant_rel,
                                                  quant_op=quant_op)
        assert result is False, "Test Case 2 Failed: Expected False, but got True"
        print_and_log("Test Case 2 Passed: Expected False, got False")

        # Example 3 of checkFixValueRange
        value = 0
        dataDictionary = pd.DataFrame(data={'c1': [0, 0, 0, 0, 0, 0, 0, None, None, None]})
        belongOp = 0  # Belong
        field = None
        quant_op = 1  # greater
        quant_rel = 0.1
        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=dataDictionary,
                                                  belongOp=Belong(belongOp), field=field, quant_rel=quant_rel,
                                                  quant_op=Operator(quant_op))
        assert result is True, "Test Case 3 Failed: Expected True, but got False"
        print_and_log("Test Case 3 Passed: Expected True, got True")

        # Example 4 of checkFixValueRange
        value = 0
        dataDictionary = pd.DataFrame(data={'c1': [0, 0, 0, 0, 0, 0, 0, None, None, None]})
        belongOp = 0  # Belong
        field = None
        quant_op = 1  # greater
        quant_rel = 0.7
        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=dataDictionary,
                                                  belongOp=Belong(belongOp), field=field, quant_rel=quant_rel,
                                                  quant_op=Operator(quant_op))
        assert result is False, "Test Case 4 Failed: Expected False, but got True"
        print_and_log("Test Case 4 Passed: Expected False, got False")

        # Example 5 of checkFixValueRange
        value = 0
        dataDictionary = pd.DataFrame(data={'c1': [0, 0, 0, 0, 0, 0, 0, None, None, None]})
        belongOp = 0  # Belong
        field = None
        quant_op = 1  # greater
        quant_abs = 3
        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=dataDictionary,
                                                  belongOp=Belong(belongOp), field=field, quant_abs=quant_abs,
                                                  quant_op=Operator(quant_op))
        assert result is True, "Test Case 5 Failed: Expected True, but got False"
        print_and_log("Test Case 5 Passed: Expected True, got True")

        # Example 6 of checkFixValueRange
        value = None
        dataDictionary = pd.DataFrame(data={'c1': [0, 0, 0, 0, 0, 0, 0, None, None, None]})
        belongOp = 0  # Belong
        field = None
        quant_op = 1  # greater
        quant_abs = 5
        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=dataDictionary,
                                                  belongOp=Belong(belongOp), field=field, quant_abs=quant_abs,
                                                  quant_op=Operator(quant_op))
        assert result is False, "Test Case 6 Failed: Expected False, but got True"
        print_and_log("Test Case 6 Passed: Expected False, got False")

        # Example 8 of checkFixValueRange
        value = 3.8
        dataDictionary = pd.DataFrame(data={'c1': [0, 0, 0, 0, 0, 0, 0, None, None, None]})
        belongOp = 1  # Not Belong
        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=dataDictionary,
                                                  belongOp=Belong(belongOp))
        assert result is True, "Test Case 8 Failed: Expected True, but got False"
        print_and_log("Test Case 8 Passed: Expected True, got True")

        # Example 9 of checkFixValueRange
        value = 0
        dataDictionary = pd.DataFrame(data={'c1': [0, 0, 0, 0, 0, 0, 0, None, None, None]})
        belongOp = 1  # Not Belong
        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=dataDictionary,
                                                  belongOp=Belong(belongOp))
        assert result is False, "Test Case 9 Failed: Expected False, but got True"
        print_and_log("Test Case 9 Passed: Expected False, got False")

        # Example 11 of checkFixValueRange
        value = 0
        dataDictionary = pd.DataFrame(data={'c1': [0, 0, 0, 0, 0, 0, 0, None, None, None]})
        belongOp = 0  # Belong
        field = 'c1'
        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=dataDictionary, field=field,
                                                  belongOp=Belong(belongOp))
        assert result is True, "Test Case 11 Failed: Expected True, but got False"
        print_and_log("Test Case 11 Passed: Expected True, got True")

        # Example 12 of checkFixValueRange
        value = 5
        dataDictionary = pd.DataFrame(data={'c1': [0, 0, 0, 0, 0, 0, 0, None, None, None]})
        belongOp = 0  # Belong
        field = 'c1'
        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=dataDictionary, field=field,
                                                  belongOp=Belong(belongOp))
        assert result is False, "Test Case 12 Failed: Expected False, but got True"
        print_and_log("Test Case 12 Passed: Expected False, got False")

        # Example 15 of checkFixValueRange
        value = None
        dataDictionary = pd.DataFrame(data={'c1': [0, 0, 0, 0, 0, 0, 0, None, None, None]})
        belongOp = 0  # Belong
        field = 'c1'
        quant_op = 1  # greater
        quant_abs = 2
        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=dataDictionary, field=field,
                                                  quant_abs=quant_abs, quant_op=Operator(quant_op),
                                                  belongOp=Belong(belongOp))
        assert result is True, "Test Case 15 Failed: Expected True, but got False"
        print_and_log("Test Case 15 Passed: Expected True, got True")

        # Example 16 of checkFixValueRange
        value = 0
        dataDictionary = pd.DataFrame(data={'c1': [0, 0, 0, 0, 0, 0, 0, None, None, None]})
        belongOp = 0  # Belong
        field = 'c1'
        quant_op = 1  # greater
        quant_abs = 10
        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=dataDictionary, field=field,
                                                  quant_abs=quant_abs, quant_op=Operator(quant_op),
                                                  belongOp=Belong(belongOp))
        assert result is False, "Test Case 16 Failed: Expected False, but got True"
        print_and_log("Test Case 16 Passed: Expected False, got False")

        # Example 18 of checkFixValueRange
        value = 7.45
        dataDictionary = pd.DataFrame(data={'c1': [0, 0, 0, 0, 0, 0, 0, None, None, None]})
        belongOp = 1  # Not Belong
        field = 'c1'
        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=dataDictionary, field=field,
                                                  belongOp=Belong(belongOp))
        assert result is True, "Test Case 18 Failed: Expected True, but got False"
        print_and_log("Test Case 18 Passed: Expected True, got True")

        # Example 19 of checkFixValueRange
        value = 0
        dataDictionary = pd.DataFrame(data={'c1': [0, 0, 0, 0, 0, 0, 0, None, None, None]})
        belongOp = 1  # Not Belong
        field = 'c1'
        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=dataDictionary, field=field,
                                                  belongOp=Belong(belongOp))
        assert result is False, "Test Case 19 Failed: Expected False, but got True"
        print_and_log("Test Case 19 Passed: Expected False, got False")

        # --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        # Casos de error añadidos
        print_and_log("")
        print_and_log("Casos de error añadidos:")

        # Example 4.5 of checkFixValueRange
        value = None
        dataDictionary = pd.DataFrame(data={'c1': [0, 0, 0, 0, 0, 0, 0, None, None, None]})
        belongOp = 0  # Belong
        field = None
        quant_op = 2  # lessEqual
        quant_rel = 0.4
        quant_abs = 50
        expected_exception = ValueError
        with self.assertRaises(expected_exception) as context:
            result = self.pre_post.checkFixValueRange(value=value, dataDictionary=dataDictionary,
                                                      belongOp=Belong(belongOp), field=field, quant_rel=quant_rel,
                                                      quant_abs=quant_abs, quant_op=Operator(quant_op))
        print_and_log("Test Case 4.5 Passed: Expected ValueError, got ValueError")

        # Example 7 of checkFixValueRange
        value = 0
        dataDictionary = pd.DataFrame(data={'c1': [0, 0, 0, 0, 0, 0, 0, None, None, None]})
        belongOp = 0  # Belong
        field = None
        quant_op = 2  # lessEqual
        expected_exception = ValueError
        with self.assertRaises(expected_exception) as context:
            result = self.pre_post.checkFixValueRange(value=value, dataDictionary=dataDictionary,
                                                      belongOp=Belong(belongOp), field=field,
                                                      quant_op=Operator(quant_op))
        print_and_log("Test Case 7 Passed: Expected ValueError, got ValueError")

        # # Example 10 of checkFixValueRange
        value = 0
        dataDictionary = pd.DataFrame(data={'c1': [0, 0, 0, 0, 0, 0, 0, None, None, None]})
        belongOp = 1  # Not Belong
        quant_op = 3
        expected_exception = ValueError
        with self.assertRaises(expected_exception) as context:
            result = self.pre_post.checkFixValueRange(value=value, dataDictionary=dataDictionary,
                                                      belongOp=Belong(belongOp), quant_op=Operator(quant_op))
        print_and_log("Test Case 10 Passed: Expected ValueError, got ValueError")

        # Example 17 of checkFixValueRange
        value = 0
        dataDictionary = pd.DataFrame(data={'c1': [0, 0, 0, 0, 0, 0, 0, None, None, None]})
        belongOp = 0  # Belong
        field = 'c1'
        quant_op = 2  # lessEqual
        expected_exception = ValueError
        with self.assertRaises(expected_exception) as context:
            result = self.pre_post.checkFixValueRange(value=value, dataDictionary=dataDictionary,
                                                      belongOp=Belong(belongOp), field=field,
                                                      quant_op=Operator(quant_op))
        print_and_log("Test Case 17 Passed: Expected ValueError, got ValueError")

        # Example 20 of checkFixValueRange
        value = 0
        dataDictionary = pd.DataFrame(data={'c1': [0, 0, 0, 0, 0, 0, 0, None, None, None]})
        belongOp = 1  # Not Belong
        field = 'c1'
        quant_op = 3
        expected_exception = ValueError
        with self.assertRaises(expected_exception) as context:
            result = self.pre_post.checkFixValueRange(value=value, dataDictionary=dataDictionary, field=field,
                                                      belongOp=Belong(belongOp), quant_op=Operator(quant_op))
        print_and_log("Test Case 20 Passed: Expected ValueError, got ValueError")
        print_and_log("")
        print_and_log("-----------------------------------------------------------")
        print_and_log("")

    def execute_CheckFixValueRangeDateTime_SimpleTests(self):
        """
        Execute the simple tests of the function checkFixValueRange
        """
        print_and_log("Testing CheckFixValueRangeDateTime Function")
        print_and_log("")
        print_and_log("Casos Básicos solicitados en la especificación del contrato:")

        # 23 Casos

        # Example 13 of checkFixValueRange
        value = None
        # dataDictionary utilizado en casi todos los ejemplos de pruebas
        dataDictionary = pd.DataFrame(data={'c1': [pd.Timestamp('20180310'), pd.Timestamp('20180310'),
                                                   pd.Timestamp('20180310'), pd.Timestamp('20180310'),
                                                   pd.Timestamp('20180310'), pd.Timestamp('20180310'),
                                                   pd.Timestamp('20180310'), None, None, None]})
        belongOp = 0  # Belong
        field = 'c1'
        quant_op = 2  # lessEqual
        quant_rel = 0.3
        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=dataDictionary,
                                                  belongOp=Belong(belongOp), field=field, quant_rel=quant_rel,
                                                  quant_op=Operator(quant_op))
        assert result is True, "Test Case 13 Failed: Expected True, but got False"
        print_and_log("Test Case 13 Passed: Expected True, got True")

        # Example 14 of checkFixValueRange
        value = None
        dataDictionary1 = pd.DataFrame(data={'c1': [pd.Timestamp('20180310'), pd.Timestamp('20180310'),
                                                    pd.Timestamp('20180310'), pd.Timestamp('20180310'),
                                                    pd.Timestamp('20180310'), pd.Timestamp('20180310'),
                                                    None, None, None, None]})
        belongOp = 0  # Belong
        field = 'c1'
        quant_op = 2  # lessEqual
        quant_rel = 0.3
        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=dataDictionary1,
                                                  belongOp=Belong(belongOp), field=field, quant_rel=quant_rel,
                                                  quant_op=Operator(quant_op))
        assert result is False, "Test Case 14 Failed: Expected False, but got True"
        print_and_log("Test Case 14 Passed: Expected False, got False")

        # Example 18 of checkFixValueRange
        value = pd.Timestamp('20240310')
        belongOp = 1  # NotBelong
        field = 'c1'
        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=dataDictionary,
                                                  belongOp=Belong(belongOp), field=field)
        assert result is True, "Test Case 18 Failed: Expected True, but got False"
        print_and_log("Test Case 18 Passed: Expected True, got True")

        # Example 14.5 of checkFixValueRange
        value = None
        belongOp = 0  # Belong
        field = 'c1'
        quant_op = 2  # lessEqual
        quant_rel = 0.4
        quant_abs = 50
        expected_exception = ValueError
        with self.assertRaises(expected_exception) as context:
            result = self.pre_post.checkFixValueRange(value=value, dataDictionary=dataDictionary,
                                                      belongOp=Belong(belongOp), field=field,
                                                      quant_rel=quant_rel,
                                                      quant_abs=quant_abs, quant_op=Operator(quant_op))
        print_and_log("Test Case 14.5 Passed: Expected ValueError, got ValueError")


        print_and_log("")
        print_and_log("Casos añadidos:")

        # Example 1 of checkFixValueRange
        value = pd.Timestamp('20110814')
        dataDictionary2 = pd.DataFrame(data={'c1': [pd.Timestamp('20180310'), pd.Timestamp('20180310'),
                                                    pd.Timestamp('20110814'), pd.Timestamp('20180310'),
                                                    pd.Timestamp('20180310'), pd.Timestamp('20180310'),
                                                    pd.Timestamp('20180310'), None, None, None]})
        belongOp = 0  # Belong
        field = None  # None
        quant_op = None  # None
        quant_rel = 0.3
        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=dataDictionary2,
                                                  belongOp=Belong(belongOp), field=field, quant_rel=quant_rel,
                                                  quant_op=quant_op)
        assert result is True, "Test Case 1 Failed: Expected True, but got False"
        print_and_log("Test Case 1 Passed: Expected True, got True")

        # Example 2 of checkFixValueRange
        value = pd.Timestamp('20171115')
        belongOp = 0  # Belong
        field = None  # None
        quant_op = None  # None
        quant_rel = 0.3
        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=dataDictionary,
                                                  belongOp=Belong(belongOp), field=field, quant_rel=quant_rel,
                                                  quant_op=quant_op)
        assert result is False, "Test Case 2 Failed: Expected False, but got True"
        print_and_log("Test Case 2 Passed: Expected False, got False")

        # Example 3 of checkFixValueRange
        value = pd.Timestamp('20180310')
        belongOp = 0  # Belong
        field = None
        quant_op = 1  # greater
        quant_rel = 0.1
        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=dataDictionary,
                                                  belongOp=Belong(belongOp), field=field, quant_rel=quant_rel,
                                                  quant_op=Operator(quant_op))
        assert result is True, "Test Case 3 Failed: Expected True, but got False"
        print_and_log("Test Case 3 Passed: Expected True, got True")

        # Example 4 of checkFixValueRange
        value = pd.Timestamp('20180310')
        belongOp = 0  # Belong
        field = None
        quant_op = 1  # greater
        quant_rel = 0.7
        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=dataDictionary,
                                                  belongOp=Belong(belongOp), field=field, quant_rel=quant_rel,
                                                  quant_op=Operator(quant_op))
        assert result is False, "Test Case 4 Failed: Expected False, but got True"
        print_and_log("Test Case 4 Passed: Expected False, got False")

        # Example 5 of checkFixValueRange
        value = pd.Timestamp('20180310')
        belongOp = 0  # Belong
        field = None
        quant_op = 1  # greater
        quant_abs = 3
        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=dataDictionary,
                                                  belongOp=Belong(belongOp), field=field, quant_abs=quant_abs,
                                                  quant_op=Operator(quant_op))
        assert result is True, "Test Case 5 Failed: Expected True, but got False"
        print_and_log("Test Case 5 Passed: Expected True, got True")

        # Example 6 of checkFixValueRange
        value = None
        belongOp = 0  # Belong
        field = None
        quant_op = 1  # greater
        quant_abs = 5
        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=dataDictionary,
                                                  belongOp=Belong(belongOp), field=field, quant_abs=quant_abs,
                                                  quant_op=Operator(quant_op))
        assert result is False, "Test Case 6 Failed: Expected False, but got True"
        print_and_log("Test Case 6 Passed: Expected False, got False")

        # Example 8 of checkFixValueRange
        value = pd.Timestamp('20161108')
        belongOp = 1  # Not Belong
        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=dataDictionary,
                                                  belongOp=Belong(belongOp))
        assert result is True, "Test Case 8 Failed: Expected True, but got False"
        print_and_log("Test Case 8 Passed: Expected True, got True")

        # Example 9 of checkFixValueRange
        value = pd.Timestamp('20180310')
        belongOp = 1  # Not Belong
        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=dataDictionary,
                                                  belongOp=Belong(belongOp))
        assert result is False, "Test Case 9 Failed: Expected False, but got True"
        print_and_log("Test Case 9 Passed: Expected False, got False")

        # Example 11 of checkFixValueRange
        value = pd.Timestamp('20180310')
        belongOp = 0  # Belong
        field = 'c1'
        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=dataDictionary, field=field,
                                                  belongOp=Belong(belongOp))
        assert result is True, "Test Case 11 Failed: Expected True, but got False"
        print_and_log("Test Case 11 Passed: Expected True, got True")

        # Example 12 of checkFixValueRange
        value = pd.Timestamp('20101225')
        belongOp = 0  # Belong
        field = 'c1'
        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=dataDictionary, field=field,
                                                  belongOp=Belong(belongOp))
        assert result is False, "Test Case 12 Failed: Expected False, but got True"
        print_and_log("Test Case 12 Passed: Expected False, got False")

        # Example 15 of checkFixValueRange
        value = None
        belongOp = 0  # Belong
        field = 'c1'
        quant_op = 1  # greater
        quant_abs = 2
        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=dataDictionary, field=field,
                                                  quant_abs=quant_abs, quant_op=Operator(quant_op),
                                                  belongOp=Belong(belongOp))
        assert result is True, "Test Case 15 Failed: Expected True, but got False"
        print_and_log("Test Case 15 Passed: Expected True, got True")

        # Example 16 of checkFixValueRange
        value = pd.Timestamp('20180310')
        belongOp = 0  # Belong
        field = 'c1'
        quant_op = 1  # greater
        quant_abs = 10
        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=dataDictionary, field=field,
                                                  quant_abs=quant_abs, quant_op=Operator(quant_op),
                                                  belongOp=Belong(belongOp))
        assert result is False, "Test Case 16 Failed: Expected False, but got True"
        print_and_log("Test Case 16 Passed: Expected False, got False")

        # Example 18 of checkFixValueRange
        value = pd.Timestamp('20150815')
        belongOp = 1  # Not Belong
        field = 'c1'
        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=dataDictionary, field=field,
                                                  belongOp=Belong(belongOp))
        assert result is True, "Test Case 18 Failed: Expected True, but got False"
        print_and_log("Test Case 18 Passed: Expected True, got True")

        # Example 19 of checkFixValueRange
        value = pd.Timestamp('20180310')
        belongOp = 1  # Not Belong
        field = 'c1'
        result = self.pre_post.checkFixValueRange(value=value, dataDictionary=dataDictionary, field=field,
                                                  belongOp=Belong(belongOp))
        assert result is False, "Test Case 19 Failed: Expected False, but got True"
        print_and_log("Test Case 19 Passed: Expected False, got False")


        # Casos de error añadidos
        print_and_log("")
        print_and_log("Casos de error añadidos:")

        # Example 4.5 of checkFixValueRange
        value = None
        belongOp = 0  # Belong
        field = None
        quant_op = 2  # lessEqual
        quant_rel = 0.4
        quant_abs = 50
        expected_exception = ValueError
        with self.assertRaises(expected_exception) as context:
            result = self.pre_post.checkFixValueRange(value=value, dataDictionary=dataDictionary,
                                                      belongOp=Belong(belongOp), field=field,
                                                      quant_rel=quant_rel,
                                                      quant_abs=quant_abs, quant_op=Operator(quant_op))
        print_and_log("Test Case 4.5 Passed: Expected ValueError, got ValueError")

        # Example 7 of checkFixValueRange
        value = pd.Timestamp('20180310')
        belongOp = 0  # Belong
        field = None
        quant_op = 2  # lessEqual
        expected_exception = ValueError
        with self.assertRaises(expected_exception) as context:
            result = self.pre_post.checkFixValueRange(value=value, dataDictionary=dataDictionary,
                                                      belongOp=Belong(belongOp), field=field,
                                                      quant_op=Operator(quant_op))
        print_and_log("Test Case 7 Passed: Expected ValueError, got ValueError")

        # # Example 10 of checkFixValueRange
        value = pd.Timestamp('20180310')
        belongOp = 1  # Not Belong
        quant_op = 3
        expected_exception = ValueError
        with self.assertRaises(expected_exception) as context:
            result = self.pre_post.checkFixValueRange(value=value, dataDictionary=dataDictionary,
                                                      belongOp=Belong(belongOp), quant_op=Operator(quant_op))
        print_and_log("Test Case 10 Passed: Expected ValueError, got ValueError")

        # Example 17 of checkFixValueRange
        value = pd.Timestamp('20180310')
        belongOp = 0  # Belong
        field = 'c1'
        quant_op = 2  # lessEqual
        expected_exception = ValueError
        with self.assertRaises(expected_exception) as context:
            result = self.pre_post.checkFixValueRange(value=value, dataDictionary=dataDictionary,
                                                      belongOp=Belong(belongOp), field=field,
                                                      quant_op=Operator(quant_op))
        print_and_log("Test Case 17 Passed: Expected ValueError, got ValueError")

        # Example 20 of checkFixValueRange
        value = pd.Timestamp('20180310')
        belongOp = 1  # Not Belong
        field = 'c1'
        quant_op = 3
        expected_exception = ValueError
        with self.assertRaises(expected_exception) as context:
            result = self.pre_post.checkFixValueRange(value=value, dataDictionary=dataDictionary, field=field,
                                                      belongOp=Belong(belongOp), quant_op=Operator(quant_op))
        print_and_log("Test Case 20 Passed: Expected ValueError, got ValueError")
        print_and_log("")
        print_and_log("-----------------------------------------------------------")
        print_and_log("")

    def execute_CheckIntervalRangeFloat_SimpleTests(self):
        """
        Execute the simple tests of the function checkIntervalRangeFloat
        """
        print_and_log("Testing checkIntervalRangeFloat Function")
        print_and_log("")

        print_and_log("Casos Básicos solicitados en la especificación del contrato:")

        # 35 casos

        # Example 1 of checkIntervalRangeFloat
        # Check that the data in the field 'c1' of the data dictionary belongs to the interval [0, 5]
        leftMargin = 0
        rightMargin = 5
        dataDictionary = pd.DataFrame(data={'c1': [0, 1, 2, 3, 4, 5]})
        closureType = 3  # ClosedClosed
        belongOp = 0  # Belong
        field = 'c1'
        result = self.pre_post.checkIntervalRangeFloat(left_margin=leftMargin, right_margin=rightMargin,
                                                       dataDictionary=dataDictionary, closureType=Closure(closureType),
                                                       belongOp=Belong(belongOp), field=field)
        assert result is True, "Test Case 1 Failed: Expected True, but got False"
        print_and_log("Test Case 1 Passed: Expected True, got True")

        # Example 2 of checkIntervalRangeFloat
        # Check that the data in the field 'c1' of the data dictionary belongs to the interval [0, 5]
        # adn returns False because the 0 is not included in the interval and there is a 0 in the data dictionary
        leftMargin = 0
        rightMargin = 5
        dataDictionary = pd.DataFrame(data={'c1': [0, 1, 2, 3, 4, 5]})
        closureType = 1  # OpenClosed
        belongOp = 0  # Belong
        field = 'c1'
        result = self.pre_post.checkIntervalRangeFloat(left_margin=leftMargin, right_margin=rightMargin,
                                                       dataDictionary=dataDictionary, closureType=Closure(closureType),
                                                       belongOp=Belong(belongOp), field=field)
        assert result is False, "Test Case 2 Failed: Expected False, but got True"
        print_and_log("Test Case 2 Passed: Expected False, got False")
        print_and_log("")


        print_and_log("Casos Básicos añadidos:")
        # Rango de prueba utilizado en todas las llamadas
        left = 0
        right = 70.4
        # field = None
        field = None
        # belongOp = 0
        belongOp = 0

        # Example 0 of checkIntervalRangeFloat
        # Check that the left margin is not bigger than the right margin
        left0 = 20
        right0 = 15
        dataDictionary = pd.DataFrame(data={'c1': [0, 2.9, 5, 25.3, 4, 67.5, 0, 0.5, None, None],
                                            'c2': [0, 0, 0.3, 1.4, 0.3, 5, 0, 0, None, None]})
        closure = 0  # OpenOpen
        expected_exception = ValueError
        with self.assertRaises(expected_exception) as context:
            result = self.pre_post.checkIntervalRangeFloat(left_margin=left0, right_margin=right0,
                                                           dataDictionary=dataDictionary, closureType=Closure(closure),
                                                           belongOp=Belong(belongOp))
        print_and_log("Test Case 0 Passed: Expected ValueError, got ValueError")

        # Example 1.1 of checkIntervalRangeFloat
        # Check that the data in the whole dictionary belongs to the interval (0, 70.4)
        dataDictionary = pd.DataFrame(data={'c1': [0, 2.9, 5, 25.3, 4, 67.5, 0, 0.5, None, None],
                                            'c2': [0, 0, 0.3, 1.4, 0.3, 5, 0, 0, None, None]})
        closure = 0  # OpenOpen
        result = self.pre_post.checkIntervalRangeFloat(left_margin=left, right_margin=right,
                                                       dataDictionary=dataDictionary, closureType=Closure(closure),
                                                       belongOp=Belong(belongOp))
        assert result is False, "Test Case 1.1 Failed: Expected False, but got True"
        print_and_log("Test Case 1.1 Passed: Expected False, got False")

        # Example 2.1 of checkIntervalRangeFloat
        # Check that the data in the whole dictionary belongs to the interval (0, 70.4)
        dataDictionary = pd.DataFrame(data={'c1': [0.1, 2.9, 5, 25.3, 4, 67.5, 42, 0.5, None, None],
                                            'c2': [7, 15, 0.3, 1.4, 0.3, 5, 7.0, 8, None, None]})
        closure = 0  # OpenOpen
        result = self.pre_post.checkIntervalRangeFloat(left_margin=left, right_margin=right,
                                                       dataDictionary=dataDictionary, closureType=Closure(closure),
                                                       belongOp=Belong(belongOp))
        assert result is True, "Test Case 2.1 Failed: Expected True, but got False"
        print_and_log("Test Case 2.1 Passed: Expected True, got True")

        # Example 3 of checkIntervalRangeFloat
        # Check that the data in the whole dictionary belongs to the interval (0, 70.4]
        dataDictionary = pd.DataFrame(data={'c1': [0.01, 2.9, 5, 25.3, 4, 67.5, 42, 0.5, None, None],
                                            'c2': [7, 15, 0.3, 1.4, 0.3, 5, 70.4, 8, None, None]})
        closure = 1  # OpenClosed
        result = self.pre_post.checkIntervalRangeFloat(left_margin=left, right_margin=right,
                                                       dataDictionary=dataDictionary, closureType=Closure(closure),
                                                       belongOp=Belong(belongOp))
        assert result is True, "Test Case 3 Failed: Expected True, but got False"
        print_and_log("Test Case 3 Passed: Expected True, got True")

        # Example 4 of checkIntervalRangeFloat
        # Check that the data in the whole dictionary belongs to the interval (0, 70.4]
        dataDictionary = pd.DataFrame(data={'c1': [0.01, 2.9, 5, 25.3, 4, 67.5, 42, 0.5, None, None],
                                            'c2': [7, 15, 0.3, 1.4, 0.3, 5, 70.5, 8, None, None]})
        closure = 1  # OpenClosed
        result = self.pre_post.checkIntervalRangeFloat(left_margin=left, right_margin=right,
                                                       dataDictionary=dataDictionary, closureType=Closure(closure),
                                                       belongOp=Belong(belongOp))
        assert result is False, "Test Case 4 Failed: Expected False, but got True"
        print_and_log("Test Case 4 Passed: Expected False, got False")

        # Example 5 of checkIntervalRangeFloat
        # Check that the data in the whole dictionary belongs to the interval [0, 70.4)
        dataDictionary = pd.DataFrame(data={'c1': [0.0, 2.9, 5, 25.3, 4, 67.5, 42, 0.5, None, None],
                                            'c2': [7, 15, 0.3, 1.4, 0.3, 5, 70.3, 8, None, None]})
        closure = 2  # ClosedOpen
        result = self.pre_post.checkIntervalRangeFloat(left_margin=left, right_margin=right,
                                                       dataDictionary=dataDictionary, closureType=Closure(closure),
                                                       belongOp=Belong(belongOp))
        assert result is True, "Test Case 5 Failed: Expected True, but got False"
        print_and_log("Test Case 5 Passed: Expected True, got True")

        # Example 6 of checkIntervalRangeFloat
        # Check that the data in the whole dictionary belongs to the interval [0, 70.4)
        dataDictionary = pd.DataFrame(data={'c1': [0.0, 2.9, 5, 25.3, 4, 67.5, 42, 0.5, None, None],
                                            'c2': [7, 15, 0.3, 1.4, 0.3, 5, 70.4, 8, None, None]})
        closure = 2  # ClosedOpen
        result = self.pre_post.checkIntervalRangeFloat(left_margin=left, right_margin=right,
                                                       dataDictionary=dataDictionary, closureType=Closure(closure),
                                                       belongOp=Belong(belongOp))
        assert result is False, "Test Case 6 Failed: Expected False, but got True"
        print_and_log("Test Case 6 Passed: Expected False, got False")

        # Example 7 of checkIntervalRangeFloat
        # Check that the data in the whole dictionary belongs to the interval [0, 70.4]
        dataDictionary = pd.DataFrame(data={'c1': [0.0, 2.9, 5, 25.3, 4, 67.5, 42, 0.5, None, None],
                                            'c2': [7, 15, 0.3, 1.4, 0.3, 5, 70.4, 8, None, None]})
        closure = 3  # ClosedClosed
        result = self.pre_post.checkIntervalRangeFloat(left_margin=left, right_margin=right,
                                                       dataDictionary=dataDictionary, closureType=Closure(closure),
                                                       belongOp=Belong(belongOp))
        assert result is True, "Test Case 7 Failed: Expected True, but got False"
        print_and_log("Test Case 7 Passed: Expected True, got True")

        # Example 8 of checkIntervalRangeFloat
        # Check that the data in the whole dictionary belongs to the interval [0, 70.4]
        dataDictionary = pd.DataFrame(data={'c1': [0.0, 2.9, 5, 25.3, 0.001, 67.5, 42, 0.5, None, None],
                                            'c2': [7, 15, 0.3, 1.4, 0.3, 5, 70.4001, 8, None, None]})
        closure = 3  # ClosedClosed
        result = self.pre_post.checkIntervalRangeFloat(left_margin=left, right_margin=right,
                                                       dataDictionary=dataDictionary, closureType=Closure(closure),
                                                       belongOp=Belong(belongOp))
        assert result is False, "Test Case 8 Failed: Expected False, but got True"
        print_and_log("Test Case 8 Passed: Expected False, got False")

        # belongOp = 1
        belongOp = 1

        # Example 9 of checkIntervalRangeFloat
        # Check that the data in the whole dictionary belongs to the interval (0, 70.4)
        dataDictionary = pd.DataFrame(data={'c1': [0, 2.9, 5, 25.3, 4, 67.5, 0, 0.5, None, None],
                                            'c2': [0, 0, 0.3, 1.4, 0.3, 5, 0, 0, None, None]})
        closure = 0  # OpenOpen
        result = self.pre_post.checkIntervalRangeFloat(left_margin=left, right_margin=right,
                                                       dataDictionary=dataDictionary, closureType=Closure(closure),
                                                       belongOp=Belong(belongOp))
        assert result is True, "Test Case 9 Failed: Expected True, but got False"
        print_and_log("Test Case 9 Passed: Expected True, got True")

        # Example 10 of checkIntervalRangeFloat
        # Check that the data in the whole dictionary belongs to the interval (0, 70.4)
        dataDictionary = pd.DataFrame(data={'c1': [0.1, 2.9, 5, 25.3, 4, 67.5, 42, 0.5, None, None],
                                            'c2': [7, 15, 0.3, 1.4, 0.3, 5, 7.0, 8, None, None]})
        closure = 0  # OpenOpen
        result = self.pre_post.checkIntervalRangeFloat(left_margin=left, right_margin=right,
                                                       dataDictionary=dataDictionary, closureType=Closure(closure),
                                                       belongOp=Belong(belongOp))
        assert result is False, "Test Case 10 Failed: Expected False, but got True"
        print_and_log("Test Case 10 Passed: Expected False, got False")

        # Example 11 of checkIntervalRangeFloat
        # Check that the data in the whole dictionary belongs to the interval (0, 70.4]
        dataDictionary = pd.DataFrame(data={'c1': [0.01, 2.9, 5, 25.3, 4, 67.5, 42, 0.5, None, None],
                                            'c2': [7, 15, 0.3, 1.4, 0.3, 5, 70.4, 8, None, None]})
        closure = 1  # OpenClosed
        result = self.pre_post.checkIntervalRangeFloat(left_margin=left, right_margin=right,
                                                       dataDictionary=dataDictionary, closureType=Closure(closure),
                                                       belongOp=Belong(belongOp))
        assert result is False, "Test Case 11 Failed: Expected False, but got True"
        print_and_log("Test Case 11 Passed: Expected False, got False")

        # Example 12 of checkIntervalRangeFloat
        # Check that the data in the whole dictionary belongs to the interval (0, 70.4]
        dataDictionary = pd.DataFrame(data={'c1': [0.01, 2.9, 5, 25.3, 4, 67.5, 42, 0.5, None, None],
                                            'c2': [7, 15, 0.3, 1.4, 0.3, 5, 70.5, 8, None, None]})
        closure = 1  # OpenClosed
        result = self.pre_post.checkIntervalRangeFloat(left_margin=left, right_margin=right,
                                                       dataDictionary=dataDictionary, closureType=Closure(closure),
                                                       belongOp=Belong(belongOp))
        assert result is True, "Test Case 12 Failed: Expected True, but got False"
        print_and_log("Test Case 12 Passed: Expected True, got True")

        # Example 13 of checkIntervalRangeFloat
        # Check that the data in the whole dictionary belongs to the interval [0, 70.4)
        dataDictionary = pd.DataFrame(data={'c1': [0.0, 2.9, 5, 25.3, 4, 67.5, 42, 0.5, None, None],
                                            'c2': [7, 15, 0.3, 1.4, 0.3, 5, 70.3, 8, None, None]})
        closure = 2  # ClosedOpen
        result = self.pre_post.checkIntervalRangeFloat(left_margin=left, right_margin=right,
                                                       dataDictionary=dataDictionary, closureType=Closure(closure),
                                                       belongOp=Belong(belongOp))
        assert result is False, "Test Case 13 Failed: Expected False, but got True"
        print_and_log("Test Case 13 Passed: Expected False, got False")

        # Example 14 of checkIntervalRangeFloat
        # Check that the data in the whole dictionary belongs to the interval [0, 70.4)
        dataDictionary = pd.DataFrame(data={'c1': [0.0, 2.9, 5, 25.3, 4, 67.5, 42, 0.5, None, None],
                                            'c2': [7, 15, 0.3, 1.4, 0.3, 5, 70.4, 8, None, None]})
        closure = 2  # ClosedOpen
        result = self.pre_post.checkIntervalRangeFloat(left_margin=left, right_margin=right,
                                                       dataDictionary=dataDictionary, closureType=Closure(closure),
                                                       belongOp=Belong(belongOp))
        assert result is True, "Test Case 14 Failed: Expected True, but got False"
        print_and_log("Test Case 14 Passed: Expected True, got True")

        # Example 15 of checkIntervalRangeFloat
        # Check that the data in the whole dictionary belongs to the interval [0, 70.4]
        dataDictionary = pd.DataFrame(data={'c1': [0.0, 2.9, 5, 25.3, 4, 67.5, 42, 0.5, None, None],
                                            'c2': [7, 15, 0.3, 1.4, 0.3, 5, 70.4, 8, None, None]})
        closure = 3  # ClosedClosed
        result = self.pre_post.checkIntervalRangeFloat(left_margin=left, right_margin=right,
                                                       dataDictionary=dataDictionary, closureType=Closure(closure),
                                                       belongOp=Belong(belongOp))
        assert result is False, "Test Case 15 Failed: Expected False, but got True"
        print_and_log("Test Case 15 Passed: Expected False, got False")

        # Example 16 of checkIntervalRangeFloat
        # Check that the data in the whole dictionary belongs to the interval [0, 70.4]
        dataDictionary = pd.DataFrame(data={'c1': [0.0, 2.9, 5, 25.3, 0.001, 67.5, 42, 0.5, None, None],
                                            'c2': [7, 15, 0.3, 1.4, 0.3, 5, 70.4001, 8, None, None]})
        closure = 3  # ClosedClosed
        result = self.pre_post.checkIntervalRangeFloat(left_margin=left, right_margin=right,
                                                       dataDictionary=dataDictionary, closureType=Closure(closure),
                                                       belongOp=Belong(belongOp))
        assert result is True, "Test Case 16 Failed: Expected True, but got False"
        print_and_log("Test Case 16 Passed: Expected True, got True")

        # field = 'c2'
        field = 'c2'
        # belongOp = 0
        belongOp = 0

        # Example 17 of checkIntervalRangeFloat
        # Check that the data in the whole dictionary belongs to the interval (0, 70.4)
        dataDictionary = pd.DataFrame(data={'c1': [0, 2.9, 5, 25.3, 4, 67.5, 0, 0.5, None, None],
                                            'c2': [0, 0, 0.3, 1.4, 0.3, 5, 0, 0, None, None]})
        closure = 0  # OpenOpen
        result = self.pre_post.checkIntervalRangeFloat(left_margin=left, right_margin=right,
                                                       dataDictionary=dataDictionary, closureType=Closure(closure),
                                                       belongOp=Belong(belongOp), field=field)
        assert result is False, "Test Case 17 Failed: Expected False, but got True"
        print_and_log("Test Case 17 Passed: Expected False, got False")

        # Example 18 of checkIntervalRangeFloat
        # Check that the data in the whole dictionary belongs to the interval (0, 70.4)
        dataDictionary = pd.DataFrame(data={'c1': [0.1, 2.9, 5, 25.3, 4, 67.5, 42, 0.5, None, None],
                                            'c2': [7, 15, 0.3, 1.4, 0.3, 5, 7.0, 8, None, None]})
        closure = 0  # OpenOpen
        result = self.pre_post.checkIntervalRangeFloat(left_margin=left, right_margin=right,
                                                       dataDictionary=dataDictionary, closureType=Closure(closure),
                                                       belongOp=Belong(belongOp), field=field)
        assert result is True, "Test Case 18 Failed: Expected True, but got False"
        print_and_log("Test Case 18 Passed: Expected True, got True")

        # Example 19 of checkIntervalRangeFloat
        # Check that the data in the whole dictionary belongs to the interval (0, 70.4]
        dataDictionary = pd.DataFrame(data={'c1': [0.01, 2.9, 5, 25.3, 4, 67.5, 42, 0.5, None, None],
                                            'c2': [7, 15, 0.3, 1.4, 0.3, 5, 70.4, 8, None, None]})
        closure = 1  # OpenClosed
        result = self.pre_post.checkIntervalRangeFloat(left_margin=left, right_margin=right,
                                                       dataDictionary=dataDictionary, closureType=Closure(closure),
                                                       belongOp=Belong(belongOp), field=field)
        assert result is True, "Test Case 19 Failed: Expected True, but got False"
        print_and_log("Test Case 19 Passed: Expected True, got True")

        # Example 20 of checkIntervalRangeFloat
        # Check that the data in the whole dictionary belongs to the interval (0, 70.4]
        dataDictionary = pd.DataFrame(data={'c1': [0.01, 2.9, 5, 25.3, 4, 67.5, 42, 0.5, None, None],
                                            'c2': [7, 15, 0.3, 1.4, 0.3, 5, 70.5, 8, None, None]})
        closure = 1  # OpenClosed
        result = self.pre_post.checkIntervalRangeFloat(left_margin=left, right_margin=right,
                                                       dataDictionary=dataDictionary, closureType=Closure(closure),
                                                       belongOp=Belong(belongOp), field=field)
        assert result is False, "Test Case 20 Failed: Expected False, but got True"
        print_and_log("Test Case 20 Passed: Expected False, got False")

        # Example 21 of checkIntervalRangeFloat
        # Check that the data in the whole dictionary belongs to the interval [0, 70.4)
        dataDictionary = pd.DataFrame(data={'c1': [0.0, -2.9, 5, 25.3, 4, 67.5, 42, 0.5, None, None],
                                            'c2': [7, 15, 0.3, 1.4, 0.3, 5, 70.3, 8, None, None]})
        closure = 2  # ClosedOpen
        result = self.pre_post.checkIntervalRangeFloat(left_margin=left, right_margin=right,
                                                       dataDictionary=dataDictionary, closureType=Closure(closure),
                                                       belongOp=Belong(belongOp), field=field)
        assert result is True, "Test Case 21 Failed: Expected True, but got False"
        print_and_log("Test Case 21 Passed: Expected True, got True")

        # Example 22 of checkIntervalRangeFloat
        # Check that the data in the whole dictionary belongs to the interval [0, 70.4)
        dataDictionary = pd.DataFrame(data={'c1': [0.0, 2.9, 5, 25.3, 4, 67.5, 42, 0.5, None, None],
                                            'c2': [7, 15, 0.3, 1.4, 0.3, 5, 70.4, 8, None, None]})
        closure = 2  # ClosedOpen
        result = self.pre_post.checkIntervalRangeFloat(left_margin=left, right_margin=right,
                                                       dataDictionary=dataDictionary, closureType=Closure(closure),
                                                       belongOp=Belong(belongOp), field=field)
        assert result is False, "Test Case 22 Failed: Expected False, but got True"
        print_and_log("Test Case 22 Passed: Expected False, got False")

        # Example 23 of checkIntervalRangeFloat
        # Check that the data in the whole dictionary belongs to the interval [0, 70.4]
        dataDictionary = pd.DataFrame(data={'c1': [0.0, -2.9, 5, 25.3, 4, 67.5, 42, 0.5, None, None],
                                            'c2': [7, 15, 0.3, 1.4, 0.3, 5, 70.4, 8, None, None]})
        closure = 3  # ClosedClosed
        result = self.pre_post.checkIntervalRangeFloat(left_margin=left, right_margin=right,
                                                       dataDictionary=dataDictionary, closureType=Closure(closure),
                                                       belongOp=Belong(belongOp), field=field)
        assert result is True, "Test Case 23 Failed: Expected True, but got False"
        print_and_log("Test Case 23 Passed: Expected True, got True")

        # Example 24 of checkIntervalRangeFloat
        # Check that the data in the whole dictionary belongs to the interval [0, 70.4]
        dataDictionary = pd.DataFrame(data={'c1': [0.0, 2.9, 5, 25.3, 0.001, 67.5, 42, 0.5, None, None],
                                            'c2': [7, 15, 0.3, 1.4, 0.3, 5, 70.4001, 8, None, None]})
        closure = 3  # ClosedClosed
        result = self.pre_post.checkIntervalRangeFloat(left_margin=left, right_margin=right,
                                                       dataDictionary=dataDictionary, closureType=Closure(closure),
                                                       belongOp=Belong(belongOp), field=field)
        assert result is False, "Test Case 24 Failed: Expected False, but got True"
        print_and_log("Test Case 24 Passed: Expected False, got False")

        # belongOp = 1
        belongOp = 1

        # Example 25 of checkIntervalRangeFloat
        # Check that the data in the whole dictionary belongs to the interval (0, 70.4)
        dataDictionary = pd.DataFrame(data={'c1': [1, 2.9, 5, 25.3, 4, 67.5, 3, 0.5, None, None],
                                            'c2': [0, 0, 0.3, 1.4, 0.3, 5, 0, 0, None, None]})
        closure = 0  # OpenOpen
        result = self.pre_post.checkIntervalRangeFloat(left_margin=left, right_margin=right,
                                                       dataDictionary=dataDictionary, closureType=Closure(closure),
                                                       belongOp=Belong(belongOp), field=field)
        assert result is True, "Test Case 25 Failed: Expected True, but got False"
        print_and_log("Test Case 25 Passed: Expected True, got True")

        # Example 26 of checkIntervalRangeFloat
        # Check that the data in the whole dictionary belongs to the interval (0, 70.4)
        dataDictionary = pd.DataFrame(data={'c1': [0.1, -2.9, 5, 25.3, 4, 67.5, 42, 0.5, None, None],
                                            'c2': [7, 15, 0.3, 1.4, 0.3, 5, 7.0, 8, None, None]})
        closure = 0  # OpenOpen
        result = self.pre_post.checkIntervalRangeFloat(left_margin=left, right_margin=right,
                                                       dataDictionary=dataDictionary, closureType=Closure(closure),
                                                       belongOp=Belong(belongOp), field=field)
        assert result is False, "Test Case 26 Failed: Expected False, but got True"
        print_and_log("Test Case 26 Passed: Expected False, got False")

        # Example 27 of checkIntervalRangeFloat
        # Check that the data in the whole dictionary belongs to the interval (0, 70.4]
        dataDictionary = pd.DataFrame(data={'c1': [0.01, 2.9, 5, 25.3, 4, 67.5, 42, 0.5, None, None],
                                            'c2': [7, 15, 0.3, 1.4, 0.3, 5, 70.4, 8, None, None]})
        closure = 1  # OpenClosed
        result = self.pre_post.checkIntervalRangeFloat(left_margin=left, right_margin=right,
                                                       dataDictionary=dataDictionary, closureType=Closure(closure),
                                                       belongOp=Belong(belongOp), field=field)
        assert result is False, "Test Case 27 Failed: Expected False, but got True"
        print_and_log("Test Case 27 Passed: Expected False, got False")

        # Example 28 of checkIntervalRangeFloat
        # Check that the data in the whole dictionary belongs to the interval (0, 70.4]
        dataDictionary = pd.DataFrame(data={'c1': [0.01, 2.9, 5, 25.3, 4, 67.5, 42, 0.5, None, None],
                                            'c2': [7, 15, 0.3, 1.4, 0.3, 5, 70.5, 8, None, None]})
        closure = 1  # OpenClosed
        result = self.pre_post.checkIntervalRangeFloat(left_margin=left, right_margin=right,
                                                       dataDictionary=dataDictionary, closureType=Closure(closure),
                                                       belongOp=Belong(belongOp), field=field)
        assert result is True, "Test Case 28 Failed: Expected True, but got False"
        print_and_log("Test Case 28 Passed: Expected True, got True")

        # Example 29 of checkIntervalRangeFloat
        # Check that the data in the whole dictionary belongs to the interval [0, 70.4)
        dataDictionary = pd.DataFrame(data={'c1': [0.0, -2.9, 5, 25.3, 4, 67.5, 42, 0.5, None, None],
                                            'c2': [7, 15, 0.3, 1.4, 0.3, 5, 70.3, 8, None, None]})
        closure = 2  # ClosedOpen
        result = self.pre_post.checkIntervalRangeFloat(left_margin=left, right_margin=right,
                                                       dataDictionary=dataDictionary, closureType=Closure(closure),
                                                       belongOp=Belong(belongOp), field=field)
        assert result is False, "Test Case 29 Failed: Expected False, but got True"
        print_and_log("Test Case 29 Passed: Expected False, got False")

        # Example 30 of checkIntervalRangeFloat
        # Check that the data in the whole dictionary belongs to the interval [0, 70.4)
        dataDictionary = pd.DataFrame(data={'c1': [0.0, 2.9, 5, 25.3, 4, 67.5, 42, 0.5, None, None],
                                            'c2': [7, 15, 0.3, 1.4, 0.3, 5, 70.4, 8, None, None]})
        closure = 2  # ClosedOpen
        result = self.pre_post.checkIntervalRangeFloat(left_margin=left, right_margin=right,
                                                       dataDictionary=dataDictionary, closureType=Closure(closure),
                                                       belongOp=Belong(belongOp), field=field)
        assert result is True, "Test Case 30 Failed: Expected True, but got False"
        print_and_log("Test Case 30 Passed: Expected True, got True")

        # Example 31 of checkIntervalRangeFloat
        # Check that the data in the whole dictionary belongs to the interval [0, 70.4]
        dataDictionary = pd.DataFrame(data={'c1': [0.0, -2.9, 5, 25.3, 4, 67.5, 42, 0.5, None, None],
                                            'c2': [7, 15, 0.3, 1.4, 0.3, 5, 70.4, 8, None, None]})
        closure = 3  # ClosedClosed
        result = self.pre_post.checkIntervalRangeFloat(left_margin=left, right_margin=right,
                                                       dataDictionary=dataDictionary, closureType=Closure(closure),
                                                       belongOp=Belong(belongOp), field=field)
        assert result is False, "Test Case 31 Failed: Expected False, but got True"
        print_and_log("Test Case 31 Passed: Expected False, got False")

        # Example 32 of checkIntervalRangeFloat
        # Check that the data in the whole dictionary belongs to the interval [0, 70.4]
        dataDictionary = pd.DataFrame(data={'c1': [0.0, 2.9, 5, 25.3, 0.001, 67.5, 42, 0.5, None, None],
                                            'c2': [7, 15, 0.3, 1.4, 0.3, 5, 70.4001, 8, None, None]})
        closure = 3  # ClosedClosed
        result = self.pre_post.checkIntervalRangeFloat(left_margin=left, right_margin=right,
                                                       dataDictionary=dataDictionary, closureType=Closure(closure),
                                                       belongOp=Belong(belongOp), field=field)
        assert result is True, "Test Case 32 Failed: Expected True, but got False"
        print_and_log("Test Case 32 Passed: Expected True, got True")

        print_and_log("")
        print_and_log("-----------------------------------------------------------")
        print_and_log("")

    def execute_CheckMissingRange_SimpleTests(self):
        """
        Execute the simple tests of the function checkMissingRange
        """
        print_and_log("Testing checkMissingRange Function")
        print_and_log("")

        print_and_log("Casos Básicos solicitados en la especificación del contrato:")

        # 30 casos posibles

        # Caso 1 Solicitado (Caso 20)
        belong = 0
        dataDictionary = pd.DataFrame(data={'colour':[None, None, 'Blue', 'Green']})
        field = 'colour'
        quant_op = 2 # lessEqual
        quant_rel = 0.5
        result = self.pre_post.checkMissingRange(dataDictionary=dataDictionary, field=field,
                                                 belongOp=Belong(belong), quant_op=Operator(quant_op),
                                                 quant_rel=quant_rel)
        assert result is True, "Test Case 20 Failed: Expected True, but got False"
        print_and_log("Test Case 20 Passed: Expected True, got True")

        # Caso 2 Solicitado (Caso 20 también)
        belong = 0
        dataDictionary =  pd.DataFrame(data={'colour':[None, -1, 'Blue', 'Green']})
        field = 'colour'
        missing_values = [-1]
        quant_op = 2  # lessEqual
        quant_rel = 0.5
        result = self.pre_post.checkMissingRange(dataDictionary=dataDictionary, field=field,
                                                 belongOp=Belong(belong), quant_op=Operator(quant_op),
                                                 quant_rel=quant_rel, missing_values=missing_values)
        assert result is True, "Test Case 20 Failed: Expected True, but got False"
        print_and_log("Test Case 20 Passed: Expected True, got True")

        # Caso 3 Solicitado (Caso 23)
        belong = 0
        dataDictionary = pd.DataFrame(data={'colour':[None, -1, 'Blue', 'Green']})
        field = 'colour'
        missing_values = [-1]
        quant_op = 2 # lessEqual
        quant_abs = 2
        result = self.pre_post.checkMissingRange(dataDictionary=dataDictionary, field=field,
                                                 belongOp=Belong(belong), quant_op=Operator(quant_op),
                                                 quant_abs=quant_abs, missing_values=missing_values)
        assert result is True, "Test Case 23 Failed: Expected True, but got False"
        print_and_log("Test Case 23 Passed: Expected True, got True")

        print_and_log("")
        print_and_log("Casos Básicos añadidos:")

        #Casos añadidos

        #Caso 1
        field = None
        belong = 0
        dataDictionary=pd.DataFrame(data={'colour':[None, -1, 'Blue', 'Green']})
        missing_values = [-1]
        result=self.pre_post.checkMissingRange(dataDictionary=dataDictionary, field=field,missing_values=missing_values,
                                                 belongOp=Belong(belong))
        assert result is True, "Test Case 1 Failed: Expected True, but got False"
        print_and_log("Test Case 1 Passed: Expected True, got True")

        #Caso 2
        belong = 0
        dataDictionary = pd.DataFrame(data={'colour': ['Red', 5, 'Blue', 'Green', 'Nulo']})
        field = None
        missing_values= ['Nulo', -8]
        quant_op = 2  # lessEqual
        quant_rel = 0.5
        result = self.pre_post.checkMissingRange(dataDictionary=dataDictionary, field=field, missing_values=missing_values,
                                                 belongOp=Belong(belong), quant_op=Operator(quant_op),
                                                 quant_rel=quant_rel)
        assert result is True, "Test Case 2 Failed: Expected True, but got False"
        print_and_log("Test Case 2 Passed: Expected True, got True")

        #Caso 3
        belong = 0
        dataDictionary = pd.DataFrame(data={'colour': ['Red', 5, 'Blue', 'Green', 'Nulo']})
        field = None
        missing_values= ['Nul', -8]
        result = self.pre_post.checkMissingRange(dataDictionary=dataDictionary, field=field, missing_values=missing_values,
                                                 belongOp=Belong(belong))
        assert result is False, "Test Case 3 Failed: Expected False, but got True"
        print_and_log("Test Case 3 Passed: Expected False, got False")

        #Caso 4
        belong = 0
        dataDictionary = pd.DataFrame(data={'colour': ['Red', 5, 'Blue', 'Green', 'Nulo']})
        field = None
        missing_values= None
        result = self.pre_post.checkMissingRange(dataDictionary=dataDictionary, field=field, missing_values=missing_values,
                                                 belongOp=Belong(belong))
        assert result is False, "Test Case 4 Failed: Expected False, but got True"
        print_and_log("Test Case 4 Passed: Expected False, got False")

        #Caso 5
        belong = 0
        dataDictionary = pd.DataFrame(data={'colour':[None, None, 'Blue', 'Green']})
        field = None
        quant_op = 2 # lessEqual
        quant_rel = 0.5
        result = self.pre_post.checkMissingRange(dataDictionary=dataDictionary, field=field,
                                                 belongOp=Belong(belong), quant_op=Operator(quant_op),
                                                 quant_rel=quant_rel)
        assert result is True, "Test Case 5 Failed: Expected True, but got False"
        print_and_log("Test Case 5 Passed: Expected True, got True")

        #Caso 6
        belong = 0
        dataDictionary = pd.DataFrame(data={'colour':[4, 5, 'Blue', 'Green']})
        field = None
        quant_op = 2 # lessEqual
        quant_rel = 0.5
        result = self.pre_post.checkMissingRange(dataDictionary=dataDictionary, field=field,
                                                 belongOp=Belong(belong), quant_op=Operator(quant_op),
                                                 quant_rel=quant_rel)
        assert result is False, "Test Case 6 Failed: Expected False, but got True"
        print_and_log("Test Case 6 Passed: Expected False, got False")

        #Caso 8
        belong = 0
        dataDictionary = pd.DataFrame(data={'colour':[4, 5, 'Blue', 'Green', 'Green']})
        field = None
        quant_op = 0 # greaterEqual
        missing_values = ['Green']
        quant_abs = 2
        result = self.pre_post.checkMissingRange(dataDictionary=dataDictionary, field=field,
                                                 belongOp=Belong(belong), quant_op=Operator(quant_op),
                                                 quant_abs=quant_abs, missing_values=missing_values)
        assert result is True, "Test Case 8 Failed: Expected True, but got False"
        print_and_log("Test Case 8 Passed: Expected True, got True")

        #Caso 9
        belong = 0
        dataDictionary = pd.DataFrame(data={'colour':[4, 5, 'Blue', 'Green', 'Green']})
        field = None
        quant_op = 0 # greaterEqual
        missing_values = ['Blue']
        quant_abs = 2
        result = self.pre_post.checkMissingRange(dataDictionary=dataDictionary, field=field,
                                                 belongOp=Belong(belong), quant_op=Operator(quant_op),
                                                 quant_abs=quant_abs, missing_values=missing_values)
        assert result is False, "Test Case 9 Failed: Expected False, but got True"
        print_and_log("Test Case 9 Passed: Expected False, got False")

        #Caso 11
        belong = 1
        dataDictionary = pd.DataFrame(data={'colour':[4, 5, 'Blue', 'Green', 'Green']})
        field = None
        missing_values = ['Red']
        result = self.pre_post.checkMissingRange(dataDictionary=dataDictionary, field=field,
                                                 belongOp=Belong(belong), missing_values=missing_values)
        assert result is True, "Test Case 11 Failed: Expected True, but got False"
        print_and_log("Test Case 11 Passed: Expected True, got True")

        #Caso 12
        belong = 1
        dataDictionary = pd.DataFrame(data={'colour':[4, 5, 'Blue', 'Green', 'Green']})
        field = None
        missing_values = ['Blue']
        result = self.pre_post.checkMissingRange(dataDictionary=dataDictionary, field=field,
                                                 belongOp=Belong(belong), missing_values=missing_values)
        assert result is False, "Test Case 12 Failed: Expected False, but got True"
        print_and_log("Test Case 12 Passed: Expected False, got False")

        #Caso 13
        belong = 1
        dataDictionary = pd.DataFrame(data={'colour':[4, 5, 'Blue', 'Green', 'Green']})
        field = None
        result = self.pre_post.checkMissingRange(dataDictionary=dataDictionary, field=field,
                                                 belongOp=Belong(belong))
        assert result is True, "Test Case 13 Failed: Expected True, but got False"
        print_and_log("Test Case 13 Passed: Expected True, got True")

        # Caso 13.1
        belong = 1
        dataDictionary = pd.DataFrame(data={'colour': [4, 5, 'Blue', 'Green', 'Green', None]})
        field = None
        result = self.pre_post.checkMissingRange(dataDictionary=dataDictionary, field=field,
                                                 belongOp=Belong(belong))
        assert result is False, "Test Case 13.1 Failed: Expected False, but got True"
        print_and_log("Test Case 13.1 Passed: Expected False, got False")

        # Caso 16
        belong = 0
        dataDictionary = pd.DataFrame(data={'colour': [None, None, 'Blue', 'Green'],
                                            'names': ['John', 'Mary', None, np.NaN]})
        field = 'colour'
        quant_op = None
        result = self.pre_post.checkMissingRange(dataDictionary=dataDictionary, field=field,
                                                    belongOp=Belong(belong), quant_op=quant_op)
        assert result is True, "Test Case 16 Failed: Expected True, but got False"
        print_and_log("Test Case 16 Passed: Expected True, got True")

        # Caso 17
        belong = 0
        dataDictionary = pd.DataFrame(data={'colour': [-1, -1, 'Blue', 'Green'],
                                            'names': ['John', 'Mary', None, np.NaN]})
        field = 'colour'
        quant_op = None
        missing_values = [-1]
        result = self.pre_post.checkMissingRange(dataDictionary=dataDictionary, field=field,
                                                 belongOp=Belong(belong), quant_op=quant_op,
                                                 missing_values=missing_values)
        assert result is True, "Test Case 17 Failed: Expected True, but got False"
        print_and_log("Test Case 17 Passed: Expected True, got True")

        # Caso 18
        belong = 0
        dataDictionary = pd.DataFrame(data={'colour': [-1, -1, 'Blue', 'Green'],
                                            'names': ['John', 'Mary', None, np.NaN]})
        field = 'colour'
        quant_op = None
        missing_values = [-2]
        result = self.pre_post.checkMissingRange(dataDictionary=dataDictionary, field=field,
                                                 belongOp=Belong(belong), quant_op=quant_op,
                                                 missing_values=missing_values)
        assert result is False, "Test Case 18 Failed: Expected False, but got True"
        print_and_log("Test Case 18 Passed: Expected False, got False")

        # Caso 19
        belong = 0
        dataDictionary = pd.DataFrame(data={'colour': [-1, -1, 'Blue', 'Green'],
                                            'names': ['John', 'Mary', None, np.NaN]})
        field = 'colour'
        quant_op = None
        missing_values = None
        result = self.pre_post.checkMissingRange(dataDictionary=dataDictionary, field=field,
                                                 belongOp=Belong(belong), quant_op=quant_op,
                                                 missing_values=missing_values)
        assert result is False, "Test Case 19 Failed: Expected False, but got True"
        print_and_log("Test Case 19 Passed: Expected False, got False")

        # Caso 21
        belong = 0
        dataDictionary = pd.DataFrame(data={'colour': [-3, -2, 'Blue', 'Green'],
                                            'names': ['John', 'Mary', None, np.NaN]})
        field = 'colour'
        missing_values = [-1]
        quant_op = 2  # lessEqual
        quant_rel = 0.5
        result = self.pre_post.checkMissingRange(dataDictionary=dataDictionary, field=field,
                                                 belongOp=Belong(belong), quant_op=Operator(quant_op),
                                                 quant_rel=quant_rel, missing_values=missing_values)
        assert result is False, "Test Case 21 Failed: Expected False, but got True"
        print_and_log("Test Case 21 Passed: Expected False, got False")

        # Caso 24
        belong = 0
        dataDictionary = pd.DataFrame(data={'colour': [None, -1, 'Blue', 'Green', -1, -1],
                                            'names': ['John', 'Mary', None, np.NaN, -1, -1]})
        field = 'colour'
        missing_values = [-1]
        quant_op = 2  # lessEqual
        quant_abs = 2
        result = self.pre_post.checkMissingRange(dataDictionary=dataDictionary, field=field,
                                                 belongOp=Belong(belong), quant_op=Operator(quant_op),
                                                 quant_abs=quant_abs, missing_values=missing_values)
        assert result is False, "Test Case 24 Failed: Expected False, but got True"
        print_and_log("Test Case 24 Passed: Expected False, got False")

        # Caso 26
        belong = 1
        dataDictionary = pd.DataFrame(data={'colour': [-2, 'Blue', 'Green', -3, -4],
                                            'names': ['John', 'Mary', None, np.NaN, None]})
        field = 'colour'
        missing_values = [-1, np.NaN]
        result = self.pre_post.checkMissingRange(dataDictionary=dataDictionary, field=field,
                                                 belongOp=Belong(belong), missing_values=missing_values)
        assert result is True, "Test Case 26 Failed: Expected True, but got False"
        print_and_log("Test Case 26 Passed: Expected True, got True")

        # Caso 27
        belong = 1
        dataDictionary = pd.DataFrame(data={'colour': [np.NaN, 'Blue', 'Green', -3, -4],
                                            'names': ['John', 'Mary', None, np.NaN, None]})
        field = 'colour'
        missing_values = [np.NaN]
        result = self.pre_post.checkMissingRange(dataDictionary=dataDictionary, field=field,
                                                 belongOp=Belong(belong), missing_values=missing_values)
        assert result is False, "Test Case 27 Failed: Expected False, but got True"
        print_and_log("Test Case 27 Passed: Expected False, got False")

        # Caso 28
        belong = 1
        dataDictionary = pd.DataFrame(data={'colour': [-1, 'Blue', 'Green', -3, -4],
                                            'names': ['John', 'Mary', None, np.NaN, np.NaN]})
        field = 'colour'
        result = self.pre_post.checkMissingRange(dataDictionary=dataDictionary, field=field,
                                                 belongOp=Belong(belong))
        assert result is True, "Test Case 28 Failed: Expected True, but got False"
        print_and_log("Test Case 28 Passed: Expected True, got True")

        # Caso 29
        belong = 1
        dataDictionary = pd.DataFrame(data={'colour': [np.NaN, 'Blue', 'Green', -3, -4],
                                            'names': ['John', 'Mary', None, np.NaN, None]})
        field = 'colour'
        result = self.pre_post.checkMissingRange(dataDictionary=dataDictionary, field=field,
                                                 belongOp=Belong(belong))
        assert result is False, "Test Case 29 Failed: Expected False, but got True"
        print_and_log("Test Case 29 Passed: Expected False, got False")

        print_and_log("")
        print_and_log("Casos de error añadidos:")

        # Caso 7
        belong = 0
        dataDictionary = pd.DataFrame(data={'colour': [4, 5, 'Blue', 'Green']})
        field = None
        quant_op = 2  # lessEqual
        quant_rel = 0.5
        quant_abs = 2
        expected_exception = ValueError
        with self.assertRaises(expected_exception) as context:
            result = self.pre_post.checkMissingRange(dataDictionary=dataDictionary, field=field,
                                                     belongOp=Belong(belong), quant_op=Operator(quant_op),
                                                     quant_rel=quant_rel, quant_abs=quant_abs)
        print_and_log("Test Case 7 Passed: Expected ValueError, got ValueError")

        # Caso 10
        belong = 0
        dataDictionary = pd.DataFrame(data={'colour': [None, None, 'Blue', 'Green']})
        field = None
        quant_op = 2  # lessEqual
        expected_exception = ValueError
        with self.assertRaises(expected_exception) as context:
            result = self.pre_post.checkMissingRange(dataDictionary=dataDictionary, field=field,
                                                     belongOp=Belong(belong), quant_op=Operator(quant_op))
        print_and_log("Test Case 10 Passed: Expected ValueError, got ValueError")

        # Caso 14
        belong = 1
        quan_abs = 5
        dataDictionary = pd.DataFrame(data={'colour': [4, 5, 'Blue', 'Green', 'Green']})
        field = None
        expected_exception = ValueError
        with self.assertRaises(expected_exception) as context:
            result = self.pre_post.checkMissingRange(dataDictionary=dataDictionary, field=field, quant_abs=quan_abs,
                                                     belongOp=Belong(belong), quant_op=Operator(quant_op))
        print_and_log("Test Case 14 Passed: Expected ValueError, got ValueError")

        # Caso 15
        belong = 0
        dataDictionary = pd.DataFrame(data={'colour': [None, None, 'Blue', 'Green'],
                                            'names': ['John', 'Mary', None, np.NaN]})
        field = 'colours'  # Error due to the inexistent field
        quant_op = 2  # lessEqual
        quant_rel = 0.5
        expected_exception = ValueError
        with self.assertRaises(expected_exception) as context:
            result = self.pre_post.checkMissingRange(dataDictionary=dataDictionary, field=field,
                                                     belongOp=Belong(belong), quant_op=Operator(quant_op),
                                                     quant_rel=quant_rel)
        print_and_log("Test Case 15 Passed: Expected ValueError, got ValueError")

        # Caso 22
        belong = 0
        dataDictionary = pd.DataFrame(data={'colour': [-3, -2, 'Blue', 'Green'],
                                            'names': ['John', 'Mary', None, np.NaN]})
        field = 'colour'
        missing_values = [-1]
        quant_op = 2  # lessEqual
        quant_rel = 0.5
        quant_abs = 2
        expected_exception = ValueError  # Error due to quant_abs and quant_op are not None at the same time
        with self.assertRaises(expected_exception) as context:
            result = self.pre_post.checkMissingRange(dataDictionary=dataDictionary, field=field,
                                                     belongOp=Belong(belong), quant_op=Operator(quant_op),
                                                     quant_rel=quant_rel, quant_abs=quant_abs,
                                                     missing_values=missing_values)
        print_and_log("Test Case 22 Passed: Expected ValueError, got ValueError")

        # Caso 25
        belong = 0
        dataDictionary = pd.DataFrame(data={'colour': [None, -1, 'Blue', 'Green', -1, -1],
                                            'names': ['John', 'Mary', None, np.NaN, -1, None]})
        field = 'colour'
        missing_values = [-1]
        quant_op = 2  # lessEqual
        expected_exception = ValueError  # Error due to quant_op is not None and quant_abs/quant_rel are both None
        with self.assertRaises(expected_exception) as context:
            result = self.pre_post.checkMissingRange(dataDictionary=dataDictionary, field=field,
                                                     belongOp=Belong(belong), quant_op=Operator(quant_op),
                                                     missing_values=missing_values)
        print_and_log("Test Case 25 Passed: Expected ValueError, got ValueError")

        # Caso 30
        belong = 1
        dataDictionary = pd.DataFrame(data={'colour': [np.NaN, 'Blue', 'Green', -3, -4, -1],
                                            'names': ['John', 'Mary', 'Peter', 'Laura', None, np.NaN]})
        field = 'colour'
        missing_values = [-1]
        quant_abs = 2
        quant_op = 0  # greaterEqual
        expected_exception = ValueError  # Error due to quant_abs, quant_op or quant_rel are not None when belongOp is 1
        with self.assertRaises(expected_exception) as context:
            result = self.pre_post.checkMissingRange(dataDictionary=dataDictionary, field=field,
                                                     belongOp=Belong(belong), missing_values=missing_values,
                                                     quant_abs=quant_abs, quant_op=Operator(quant_op))
        print_and_log("Test Case 30 Passed: Expected ValueError, got ValueError")


        print_and_log("")
        print_and_log("-----------------------------------------------------------")
        print_and_log("")


    def execute_CheckInvalidValues_SimpleTests(self):
        """
        Execute the simple tests of the function checkInvalidValues
        """
        print_and_log("Testing checkInvalidValues Function")
        print_and_log("")

        print_and_log("Casos Básicos solicitados en la especificación del contrato:")

        # 30 casos posibles

        # Caso 19 Solicitado
        belong = 0 # BELONG
        dataDictionary = pd.DataFrame(data={'colour':[-1, -1, 'Blue', 'Green']})
        invalid_values = [-1]
        field = 'colour'
        quant_op = 2 # lessEqual
        quant_rel = 0.5
        result = self.pre_post.checkInvalidValues(dataDictionary=dataDictionary, field=field,
                                                  belongOp=Belong(belong), quant_op=Operator(quant_op),
                                                  quant_rel=quant_rel, invalid_values=invalid_values)
        assert result is True, "Test Case 19 Failed: Expected True, but got False"
        print_and_log("Test Case 19 Passed: Expected True, got True")

        # Caso 19.1 Solicitado
        belong = 0 # BELONG
        dataDictionary = pd.DataFrame(data={'colour':[-1, 0, 'Blue', 'Green']})
        invalid_values = [-1, 0]
        field = 'colour'
        quant_op = 2 # lessEqual
        quant_rel = 0.5
        result = self.pre_post.checkInvalidValues(dataDictionary=dataDictionary, field=field,
                                                  belongOp=Belong(belong), quant_op=Operator(quant_op),
                                                  quant_rel=quant_rel, invalid_values=invalid_values)
        assert result is True, "Test Case 19.1 Failed: Expected True, but got False"
        print_and_log("Test Case 19.1 Passed: Expected True, got True")

        # Caso 22 Solicitado
        belong = 0 # BELONG
        dataDictionary = pd.DataFrame(data={'colour':[-1, 0, 'Blue', 'Green']})
        invalid_values = [-1, 0]
        field = 'colour'
        quant_op = 2 # lessEqual
        quant_abs = 2
        result = self.pre_post.checkInvalidValues(dataDictionary=dataDictionary, field=field,
                                                  belongOp=Belong(belong), quant_op=Operator(quant_op),
                                                  quant_abs=quant_abs, invalid_values=invalid_values)
        assert result is True, "Test Case 22 Failed: Expected True, but got False"
        print_and_log("Test Case 22 Passed: Expected True, got True")


        print_and_log("")
        print_and_log("Casos Básicos añadidos:")


        # Caso 1
        belong = 0
        dataDictionary = pd.DataFrame(data={'colour': [-1, 0, 'Blue', 'Green']})
        invalid_values = [-1, 0]
        field = None
        result = self.pre_post.checkInvalidValues(dataDictionary=dataDictionary, field=field,
                                                    belongOp=Belong(belong), invalid_values=invalid_values)
        assert result is True, "Test Case 1 Failed: Expected True, but got False"
        print_and_log("Test Case 1 Passed: Expected True, got True")

        # Caso 2
        belong = 0
        dataDictionary = pd.DataFrame(data={'colour': [2, 3, 'Blue', 'Green']})
        invalid_values = [-1, 0]
        field = None
        result = self.pre_post.checkInvalidValues(dataDictionary=dataDictionary, field=field,
                                                    belongOp=Belong(belong), invalid_values=invalid_values)
        assert result is False, "Test Case 2 Failed: Expected False, but got True"
        print_and_log("Test Case 2 Passed: Expected False, got False")

        # Caso 3
        belong = 0
        dataDictionary = pd.DataFrame(data={'colour': [-1, 0, 'Blue', 'Green']})
        field = None
        invalid_values = None
        result = self.pre_post.checkInvalidValues(dataDictionary=dataDictionary, field=field,
                                                    belongOp=Belong(belong), invalid_values=invalid_values)
        assert result is False, "Test Case 3 Failed: Expected False, but got True"
        print_and_log("Test Case 3 Passed: Expected False, got False")

        # Caso 4
        belong = 0
        dataDictionary = pd.DataFrame(data={'colour': [-1, 0, 'Blue', 'Green']})
        field = None
        invalid_values = [-1, 0]
        quant_op = 2 # lessEqual
        quant_rel = 0.5
        result = self.pre_post.checkInvalidValues(dataDictionary=dataDictionary, field=field,
                                                  invalid_values=invalid_values, quant_op=Operator(quant_op),
                                                    quant_rel=quant_rel, belongOp=Belong(belong))
        assert result is True, "Test Case 4 Failed: Expected True, but got False"
        print_and_log("Test Case 4 Passed: Expected True, got True")

        # Caso 5
        belong = 0
        dataDictionary = pd.DataFrame(data={'colour': [-1, 0, 'Blue', 'Green']})
        field = None
        invalid_values = [-1, 0]
        quant_op = 1 # Greater
        quant_rel = 0.5
        result = self.pre_post.checkInvalidValues(dataDictionary=dataDictionary, field=field,
                                                  invalid_values=invalid_values, quant_op=Operator(quant_op),
                                                    quant_rel=quant_rel, belongOp=Belong(belong))
        assert result is False, "Test Case 5 Failed: Expected False, but got True"
        print_and_log("Test Case 5 Passed: Expected False, got False")

        # Caso 6
        belong = 0
        dataDictionary = pd.DataFrame(data={'colour': [-1, 0, 'Blue', 'Green']})
        field = None
        invalid_values = None
        quant_op = 2
        quant_rel = 0.5
        result = self.pre_post.checkInvalidValues(dataDictionary=dataDictionary, field=field,
                                                  invalid_values=invalid_values, quant_op=Operator(quant_op),
                                                    quant_rel=quant_rel, belongOp=Belong(belong))
        assert result is False, "Test Case 6 Failed: Expected False, but got True"
        print_and_log("Test Case 6 Passed: Expected False, got False")

        # Caso 7
        belong = 0
        dataDictionary = pd.DataFrame(data={'colour': [-1, 0, 'Blue', 'Green']})
        field = None
        invalid_values = [-1, 0]
        quant_op = 4 # Equal
        quant_abs = 2
        result = self.pre_post.checkInvalidValues(dataDictionary=dataDictionary, field=field,
                                                  invalid_values=invalid_values, quant_op=Operator(quant_op),
                                                    quant_abs=quant_abs, belongOp=Belong(belong))
        assert result is True, "Test Case 7 Failed: Expected True, but got False"
        print_and_log("Test Case 7 Passed: Expected True, got True")

        # Caso 8
        belong = 0
        dataDictionary = pd.DataFrame(data={'colour': [-1, 0, 'Blue', 'Green']})
        field = None
        invalid_values = [-1, 0]
        quant_op = 4 # Equal
        quant_abs = 1
        result = self.pre_post.checkInvalidValues(dataDictionary=dataDictionary, field=field,
                                                  invalid_values=invalid_values, quant_op=Operator(quant_op),
                                                    quant_abs=quant_abs, belongOp=Belong(belong))
        assert result is False, "Test Case 8 Failed: Expected False, but got True"
        print_and_log("Test Case 8 Passed: Expected False, got False")

        # Caso 9
        belong = 0
        dataDictionary = pd.DataFrame(data={'colour': [-1, 0, 'Blue', 'Green']})
        field = None
        invalid_values = None
        quant_op = 4 # Equal
        quant_abs = 2
        result = self.pre_post.checkInvalidValues(dataDictionary=dataDictionary, field=field,
                                                  invalid_values=invalid_values, quant_op=Operator(quant_op),
                                                    quant_abs=quant_abs, belongOp=Belong(belong))
        assert result is False, "Test Case 9 Failed: Expected False, but got True"
        print_and_log("Test Case 9 Passed: Expected False, got False")

        # Caso 12
        belong = 1
        dataDictionary = pd.DataFrame(data={'colour': [3, 2, 'Blue', 'Green', 'Green']})
        field = None
        invalid_values = [-1, 0]
        result = self.pre_post.checkInvalidValues(dataDictionary=dataDictionary, field=field,
                                                  invalid_values=invalid_values, belongOp=Belong(belong))
        assert result is True, "Test Case 12 Failed: Expected True, but got False"
        print_and_log("Test Case 12 Passed: Expected True, got True")

        # Caso 13
        belong = 1
        dataDictionary = pd.DataFrame(data={'colour': [-1, 2, 'Blue', 'Green', 'Green']})
        field = None
        invalid_values = [-1, 0]
        result = self.pre_post.checkInvalidValues(dataDictionary=dataDictionary, field=field,
                                                  invalid_values=invalid_values, belongOp=Belong(belong))
        assert result is False, "Test Case 13 Failed: Expected False, but got True"
        print_and_log("Test Case 13 Passed: Expected False, got False")



        # Caso 16
        belong = 0
        dataDictionary = pd.DataFrame(data={'colour': [-1, 0, 'Blue', 'Green', 'Green'],
                                            'names': ['John', 'Mary', None, np.NaN, None]})
        quant_op = None
        field = 'colour'
        invalid_values = [-1, 0]
        result = self.pre_post.checkInvalidValues(dataDictionary=dataDictionary, field=field,
                                                  invalid_values=invalid_values, quant_op=quant_op,
                                                  belongOp=Belong(belong))
        assert result is True, "Test Case 16 Failed: Expected True, but got False"
        print_and_log("Test Case 16 Passed: Expected True, got True")

        # Caso 17
        belong = 0
        dataDictionary = pd.DataFrame(data={'colour': [2, 3, 'Blue', 'Green', 'Green'],
                                            'names': ['John', 'Mary', None, np.NaN, None]})
        invalid_values = [-1, 0]
        field = 'colour'
        quant_op = None
        result = self.pre_post.checkInvalidValues(dataDictionary=dataDictionary, field=field,
                                                  invalid_values=invalid_values, quant_op=quant_op,
                                                  belongOp=Belong(belong))
        assert result is False, "Test Case 17 Failed: Expected False, but got True"
        print_and_log("Test Case 17 Passed: Expected False, got False")

        # Caso 18
        belong = 0
        dataDictionary = pd.DataFrame(data={'colour': [-1, 0, 'Blue', 'Green', 'Green'],
                                            'names': ['John', 'Mary', None, np.NaN, None]})
        field = 'colour'
        invalid_values = None
        quant_op = None
        result = self.pre_post.checkInvalidValues(dataDictionary=dataDictionary, field=field,
                                                  invalid_values=invalid_values, quant_op=quant_op,
                                                  belongOp=Belong(belong))
        assert result is False, "Test Case 18 Failed: Expected False, but got True"
        print_and_log("Test Case 18 Passed: Expected False, got False")

        # Caso 20
        belong = 0
        dataDictionary = pd.DataFrame(data={'colour': [-1, 0, 'Blue', 'Green', 'Green'],
                                            'names': ['John', 'Mary', None, np.NaN, None]})
        invalid_values = [-1, 0]
        field = 'colour'
        quant_op = 1 # Greater
        quant_rel = 0.5
        result = self.pre_post.checkInvalidValues(dataDictionary=dataDictionary, field=field,
                                                    invalid_values=invalid_values, quant_op=Operator(quant_op),
                                                    quant_rel=quant_rel, belongOp=Belong(belong))
        assert result is False, "Test Case 20 Failed: Expected False, but got True"
        print_and_log("Test Case 20 Passed: Expected False, got False")

        # Caso 21
        belong = 0
        dataDictionary = pd.DataFrame(data={'colour': [-1, 0, 'Blue', 'Green', 'Green'],
                                            'names': ['John', 'Mary', None, np.NaN, None]})
        invalid_values = None
        field = 'colour'
        quant_op = 1 # Greater
        quant_rel = 0.5
        result = self.pre_post.checkInvalidValues(dataDictionary=dataDictionary, field=field,
                                                    invalid_values=invalid_values, quant_op=Operator(quant_op),
                                                    quant_rel=quant_rel, belongOp=Belong(belong))
        assert result is False, "Test Case 21 Failed: Expected False, but got True"
        print_and_log("Test Case 21 Passed: Expected False, got False")

        # Caso 23
        belong = 0
        dataDictionary = pd.DataFrame(data={'colour': [-1, 0, 'Blue', 'Green', 'Green'],
                                            'names': ['John', 'Mary', None, np.NaN, None]})
        invalid_values = [-1, 0]
        field = 'colour'
        quant_op = 0 # GreaterEqual
        quant_abs = 3
        result = self.pre_post.checkInvalidValues(dataDictionary=dataDictionary, field=field,
                                                    invalid_values=invalid_values, quant_op=Operator(quant_op),
                                                    quant_abs=quant_abs, belongOp=Belong(belong))
        assert result is False, "Test Case 23 Failed: Expected False, but got True"
        print_and_log("Test Case 23 Passed: Expected False, got False")

        # Caso 24
        belong = 0
        dataDictionary = pd.DataFrame(data={'colour': [-1, 0, 'Blue', 'Green', 'Green'],
                                            'names': ['John', 'Mary', None, np.NaN, None]})
        invalid_values = None
        field = 'colour'
        quant_op = 0 # GreaterEqual
        quant_abs = 3
        result = self.pre_post.checkInvalidValues(dataDictionary=dataDictionary, field=field,
                                                    invalid_values=invalid_values, quant_op=Operator(quant_op),
                                                    quant_abs=quant_abs, belongOp=Belong(belong))
        assert result is False, "Test Case 24 Failed: Expected False, but got True"
        print_and_log("Test Case 24 Passed: Expected False, got False")

        # Caso 27
        belong = 1
        dataDictionary = pd.DataFrame(data={'colour': [3, 2, 'Blue', 'Green', 'Green', None],
                                            'names': ['John', 'Mary', None, np.NaN, None, None]})
        invalid_values = [-1, 0]
        field = 'colour'
        result = self.pre_post.checkInvalidValues(dataDictionary=dataDictionary, field=field,
                                                  invalid_values=invalid_values, belongOp=Belong(belong))
        assert result is True, "Test Case 27 Failed: Expected True, but got False"
        print_and_log("Test Case 27 Passed: Expected True, got True")

        # Caso 28
        belong = 1
        dataDictionary = pd.DataFrame(data={'colour': [-1, 0, 'Blue', 'Green', 'Green', None],
                                            'names': ['John', 'Mary', None, np.NaN, None, None]})
        invalid_values = [-1, 0]
        field = 'colour'
        result = self.pre_post.checkInvalidValues(dataDictionary=dataDictionary, field=field,
                                                  invalid_values=invalid_values, belongOp=Belong(belong))
        assert result is False, "Test Case 28 Failed: Expected False, but got True"
        print_and_log("Test Case 28 Passed: Expected False, got False")

        # Caso 29
        belong = 1
        dataDictionary = pd.DataFrame(data={'colour': [-1, 0, 'Blue', 'Green', 'Green', None],
                                            'names': ['John', 'Mary', None, np.NaN, None, None]})
        invalid_values = None
        field = 'colour'
        result = self.pre_post.checkInvalidValues(dataDictionary=dataDictionary, field=field,
                                                  invalid_values=invalid_values, belongOp=Belong(belong))
        assert result is True, "Test Case 29 Failed: Expected True, but got False"
        print_and_log("Test Case 29 Passed: Expected True, got True")

        print_and_log("")
        print_and_log("Casos de error añadidos:")

        # Caso 10
        belong = 0
        dataDictionary = pd.DataFrame(data={'colour': [-1, 0, 'Blue', 'Green', 'Green']})
        field = None
        invalid_values = [-1, 0]
        quant_op = 0  # GreaterEqual
        quant_abs = 2
        quant_rel = 0.5
        expected_exception = ValueError
        with self.assertRaises(expected_exception) as context:
            result = self.pre_post.checkInvalidValues(dataDictionary=dataDictionary, field=field,
                                                      invalid_values=invalid_values, quant_op=Operator(quant_op),
                                                      quant_abs=quant_abs, quant_rel=quant_rel,
                                                      belongOp=Belong(belong))
        print_and_log("Test Case 10 Passed: Expected ValueError, got ValueError")

        # Caso 11
        belong = 0
        dataDictionary = pd.DataFrame(data={'colour': [-1, 0, 'Blue', 'Green', 'Green']})
        field = None
        invalid_values = [-1, 0]
        quant_op = 0
        expected_exception = ValueError
        with self.assertRaises(expected_exception) as context:
            result = self.pre_post.checkInvalidValues(dataDictionary=dataDictionary, field=field,
                                                      invalid_values=invalid_values, quant_op=Operator(quant_op),
                                                      belongOp=Belong(belong))
        print_and_log("Test Case 11 Passed: Expected ValueError, got ValueError")

        # Caso 14
        belong = 1
        dataDictionary = pd.DataFrame(data={'colour': [-1, 0, 'Blue', 'Green', 'Green']})
        field = None
        invalid_values = [-1, 0]
        quant_op = 2
        quant_rel = 0.5
        expected_exception = ValueError
        with self.assertRaises(expected_exception) as context:
            result = self.pre_post.checkInvalidValues(dataDictionary=dataDictionary, field=field,
                                                      invalid_values=invalid_values, quant_op=Operator(quant_op),
                                                      quant_rel=quant_rel, belongOp=Belong(belong))
        print_and_log("Test Case 14 Passed: Expected ValueError, got ValueError")

        # Caso 15
        belong = 0
        dataDictionary = pd.DataFrame(data={'colour': [-1, 0, 'Blue', 'Green', 'Green'],
                                            'names': ['John', 'Mary', None, np.NaN, None]})
        field = 'colours'
        invalid_values = [-1, 0]
        quant_op = 2
        quant_rel = 0.5
        expected_exception = ValueError
        with self.assertRaises(expected_exception) as context:
            result = self.pre_post.checkInvalidValues(dataDictionary=dataDictionary, field=field,
                                                      invalid_values=invalid_values, quant_op=Operator(quant_op),
                                                      quant_rel=quant_rel, belongOp=Belong(belong))
        print_and_log("Test Case 15 Passed: Expected ValueError, got ValueError")

        # Caso 25
        belong = 0
        dataDictionary = pd.DataFrame(data={'colour': [-1, 0, 'Blue', 'Green', 'Green', None],
                                            'names': ['John', 'Mary', None, np.NaN, None, None]})
        invalid_values = [-1, 0]
        field = 'colour'
        quant_op = 0  # GreaterEqual
        quant_abs = 3
        quant_rel = 0.5
        expected_exception = ValueError
        with self.assertRaises(expected_exception) as context:
            result = self.pre_post.checkInvalidValues(dataDictionary=dataDictionary, field=field,
                                                      invalid_values=invalid_values, quant_op=Operator(quant_op),
                                                      quant_abs=quant_abs, quant_rel=quant_rel,
                                                      belongOp=Belong(belong))
        print_and_log("Test Case 25 Passed: Expected ValueError, got ValueError")

        # Caso 26
        belong = 0
        dataDictionary = pd.DataFrame(data={'colour': [-1, 0, 'Blue', 'Green', 'Green', None],
                                            'names': ['John', 'Mary', None, np.NaN, None, None]})
        invalid_values = [-1, 0]
        field = 'colour'
        quant_op = 0
        expected_exception = ValueError
        with self.assertRaises(expected_exception) as context:
            result = self.pre_post.checkInvalidValues(dataDictionary=dataDictionary, field=field,
                                                      invalid_values=invalid_values, quant_op=Operator(quant_op),
                                                      belongOp=Belong(belong))
        print_and_log("Test Case 26 Passed: Expected ValueError, got ValueError")

        # Caso 30
        belong = 1
        dataDictionary = pd.DataFrame(data={'colour': [-1, 0, 'Blue', 'Green', 'Green', None],
                                            'names': ['John', 'Mary', None, np.NaN, None, None]})
        invalid_values = [-1, 0]
        field = 'colour'
        quant_op = 1
        quant_rel = 0.5
        expected_exception = ValueError
        with self.assertRaises(expected_exception) as context:
            result = self.pre_post.checkInvalidValues(dataDictionary=dataDictionary, field=field,
                                                      invalid_values=invalid_values, quant_op=Operator(quant_op),
                                                      quant_rel=quant_rel, belongOp=Belong(belong))
        print_and_log("Test Case 30 Passed: Expected ValueError, got ValueError")


        print_and_log("")
        print_and_log("-----------------------------------------------------------")
        print_and_log("")

    def execute_CheckOutliers_SimpleTests(self):
        """
        Execute the simple tests of the function checkOutliers
        """
        print_and_log("Testing checkOutliers Function")
        print_and_log("")

        print_and_log("Casos Básicos añadidos:")

        # Caso 1
        dataframe = pd.DataFrame(data={'colour': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                                            'names': ['John', 'Mary', None, np.NaN, None, None, None, None, None, None]})
        result = self.pre_post.checkOutliers(dataDictionary=dataframe, axis_param=0)
        assert result is False, "Test Case 1 Failed: Expected False, but got True"
        print_and_log("Test Case 1 Passed: Expected False, got False")
