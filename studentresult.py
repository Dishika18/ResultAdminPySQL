import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("C:\\Users\\vaish\\Downloads\\Book2.csv",index_col="ROLL NO.")

#CLASS 12TH RESULT MENU
print("                          ---------------")
print(" CLASS 12TH RESULT ANALYSIS FOR SCIENCE STREAM")
print("                          ----------------")
print(" MAIN MENU:")
print(" 1. DISPLAY RESULT SHEET")
print(" 2. TO INSERT, UPDATE & DELETE A RECORD ")
print(" 3. DISPLAY RECORDS")
print(" 4. MAXIMUM AND MINIMUM MARKS OBTAINED SUBJECT WISE")
print(" 5. SUBJECTWISE MEAN/AVERAGE ")
print(" 6. TOP 10 SCORERS OVERALL AND SUBJECTWISE")
print(" 7. DISPLAY DETAILS OF A SPECIFIC STUDENT ")
print(" 8. NO. OF STUDENTS SCORING 90 & ABOVE SUBJECTWISE ")
print(" 9. DATA VISUALISATION")
print(" 10. EXIT")
print("____________________________________________________________________________")
x=int(input("ENTER YOUR CHOICE:"))



print( "                                 ************                              ") 
# RESULT SHEET
if x==1:
    sname=input("Please Enter School Name:")
    sch_code=int(input("Enter School Code : "))
    session=input("Enter Session : ")
    print("_____________________________________________________________________________________")
    print("---------------CLASS 12TH SCIENCE STREAM RESULT-----------------")
    print("SCHOOL NAME:",sname)
    print("SCHOOL CODE:",sch_code)
    print("SESSION:",session)
    print("                      *************                          ")
    print(df)
    
#INSERTING AND DELETING A RECORD
if x==2:
    print("1. Insert a record")
    print("2. Delete a record")
    print("3. Update a record")
    z=int(input("Enter your choice:"))
    if z==1:
        a=int(input("Enter roll no.:"))
        b=input("Enter your name:")
        c=int(input("Enter marks in maths:"))
        d=int(input("Enter marks in physics:"))
        e=int(input("Enter marks in chemistry:"))
        f=int(input("Enter marks in english:"))
        g=int(input("Enter marks in biology:"))
        h=int(input("Enter marks in ip:"))
        i=df.sum(axis=0)
        df.at[a,:]=[b,c,d,e,f,g,h,i]
        print("Data successfully added")
    elif z==2:
        a=int(input("Enter the roll no. whose record has to be deleted:"))
        df.drop([a],inplace=True)
        print("Data successfully deleted")
    elif z==3:
        a=int(input("Enter roll no. whose record has to be updated:"))
        b=input("Enter your name:")
        c=int(input("Enter marks in maths:"))
        d=int(input("Enter marks in physics:"))
        e=int(input("Enter marks in chemistry:"))
        f=int(input("Enter marks in english:"))
        g=int(input("Enter marks in biology:"))
        h=int(input("Enter marks in ip:"))
        i=df.sum(axis=0)
        df.at[a,:]=[b,c,d,e,f,g,h,i]
        print("Data successfully modified")
    else:
        print("INVALID CHOICE:please enter correct choice")

#USING HEAD AND TAIL FOR OBTAINING RECORDS OF A DATAFRAME

if x==3:
    y=int(input("ENTER 1 FOR OBTAINING RECORD FROM TOP AND 2 FROM BOTTOM:"))
    if y==1:
        n=int(input("ENTER NO. OF ROWS TO BE OBTAINED:"))
        print(df.head(n)) 
    elif y==2:
        m=int(input("ENTER NO. OF ROWS TO BE OBTAINED:"))
        print(df.tail(m)) 
    else:
        print("INVALID CHOICE:please enter correct choice")
# HIGHEST MARKS OBTAINED IN EACH SUBJECT
if x==4:    
    print("1.MAXIMUM MARKS SUBJECTWISE") 
    print("2.MINIMUM MARKS SUBJECTWISE")
    mks=int(input("ENTER YOUR CHOICE:"))   
    if mks==1:        
        sub=input("Enter the subject whose maximum marks you want to display:")     
        if sub=="MATHS":           
            print(df["MATHS"].max())   
        if sub=="PHY":         
            print(df["PHY"].max())  
        if sub=="CHEM":      
            print(df["CHEM"].max())    
        if sub=="BIO":           
            print(df["BIO"].max())       
        if sub=="ENG":           
            print(df["ENG"].max())     
        if sub=="IP":       
            print(df["IP"].max())    
        else:         
            print("INVALID CHOICE:please enter correct choice")    
    elif mks==2:        
        sub=input("Enter the subject whose minimum marks you want to display:")   
        if sub=="MATHS":          
            print(df["MATHS"].min())    
        if sub=="PHY":        
            print(df["PHY"].min())         
        if sub=="CHEM":      
            print(df["CHEM"].min())      
        if sub=="BIO":          
            print(df["BIO"].min())      
        if sub=="ENG":            
            print(df["ENG"].min())       
        if sub=="IP":        
            print(df["IP"].min())    
        else:         
            print("INVALID CHOICE:please enter correct choice")
else:       
    print("Please enter valid choice")  
#AVERAGE/MEAN SUBJECTWISE
if x==5:    
    avg=input("Enter subject for which average is to be calculated:")   
    if avg=="MATHS":          
        print(df['MATHS'].mean(axis=0))   
    elif avg=="PHY":           
        print(df['PHY'].mean(axis=0))  
    elif avg=="CHEM":      
        print(df['CHEM'].mean(axis=0))   
    elif avg=="ENG":           
        print(df['ENG'].mean(axis=0))  
    elif avg=="BIO":          
        print(df['BIO'].mean(axis=0))  
    elif avg=="IP":           
        print(df['IP'].mean(axis=0))   
else:        
    print("INVALID CHOICE:please enter correct choice") 
        
#TOP STUDENTS
if x==6:   
    print("1.OVERALL ")  
    print("2.SUBJECTWISE")  
    std=int(input("ENTER YOUR CHOICE:"))   
    if std==1:        
        print("Top 10 scoring students on basis of overall marks:")     
        dfl=df.sort_values(by=["TOTAL M."],ascending=False).head(10)   
        print(dfl) 
    elif std==2:   
        print("1.MATHS")     
        print("2.PHY")       
        print("3.CHEM")      
        print("4.ENG")     
        print("5.BIO")    
        print("6.IP")     
        ch=int(input("ENTER YOUR CHOICE:"))    
        if ch==1:        
            print("Top 10 scorers in mathematics:")    
            dfl=df.sort_values(by=["MATHS"],ascending=False).head(10)        
            print(dfl)  
        elif ch==2:     
            print("Top 10 scorers in physics:")    
            dfl=df.sort_values(by=["PHY"],ascending=False).head(10)      
            print(dfl)  
        elif ch==3:         
            print("Top 10 scorers in chemistry:")     
            dfl=df.sort_values(by=["CHEM"],ascending=False).head(10)     
            print(dfl)   
        elif ch==4:      
            print("Top 10 scorers in english:")          
            dfl=df.sort_values(by=["ENG"],ascending=False).head(10)    
            print(dfl)     
        elif ch==5:      
            print("Top 10 scorers in biology:")    
            dfl=df.sort_values(by=["BIO"],ascending=False).head(10)        
            print(dfl)        
        elif ch==6:           
            print("Top 10 scorers in mathematics:")        
            dfl=df.sort_values(by=["MATHS"],ascending=False).head(10)  
            print(dfl)    
        else:          
            print("INVALID CHOICE:please enter correct choice") 
    else:    
            print("INVALID CHOICE:please enter correct choice")
            
#DISPLAYING DETAILS OF A SPECIFIC STUDENT
if x==7:    
    rno=int(input("ENTER YOUR ROLL NO.:"))  
    print(df.loc[rno:rno,:])    
#NO. OF STUDENTS SCORING ABOVE 90
if x==8:   
    print("1.MATHS")   
    print("2.PHY")   
    print("3.CHEM")  
    print("4.ENG") 
    print("5.BIO")  
    print("6.IP")
    ef=int(input("Enter your choice for 90 and above scoring students subjectwise:"))    
    if ef==1:       
        print("NO. OF STUDENTS SCORING 90 AND ABOVE IN MATHEMATICS:")   
        print(df.loc[(df.MATHS>=90),'MATHS'].count())   
    elif ef==2: 
        print("NO. OF STUDENTS SCORING 90 AND ABOVE IN PHYSICS:")  
        print(df.loc[(df.PHY>=90),'PHY'].count())     
    elif ef==3:     
        print("NO. OF STUDENTS SCORING 90 AND ABOVE IN CHEMISTRY:")     
        print(df.loc[(df.CHEM>=90),'CHEM'].count())   
    elif ef==4:     
        print("NO. OF STUDENTS SCORING 90 AND ABOVE IN ENGLISH:")     
        print(df.loc[(df.ENG>=90),'ENG'].count())  
    elif ef==5:      
        print("NO. OF STUDENTS SCORING 90 AND ABOVE IN BIOLOGY:")     
        print(df.loc[(df.BIO>=90),'BIO'].count())      
    elif ef==6:       
        print("NO. OF STUDENTS SCORING 90 AND ABOVE IN IP:")  
        print(df.loc[(df.IP>=90),'IP'].count())
else:       
    print("INVALID CHOICE:please enter correct choice")
    
    
#DATA VISUALISATION(GRAPHICAL REPRESENTATION)
if x==9:  
    print("Data Visualization Menu") 
    print("1. Subjectwise Line Plot")
    print("2. Bar Chart for specific student performance")  
    print("3. Subjectwise Histogram")
    gr=int(input("Please enter your choice:")) 
    if gr==1:  
        print("1.MATHS") 
        print("2.PHY")  
        print("3.CHEM")   
        print("4.ENG")  
        print("5.BIO")   
        print("6.IP")    
        print("7.Multiline subjectwise line plot")   
        v=int(input("Enter your choice:"))
        if v==1:    
              plt.plot(df.MATHS,color="orange")    
              plt.xlabel("Roll no.")      
              plt.ylabel("Marks secured in mathematics")      
        elif v==2:     
             plt.plot(df.PHY,color='green')    
             plt.xlabel("Roll no.")     
             plt.ylabel("Marks secured in physics")      
        elif v==3:     
             plt.plot(df.CHEM,color='cyan')      
             plt.xlabel("Roll no.")      
             plt.ylabel("Marks secured in chemistry")    
        elif v==4:  
               plt.plot(df.ENG,color='yellow')       
               plt.xlabel("Roll no.")      
               plt.ylabel("Marks secured in english")   
        elif v==5:   
              plt.plot(df.BIO,color='red')     
              plt.xlabel("Roll no.")     
              plt.ylabel("Marks secured in biology")         
        elif v==6:     
             plt.plot(df.IP,color='blue')    
             plt.xlabel("Roll no.")        
             plt.ylabel("Marks secured in ip")    
        elif v==7:  
            plt.plot(df.PHY,df.MATHS,df.CHEM,df.IP,df.ENG,df.BIO)   
            plt.xlabel("Roll no.")        
            plt.ylabel("Marks secured")   
    else:      
        print("Invalid choice: please enter again")
            
    if gr==2:    
        n=int(input("enter your roll no.:"))     
        cd=int(input("ENTER 1 FOR HORIZONTAL AND 2 FOR VERTICAL BAR PLOT:"))    
        if cd==1:      
               df.loc[n:n,:].plot(kind="bar")          
               plt.xlabel("ROLL NO.")           
               plt.ylabel("Marks secured")
        elif cd==2:              
            df.loc[n:n,:].plot(kind="barh")     
            plt.xlabel("Marks secured")         
            plt.ylabel("ROLL NO.")      
        else:          
            print("Invalid choice: please enter again")       
    else:    
        print("Invalid choice: please enter again")  

    if gr==3:    
        print("1.MATHS")   
        print("2.PHY")    
        print("3.CHEM")   
        print("4.ENG")    
        print("5.BIO")    
        print("6.IP")     
        q=int(input("Enter your choice:"))  
        if q==1:          
            plt.hist(df.MATHS,bins=5,color='red')
            plt.title("Marks scored in mathematics")   
            plt.show()
        elif q==2:       
            plt.hist(df.PHY,bins=5,color='green')  
            plt.title("Marks scored in physics")  
            plt.show()
        elif q==3:
            plt.hist(df.CHEM,bins=5,color='magenta')
            plt.title("Marks scored in chemistry")          
            plt.show()      
        elif q==4:          
            plt.hist(df.ENG,bins=5,color='blue')           
            plt.title("Marks scored in english")           
            plt.show()      
        elif q==5:           
            plt.hist(df.BIO,bins=5,color='yellow')           
            plt.title("Marks scored in bio ")           
            plt.show()      
        elif q==6:            
            plt.hist(df.IP,bins=5,color='orange')            
            plt.title("Marks scored in IP")            
            plt.show()      
        else:
            print("Invalid choice: please enter again")  
    
#EXIT MENU
if x==10:  
    print("DO YOU REALLY WANT TO QUIT?")  
    xy=input("ENTER EITHER YES FOR EXITING THE PROGRAM OR NO:") 
    if xy=="YES" or xy=="yes":   
        print("THANK YOU FOR USING OUR PROGRAM")  
        print("............EXITING.............") 
    elif xy=="NO" or xy=='no':     
        print() 
    else:     
        print("INVALID CHOICE: please try again")
