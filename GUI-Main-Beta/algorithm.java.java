import java.util.*;


// if the code didnt work change the file name to "temp.java"
public class temp {    
    private static final String[] days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday"}; //constant cannot be 
    private static final String[] classesYearOne = {"Basic Electrical Engneering", "Graphics And Design", "Engneering Math", "Engineering Physics", "Programming C"};
    private static final String[] classesYearTwoTheory = {"Analog Electronic Circuits", "Data structure & Algorithms", "IT Workshop (Sci Lab/MATLAB) Theory", "Digital Logic" , "Differential Calculus", "Engineering Biology", "Linguistics & Oral Communication"};

    private static boolean[] classesYearTwoAssigned = new boolean[classesYearTwoTheory.length];

    private static final String[] classesYearTwoPractical = {"Analog Electronic Circuits Laboratory", "Data structure & Algorithms Laboratory", "IT Workshop (Sci Lab/MATLAB) Laboratory", "Digital Logic Laboratory"};
    private static final int[] classeshavePractical = {1,1,1,1,0,0,0};
    private static final int[] classesYearTwoPriority = {2,1,1,1,1,3,3};
    private static boolean[] classesYearTwoAssignedTheory = new boolean[classesYearTwoTheory.length]; //initialised to false every element
    private static final int[] classesYearTwoTheoryCredit = {3,3,1,3,2,3,0};
    private static final int[] classesYearTwoPracticalCredit = {2,2,2,2};
    private static final String[] classesYearTwoPracticalClass = {"212", "G01", "G03", "218"};  

    private static final String[] laboratoryClassRoomsPool = {"212", "GO1", "G02","GO3", "G20", "218", "203", "204"};
    private static final String[] laboratoryTeacherPool = {"APR", "CK", "PDE", "IC", "CT", "PPS", "AR", "KKC"};
    private static final String[] theoryClassFacultyPoolCSE = {"SGP", "SS", "SB", "DD", "SG", "AB", "SKG"};
    private static final String[] theoryClassFacultyPoolIT = {"KGH", "PSC", "SPJ", "NSM", "ND", "ACH", "PKS"};

    private static final String[] classesYearOneEvenSemesterTheory = {"Basic Electrical Engineering", "Graphics And Design", "Engneering Math", "Engineering Physics", "Problem for Problem Solving in C"};
    private static final int[] classesYearOneEvenSemesterTheoryCredit = {};
    private static final String[] classesYearOneEvenSemesterPractical = {"Basic Electrical Engineering Laboratory", "Graphics And Design Laboratory", "Engineering Physics Laboratory", "Problem for Problem Solving in C Laboratory"};
    private static final int[] classesYearOneEvenSemesterPracticalCredit = {2,2,2,2};

    private static final String[] classesYearTwoEvenSemesterTheory = {"Discrete Mathematics","Computer Organization & Architecture", "Operating Systems","Design & Analysis of Algorithms", "Economics & Accountancy", "Environmental Sciences", "Business Communications"};
    private static final int[] classesYearTwoEvenSemesterTheoryCredit = {4,3,3,3,2,0,0};
    private static final String[] classesYearTwoEvenSemesterPractical = {"Computer Organization & Architecture Laboratory", "Operating Systems Laboratory", "Design & Analysis of Algorithms Laboratory"};
    private static final int[] classesYearTwoEvenSemesterPracticalCredit = {2,2,2};

    private static int[] classesYearTwoEvenSemesterHoursRequiredTheory = new int[classesYearTwoEvenSemesterTheory.length];
    private static boolean[] classesYearTwoEvenSemesterAssignedTheory = new boolean[classesYearTwoEvenSemesterHoursRequiredTheory.length];


    private static final String[] classesYearThreeEvenSemesterTheory = {"Compiler Design","Computer Networks","Professional Elective-II", "Professional Elective-III", "Open Elective I"};
    private static final int[] classesYearThreeEvenSemesterTheoryCredit = {3,3,3,3,3};
    private static final String[] classesYearThreeEvenSemesterPractical = {"Compiler Design Laboratory","Computer Networks Laboratory","Python Programming Laboratory", "Project-I" ,"Group Discussion & Personal Interview"};
    private static final int[] classesYearThreeEvenSemesterPracticalCredit = {2,2,2,3,1};

    private static int[] classesYearThreeEvenSemesterHoursRequiredTheory = new int[classesYearThreeEvenSemesterTheoryCredit.length];
    private static boolean[] classesYearThreeEvenSemesterAssignedTheory = new boolean[classesYearThreeEvenSemesterHoursRequiredTheory.length];


    private static final String[] classesYearFourEvenSemesterTheory = {"Professional Elective VI" ,"Open Elective III" ,"Open Elective IV"};
    private static final int[] classesYearFourEvenSemesterTheoryCredit = {3,3,3};
    private static final String[] classesYearFourEvenSemesterPractical = {"Project-III"};
    private static final int[] classesYearFourEvenSemesterPracticalCredit = {6};
    

    private static int[] classesYearFourEvenSemesterHoursRequiredTheory = new int[classesYearFourEvenSemesterTheoryCredit.length];
    private static boolean[] classesYearFourEvenSemesterAssignedTheory = new boolean[classesYearFourEvenSemesterHoursRequiredTheory.length];


    public static void classesHoursRequired() {
        // use switch case to determine which year you will take into account
        for (int i = 0; i < classesYearTwoTheoryCredit.length; i++) {
            if(classesYearTwoTheoryCredit[i] == 0) // when the subject is non-credit course, we need to give it 1 class in a week
            classesYearTwoEvenSemesterHoursRequiredTheory[i] = classesYearTwoTheoryCredit[i] + 1;
            else classesYearTwoEvenSemesterHoursRequiredTheory[i] = classesYearTwoTheoryCredit[i];
        }

        for (int i = 0; i < classesYearThreeEvenSemesterTheoryCredit.length; i++) {
            if(classesYearTwoTheoryCredit[i] == 0) // when the subject is non-credit course, we need to give it 1 class in a week
            classesYearThreeEvenSemesterHoursRequiredTheory[i] = classesYearThreeEvenSemesterTheoryCredit[i] + 1;
            else classesYearThreeEvenSemesterHoursRequiredTheory[i] = classesYearThreeEvenSemesterTheoryCredit[i];
        }

        for (int i = 0; i < classesYearFourEvenSemesterTheoryCredit.length; i++) {
            if(classesYearFourEvenSemesterTheoryCredit[i] == 0) // when the subject is non-credit course, we need to give it 1 class in a week
            classesYearFourEvenSemesterHoursRequiredTheory[i] = classesYearFourEvenSemesterTheoryCredit[i] + 1;
            else classesYearFourEvenSemesterHoursRequiredTheory[i] = classesYearFourEvenSemesterTheoryCredit[i];
        }
    }
    
    private static int getDay(String day) {
        switch(day) {
            case "Monday": return 1;
            case "Tuesday": return 2;
            case "Wednesday": return 3;
            case "Thursday": return 4;
            default: return 5;
        }
    }

    private static void mapTeachers(Map<String, time> sub, String[] teacher, String[] teacherOffDays) {
        for (int i = 0; i < teacherOffDays.length; i++) {
            
            if(teacherOffDays[i] == null) //tecaher can take all the days
            {
                sub.put(teacher[i], new time(true));
            }
            else {
                int j = getDay(teacherOffDays[i])  - 1;
                time t = new time(j);
                sub.put(teacher[i], t);
            }
        }
    }

    public static void main(String[] args) {      
        
        Map<String, String> map = new HashMap<>();
        int count = 10;

        String[] teacher = {"SGP", "SS", "SN", "RD", "NRD", "PDe", "PD"};
        //create a map which stores the timings of the teacher taking the class
        Map<String, time> sub  = new HashMap<>();

        String[] teacherOffDays = {null, "Tuesday", "Wednesday", "Thursday", "Friday", "Monday", "Tuesday"};

        //map the teachers to the days they are off of taking the class
        //and that day you cannot assign that particular laboratory subject
        
        String[] labTechnicians = {"PPS", "APR", "IC", "CK"};

        Map<String, String> subTeacher = new HashMap<>();



        boolean[] isSubjectAssigned = new boolean[classesYearTwoTheory.length];



        System.out.println("Lab Schedule for Group A:");
        assignLabClasses(labTechnicians, teacher, 0);
        System.out.println();
        System.out.println("Lab Schedule for Group B:");
        assignLabClasses(labTechnicians, teacher, 1);

        String[][] theoryClassesYearTwo = new String[4][5];
        boolean[][] isBookedYearTwo = new boolean[4][5];

        String[][] theroyClassesYearThree = new String[4][5];
        boolean[][] isBookedYearThree = new boolean[4][5];

        String[][] theroyClassesYearFour = new String[4][5];
        boolean[][] isBookedYearFour = new boolean[4][5];

        classesHoursRequired();
        assignFirstHourYearTwo(theoryClassesYearTwo, isBookedYearTwo);


        
        assignTheoryClassesYearTwo(theoryClassesYearTwo, isBookedYearTwo);
        


        assignReaminingSubjectsYearTwo(theoryClassesYearTwo, isBookedYearTwo);

        System.out.println("\nTheory Classes Even Semester Year Two:");

        for (String[] array : theoryClassesYearTwo) {
            for (String string : array) {
                System.out.print(string + " ");
                
            }
            System.out.println();
            
        }


        // Even Semester Year Three
        assignFirstHourYearThree(theroyClassesYearThree, isBookedYearThree);
        assignTheoryClassesYearThree(theroyClassesYearThree, isBookedYearThree);
        assignReaminingSubjectsYearThree(theroyClassesYearThree, isBookedYearThree);

        System.out.println("\nTheory Classes Even Semester Year Three:");

        for (String[] array : theroyClassesYearThree) {
            for (String string : array) {
                System.out.print(string + " ");
                
            }
            System.out.println();
            
        }

        //Even Semester Year Four
        assignFirstHourYearFour(theroyClassesYearFour, isBookedYearFour);
        assignTheoryClassesYearFour(theroyClassesYearFour, isBookedYearFour);
        assignReaminingSubjectsYearFour(theroyClassesYearFour, isBookedYearFour);

        System.out.println("\nTheory Classes Even Semester Year Four:");

        for (String[] array : theroyClassesYearFour) {
            for (String string : array) {
                System.out.print(string + " ");
                
            }
            System.out.println();
            
        }
        
    }

    private static void assignReaminingSubjectsYearFour(String[][] theoryClasses, boolean[][] isBooked) {
        int count = 0;
        for (int i : classesYearFourEvenSemesterHoursRequiredTheory) {
            if(i != 0) count += i;
        }
        int countClass = 0;
        for(int i = 1; i < 4; i++) {
            for(int j = 0; j < 5; j++) {
                if(theoryClasses[i][j] == null) countClass++;
            }
        }

        remclass[] rem = new remclass[countClass];
        int k = 0;
        // System.out.println();
        for(int i = 1; i < 4; i++) {
            for(int j = 0; j < 5; j++) {
                if(theoryClasses[i][j] == null) {
                    rem[k++] = new remclass(i, j);
                }
            }
        }
        int timeRand = (int)(Math.random() * ( countClass - 0)) + 0;

        int prevVal = count;
        
        while(count != 0) {
            
            for (int i = 0; i < classesYearFourEvenSemesterHoursRequiredTheory.length; i++) {
                if(classesYearFourEvenSemesterHoursRequiredTheory[i] != 0) { //perform the operations
                    classesYearFourEvenSemesterHoursRequiredTheory[i]--;
                    count--;
                    int row = rem[timeRand % countClass].getRow();
                    int col = rem[timeRand % countClass].getCol();
                    timeRand++;
                    theoryClasses[row][col] = classesYearFourEvenSemesterTheory[i];
                }
            }

            if (prevVal == count) {
                System.out.println("There are no possible schedule for the given constraints");
                count = 0;
            }

            prevVal = count;
        }
    }

    private static void assignReaminingSubjectsYearThree(String[][] theoryClasses, boolean[][] isBooked) {
        int count = 0;
        for (int i : classesYearThreeEvenSemesterHoursRequiredTheory) {
            if(i != 0) count += i;
        }
        int countClass = 0;
        for(int i = 1; i < 4; i++) {
            for(int j = 0; j < 5; j++) {
                if(theoryClasses[i][j] == null) countClass++;
            }
        }
       
        remclass[] rem = new remclass[countClass];
        int k = 0;
        // System.out.println();
        for(int i = 1; i < 4; i++) {
            for(int j = 0; j < 5; j++) {
                if(theoryClasses[i][j] == null) {
                    rem[k++] = new remclass(i, j);
                }
            }
        }
        int timeRand = (int)(Math.random() * ( countClass - 0)) + 0;

        int prevVal = count;
        
        while(count != 0) {
            
            for (int i = 0; i < classesYearThreeEvenSemesterHoursRequiredTheory.length; i++) {
                if(classesYearThreeEvenSemesterHoursRequiredTheory[i] != 0) { //perform the operations
                    classesYearThreeEvenSemesterHoursRequiredTheory[i]--;
                    count--;
                    int row = rem[timeRand % countClass].getRow();
                    int col = rem[timeRand % countClass].getCol();
                    timeRand++;
                    theoryClasses[row][col] = classesYearThreeEvenSemesterTheory[i];
                }
            }

            if (prevVal == count) {
                System.out.println("There are no possible schedule for the given constraints");
                count = 0;
            }

            prevVal = count;
        }
    }

    private static void assignReaminingSubjectsYearTwo(String[][] theoryClasses, boolean[][] isBooked) {
        int count = 0;
        for (int i : classesYearTwoEvenSemesterHoursRequiredTheory) {
            if(i != 0) count += i;
        }
        int countClass = 0;
        for(int i = 1; i < 4; i++) {
            for(int j = 0; j < 5; j++) {
                if(theoryClasses[i][j] == null) countClass++;
            }
        }
        remclass[] rem = new remclass[countClass];
        int k = 0;
        // System.out.println();
        for(int i = 1; i < 4; i++) {
            for(int j = 0; j < 5; j++) {
                if(theoryClasses[i][j] == null) {
                    rem[k++] = new remclass(i, j);
                }
            }
        }

        int timeRand = (int)(Math.random() * ( countClass - 0)) + 0;

        int prevVal = count;
        
        while(count != 0) {
            
            for (int i = 0; i < classesYearTwoEvenSemesterHoursRequiredTheory.length; i++) {
                if(classesYearTwoEvenSemesterHoursRequiredTheory[i] != 0) { //perform the operations
                    classesYearTwoEvenSemesterHoursRequiredTheory[i]--;
                    count--;
                    int row = rem[timeRand % countClass].getRow();
                    int col = rem[timeRand % countClass].getCol();
                    timeRand++;
                    theoryClasses[row][col] = classesYearTwoTheory[i];
                }
            }

            if (prevVal == count) {
                System.out.println("There are no possible schedule for the given constraints");
                count = 0;
            }

            prevVal = count;
        }
    }

    private static void assignFirstHourYearTwo(String[][] theoryClasses, boolean[][] isBooked) {
        boolean[] isDayAssigned = new boolean[days.length];


        int count = 0;
        // using while loop we assign classes to the first hour until there are no more days left
       
    
        int timeRand = (int)(Math.random() * ( 5 - 0)) + 0;
        int subRand = (int)(Math.random() * (classesYearTwoAssignedTheory.length - 1 - 0)) + 0;
        while(count != 5) {

            // System.out.println("S" + count);
            
            if(classesYearTwoEvenSemesterHoursRequiredTheory[subRand % (classesYearTwoAssignedTheory.length - 1)] == 0) {
                subRand++; // concept of Ageing.
                continue;
            }

            theoryClasses[0][timeRand % 5] = classesYearTwoTheory[subRand % (classesYearTwoAssignedTheory.length - 1)];

            isDayAssigned[timeRand % 5] = classesYearTwoAssignedTheory[subRand % (classesYearTwoAssignedTheory.length - 1)] = true;

            //decraese the number of classes required by 1
            classesYearTwoEvenSemesterHoursRequiredTheory[subRand % (classesYearTwoEvenSemesterHoursRequiredTheory.length - 1)]--;

            timeRand++;
            subRand++;
            count++;
        }
    }

    private static void assignFirstHourYearThree(String[][] theoryClasses, boolean[][] isBooked) {
        boolean[] isDayAssigned = new boolean[days.length];

        int count = 0;
        // using while loop we assign classes to the first hour until there are no more days left
        
        int timeRand = (int)(Math.random() * ( 5 - 0)) + 0;
        int subRand = (int)(Math.random() * (classesYearThreeEvenSemesterTheory.length - 1 - 0)) + 0;
        while(count != 5) {

            // System.out.println("S" + count);
            
            if(classesYearThreeEvenSemesterHoursRequiredTheory[subRand % (classesYearThreeEvenSemesterTheory.length - 1)] == 0) {
                subRand++; // concept of Ageing.
                continue;
            }

            theoryClasses[0][timeRand % 5] = classesYearThreeEvenSemesterTheory[subRand % (classesYearThreeEvenSemesterTheory.length - 1)];

            isDayAssigned[timeRand % 5] = classesYearThreeEvenSemesterAssignedTheory[subRand % (classesYearThreeEvenSemesterTheory.length - 1)] = true;

            //decraese the number of classes required by 1
            classesYearThreeEvenSemesterHoursRequiredTheory[subRand % (classesYearThreeEvenSemesterTheory.length - 1)]--;

            timeRand++;
            subRand++;
            count++;
        }
    }

    private static void assignFirstHourYearFour(String[][] theoryClasses, boolean[][] isBooked) {
        boolean[] isDayAssigned = new boolean[days.length];

        int count = 0;
        int timeRand = (int)(Math.random() * ( 5 - 0)) + 0;
        int subRand = (int)(Math.random() * (classesYearFourEvenSemesterAssignedTheory.length - 1 - 0)) + 0;
        while(count != 5) {

            // System.out.println("S" + count);
            
            if(classesYearFourEvenSemesterHoursRequiredTheory[subRand % (classesYearFourEvenSemesterHoursRequiredTheory.length - 1)] == 0) {
                subRand++; // concept of Ageing.
                continue;
            }

            theoryClasses[0][timeRand % 5] = classesYearFourEvenSemesterTheory[subRand % (classesYearFourEvenSemesterTheory.length - 1)];

            isDayAssigned[timeRand % 5] = classesYearFourEvenSemesterAssignedTheory[subRand % (classesYearFourEvenSemesterAssignedTheory.length - 1)] = true;

            //decraese the number of classes required by 1
            classesYearFourEvenSemesterHoursRequiredTheory[subRand % (classesYearFourEvenSemesterHoursRequiredTheory.length - 1)]--;

            timeRand++;
            subRand++;
            count++;
        }
    }

    private static boolean isClassSlotBooked(boolean[][] isBooked, int i, int j) {
        return isBooked[i][j];
    }

    private static void assignTheoryClassesYearTwo(String[][] theoryClasses, boolean[][] isBooked) {
        for(int i = 1; i < 4; i++) {
            int timeRand = (int)(Math.random() * ( 5 - 0)) + 0;
            int subRand = (int)(Math.random() * (classesYearTwoAssignedTheory.length - 1 - 0)) + 0;
            for (int j = 0; j < 4; j++) {
                // if(isClassSlotBooked(isBooked, i, j)) { //the class slot is booked, we cannot do anything
                //     //do nothing
                // }
                // else { //assign the classes as per the schedule and time slots available
                    if(classesYearTwoEvenSemesterHoursRequiredTheory[subRand % (classesYearTwoAssignedTheory.length - 1)] == 0) {
                        subRand++; // concept of Ageing.
                        continue;
                    }
        
                    theoryClasses[i][timeRand % 5] = classesYearTwoTheory[subRand % (classesYearTwoAssignedTheory.length - 1)];
        
                    isBooked[i][timeRand % 5] = classesYearTwoAssignedTheory[subRand % (classesYearTwoAssignedTheory.length - 1)] = true;    

                    //decraese the number of classes required by 1
                    classesYearTwoEvenSemesterHoursRequiredTheory[subRand % (classesYearTwoEvenSemesterHoursRequiredTheory.length - 1)]--;

                    timeRand++;
                    subRand++;
                }
            
        }
    }

    private static void assignTheoryClassesYearThree(String[][] theoryClasses, boolean[][] isBooked) {
        for(int i = 1; i < 4; i++) {
            int timeRand = (int)(Math.random() * ( 5 - 0)) + 0;
            int subRand = (int)(Math.random() * (classesYearThreeEvenSemesterTheory.length - 1 - 0)) + 0;
            for (int j = 0; j < 4; j++) {
                // if(isClassSlotBooked(isBooked, i, j)) { //the class slot is booked, we cannot do anything
                //     //do nothing
                // }
                // else { //assign the classes as per the schedule and time slots available
                    if(classesYearThreeEvenSemesterHoursRequiredTheory[subRand % (classesYearThreeEvenSemesterTheory.length - 1)] == 0) {
                        subRand++; // concept of Ageing.
                        continue;
                    }
        
                    theoryClasses[i][timeRand % 5] = classesYearThreeEvenSemesterTheory[subRand % (classesYearThreeEvenSemesterTheory.length - 1)];
        
                    isBooked[i][timeRand % 5] = classesYearThreeEvenSemesterAssignedTheory[subRand % (classesYearThreeEvenSemesterAssignedTheory.length - 1)] = true;    

                    //decraese the number of classes required by 1
                    classesYearThreeEvenSemesterHoursRequiredTheory[subRand % (classesYearThreeEvenSemesterHoursRequiredTheory.length - 1)]--;

                    timeRand++;
                    subRand++;
                }
            
        }
    }

    private static void assignTheoryClassesYearFour(String[][] theoryClasses, boolean[][] isBooked) {
        for(int i = 1; i < 4; i++) {
            int timeRand = (int)(Math.random() * ( 5 - 0)) + 0;
            int subRand = (int)(Math.random() * (classesYearFourEvenSemesterTheory.length - 1 - 0)) + 0;
            for (int j = 0; j < 4; j++) {
                // if(isClassSlotBooked(isBooked, i, j)) { //the class slot is booked, we cannot do anything
                //     //do nothing
                // }
                // else { //assign the classes as per the schedule and time slots available
                    if(classesYearTwoEvenSemesterHoursRequiredTheory[subRand % (classesYearFourEvenSemesterTheory.length - 1)] == 0) {
                        subRand++; // concept of Ageing.
                        continue;
                    }
        
                    theoryClasses[i][timeRand % 5] = classesYearFourEvenSemesterTheory[subRand % (classesYearFourEvenSemesterTheory.length - 1)];
        
                    isBooked[i][timeRand % 5] = classesYearFourEvenSemesterAssignedTheory[subRand % (classesYearFourEvenSemesterTheory.length - 1)] = true;    

                    //decraese the number of classes required by 1
                    classesYearFourEvenSemesterHoursRequiredTheory[subRand % (classesYearFourEvenSemesterHoursRequiredTheory.length - 1)]--;

                    timeRand++;
                    subRand++;
                }
            
        }
    }

    private static void assignLabClasses(String[] labTechnicians, String[] teacher, int choice) {
        //using a for loop, we assign the lab technicians with their respective laboratory and assign a day in sequence
        if(choice == 0) { //we generate for group A
            for (int i = 0; i < labTechnicians.length; i++) {
                int timeRand = (int)(Math.random() * 10);
                if(timeRand <= 5) timeRand = 5;
                if(timeRand >= 6) timeRand = 6;
                System.out.println(labTechnicians[i] + " " + classesYearTwoPracticalClass[i] + " " + classesYearTwoPractical[i] + " " + days[i] + " Time: " + time[timeRand] + "-" + time[timeRand + 3]);
            }
        }
        else { // we generate for group B
            for (int i = 0; i < labTechnicians.length; i++) {
                int timeRand = (int)(Math.random() * 10);
                if(timeRand <= 5) timeRand = 5;
                if(timeRand >= 6) timeRand = 6;
                System.out.println(labTechnicians[labTechnicians.length - i - 1] + " " + classesYearTwoPracticalClass[labTechnicians.length - i - 1] + " " + classesYearTwoPractical[labTechnicians.length - i - 1] + " " + days[i] + " Time: " + time[timeRand] + "-" + time[timeRand + 3]);
            }
        }
        
    }

    private static final String firstTime = "10:00";
    private static final String[] time = {firstTime, "10:50", "11:40", "12:30", "1:20", "2:10", "3:00", "3:50", "4:40", "5:30"};
    private static final String recesses = time[4] + "-" + time[5];

    
    static int count = 0;
    static int countMaster = 0;

 

}

class facultySub {
    Map<Integer, List<String>> map = new HashMap<Integer, List<String>>();

    facultySub(int year, String subject) {
        List <String> list = new ArrayList<>();
        //check if the map is emoty or not
        //if the map is empty create a new map; otherwise loop through the value and update it
        
        if(map.isEmpty()) {
            list.add(subject);
            map.put(year, list);
        } else {
            for(Map.Entry m : map.entrySet()) {
                if((int)m.getKey() == year) {
                    list = (List<String>)m.getValue();
                    list.add(subject);
                    map.put(year, list);
                    break;
                }
            }
        }
    }
}

class classD {

    String classes;
    String time;
    String facultyName;
    String day;
    boolean isLab;
    int creditTh;
    int creditLb; // to be set whenever the lab classes are present

    public classD() {
        classes = time = facultyName = day = "";
        isLab = false;
        creditLb = creditTh = 0;
    }

    public String getClasses() {
        return classes;
    }

    public void setClasses(String classes) {
        this.classes = classes;
    }

    public String getTime() {
        return time;
    }

    public void setTime(String time) {
        this.time = time;
    }

    public String getFaculty() {
        return facultyName;
    }

    public void setFaculty(String facultyName) {
        this.facultyName = facultyName;
    }


    public int getCreditTh() {
        return creditTh;
    }

    public void setCreditTh(int creditTh) {
        this.creditTh = creditTh;
    }

    public int getCreditLb() {
        return creditLb;
    }

    public void setCreditLb(int creditLb) {
        this.creditLb = creditLb;
    }

    public boolean isLabPresent() {
        return isLab;
    }

    public void setLabPresent(boolean isLab) {
        this.isLab = isLab;
    }

    public String getDay() {
        return day;
    }

    public void setDay(String day) {
        this.day = day;
    }

    public classD(String classes, String time, String facultyName, String day, boolean isLab, int creditTh, int creditLb) {
        setClasses(classes);
        setDay(day);
        setFaculty(facultyName);
        setTime(time);
        setLabPresent(isLab);
        setCreditTh(creditTh);
        if(isLab) setCreditLb(creditLb);
    }

    public String getData() {
        return getClasses() + " " + getFaculty() + " " + getTime() + " " + getDay();
    }
}

class time {
    int[] day = new int[5];
    boolean[][] slot = new boolean[5][8];
    boolean noOffDay;

    time() {
        noOffDay = false;
    }
    
    time(boolean noOffDay) {
        //slot1 = slot2 = slot3 = slot4 = slot5 = slot6 = slot7 = slot8 = 0;
        this.noOffDay = noOffDay;
    }

    time(int i) {
        day[i] = -1; // to indicate that the day is off
    }

    public boolean getOffDay() {
        return noOffDay;
    }

    public int getDay(int i) {
        return day[i];
    }

    public void bookSlot(int i, int j) {
        slot[i][j] = true;
    }

    public void unbookSlot(int i, int j) {
        slot[i][j] = false;
    }

    public boolean getSlot(int i, int j) {
        return slot[i][j];
    }
}

class remclass {
    int i;
    int j;
    public remclass(int i, int j) {
        this.i = i;
        this.j = j;
    }

    public int getRow(){ return i;}

    public int getCol() {return j;}
}