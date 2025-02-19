import matplotlib.pyplot as plt
import textwrap

# Data
tasks = ['Create an assignment', 'View submissions', 'Edit a rubric', 'Grade an assignment',
         'Submit an assignment', 'Filter assignments', 'View assignment rubric and feedback']
difficulty_scores = [1.1875, 1.0, 1.0625, 1.5, 1.1875, 1.0625, 1.125]
difficulty_labels = ['Easy', 'Easy', 'Easy', 'Easy-Medium', 'Easy', 'Easy', 'Easy']

# Create the bar chart
fig, ax = plt.subplots(figsize=(12, 6))
bar_colors = ['#4CAF50' if label == 'Easy' else '#FF9800' for label in difficulty_labels]
bars = ax.bar(tasks, difficulty_scores, color=bar_colors)

# Set the y-axis range from 0 to 3
ax.set_ylim(1, 3)

# Add labels and title
ax.set_xlabel('Tasks', fontsize=20)
ax.set_ylabel('Difficulty Score', fontsize=22)
ax.set_title('Task Difficulty Scores', fontsize=26, fontweight='bold')

# Add difficulty labels to the bars
for bar, label in zip(bars, difficulty_labels):
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), label,
            ha='center', va='bottom', fontsize=20)

# Wrap the x-axis labels
wrapped_tasks = ['\n'.join(textwrap.wrap(task, width=15)) for task in tasks]
plt.xticks(range(len(tasks)), wrapped_tasks, fontsize=14, rotation=0, ha='center')

# Adjust the layout to separate the x-axis labels
plt.subplots_adjust(bottom=0.25)

# Adjust the layout and display the chart
plt.tight_layout()
plt.show()