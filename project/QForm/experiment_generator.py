import experiment as exp
from project import global_conf as global_project_conf


def run_create_experiments_set(dataset):
    exp.launch_QForm()

    results_experiments = []

    for experiment in dataset:
        path_geometry = global_project_conf.path_save__ + "\\" + dataset["name_model"]

        res = exp.create_experiment(path_geometry, dataset["VX"], dataset["VY"])

        results_experiments.append(res)

    return results_experiments
