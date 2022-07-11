from project.Excel.QForm import QForm_IO as load_data
from project.QForm.project import experiment_generator as gen_exp


def run_work_QForm():
    params = load_data.load_qform_params()

    results = gen_exp.run_create_experiments_set(params)

    load_data.get_results_qform(results)

run_work_QForm()
