from project.configs import geometry_conf as global_conf


def visibility():
    mode = InteractionMode.Solid

    ViewHelper.SetViewMode(mode, None)


def save_model(name, path=global_conf.path_save):
    options = ExportOptions.Create()
    DocumentSave.Execute(path + "\\" + name + ".stp", options)


def remove_model():
    selection = BodySelection.Create(GetRootPart().Bodies[0])
    result = Delete.Execute(selection)
