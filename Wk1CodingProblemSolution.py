str_input = input("What is your name and age? ")
#Example Solution for part 1:

#if (not str_input.startswith("Name:")):
 #   print("Bad Input")
#if (not str_input.endswith("years old")):
 #   print("Bad Input")
#if ("Adolf" in str_input):
 #   print("Bad Input")
 
#If two or all three if statements are satisfied it will say bad input thrice...
#So we must run the second if statement ONLY IF THE FIRST ONE IS NOT SATISFIED
#So we put the next if statement in the else of the previous if statement
# This way it won't say bad input twice or thrice if more than one if statements are satisfied

#Example solution 2, correct version
#There is a lot of indentation going on here, very important to understand indentation well
#Next educational we will learn a shortcut called elif to make our lives a bit easier
if (not str_input.startswith("Name:")):
    print("Bad Input")
else:
    if (not str_input.endswith("years old")):
        print("Bad Input")
    else:
        if ("Adolf" in str_input):
            print("Bad Input")
        else: #We only want to run the rest of the code if the input was valid
            comma_location = str_input.find(",")
            period_location = str_input.find(".")
            first_name = str_input[comma_location+2:period_location]
            str_output = "Good evening " + first_name + ", "
            age_location = str_input.find("Age: ")+5
            #you could have also used "years old" and worked backwards from there
            age = int(str_input[age_location:age_location+2])
            #we want to include two digits so we add two to age location
            str_stage = ""
            str_extra = "."
            if (age>=0 and age<2):
                str_stage = "baby"
            if (age>1 and age<4):
                str_stage = "child"
            if (age>3 and age<10):
                str_stage = "kid"
            if (age>9 and age<13):
                str_stage = "preteen"
            if (age>12 and age<20):
                str_stage = "teen"
            if (age>19):
                str_stage = "adult"
            if (age==16):
                str_extra = ", and you have just become legal driving age."
            if (age==19):
                str_extra = ", and you have just become legal drinking age."
            str_output = str_output + "and you are a " + str_stage + str_extra
            print(str_output)
            
