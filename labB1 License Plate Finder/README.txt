Make a Python3 file that satisfies the following requirements:

    The file must define a class named Plates that can be used to search
    for information about cars given the license plate.

    The constructor must take a filename and read information from the file.
    The file will have one line for each car with tab characters between 
    fields. The first field is the license plate number.

    The class must have a method "findByPlate" that takes a license plate
    as parameter. It must return the extra information known about the
    car in a list of strings, or None if the plate is not recognized.
  
    With a database of 1000 license plates, must be able to complete
    50 searches per second.

    You should not change the test.py file.

    You must not use built in sorting or searching functions, including
    "index," "sort" and "sorted."

    If the file is run, it should run the code provided in the intial LabB1.py
    file, and out exactly:

Plates file: sampleplates.txt
findByPlate('GPA1905')
Expected answer: ['Chevrolet', 'Corvette Coupe', '2008', 'pink', 'Sylvia Cheers']
Actual answer: ['Chevrolet', 'Corvette Coupe', '2008', 'pink', 'Sylvia Cheers']
