import Techniovision


def inside_contest(faculty, file_name):
    program_dict = {}
    id_list = []
    f = open(file_name, 'r')
    for line in f:
        current_line = line.split()
        if current_line[0] == "inside":
            if faculty == current_line[-1]:
                program = current_line[-2]
                if not current_line[1] in id_list:
                    if program in program_dict:
                        program_dict[program] += 1
                    else:
                        program_dict[program] = 1
        if current_line[0] == "staff":
            if faculty == current_line[-1]:
                program = current_line[3]
                if program in program_dict:
                    program_dict[program] += 20
                else:
                    program_dict[program] = 20
    f.close()
    max_val = 0
    max_element= -1
    for k, v in program_dict:
        if v > max_val:
            max_val = v
            max_element = k
    return max_element


def get_faculty_list(file_name):
    f_list = []
    f = open(file_name, 'r')
    for line in f:
        current_line = line.split()
        if current_line[0] == "staff":
            f_list += current_line[-1]
    f.close()
    return f_list


faculty_list = get_faculty_list("input.txt")
faculty_dict = {}
for faculty in faculty_list:
    faculty_dict[inside_contest(faculty, "input.txt")] = faculty
techniovision = Techniovision.TechniovisionCreate()
f = open("input.txt", 'r')
for line in f:
    current_line = line.split()
    if current_line[0] == "techniovision":
        Techniovision.TechniovisionStudentVotes(techniovision, int(current_line[1]), str(current_line[-1]), str(faculty_dict[current_line[-2]]))
f.close()
Techniovision.TechniovisionWinningFaculty(techniovision)
Techniovision.TechniovisionDestroy(techniovision)
