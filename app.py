import streamlit as st
from pawpal_system import Owner, Pet, Task, Scheduler

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")
st.title("🐾 PawPal+")

# --- Session state ---
if "owner" not in st.session_state:
    st.session_state.owner = Owner("")
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# --- Owner + Pet info ---
st.subheader("Owner & Pet")
col1, col2, col3 = st.columns(3)
with col1:
    owner_name = st.text_input("Owner name", value="Jordan")
with col2:
    pet_name = st.text_input("Pet name", value="Mochi")
with col3:
    species = st.selectbox("Species", ["dog", "cat", "other"])

st.divider()

# --- Add tasks ---
st.subheader("Add a Task")
col1, col2, col3, col4 = st.columns(4)
with col1:
    task_title = st.text_input("Task", value="Morning walk")
with col2:
    task_time = st.time_input("Time", value=None)
with col3:
    duration = st.number_input("Duration (min)", min_value=1, max_value=240, value=30)
with col4:
    frequency = st.selectbox("Frequency", ["daily", "weekly", "once"])

if st.button("Add task"):
    if task_time:
        time_str = task_time.strftime("%I:%M %p").lstrip("0")
        st.session_state.tasks.append({
            "title": task_title,
            "time": time_str,
            "duration_minutes": int(duration),
            "frequency": frequency,
        })
    else:
        st.warning("Please set a time for the task.")

if st.session_state.tasks:
    st.write("Tasks added:")
    st.table([
        {"Task": t["title"], "Time": t["time"], "Duration (min)": t["duration_minutes"], "Frequency": t["frequency"]}
        for t in st.session_state.tasks
    ])
else:
    st.info("No tasks yet. Add one above.")

st.divider()

# --- Generate schedule ---
if st.button("Generate Schedule"):
    owner = st.session_state.owner
    owner.name = owner_name

    pet = Pet(pet_name, species, 0)
    for t in st.session_state.tasks:
        pet.add_task(Task(t["title"], t["time"], t["frequency"], t["duration_minutes"]))

    owner.pets = [pet]
    scheduler = Scheduler(owner)

    # Sorted plan as a table
    plan = scheduler.get_daily_plan()
    st.subheader("Today's Schedule")
    if plan:
        st.table([
            {
                "Status":   "✅ Done" if task.completed else "○ Pending",
                "Time":     task.time,
                "Task":     task.description,
                "Duration": f"{task.duration_minutes} min",
                "Repeat":   task.frequency,
            }
            for task in plan
        ])
    else:
        st.info("No tasks scheduled yet.")

    # Conflict warnings
    st.divider()
    warnings = scheduler.check_conflicts()
    if warnings:
        st.subheader("⚠️ Scheduling Conflicts")
        st.caption("These tasks overlap. Consider adjusting the start time of one of them.")
        for msg in warnings:
            st.warning(msg)
    else:
        st.success("✅ No conflicts — your schedule looks good!")
