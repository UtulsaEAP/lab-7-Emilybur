def courseGrade():
    
    # TODO: Declare any necessary variables here. 
    filename = input()
    output_filename = "./report.txt" 
    last_names =[]
    first_names =[]
    mid1s =[]
    mid2s =[]
    finals =[]
    # TODO: Read a file name from the user and read the tsv file here. 
    with open(filename,"r") as file:
        lines = file.readlines()
   
    for line in lines:
        #parse the line
        line = line.strip()
        last, first, mid1, mid2, final = line.split("\t")
        mid1 = float(mid1)
        mid2 = float(mid2)
        final = float(final)
        #avg_exam = (mid1 + mid2 + final)/3
        last_names.append(last)
        first_names.append(first)
        mid1s.append(mid1)
        mid2s.append(mid2)
        finals.append(final)

    mid1_avg = sum(mid1s)/len(mid1s)
    mid2_avg = sum(mid2s)/len(mid2s)
    final_avg = sum(finals)/len(finals)
    # TODO: Compute student grades and exam averages, then output results to a text file here. 
    with open(output_filename,"w") as file:
        for i in range(len(first_names)):
            avg_exam = (mid1s[i]+mid2s[i]+finals[i])/3
            if 90 <= avg_exam:
                grade = "A"
            elif 80 <= avg_exam and avg_exam < 90:
                grade = "B"
            elif 70 <= avg_exam and avg_exam < 80:
                grade = "C"
            elif 60 <= avg_exam and avg_exam < 70:
                grade = "D"
            else: 
                grade = "F"
            file.write(str(last_names[i]) + "\t" + str(first_names[i]) + "\t" + str(mid1s[i]) + "\t" + str(mid2s[i]) + "\t" + str(finals[i]) + "\t"+str(grade)+"\n")
        file.write("Averages: midterm1 "+str(mid1_avg)+", midterm2 "+str(mid2_avg)+", final "+str(final_avg))
    return

if __name__ == "__main__":
    courseGrade()
    
    