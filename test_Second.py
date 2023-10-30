import json
import os
import pytest
import Second

# Define the path to the test JSON file - This allows us to isolate the test data from your actual filesystem
TEST_JSON_PATH = 'tmp/deps.json'

@pytest.fixture
def sample_data(tmpdir):
    # Create a temporary directory to store the test JSON file
    tmp_dir = tmpdir.mkdir('test_data')

    # Define sample JSON data for testing
    with open(TEST_JSON_PATH, 'r') as file:
        sample_data = json.load(file)

    # Create the test JSON file in the temporary directory
    test_json_path = os.path.join(tmp_dir, 'deps.json')
    with open(test_json_path, 'w') as json_file:
        json.dump(sample_data, json_file)

    return test_json_path

def test_print_nested_json(sample_data, capsys):
    # Call the function from your module to print the nested structure
    with open(sample_data, 'r') as file:
        data = json.load(file)

    for package in data:
        Second.print_nested_json(data, package)

    # Capture the printed output
    captured = capsys.readouterr()

    # Define the expected output
    expected_output = "- pkg1\n  - pkg2\n    - pkg3\n  - pkg3\n- pkg2\n  - pkg3\n- pkg3\n"

    # Assert that the captured output matches the expected output
    assert captured.out == expected_output

if __name__ == "__main__":
    pytest.main([__file__])
