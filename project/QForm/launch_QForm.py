from project.Excel.QForm import QForm_IO as load_data

params = load_data.load_qform_params()


row_1 = {
    "tool_1_PZ": 1,
    "tool_2_PY": 2,
    "tool_3_PX": 3,
    "mean_stress_equal": 100
}

row_2 = {
    "tool_1_PZ": 10,
    "tool_2_PY": 5,
    "tool_3_PX": 1,
    "mean_stress_equal": -100
}

dataset = []

dataset.append(row_1)
dataset.append(row_2)

load_data.get_results_qform(dataset)
