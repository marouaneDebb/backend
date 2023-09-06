import vtk

# Load VTP file
vtp_file_path = "Sample_1_d_predicted_step5.vtp"

reader = vtk.vtkXMLPolyDataReader()
reader.SetFileName(vtp_file_path)
reader.Update()

poly_data = reader.GetOutput()

# Convert to OBJ format
obj_writer = vtk.vtkOBJWriter()
obj_file_path = "Sample_1_d_predicted_step5.obj"
obj_writer.SetFileName(obj_file_path)
obj_writer.SetInputData(poly_data)
obj_writer.Update()

print("VTP file converted to OBJ:", obj_file_path)
