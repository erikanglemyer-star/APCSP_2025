import random

question_bank = [
    {
        "question": "What is the pandas library primarily designed for?",
        "options": [
            "A) Web development and server management",
            "B) Data manipulation and analysis",
            "C) Machine learning model training",
            "D) Network security and encryption"
        ],
        "answer": "B",
        "explanation": "pandas is a powerful open-source tool designed for data manipulation and analysis."
    },
    {
        "question": "Which two high-level data structures does pandas provide?",
        "options": [
            "A) List and Dictionary",
            "B) Array and Matrix",
            "C) DataFrame and Series",
            "D) Table and Column"
        ],
        "answer": "C",
        "explanation": "pandas provides the DataFrame and Series data structures for handling structured data."
    },
    {
        "question": "What Python library is pandas built on top of?",
        "options": [
            "A) Matplotlib",
            "B) SciPy",
            "C) Seaborn",
            "D) NumPy"
        ],
        "answer": "D",
        "explanation": "pandas is built on top of NumPy, which allows it to offer fast and efficient operations on large datasets."
    },
    {
        "question": "Which of the following file formats can pandas work with? (Choose the most complete answer)",
        "options": [
            "A) CSV and Excel only",
            "B) CSV, Excel, SQL databases, and JSON",
            "C) JSON and XML only",
            "D) SQL databases and CSV only"
        ],
        "answer": "B",
        "explanation": "pandas can work with CSV, Excel, SQL databases, and JSON files seamlessly."
    },
    {
        "question": "What plotting libraries does pandas integrate with for visualizations?",
        "options": [
            "A) Plotly and Bokeh",
            "B) D3.js and Chart.js",
            "C) Matplotlib and Seaborn",
            "D) Altair and Vega"
        ],
        "answer": "C",
        "explanation": "pandas integrates with Matplotlib and Seaborn for generating visualizations."
    },
    {
        "question": "Why is memory management especially important when working with large datasets in Python?",
        "options": [
            "A) Python automatically optimizes all memory usage",
            "B) Large data operations can involve gigabytes or terabytes of data, making optimization essential",
            "C) Memory management only matters for small datasets",
            "D) Python has unlimited memory by default"
        ],
        "answer": "B",
        "explanation": "In large data processing, operations may involve gigabytes or terabytes of data, making memory optimization essential."
    },
    {
        "question": "Which of the following is a technique to reduce memory overhead when working with large data?",
        "options": [
            "A) Using less efficient data types",
            "B) Avoiding the use of any libraries",
            "C) Using more memory-efficient data types and libraries like pandas and NumPy",
            "D) Loading all data into memory at once"
        ],
        "answer": "C",
        "explanation": "Using memory-efficient data types and leveraging pandas and NumPy can significantly reduce memory overhead."
    },
    {
        "question": "What does a memory leak lead to in data-intensive applications?",
        "options": [
            "A) Faster processing speeds",
            "B) Performance degradation or application crashes",
            "C) Improved data accuracy",
            "D) Better memory allocation"
        ],
        "answer": "B",
        "explanation": "Memory leaks can lead to performance degradation or even application crashes."
    },
    {
        "question": "Which pandas function is used to read large CSV files?",
        "options": [
            "A) pandas.load_csv()",
            "B) pandas.import_csv()",
            "C) pandas.read_csv()",
            "D) pandas.open_csv()"
        ],
        "answer": "C",
        "explanation": "The read_csv() function in pandas is used to read CSV files efficiently."
    },
    {
        "question": "What parameter in read_csv() allows you to read a large file in smaller pieces?",
        "options": [
            "A) filesize",
            "B) chunksize",
            "C) batchsize",
            "D) blocksize"
        ],
        "answer": "B",
        "explanation": "The chunksize parameter in read_csv() determines the number of rows to be read into a DataFrame at a time."
    },
    {
        "question": "What does specifying the chunksize parameter in read_csv() return?",
        "options": [
            "A) A single large DataFrame",
            "B) A list of all rows",
            "C) An iterable object for processing chunks separately",
            "D) A dictionary of column names"
        ],
        "answer": "C",
        "explanation": "Specifying chunksize returns an iterable object, allowing operations on each chunk separately."
    },
    {
        "question": "Which parameter in read_csv() allows you to load only specific columns?",
        "options": [
            "A) columns",
            "B) select",
            "C) fields",
            "D) usecols"
        ],
        "answer": "D",
        "explanation": "The usecols parameter in read_csv() allows selective loading of only the necessary columns."
    },
    {
        "question": "What is the primary benefit of reading a large CSV file in chunks?",
        "options": [
            "A) It increases the file size",
            "B) It significantly reduces memory usage",
            "C) It slows down the processing speed",
            "D) It converts the file to JSON format"
        ],
        "answer": "B",
        "explanation": "Reading data in chunks significantly reduces memory usage by processing manageable segments at a time."
    },
    {
        "question": "What can garbage collection and memory profiling tools help developers do?",
        "options": [
            "A) Write faster algorithms",
            "B) Identify and mitigate memory-related issues",
            "C) Convert data formats automatically",
            "D) Generate visualizations"
        ],
        "answer": "B",
        "explanation": "Garbage collection and memory profiling tools help developers identify and mitigate memory-related issues."
    },
    {
        "question": "Pandas is described as a 'cornerstone library' because it:",
        "options": [
            "A) Replaces all other Python libraries",
            "B) Only works with small datasets",
            "C) Enhances Python's capabilities as a data analysis tool for simple to complex tasks",
            "D) Is the only library for web scraping"
        ],
        "answer": "C",
        "explanation": "pandas is a cornerstone library that enhances Python's capabilities for data analysis, from simple aggregations to complex transformations."
    }
]


def run_quiz():
    print("=" * 60)
    print("   🐍 Python Tools for Large Data - Quiz Game")
    print("=" * 60)
    print("Get 3 correct answers IN A ROW to win!")
    print("One wrong answer and you start your streak over.\n")

    streak = 0
    used_questions = []

    while streak < 3:
        # Reset used questions if we've gone through them all
        if len(used_questions) == len(question_bank):
            used_questions = []

        # Pick a random question not recently used
        available = [q for i, q in enumerate(question_bank) if i not in used_questions]
        question = random.choice(available)
        used_questions.append(question_bank.index(question))

        print(f"🔥 Streak: {streak}/3")
        print(f"\nQuestion: {question['question']}\n")
        for option in question["options"]:
            print(f"  {option}")

        while True:
            answer = input("\nYour answer (A/B/C/D): ").strip().upper()
            if answer in ["A", "B", "C", "D"]:
                break
            print("Please enter A, B, C, or D.")

        if answer == question["answer"]:
            streak += 1
            print(f"\n✅ Correct! {question['explanation']}")
            if streak < 3:
                print(f"🔥 Streak: {streak}/3 — Keep going!\n")
                print("-" * 60)
        else:
            print(f"\n❌ Incorrect! The correct answer was {question['answer']}.")
            print(f"   {question['explanation']}")
            streak = 0
            print(f"\n😬 Streak reset to 0. Start over!\n")
            print("=" * 60)

    print("\n🏆 Congratulations! You got 3 in a row correct!")
    print("You've mastered Python Tools for Large Data!\n")
    print("=" * 60)
    print("       🎉 YOUR COMPLETION CODE IS: 🎉")
    print()
    print(r"  _    _                    _          ")




    
    print(r" | |  | |                  | |         ")






    print(r" | |__| |  __ _ __      __ | | __  ___ ")






    print(r" |  __  | / _` |\ \ /\ / / | |/ / / __|")






    print(r" | |  | || (_| | \ V  V /  |   <  \__ \ ")






    print(r" |_|  |_| \__,_|  \_/\_/   |_|\_\ |___/")
    print()
    print("=" * 60)


if __name__ == "__main__":
    play_again = "y"
    while play_again.lower() == "y":
        run_quiz()
        play_again = input("Play again? (y/n): ").strip().lower()

    print("\nThanks for playing! Keep learning Python! 🐍")
