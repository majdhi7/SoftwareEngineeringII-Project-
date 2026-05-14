import os
import shutil

folders = [
    "Week-01-02",
    "Week-03-04",
    "Week-05-06",
    "Week-07-08",
    "Week-09-10",
    "Week-11-12",
    "Week-13-14",
    "Week-15-16",
    "Project"
]

for f in folders:
    os.makedirs(f, exist_ok=True)

# Move Evidences
if os.path.exists("Evidence(0).pdf"): shutil.move("Evidence(0).pdf", "Week-01-02/evidence-1.pdf")
if os.path.exists("Evidence(1).pdf"): shutil.move("Evidence(1).pdf", "Week-03-04/evidence-2.pdf")
if os.path.exists("Evidence(2).pdf"): shutil.move("Evidence(2).pdf", "Week-05-06/evidence-3.pdf")
if os.path.exists("Evidence(3).pdf"): shutil.move("Evidence(3).pdf", "Week-09-10/evidence-4.pdf")

# Move Activity Diagrams to Project
if os.path.exists("ActivityDiagram.png"): shutil.move("ActivityDiagram.png", "Project/diagram.png")
if os.path.exists("ActivityDiagram.drawio"): shutil.move("ActivityDiagram.drawio", "Project/diagram.drawio")

# Create reflection.md files
ref1 = """# Reflection - Week 01-02

## Goals
- Master the HIMMA cycle (Understand -> Practice -> Evidence) to transition from passive learning to active "Asset Building".
- Adopt a "Market Mindset" to ensure all portfolio submissions meet strict corporate delivery standards.

## Reflection
The transition in CPIT-455 from passive memorization to "Evidence-First Thinking" is a welcome challenge. Instead of just aiming to pass an exam, building a portfolio folder as a "Memory of Achievement" provides a tangible way to demonstrate actual software engineering competence. The V1 -> V2 iteration process is particularly encouraging; treating initial failures as a necessary step for improvement removes the pressure of perfection and builds genuine professional discipline.
"""
with open("Week-01-02/reflection.md", "w", encoding="utf-8") as f: f.write(ref1)

ref2 = """# Reflection - Week 03-04

## Goals
- Analyze the failure chain (Fault -> Error -> Failure) to intercept system bugs before they impact the user.
- Select and justify the correct reliability metrics (POFOD, ROCOF, Availability) based on specific system usage profiles.

## Reflection
Exploring dependability as a Socio-Technical System highlights that software does not exist in a vacuum; it operates within complex human and organizational environments. Applying these concepts to local infrastructure like the Nusuk app made the distinction between Reliability and Availability much clearer. Analyzing the Anatomy of a Crash (Fault -> Error -> Failure) was the most valuable takeaway, as it showed how architectural strategies like diversity can intercept an internal error before it becomes a visible system failure.
"""
with open("Week-03-04/reflection.md", "w", encoding="utf-8") as f: f.write(ref2)

ref3 = """# Reflection - Week 05-06

## Goals
- Distinguish between system Reliability (conformance to spec) and Safety (freedom from harm).
- Apply the ALARP principle and use deductive Fault Tree Analysis to build a formal Safety Case.

## Reflection
The "Safety Paradox" discussed this week completely changed my perspective on system design. The idea that a system can be 100% reliable in executing its code but still cause a catastrophic accident if the specification is flawed emphasizes the need for rigorous hazard analysis. Learning to write negative "Shall Not" safety requirements, rather than just functional requirements, proved that in critical systems, defining what a system must never do is just as important as defining what it should do.
"""
with open("Week-05-06/reflection.md", "w", encoding="utf-8") as f: f.write(ref3)

ref4 = """# Reflection - Week 09-10

## Goals
- Master the Resilience Lifecycle: Design systems capable of maintaining critical services during a disruption by implementing the four stages of resilience: Recognition, Resistance, Recovery, and Reinstatement.
- Integrate Sociotechnical Defenses: Apply the "Swiss Cheese" model to system architecture, utilizing diverse, multi-layered technical and human defenses to prevent active failures and latent conditions from aligning.
- Balance Automation and Human Expertise: Architect systems that avoid the "automation trap." I will ensure that operational efficiency does not become so rigid that it eliminates the flexible human expertise required to manage unexpected complex failures.

## Reflection
The transition into Resilience Engineering highlights a critical reality in enterprise architecture: systems will eventually face disruptions they were not explicitly designed to handle. While our earlier focus on Reliability was about avoiding failure, Resilience is about acknowledging failure and designing the system to survive it. Understanding the cycle of Recognition, Resistance, Recovery, and Reinstatement provides a structured framework for survival.

The most profound takeaway from this lecture is the concept of Sociotechnical Resilience. In the IT industry, it is tempting to view humans purely as a source of error. However, the lecture rightly positions human expertise and adaptability as the foundation of true resilience. Over-automating a critical system like the Nusuk App could actually degrade its resilience, as algorithms cannot negotiate complex physical world crises (like crowd crushing) the way trained personnel can.
"""
with open("Week-09-10/reflection.md", "w", encoding="utf-8") as f: f.write(ref4)

# Delete old PDF files and txt files
for file in os.listdir("."):
    if file.endswith(".pdf") or file.endswith(".txt") or file == "extract.py":
        os.remove(file)
