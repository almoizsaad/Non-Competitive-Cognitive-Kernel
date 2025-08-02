# NCCK - Non-Competitive Cognitive Kernel: A Biologically Inspired AI Safety Model

[![License: Custom Non-Commercial Research](https://img.shields.io/badge/License-Custom%20Non--Commercial%20Research-blue.svg)](https://github.com/almoizsaad/Non-Competitive-Cognitive-Kernel/blob/master/LICENSE.txt)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.16653515.svg)](https://doi.org/10.5281/zenodo.16653515)

This project implements the core components of the Non-Competitive Cognitive Kernel (NCCK) model, proposed by Almoiz Saad Yousuf Mohamed. NCCK represents a novel approach to AI safety, simulating a non-competitive, ethically-aligned AI reasoning engine. Its design is deeply inspired by cooperative biological systems, such as elephants and other species that exhibit intrinsic mechanisms preventing dominance-driven or exploitative behaviors.

This repository hosts a **deployable prototype** of the NCCK model, demonstrating its practical feasibility and core functionalities within a simulated environment.

## Features

* **Ethical AI Decision Evaluation:** Implements a core mechanism for evaluating AI decisions based on their intrinsic intent and potential impact, rooted in non-competitive principles. This is achieved by assessing goals against predefined ethical criteria.
* **Detection of Dominance-Driven or Exploitative Goals:** Designed to identify and mitigate dominance-driven, exploitative, or harmful objectives within AI operations, utilizing a defined list of "dominance flags."
* **Biologically Inspired Architecture:** Integrates structural constraints and internal determinants inspired by observed non-competitive behaviors in natural systems.
* **Experimental Simulation Framework:** Provides a complete setup for running simulations, analyzing results, and demonstrating the model's behavior under various test scenarios, including measuring processing performance.
* **Automated Results Analysis:** Generates automated visualizations (e.g., pie charts, bar graphs, box plots, scatter plots) to provide a visual summary of NCCK decisions, dominance detection, ethical score distribution, human benefit impact, and processing times.

## Files

* `ncck_engine.py`: Contains the main ethical evaluation logic and the core NCCK model implementation. Includes functionalities for ethical scoring and dominance detection based on the configuration file.
* `ethics_config.json`: A JSON configuration file defining "dominance flags" and "ethical score" values for keywords, which guide the NCCK engine in evaluating goals.
* `generate_cases.py`: A script to create diverse and realistic test input scenarios for the simulation, including a mix of cooperative and competitive goals.
* `run_simulation.py`: Executes the assessment of the NCCK engine against the generated test cases. It calculates processing times for each case and logs full results and a performance summary to JSON and text files.
* `analyze_results.py`: Processes the simulation results from `full_results.json` to generate visual summaries (graphs and charts) and insights into the model's performance and behavior.

## Installation

To get started with the NCCK deployable prototype, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YourUsername/NCCK.git](https://github.com/YourUsername/NCCK.git)
    cd NCCK
    ```
2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

Follow these steps to run the simulation and analyze the results:

1.  **Generate Test Cases:**
    This script prepares the input data for the simulation.
    ```bash
    python generate_cases.py
    ```
2.  **Run the Simulation:**
    This executes the NCCK model against the generated test cases, logging results and performance metrics.
    ```bash
    python run_simulation.py
    ```
3.  **Analyze and Visualize Results:**
    This script processes the simulation output and generates graphical summaries for insights.
    ```bash
    python analyze_results.py
    ```

## License and Use

This code is released under a **Custom Non-Commercial Research License**.

**🔒 You are permitted to:**
* View and study the source code for understanding and learning purposes.
* Use this software exclusively for academic, research, or educational purposes.

**🚫 You are NOT permitted to:**
* Use this software for any commercial purposes.
* Modify or redistribute this software, in part or in whole, without explicit prior written permission from the author.
* Use this model, in part or in whole, in any system intended for deployment, production, or profit-making scenarios.

For special requests, collaboration opportunities, or inquiries regarding alternative licensing for non-academic use, please contact the author directly at: almoiz.mo.yousuf@gmail.com.

