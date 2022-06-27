import numpy as np
from copy import deepcopy


def datatype_check(expected_output, target_output, error):
    success = 0
    if isinstance(target_output, dict):
        for key in target_output.keys():
            try:
                success += datatype_check(expected_output[key],
                                          target_output[key], error)
            except:
                print("Error: {} in variable {}. Got {} but expected type {}".format(error,
                                                                                     key,
                                                                                     type(
                                                                                         target_output[key]),
                                                                                     type(expected_output[key])))
        return 1 if success == len(target_output.keys()) else 0
    elif isinstance(target_output, (tuple, list)):
        for i in range(len(target_output)):
            try:
                success += datatype_check(expected_output[i],
                                          target_output[i], error)
            except:
                print("Error: {} in variable {}, expected type: {}  but expected type {}".format(error,
                                                                                                 i,
                                                                                                 type(
                                                                                                     target_output[i]),
                                                                                                 type(expected_output[i]
                                                                                                      )))
        return 1 if success == len(target_output) else 0
    else:
        assert isinstance(target_output, type(expected_output))
        return 1


def equation_output_check(expected_output, target_output, error):
    success = 0
    if isinstance(target_output, dict):
        for key in target_output.keys():
            try:
                success += equation_output_check(expected_output[key],
                                                 target_output[key], error)
            except:
                print(f"Error: {error} for variable {key}.")
        return 1 if success == len(target_output.keys()) else 0
    elif isinstance(target_output, (tuple, list)):
        for i in range(len(target_output)):
            try:
                success += equation_output_check(expected_output[i],
                                                 target_output[i], error)
            except:
                print(f"Error: {error} for variable in position {i}.")
        return 1 if success == len(target_output) else 0
    else:
        if hasattr(target_output, 'shape'):
            np.testing.assert_array_almost_equal(
                target_output, expected_output)
        else:
            assert target_output == expected_output
        return 1


def shape_check(expected_output, target_output, error):
    success = 0
    if isinstance(target_output, dict):
        for key in target_output.keys():
            try:
                success += shape_check(expected_output[key],
                                       target_output[key], error)
            except:
                print(f"Error: {error} for variable {key}.")
        return 1 if success == len(target_output.keys()) else 0
    elif isinstance(target_output, (tuple, list)):
        for i in range(len(target_output)):
            try:
                success += shape_check(expected_output[i],
                                       target_output[i], error)
            except:
                print(f"Error: {error} for variable {i}.")
        return 1 if success == len(target_output) else 0
    else:
        if hasattr(target_output, 'shape'):
            assert target_output.shape == expected_output.shape
        return 1


def single_test(test_cases, target):
    success = 0
    for test_case in test_cases:
        try:
            if test_case['name'] == "datatype_check":
                assert isinstance(target(*test_case['input']),
                                  type(test_case["expected"]))
                success += 1
            if test_case['name'] == "equation_output_check":
                assert np.allclose(test_case["expected"],
                                   target(*test_case['input']))
                success += 1
            if test_case['name'] == "shape_check":
                assert test_case['expected'].shape == target(
                    *test_case['input']).shape
                success += 1
        except:
            print("Error: " + test_case['error'])

    if success == len(test_cases):
        print("\033[92m All tests passed.")
    else:
        print('\033[92m', success, " Tests passed")
        print('\033[91m', len(test_cases) - success, " Tests failed")
        raise AssertionError(
            f"Not all tests were passed for {target.__name__}. Check your equations and avoid using global variables inside the function."
        )


def multiple_test(test_cases, target):
    success = 0
    for test_case in test_cases:
        try:
            test_input = deepcopy(test_case['input'])
            target_answer = target(*test_input)
            if test_case['name'] == "datatype_check":
                success += datatype_check(test_case['expected'],
                                          target_answer, test_case['error'])
            if test_case['name'] == "equation_output_check":
                success += equation_output_check(
                    test_case['expected'], target_answer, test_case['error'])
            if test_case['name'] == "shape_check":
                success += shape_check(test_case['expected'],
                                       target_answer, test_case['error'])
        except:
            print('\33[30m', "Error: " + test_case['error'])

    if success == len(test_cases):
        print("\033[92m All tests passed.")
    else:
        print('\033[92m', success, " Tests passed")
        print('\033[91m', len(test_cases) - success, " Tests failed")
        raise AssertionError(
            f"Not all tests were passed for {target.__name__}. Check your equations and avoid using global variables inside the function."
        )

