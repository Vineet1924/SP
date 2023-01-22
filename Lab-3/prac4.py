def student_data(**data):
    for element in data:
   	 print(str(element) + " = " + str(data[element]))
         
student_data(student_id = "059", student_name = "Vineet", student_class = "A3")
