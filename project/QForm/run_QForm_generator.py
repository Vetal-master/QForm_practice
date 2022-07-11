from project.Excel.QForm import QForm_IO as load_data

params = load_data.load_qform_params()

dataset = {
    "tool_1_PZ": [10, 1],
    "tool_2_PY": [5, 2],
    "tool_3_PX": [1, 3],
    "mean_stress_equal": [-100, 100]
}

load_data.get_results_qform(dataset)
