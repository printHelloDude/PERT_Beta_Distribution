import math

tasks = {}  # Dictionary to store tasks
total_duration = 0  # Total task duration
sum_variances = 0  # Sum of task deviations

while True:
    task_title = input("Enter the task title (or 'q' to quit): ")
    if task_title == 'q':
        break

    tasks[len(tasks) + 1] = {'title': task_title}

    analysis_type = input("Enter the analysis type (three or two point): ")
    if analysis_type not in ['three', 'two']:
        print("Invalid analysis type. Please try again.")
        continue

    while True:
        try:
            optimistic = int(input("Enter the optimistic estimate in minutes (O): "))
            pessimistic = int(input("Enter the pessimistic estimate in minutes (P): "))

            if pessimistic < optimistic:
                print("Error: Pessimistic estimate cannot be less than the optimistic estimate.")
                continue

            if analysis_type == 'three':
                most_likely = int(input("Enter the most likely estimate in minutes (M): "))

            break
        except ValueError:
            print("Invalid input. Please enter integer values and try again.")

    if analysis_type == 'three':
        duration = round((optimistic + 4 * most_likely + pessimistic) / 6)
    else:
        duration = round((3 * optimistic + 2 * pessimistic) / 5)

    tasks[len(tasks)]['duration'] = duration
    tasks[len(tasks)]['deviation'] = round((pessimistic - optimistic) / 6, 1)

    # Update total duration and sum of variances
    total_duration += duration
    sum_variances += tasks[len(tasks)]['deviation']

# Square the sum of variances
sum_variances_squared = sum_variances ** 2

# Calculate project time
project_time = total_duration + 2 * math.sqrt(sum_variances_squared)

# Display task sheet
print("\nTask Sheet:")
print("------------")
for task_num, task in tasks.items():
    print(f"Task {task_num}: {task['title']} - Duration: {task['duration']} minutes, Deviation: +/- {task['deviation']:.1f} minutes")

# Display project time
print(f"\nProject Time: {project_time} minutes")

# Ask if user wants to quit
quit_prompt = input("\nDo you want to quit? (yes/no): ")
if quit_prompt.lower() == "yes":
    print("Goodbye!")
else:
    print("Continuing...")
