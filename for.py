students = {
    "male": ["Tom", "Charlie", "Harry", "Frank"],
    "female":["Sarah", "Huda", "Samantha", "Emily", "Elizabeth"]
    }

for key in students.keys():
    for name in students[key]:
        if "h" in name:
            print(name)
