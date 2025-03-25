import streamlit as st
import threading
import time
import tkinter as tk
from tkinter import messagebox
from pushbullet import Pushbullet  # Import the Pushbullet library  

# Function to display the medicine adherence tracker
def medicine_adherence_tracker():
    c1, c2 = st.columns([30, 50])
    c2.title("DoseGuard: Sends Timely Medication Reminders")
    c1.image("logo-removebg-preview.png")


    # User input for medicines
    st.subheader("Enter Prescribed Medicines")
    num_medicines = st.number_input("Enter the number of prescribed medicines:", min_value=1, step=1, value=1)
    medicines = []
    for i in range(num_medicines):
        medicine = st.text_input(f"Medicine {i + 1}:", key=f"medicine_{i}")  # Unique key for medicine input
        medicines.append(medicine.strip())

    # User input for time slots
    st.subheader("Select Time Slots for Medicines")
    time_slots = []
    for i, med in enumerate(medicines):
        st.write(f"For {med}:")
        hour = st.slider(f"Select Hour for {med}:", 0, 23, key=f"{med}_hour")  # Unique key for hour slider
        minute = st.slider(f"Select Minute for {med}:", 0, 59, key=f"{med}_minute")  # Unique key for minute slider
        time_slots.append((hour, minute))

    # Schedule button
    if st.button("Schedule"):
        st.write("Reminders scheduled successfully!")

        # Start thread to schedule reminders
        threading.Thread(target=schedule_reminders, args=(medicines, time_slots), daemon=True).start()  # Added daemon=True

# Function to display pop-up reminders
def show_reminder(message):
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    messagebox.showinfo("Medicine Reminder", message)
    root.destroy()

# Function to send reminder using Pushbullet
def send_pushbullet_reminder(medicine):
    pushbullet_api_key = "o.QO25EKuCfms2sqe9nBpRItB2Z8RmVfHQ"  # Replace with your Pushbullet API key
    pb = Pushbullet(pushbullet_api_key)
    pb.push_note("Medicine Reminder", f"Don't forget to take your {medicine}!")

# Function to continuously check for reminders and display pop-ups
def schedule_reminders(medicines, time_slots):
    while True:
        current_time = time.localtime()
        current_hour = current_time.tm_hour
        current_minute = current_time.tm_min

        print(f"Current time: {current_hour}:{current_minute}")  # Debug print
        for med, slot in zip(medicines, time_slots):
            if current_hour == slot[0] and current_minute == slot[1]:
                print(f"Reminder for {med} triggered.")  # Debug print
                st.warning(f"Don't forget to take your {med}!")  # Show notification in Streamlit
                send_pushbullet_reminder(med)  # Send Pushbullet reminder
                time.sleep(60)  # Wait for 1 minute before checking again to avoid multiple triggers
        time.sleep(10)  # Check every 10 seconds to reduce CPU usage


# Run the application
if __name__ == "__main__":
    medicine_adherence_tracker()
