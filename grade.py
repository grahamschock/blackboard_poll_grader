#Author: Graham Schock gschock@gwu.edu
import csv


reader = csv.DictReader(open('results.csv', encoding = 'utf-8-sig'))
answers = {}
students = {}
student_names = [];
master_score = [];

for row in reader:
    if "Integration" in row['AttendeeType']:
        answers[row['PollQuestion']] = row['AttendeePollAnswer']
    else:
        if row['AttendeeName'] in student_names:
            pass
        else :
            student_names.append(row['AttendeeName'])

reader = csv.DictReader(open('results.csv', encoding = 'utf-8-sig'))        
for row in reader:
    if "Integration" in row['AttendeeType']:
        pass
    elif answers[row['PollQuestion']] in row['AttendeePollAnswer']:
        students[row['AttendeeName'], row['PollQuestion']] = [row['AttendeePollAnswer'], "Correct"]
    else:
        students[row['AttendeeName'], row['PollQuestion']] = [row['AttendeePollAnswer'], "Incorrect"]
        
answer_header = []
answer_header.append("Name")
answer_header.append("Score out of: " + str(len(answers)))

for answer in answers:
    answer_header.append([answer,answers[answer]])

with open('grades.csv', mode = 'w', newline = '') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(answer_header)
    
        
for name in student_names:
    score = 0
    scores = [];
    scores.append(name);
    for answer in answers:
        if "Correct" in students[name, answer] :
            score = score + 1
        scores.append(students[name,answer])
    scores.insert(1, score)
    with open('grades.csv', mode = 'a', newline = '') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow(scores)

