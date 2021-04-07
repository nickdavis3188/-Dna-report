#Import modules
from patient import Patient
import random
import re

#initialize global variable
random.seed(5) # random seed used for reproducibility
MAX_STRAND=20



########################
##### Functions ########
########################

def display_menu():
    """ Display all the options, no input, no output """
    print("\n1-List; 2-Info; 3-Remove; 4-Insert; 5-Compare; 6-Compare all; 7-Analyze")


def random_base():
    """select the letter A,C,G,T at random, output (String) """
    bases=["A","C","G","T"]
    return random.choice(bases)


def random_strand():
    """ this generate a random strans  and also set the conditions"""
    # local var
    diabetes = ""
    blue_eyes = ""
    three_eyes = ""
    strans = ""

    # instanciating dictionary object
    final_res = dict()
    for i in range(0,MAX_STRAND):
        strans += random_base() 
    # for three_eyes
    if "AAA" in strans:
        three_eyes = "True"
    else:
        three_eyes = "False"
    # for blue_eyes
    if "GGA" in strans:
        blue_eyes = "True"
    else:
        blue_eyes = "False"
    # diabetes
    if "CTA" in strans:
        diabetes = "True"
    else:
        diabetes = "False"
    # assigning values with keys to the dictionary
    final_res['strand'] = strans
    final_res['diabetes'] = diabetes
    final_res['blue'] = blue_eyes
    final_res['three'] = three_eyes

    return final_res

# Storage for each initiation   
init_storage = [
    Patient("Andrea",37,random_strand()['strand'], random_strand()['diabetes'], random_strand()['blue'], random_strand()['three']),
    Patient("Bob",28,random_strand()['strand'], random_strand()['diabetes'], random_strand()['blue'], random_strand()['three']),
    Patient("Brooke",34,random_strand()['strand'], random_strand()['diabetes'], random_strand()['blue'], random_strand()['three']),
    Patient("Connor",27,random_strand()['strand'], random_strand()['diabetes'], random_strand()['blue'], random_strand()['three']),
    Patient("James",25,random_strand()['strand'], random_strand()['diabetes'], random_strand()['blue'], random_strand()['three']),
    Patient("Jenna",44,random_strand()['strand'], random_strand()['diabetes'], random_strand()['blue'], random_strand()['three']),
    Patient("John",45,random_strand()['strand'], random_strand()['diabetes'], random_strand()['blue'], random_strand()['three']),
    Patient("Julie",37,random_strand()['strand'], random_strand()['diabetes'], random_strand()['blue'], random_strand()['three']),
    Patient("Kate",48,random_strand()['strand'], random_strand()['diabetes'], random_strand()['blue'], random_strand()['three']),
    Patient("Keith",28,random_strand()['strand'], random_strand()['diabetes'], random_strand()['blue'], random_strand()['three']),
    Patient("Kelly",25,random_strand()['strand'], random_strand()['diabetes'], random_strand()['blue'], random_strand()['three']),
    Patient("Luke",33,random_strand()['strand'], random_strand()['diabetes'], random_strand()['blue'], random_strand()['three']),
    Patient("Mark",34,random_strand()['strand'], random_strand()['diabetes'], random_strand()['blue'], random_strand()['three']),
    Patient("Pat",26,random_strand()['strand'], random_strand()['diabetes'], random_strand()['blue'], random_strand()['three']),
    Patient("Taylor",30,random_strand()['strand'], random_strand()['diabetes'], random_strand()['blue'], random_strand()['three']),
    Patient("Tony",55,random_strand()['strand'], random_strand()['diabetes'], random_strand()['blue'], random_strand()['three'])
]

##### Functions continuation########
########################

# show all Patient in the list
def list_all_patient():
    """
    This function list out all the patient and thier info 
    """
    counts = 1
    # HEADER
    print("ID"," "*(7-len(init_storage[3].age)),"   ",
        "Name", " "*(9-len(init_storage[2].name)),"   ",
        " Age", " "*(8-len(init_storage[2].strand)),"  ",
        "DNA-strand (20 length) ",
        " Diabetes"," "*(3-len(init_storage[3].age)),"   ",
        "Blue-eyes", " "*(4-len(init_storage[2].name)),"  ",
        "Three-eyes","    \n")
    print("===================================================================================================")

    # This iterate the all the Patient info in table
    for patients_index in range(len(init_storage)):
        print(counts," "*(7-len(init_storage[patients_index].age)),"   ",
            init_storage[patients_index].name, " "*(9-len(init_storage[patients_index].name)),"   ",
            init_storage[patients_index].age, " "*(7-len(init_storage[patients_index].strand)),"   ",
            init_storage[patients_index].strand," "*(7-len(init_storage[patients_index].has_diabetis)),"   ",
            init_storage[patients_index].has_diabetis, " "*(7-len(init_storage[patients_index].has_Blue_eyes)),"   ",
            init_storage[patients_index].has_Blue_eyes, " "*(7-len(init_storage[patients_index].has_Three_eyes)),"   ",
            init_storage[patients_index].has_Three_eyes,":   ")
        
        # this increment the counts variable
        counts +=1


# list_all_patient()
# inseert new Patient

def insert_new_Patient():
    """
    this allows you to append a Patient into the memory
    """
    # A try and except Block to cheack errors
    try:

        # this request for the agumet to initiate new Petient
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        strand = input("Enter DNA strand: ")

        name.strip()
        strand.strip()

        # local var
        diabetes = ""
        blue_eyes = ""
        three_eyes = ""

        # check for input !== ""
        if len(name) == 0 or len(age) == 0:
            raise Exception("pls check your input and try agen")
        else:
            # check for alphabet
            if re.search('[a-zA-Z]', age) == True:
                raise Exception("Sorry Age must be an integer")
        
        # check for strand length
        if len(strand) == MAX_STRAND:
            # for three_eyes
            if "AAA" in strand:
                three_eyes = "True"
            else:
                three_eyes = "False"
            # for blue_eyes
            if "GGA" in strand:
                blue_eyes = "True"
            else:
                blue_eyes = "False"
                # diabete
            if "CTA" in strand:
                diabetes = "True"
            else:
                diabetes = "False"
            
            # insert
            init_storage.append( Patient(name,age,strand,diabetes,blue_eyes,three_eyes))  

            return "Succesfull"

        else:
            raise Exception("Bad input! -length must be 20") 

        # this append a new initiated Patient into the init_storage

    # this block catches any error that occurs   
    except Exception as err:
       if err:
            return err



# Delete Patient
def remove_patient():
    """
    this function helps to remove a patient from the memory
    """
    try:
        # input a number to perform a delete action
        patient_index = input("Who do you want to remove (enter number):")

        if len(patient_index) != 0 and re.search('[a-zA-Z]', patient_index) != False:

            # convert indext to an integer
            converted_indext = int(patient_index)

            to_main_index = converted_indext  - 1

            # this perform the delete action in the memory
            del init_storage[to_main_index]
            return "Successfull"
        else:
            raise Exception("pls check your input and try agen")    
    # error block
    except Exception as err:
       if err:
            return err



# Patient statistics
def info():
    """
    This function display the statistics of all patient
    """
    # empty arrays for calculation
    range_twenty = []
    range_thirty = []
    range_fourty = []
    range_fifty = []

    # 20
    for i in range(0,len(init_storage)):
        if int(init_storage[i].age) >= 20 and int(init_storage[i].age) < 30:
            range_twenty.append(init_storage[i].age)
            
    
    # 30
    for i in range(0,len(init_storage)):
        if int(init_storage[i].age) >= 30 and int(init_storage[i].age) < 40:
            range_thirty.append(init_storage[i].age)

    # 40
    for i in range(0,len(init_storage)):
        if int(init_storage[i].age) >= 40 and int(init_storage[i].age) < 50:
            range_fourty.append(init_storage[i].age)

    # 50
    for i in range(0,len(init_storage)):
        if int(init_storage[i].age) >= 50 and int(init_storage[i].age) < 60:
            range_fifty.append(init_storage[i].age)

    # mean
    total_value = 0
    for index in range(0,len(init_storage)):
        total_value += int(init_storage[index].age) 

    # ########  Conditions
    check_diabetes = []
    check_blu = []
    check_three = []

    for index in range(0,len(init_storage)):
        if init_storage[index].has_diabetis == "True":
           check_diabetes.append(init_storage[index].has_diabetis)      
    total1 = (len(check_diabetes)* 100)/len(init_storage)
    # blue
    for index in range(0,len(init_storage)):
        if init_storage[index].has_Blue_eyes == "True":
           check_blu .append(init_storage[index].has_Blue_eyes)      
    total2 = (len(check_blu)* 100)/len(init_storage)
    # three
    for index in range(0,len(init_storage)):
        if init_storage[index].has_Three_eyes == "True":
           check_three.append(init_storage[index].has_Three_eyes)      
    total3 = (len(check_three)* 100)/len(init_storage)
# ####################
    
        
    # Display statistics
    print(f"#Patients: {len(init_storage)}")
    print("< 20 : 0.0%")
    print(f"20's : {round((len(range_twenty)* 100)/ len(init_storage),1)}%")
    print(f"30's : {round((len(range_thirty)* 100)/ len(init_storage),1)}%")
    print(f"40's : {round((len(range_fourty)* 100)/ len(init_storage),1)}%")
    print(f"50's : {round((len(range_fifty)* 100)/ len(init_storage),1)}%")
    print(">60 : 0.0% \n")
    print(f"Age Mean: {round(total_value/len(init_storage),1)}")
    print(f"Diabetes: {round(total1,1)}%")
    print(f"Blue-eyes: {round(total2,1)}%")
    print(f"Three-eyes: {round(total3,1)}%")
    # range 10 to 20

        


#  compare
def compare():
    """
    tis function compare two patient strand for similarities
    """
    try:
        # getting inputs from user
        first_patient = input("First patient (enter number): ")
        second_patient = input("Second patient (enter number): ")
        # check for  len
        if len(first_patient) == 0 or len(second_patient) == 0:
            raise Exception("please check your input and try agen")
        # check for alphabet
        if re.search('[a-zA-B]', first_patient) == True and re.search('[a-zA-B]', second_patient) == True:
            raise Exception("Your input cannot contain an Alphabet")
        else:
            # convert to int
            converted_indext1 = int(first_patient) - 1
            converted_indext2 = int(second_patient) - 1
            if converted_indext1 >= 1 and converted_indext1 < len(init_storage) or converted_indext2 >= 1 and converted_indext2 < len(init_storage):
                    
                first_patient_strand = []
                second_patient_strand = []
                result = []
                compared_strand = ""
                final_result = dict()

                # getting strans from memory
                fStrand = init_storage[converted_indext1].strand
                SStrand = init_storage[converted_indext2].strand

                for index in range(0,len(fStrand)):
                    first_patient_strand.append(fStrand[index])
                    second_patient_strand.append(SStrand[index])

                # setting  non similer stran to x
                for index in range(0,len(first_patient_strand)):
                    if first_patient_strand[index] != second_patient_strand[index]:
                        result.append("x")
                    else:
                        result.append(first_patient_strand[index])


                for index2 in range(0,len(result)):
                    compared_strand += result[index2]


                current_strand = []
                total_letter = 0
            
                for index in range(0,len(compared_strand)):
                    if compared_strand[index] != "x":
                        current_strand.append(compared_strand[index])
                

                for index2 in range(0,len(current_strand)):
                    total_letter += 1 

                # calculate for similariy %
                output_total = (total_letter * 10)/2

            
                # assigning values with key to the dictionary object
                final_result['Strand'] = compared_strand
                final_result['Statment'] = f"Patients {converted_indext1} and {converted_indext2} common strand is {compared_strand}"
                final_result['Simler'] = f"They are similar at {round(output_total,1)}%"
                final_result["clearStatement"] = f"{init_storage[converted_indext1].name} vs {init_storage[converted_indext2].name} {round(output_total,1)}%"
                return final_result  
            else:
                
                raise Exception("Input too large please check yor input and try agen")

            # error block
    except Exception as err:
        if err:
            return err


# compare all

# this function compare the DNA strand between all patients and return
    # some information about their DNA similarity.
def compare_all():
    """
    this function compare the DNA strand between all patients and return
    some information about their DNA similarity.
    """
    for index1 in range(0,len(init_storage)):
        # 
        for index2 in range(len(init_storage)):
            first_patient_strand = []
            second_patient_strand = []
            result = []
            compared_strand = ""

            fStrand = init_storage[index1].strand
            SStrand = init_storage[index2].strand

            for i in range(0,len(fStrand)):
                first_patient_strand.append(fStrand[i])
                second_patient_strand.append(SStrand[i])

            for i in range(0,len(first_patient_strand)):
                if first_patient_strand[i] != second_patient_strand[i]:
                    result.append("x")
                else:
                    result.append(first_patient_strand[i])


            for i in range(0,len(result)):
                compared_strand += result[i]


            current_strand = []
            total_letter = 0

            for ind in range(0,len(compared_strand)):
                if compared_strand[ind] != "x":
                    current_strand.append(compared_strand[ind])
            

            for i in range(0,len(current_strand)):
                total_letter += 1 

            output_total = (total_letter * 10)/2
            if round(output_total,1) > 33.0:    
                print(f"{init_storage[index1].name} vs {init_storage[index2].name} {round(output_total,1)}%") 




# find pattern function helps 


#     this function accepts the list of patients and the
    # DNA sequence of the condition
def find_pattern():
    """
    this function accepts the list of patients and the
    DNA sequence of the condition
    """
    try:
        # getting users input
        condition = input("Which condition are you looking for: ")
        sequence = input("Enter sequence: ")

        if condition.lower() == "diabetes" and sequence.upper() == "CTA":
            checTrue = []
            for index in range(0,len(init_storage)):
                if init_storage[index].has_diabetis == "True":
                    checTrue.append(init_storage[index].has_diabetis)      
            total = (len(checTrue)* 100)/len(init_storage)

            return f"Patients with the Diabetes condition: {round(total,1)}%"
        elif condition == "blue-eyes" and sequence == "GGA":
            checTrue = []
            for index in range(0,len(init_storage)):
                if init_storage[index].has_Blue_eyes == "True":
                    checTrue.append(init_storage[index].has_Blue_eyes)      
            total = (len(checTrue)* 100)/len(init_storage)

            return f"Patients with the Diabetes condition: {round(total,1)}%"
        elif condition == "three-eyes" and sequence == "AAA":
            checTrue = []
            for index in range(0,len(init_storage)):
                if init_storage[index].has_Blue_eyes == "True":
                    checTrue.append(init_storage[index].has_Blue_eyes)      
            total = (len(checTrue)* 100)/len(init_storage)

            return f"Patients with the Diabetes condition: {round(total,1)}%"

        else:
            raise Exception("Condition and sequence not found pls confirm your spellings and try agen")

    except Exception as err:
        if err:
            return err

