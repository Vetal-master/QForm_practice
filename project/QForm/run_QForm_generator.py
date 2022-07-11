from project.Excel.QForm import QForm_IO as load_data
from project.QForm.project import experiment_generator as gen_exp

params = load_data.load_qform_params()

for p in params:
    print(p)

# dataset = {
#     "tool_1_PZ": [10, 1],
#     "tool_2_PY": [5, 2],
#     "tool_3_PX": [1, 3],
#     "mean_stress_equal": [-100, 100]
# }

results = gen_exp.run_create_experiments_set(params)

print(results)

load_data.get_results_qform(results)
