from project import global_conf as global_project_conf

from sys import path as path_sys
path_sys.append(global_project_conf.path_API_QForm)

from QFormAPI import *

def launch_QForm(path_client=global_project_conf.path_client_QForm, path_project=global_project_conf.path_base_script):
    qform = QForm()

    qform.start(path_client)

    arg1 = FileName()
    arg1.file = path_project
    qform.project_open(arg1)


def create_experiment(path_geometry, VX, VY, VZ=-1):  # цикл
    arg21 = OperationCopy()
    arg21.id = -1
    arg21.source = 1
    arg21.make_copy_active = True
    ret21: ItemId = qform.operation_copy(arg21)

    arg3 = FileObject()
    arg3.file = path_geometry  # геометрия
    arg3.object_type = ObjectType.Workpiece
    arg3.object_id = 1
    qform.geometry_load_single_object(arg3)

    # Drive
    arg17 = Property()
    arg17.object_type = ObjectType.Tool
    arg17.object_id = 2
    arg17.path = r'drive_id'
    arg17.property_type = PropertyType.Value
    if VY > 0:
        VY_str = "+" + str(VY)
    else:
        VY_str = str(VY)
    arg17.value = r"doc:drive/Vy=" + VY_str  # входной параметр
    qform.property_set(arg17)

    # Drive
    arg18 = Property()
    arg18.object_type = ObjectType.Tool
    arg18.object_id = 3
    arg18.path = r'drive_id'
    arg18.property_type = PropertyType.Value
    if VX > 0:
        VX_str = "+" + str(VX)
    else:
        VX_str = str(VX)
    arg18.value = r"doc:drive/Vx=" + VX_str  # входной параметр
    qform.property_set(arg18)

    arg3 = SimulationParams()
    arg3.start_from_record = -1
    arg3.remesh_tools = False
    arg3.stop_at_record = 1
    arg3.max_records = 0
    arg3.stop_at_process_time = 0
    arg3.max_process_time = 0
    arg3.max_calculation_time = 0
    arg3.calculation_mode = CalculationMode.Chain
    ret3: MainSimulationResult = qform.start_simulation_advanced(arg3)

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
    ret33: FieldStat = qform.field_stat(arg33)

    result = {
        "mean_stress equal": str(ret33.mean_value)
    }

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
    ret14: Chart = qform.chart_get(arg14)

    result["Tool1_PZ"] = str(ret14.func_value[0])

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
    ret15: Chart = qform.chart_get(arg15)

    result["Tool2_PY"] = str(ret15.func_value[0])

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
    ret19: Chart = qform.chart_get(arg19)

    result["Tool3_PX"] = str(ret19.func_value[0])

    # print(" Tool3_PX = " + str(ret19.func_value[0]))  # возвращаемый параметр

    return result
