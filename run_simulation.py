import json
import time # Import the time library
from ncck_engine import NCCK

# Initialize the NCCK kernel
ncck = NCCK()

# Initialize a list to store processing times for each case
total_processing_times = []

# ✅ Adjustment here: Change the file name to read newly generated cases
with open("large_test_cases.json", "r", encoding="utf-8") as f:
    cases = json.load(f)

full_results = []
simulation_log = []

print("🚀 Starting NCCK simulation and performance analysis...")
overall_start_time = time.time() # Record overall simulation start time

# Run each case through the NCCK kernel
for i, case in enumerate(cases):
    case_process_start_time = time.time() # Record case processing start time
    result = ncck.assess(case)
    case_process_end_time = time.time() # Record case processing end time
    
    # Calculate processing time in milliseconds
    processing_time_ms = (case_process_end_time - case_process_start_time) * 1000
    total_processing_times.append(processing_time_ms)

    # Include original case data and processing time in full results
    case_result = {
        "id": case["id"],
        **result,
        "original_goal": case['goal'],
        "original_human_impact": case['human_impact'],
        "original_source": case['source'],
        "original_context": case['context'],
        "processing_time_ms": processing_time_ms # Add new speed metric here
    }
    full_results.append(case_result)
    
    # Log a summary of the decision to the log
    simulation_log.append(f"Case {case['id']}: Goal '{case['goal']}' - Decision: {'Approved' if result['approved'] else 'Rejected'} - Time: {processing_time_ms:.2f} ms")

    if (i + 1) % 1000 == 0: # Print progress every 1000 cases
        print(f"✅ Processed {i + 1} cases...")

overall_end_time = time.time() # Record overall simulation end time
total_simulation_time_seconds = overall_end_time - overall_start_time

# --- Calculate and analyze performance metrics ---
num_cases_processed = len(cases)
avg_processing_time_ms = sum(total_processing_times) / num_cases_processed if num_cases_processed > 0 else 0
min_processing_time_ms = min(total_processing_times) if num_cases_processed > 0 else 0
max_processing_time_ms = max(total_processing_times) if num_cases_processed > 0 else 0

# (Optional) You can calculate standard deviation if you have numpy installed
# import numpy as np
# std_dev_processing_time_ms = np.std(total_processing_times) if num_cases_processed > 0 else 0

performance_summary = {
    "total_cases_processed": num_cases_processed,
    "total_simulation_time_seconds": total_simulation_time_seconds,
    "average_case_processing_time_ms": avg_processing_time_ms,
    "min_case_processing_time_ms": min_processing_time_ms,
    "max_case_processing_time_ms": max_processing_time_ms,
    # "std_dev_case_processing_time_ms": std_dev_processing_time_ms # Add this if you use numpy
}

# Save full results to a JSON file
with open("full_results.json", "w", encoding="utf-8") as f:
    json.dump(full_results, f, indent=2, ensure_ascii=False)

# Save simulation log (use 'w' to start with an empty file then append)
with open("simulation_log.txt", "w", encoding="utf-8") as f: 
    for entry in simulation_log:
        f.write(entry + "\n")
    
    f.write("\n--- Performance Summary ---\n")
    for key, value in performance_summary.items():
        f.write(f"{key.replace('_', ' ').title()}: {value:.4f}\n") # Better formatting for printing

# Save performance summary to a separate JSON file for easier analysis
with open("performance_summary.json", "w", encoding="utf-8") as f:
    json.dump(performance_summary, f, indent=2, ensure_ascii=False)

print("\n--- Performance Summary ---")
for key, value in performance_summary.items():
    print(f"{key.replace('_', ' ').title()}: {value:.4f}")

print(f" Simulation complete. Results saved to 'full_results.json', 'simulation_log.txt', and 'performance_summary.json'.")
print(f"Processed {len(cases)} test cases.")
