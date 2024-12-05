import os
import pytest
import json
import asyncio
import presentation_code
import file
path_presentation = r"C:\Users\noa-m\Desktop\נעה\לימודים\סמסטר ב\exln\python-final-project-2-final_project_ex4\final-project-2-NoaAizen\presentation _test.pptx"


@pytest.mark.asyncio
async def test_read_presentation_and_save_to_json():
    """
    Test case for reading a presentation and saving summaries to JSON.
    """
    print(f"Checking if file exists: {path_presentation}")
    assert os.path.exists(path_presentation), f"File not found: {path_presentation}"
    summaries = await presentation_code.read_presentation(path_presentation, timeout=30)
    print(f"Summaries generated: {bool(summaries)}")
    assert summaries, "No summaries generated"
    file_name, _ = os.path.splitext(os.path.basename(path_presentation))
    output_filename = f"{file_name}.json"

    print(f"Saving to JSON: {output_filename}")
    file.save_to_json(output_filename, summaries)

    print(f"Checking if output file exists: {output_filename}")
    assert os.path.exists(output_filename), f"Output file not found: {output_filename}"

    print("Reading saved data...")
    with open(output_filename, 'r', encoding='utf-8') as f:
        saved_data = json.load(f)
    print("Comparing saved data with original summaries...")
    assert saved_data == summaries, "Saved data does not match original summaries"



if __name__ == "__main__":
    pytest.main()