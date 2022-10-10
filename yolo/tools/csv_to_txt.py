import csv
# csv_file = raw_input('Enter the name of your input file: ')
# txt_file = raw_input('Enter the name of your output file: ')

csv_file = '/Users/skasmani/GithubRepo/tf-yolo/data/aircraft dataset yolov5.v1i.tensorflow/valid/_annotations.csv'
txt_file = '/Users/skasmani/GithubRepo/tf-yolo/data/aircraft dataset yolov5.v1i.tensorflow/valid/_annotations.txt'
with open(txt_file, "w") as my_output_file:
    with open(csv_file, "r") as my_input_file:
        [ my_output_file.write(" ".join(row)+'\n') for row in csv.reader(my_input_file)]
    my_output_file.close()


