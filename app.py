import streamlit as st
from pawpal_system import Owner, Pet, Task, Scheduler

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

st.markdown(
    """
Welcome to the PawPal+ starter app.

This file is intentionally thin. It gives you a working Streamlit app so you can start quickly,
but **it does not implement the project logic**. Your job is to design the system and build it.

Use this app as your interactive demo once your backend classes/functions exist.
"""
)

with st.expander("Scenario", expanded=True):
    st.markdown(
        """
**PawPal+** is a pet care planning assistant. It helps a pet owner plan care tasks
for their pet(s) based on constraints like time, priority, and preferences.

You will design and implement the scheduling logic and connect it to this Streamlit UI.
"""
    )

with st.expander("What you need to build", expanded=True):
    st.markdown(
        """
At minimum, your system should:
- Represent pet care tasks (what needs to happen, how long it takes, priority)
- Represent the pet and the owner (basic info and preferences)
- Build a plan/schedule for a day that chooses and orders tasks based on constraints
- Explain the plan (why each task was chosen and when it happens)
"""
    )

st.divider()

st.subheader("Quick Demo Inputs (UI only)")
owner_name = st.text_input("Owner name", value="Jordan")
pet_name = st.text_input("Pet name", value="Mochi")
species = st.selectbox("Species", ["dog", "cat", "other"])

# Initialize session state for owner
if "owner" not in st.session_state:
    st.session_state.owner = Owner(name=owner_name)
    st.session_state.owner.add_pet(Pet(name=pet_name, species=species))

# Update owner name if changed
st.session_state.owner.name = owner_name

# Ensure pet exists and update if changed
if not st.session_state.owner.pets:
    st.session_state.owner.add_pet(Pet(name=pet_name, species=species))
else:
    st.session_state.owner.pets[0].name = pet_name
    st.session_state.owner.pets[0].species = species

st.markdown("### Tasks")
st.caption("Add a few tasks. In your final version, these should feed into your scheduler.")

col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    task_title = st.text_input("Task title", value="Morning walk")
with col2:
    duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
with col3:
    priority = st.selectbox("Priority", ["low", "medium", "high", "urgent"], index=2)
with col4:
    task_date = st.text_input("Date (YYYY-MM-DD)", value="2026-04-03")
with col5:
    task_time = st.text_input("Time (HH:MM)", value="07:00")

frequency = st.selectbox("Frequency", ["once", "daily", "weekly"], index=1)

if st.button("Add task"):
    task = Task(
        title=task_title,
        date=task_date,
        time=task_time,
        duration_minutes=int(duration),
        priority=priority,
        frequency=frequency
    )
    if st.session_state.owner.pets:
        st.session_state.owner.pets[0].add_task(task)
        st.success(f"Task '{task_title}' added to {pet_name}!")
    else:
        st.error("No pet found to add task to.")

# Display current tasks
if st.session_state.owner.pets and st.session_state.owner.pets[0].tasks:
    st.write("Current tasks:")
    task_data = [
        {
            "Title": t.title,
            "Date": t.date,
            "Time": t.time,
            "Duration": f"{t.duration_minutes} min",
            "Priority": t.priority,
            "Frequency": t.frequency,
            "Completed": "✓" if t.completed else "○"
        }
        for t in st.session_state.owner.pets[0].get_tasks()
    ]
    st.table(task_data)
else:
    st.info("No tasks yet. Add one above.")

st.divider()

st.subheader("Build Schedule")
st.caption("This button should call your scheduling logic once you implement it.")

if st.button("Generate schedule"):
    scheduler = Scheduler()
    schedule = scheduler.generate_schedule(st.session_state.owner)
    
    if schedule:
        st.write("Generated Schedule:")
        schedule_data = [
            {
                "Title": t.title,
                "Date": t.date,
                "Time": t.time,
                "Duration": f"{t.duration_minutes} min",
                "Priority": t.priority,
                "Completed": "✓" if t.completed else "○"
            }
            for t in schedule
        ]
        st.table(schedule_data)
        
        explanation = scheduler.build_explanation(schedule)
        st.text_area("Schedule Explanation", value=explanation, height=200)
        
        conflicts = scheduler.detect_conflicts(schedule)
        if conflicts:
            for conflict in conflicts:
                st.warning(conflict)
        else:
            st.success("No conflicts detected.")
    else:
        st.info("No tasks to schedule.")
