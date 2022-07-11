def visibility():
    mode = InteractionMode.Solid

    ViewHelper.SetViewMode(mode, None)


def save_model(name, path=path_save__):
    options = ExportOptions.Create()

    DocumentSave.Execute(path + "\\" + name + ".stp", options)


def remove_model():
    selection = BodySelection.Create(GetRootPart().Bodies[0])

    result = Delete.Execute(selection)
