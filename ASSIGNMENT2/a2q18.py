gender=str(input("Enter your gender in 'male' or 'female' :"))
age=int(input("Enter your age :"))
condition=str(input("Enter your health condition in 'excellent' or 'poor' :" ))
place=str(input("Enter where you live in 'city' or 'village' :"))


if age>=25 and age<=35 :

    if gender == 'male':
        if condition == 'excellent':
            if place == 'city':
                print("Your premium is Rs 4 per thousand and your policy amount cannot exceed Rs 2,00,000 .")
                
            elif place=='village':
                print("Your premium is Rs 6 per thousand and your policy amount cannot exceed Rs 10,000 .")
            else :
                print("Your are not insured .")
        else :
            print("Your are not insured .")      
                

    elif gender == 'female':
        if condition=='excellent':
            if place=='city':
                print("Your premium is Rs 3 per thousand and your policy amount cannot exceed Rs 1,00,000 .")
            else :
                print("Your are not insured .")   
        else :
            print("Your are not insured .")        

    else :
        print("Your are not insured .")


else :
    print("Your are not insured .")

         
    
    
