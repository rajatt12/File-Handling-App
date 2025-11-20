import streamlit as st
from pathlib import Path
import os

def readfileandfolder():
    path = Path('')
    items = list(path.rglob('*'))
    return items

def create_file(name, data):
    try:
        p = Path(name)
        if not p.exists() and not p.is_dir():
            with open(p, "w") as fs:
                fs.write(data)
            return "File created successfully."
        else:
            return "This file already exists or is a directory."
    except Exception as err:
        return f"Error occurred: {err}"

def read_file(name):
    try:
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p, 'r') as fs:
                data = fs.read()
            return data
        else:
            return "The file doesn't exist."
    except Exception as err:
        return f"An error occurred: {err}"

def update_file(name, option, new_name=None, data=None):
    try:
        p = Path(name)
        if p.exists() and p.is_file():
            if option == "Rename":
                if new_name:
                    P2 = Path(new_name)
                    p.rename(P2)
                    return f"File renamed to {new_name}."
                else:
                    return "New file name not provided."
            elif option == "Overwrite":
                if data is not None:
                    with open(p, 'w') as fs:
                        fs.write(data)
                    return "File overwritten successfully."
                else:
                    return "No data provided to overwrite."
            elif option == "Append":
                if data is not None:
                    with open(p, 'a') as fs:
                        fs.write(data)
                    return "Data appended successfully."
                else:
                    return "No data provided to append."
        else:
            return "File does not exist."
    except Exception as err:
        return f"An error occurred: {err}"

def delete_file(name):
    try:
        p = Path(name)
        if p.exists() and p.is_file():
            os.remove(p)
            return "File removed successfully."
        else:
            return "No such file exists."
    except Exception as err:
        return f"An error occurred: {err}"

# Streamlit UI
st.title("File Management System")

# Display files and folders
st.subheader("Files and Folders in Current Directory")
items = readfileandfolder()
for i, item in enumerate(items):
    st.text(f"{i+1}: {item}")

operation = st.radio("Choose an operation", ("Create File", "Read File", "Update File", "Delete File"))

if operation == "Create File":
    filename = st.text_input("Enter the file name to create")
    filedata = st.text_area("Enter content for the new file")
    if st.button("Create File"):
        message = create_file(filename, filedata)
        st.success(message)

elif operation == "Read File":
    filename = st.text_input("Enter the file name to read")
    if st.button("Read File"):
        content = read_file(filename)
        st.text_area("File Content", content, height=300)

elif operation == "Update File":
    filename = st.text_input("Enter the file name to update")
    update_option = st.selectbox("Choose update action", ["Rename", "Overwrite", "Append"])
    new_name = None
    data = None
    if update_option == "Rename":
        new_name = st.text_input("Enter the new file name")
    else:
        data = st.text_area("Enter content")

    if st.button("Update File"):
        message = update_file(filename, update_option, new_name, data)
        st.success(message)

elif operation == "Delete File":
    filename = st.text_input("Enter the file name to delete")
    if st.button("Delete File"):
        message = delete_file(filename)
        st.success(message)
