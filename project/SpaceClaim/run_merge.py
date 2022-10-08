import fileinput
import os

path_files = [r"../global_conf.py",
              r"./project/configs/import.py",
              r"./project/configs/geometry_generator_conf.py",
              r"./project/geometry/SC_cube.py",
              r"./project/geometry/SC_sphere.py",
              r"./project/geometry/SC_ellipse.py",
              r"./project/geometry/SC_utils.py",
              r"./project/handlers/h_cube.py",
              r"./project/handlers/h_ellipse.py",
              r"./project/handlers/h_sphere.py",
              r"./project/model_generator.py",
              r"./project/porosity_generator.py",
              r"./project/run_model_generator.py"]


def run_merge():
    try:
        os.remove(r'D:\2022\pycharm_projects\QForm_practice\project\SpaceClaim\merged.py')
    except OSError as e:
        print("File not exist, create file")

    with open(r'D:\2022\pycharm_projects\QForm_practice\project\SpaceClaim\merged.py', 'w+') as file:
        for path_file in path_files:
            input_lines = fileinput.input(path_file, mode="r")

            line_delimiter = "\n\n"

            file.writelines(input_lines)

            file.writelines(line_delimiter)

    print("END MERGE")


run_merge()