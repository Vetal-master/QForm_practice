from math import fabs as abs_

from project import global_conf as global_project_conf
from project.QForm.project.configs import experiment_conf as conf

from sys import path as path_sys

path_sys.append(global_project_conf.path_API_QForm)

from QFormAPI import *


def launch_QForm(path_client=global_project_conf.path_client_QForm, path_project=conf.path_base_script):
    qform = QForm()

    qform.start(path_client)

    arg1 = FileName()
    arg1.file = path_project
    qform.project_open(arg1)

    return qform


def create_drive(connection, V, axis):
    str_module__V = str(abs_(V))

    name_drive = r"V" + axis + "==" + str(V)

    print(name_drive)

    if V > 0:
        direction = r"1"
    else:
        direction = r"-1"

    QForm_name_drive = r'doc:drive/' + name_drive

    print(r'parts/17/value:32/' + axis)

    arg2 = DbProperty()
    arg2.db_path = QForm_name_drive  # название привода
    arg2.prop_path = r'parts/17/value:32/' + axis  # если Vx  -  то x и т.д.
    arg2.value = direction  # направление скорости
    connection.db_property_set(arg2)

    # Nominal velocity [mm/s]
    arg5 = DbProperty()
    arg5.db_path = QForm_name_drive
    arg5.prop_path = r'hyd_speed'
    arg5.value = str_module__V  # скорость по модулю
    connection.db_property_set(arg5)

    # Maximum load [MN]
    arg6 = DbProperty()
    arg6.db_path = QForm_name_drive  # меняем только путь
    arg6.prop_path = r'hyd_max_load'
    arg6.value = r'1e10'
    connection.db_property_set(arg6)

    # Nominal to maximum load ratio
    arg7 = DbProperty()
    arg7.db_path = QForm_name_drive  # меняем только путь
    arg7.prop_path = r'hyd_loadpercent'
    arg7.value = r'1'
    connection.db_property_set(arg7)

    # Drive type
    arg9 = DbProperty()
    arg9.db_path = QForm_name_drive  # меняем только путь
    arg9.prop_path = r'hyd_type'
    arg9.value = r'ind'
    connection.db_property_set(arg9)

    arg8 = SrcTargetPath()
    arg8.source_path = QForm_name_drive  # название привода
    arg8.target_path = QForm_name_drive  # меняем только путь
    connection.db_object_save(arg8)

    if axis == r"x":
        index_tool = 3
    elif axis == r"y":
        index_tool = 2
    elif axis == r"z":
        index_tool = 1

    arg17 = Property()
    arg17.object_type = ObjectType.Tool
    arg17.object_id = index_tool  # меняем только путь
    arg17.path = r'drive_id'
    arg17.property_type = PropertyType.Value
    arg17.value = QForm_name_drive
    connection.property_set(arg17)


def create_experiment(connection, dataset, path_geometry, VX, VY, VZ=-1):  # цикл
    print(path_geometry)
    print(VX)
    print(VY)
    print(VZ)

    arg21 = OperationCopy()
    arg21.id = -1
    arg21.source = 1
    arg21.make_copy_active = True
    ret21: ItemId = connection.operation_copy(arg21)

    arg3 = FileObject()
    arg3.file = path_geometry  # геометрия
    arg3.object_type = ObjectType.Workpiece
    arg3.object_id = 1
    connection.geometry_load_single_object(arg3)

    # DRIVE-----------------
    create_drive(connection, VX, r"x")
    create_drive(connection, VY, r"y")
    create_drive(connection, VZ, r"z")
    # DRIVE-----------------

    arg3 = SimulationParams()
    arg3.start_from_record = -1
    arg3.remesh_tools = False
    arg3.stop_at_record = 1
    arg3.max_records = 0
    arg3.stop_at_process_time = 0
    arg3.max_process_time = 0
    arg3.max_calculation_time = 0
    arg3.calculation_mode = CalculationMode.Chain
    ret3: MainSimulationResult = connection.start_simulation_advanced(arg3)

    # Mean Stress [MPa]
    arg33 = FieldStatAtMesh()
    arg33.object_type = ObjectType.Workpiece
    arg33.object_id = 1
    arg33.mesh_index = 0
    arg33.field = r'stress_mean'
    arg33.field_source = FieldSource.MainSimulation
    arg33.source_object = -1
    arg33.source_operation = -1
    arg33.interval_count = 25
    arg33.histogram_by = HistogramBy.ByNodes
    arg33.percentile_1_level = 5
    arg33.percentile_2_level = 95
    ret33: FieldStat = connection.field_stat(arg33)

    dataset["mean_stress_equal"].append(str(ret33.mean_value))

    # print(" mean_stress equal = " + str(ret33.mean_value))  # возвращаемый параметр

    # Load Z [MN], Time [s]
    arg14 = ChartId()
    arg14.arg_object_type = ObjectType.Tool
    arg14.arg_object_id = 1
    arg14.arg_subobject = -2147483648
    arg14.arg_id = 1000
    arg14.func_object_type = ObjectType.Tool
    arg14.func_object_id = 1
    arg14.func_subobject = -2147483648
    arg14.func_id = 3
    ret14: Chart = connection.chart_get(arg14)

    dataset["tool_1_PZ"].append(ret14.func_value[0])

    # dataset["tool_1_PZ"].append(str(ret14.func_value[0]))

    # print(" Tool1_PZ = " + str(ret14.func_value[0]))  # возвращаемый параметр

    # Load Z [MN], Time [s]
    arg15 = ChartId()
    arg15.arg_object_type = ObjectType.Tool
    arg15.arg_object_id = 2
    arg15.arg_subobject = -2147483648
    arg15.arg_id = 1000
    arg15.func_object_type = ObjectType.Tool
    arg15.func_object_id = 1
    arg15.func_subobject = -2147483648
    arg15.func_id = 2
    ret15: Chart = connection.chart_get(arg15)

    dataset["tool_2_PY"].append(ret15.func_value[0])

    # dataset["tool_2_PY"].append(str(ret15.func_value[0]))

    # print(" Tool2_PY = " + str(ret15.func_value[0]))  # возвращаемый параметр

    # Load Z [MN], Time [s]
    arg19 = ChartId()
    arg19.arg_object_type = ObjectType.Tool
    arg19.arg_object_id = 3
    arg19.arg_subobject = -2147483648
    arg19.arg_id = 1000
    arg19.func_object_type = ObjectType.Tool
    arg19.func_object_id = 1
    arg19.func_subobject = -2147483648
    arg19.func_id = 1
    ret19: Chart = connection.chart_get(arg19)

    dataset["tool_3_PX"].append(ret19.func_value[0])

    # dataset["tool_3_PX"].append(str(ret19.func_value[0]))

    # print(" Tool3_PX = " + str(ret19.func_value[0]))  # возвращаемый параметр
