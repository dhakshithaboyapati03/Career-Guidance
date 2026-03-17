name = input("Enter your name: ")
skill = input("Enter your main interest (technology / biology / business / creativity): ")

print("\nAI Career Guidance Result for", name)

if skill == "technology":
    print("\nRecommended Career: Software Engineer")
    print("Suitable Stream: MPC")
    print("Courses: B.Tech Computer Science, BCA, Python Programming")

    print("\nRecommended Career: Data Scientist")
    print("Suitable Stream: MPC")
    print("Courses: B.Sc Data Science, Machine Learning")

elif skill == "biology":
    print("\nRecommended Career: Doctor")
    print("Suitable Stream: BiPC")
    print("Courses: MBBS")

    print("\nRecommended Career: Biotechnologist")
    print("Suitable Stream: MPC or BiPC")
    print("Courses: B.Sc Biotechnology")

elif skill == "business":
    print("\nRecommended Career: Business Analyst")
    print("Suitable Stream: Commerce")
    print("Courses: BBA, MBA")

elif skill == "creativity":
    print("\nRecommended Career: Graphic Designer")
    print("Suitable Stream: Any Stream")
    print("Courses: Graphic Design, UI/UX Design")

else:
    print("Please enter a valid interest.")
