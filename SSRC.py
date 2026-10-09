student_data = {
"id1": {"name": "John", "class": "8A", "subject": "Math"},
"id2": {"name": "Mary", "class": "8B", "subject": "Science"},
"id3": {"name": "David", "class": "8A", "subject": "English"},
"id4": {"name": "John", "class": "8A", "subject": "Math"}
}
print("Original Student Records:")
print(student_data)
print("\nStudent id1:", student_data.get("id1", "Not Found"))
print("Student id5:", student_data.get("id5", "Not Found"))
student_data["id5"] = {
"name": "Sarah",
"class": "8C",
"subject": "History"
}
print("\nAfter Adding Student:")
print(student_data)
student_data["id2"]["subject"] = "Math"
print("\nAfter Updating Student:")
print(student_data)
cleaned_data = {}
seen_records = []
for student_id, details in student_data.items():
    record = (details["name"], details["class"], details["subject"])
    if record not in seen_records:
        seen_records.append(record)
        cleaned_data[student_id] = details
student_data = cleaned_data
print("After removing duplicates:")
print(student_data)
student_data.pop("id4", None)
print("Number of students:", len(student_data))
print("Final Student records:")
for student_id, details in student_data.items():
    print(student_id, ":", details)