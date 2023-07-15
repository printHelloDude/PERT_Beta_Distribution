import math

while True:
    tasks = {}  # Dictionary to store tasks
    total_duration = 0  # Total task duration
    sum_variances = 0  # Sum of task deviations

    while True:
        task_title = input("Enter the task title (or 'q' to quit): ")
        if task_title == 'q':
            break

        tasks[len(tasks) + 1] = {'title': task_title}

        analysis_type = input("Enter the analysis type (three or two): ")
        if analysis_type not in ['three', 'two']:
            print("Invalid analysis type. Please try again.")
            continue

        while True:
            try:
                optimistic = float(input("Enter the optimistic estimate in hours (O): "))
                pessimistic = float(input("Enter the pessimistic estimate in hours (P): "))

                if pessimistic < optimistic:
                    print("Error: Pessimistic estimate cannot be less than the optimistic estimate.")
                    continue

                if analysis_type == 'three':
                    most_likely = float(input("Enter the most likely estimate in hours (M): "))

                break
            except ValueError:
                print("Invalid input. Please enter numeric values and try again.")

        if analysis_type == 'three':
            duration = (optimistic + 4 * most_likely + pessimistic) / 6
        else:
            duration = (3 * optimistic + 2 * pessimistic) / 5

        tasks[len(tasks)]['duration'] = duration
        tasks[len(tasks)]['deviation'] = (pessimistic - optimistic) / 6

        # Update total duration and sum of variances
        total_duration += duration
        sum_variances += tasks[len(tasks)]['deviation']

    # Calculate project time
    project_time = total_duration + 2 * math.sqrt(sum_variances ** 2)

    # Display task tab
    print("\nTask Sheet:")
    print("------------")
    for task_num, task in tasks.items():
        print(f"Task {task_num}: {task['title']} - Duration: {task['duration']:.2f} hours, Deviation: +/- {task['deviation']:.2f} hours")

    # Display project time
    print(f"\nProject Time: {project_time:.2f} hours")

    # Ask if user wants to quit or reinitialize
    quit_prompt = input("\nDo you want to quit or restart? (q/r): ")
    if quit_prompt.lower() == "q":
        print("Goodbye!")
        break
    elif quit_prompt.lower() == "r":
        print("Restarting...")
        continue
    else:
        print("Invalid input. You need to force close the program.")
        break
