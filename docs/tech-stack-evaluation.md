# Tech Stack Evaluation

## Project
Personalized Skincare Ingredient Compatibility Assessment System Using Machine Learning

## Requirements that drive the decision
- FR1: The system shall analyse a user's facial image to classify skin condition.
- FR2: The system shall extract skincare ingredients from an uploaded product image using OCR.
- FR3: The system shall assess ingredient compatibility based on the detected skin condition.
- NFR1: The system shall protect user information and uploaded images.
- NFR2: The system shall provide results within a reasonable processing time.

## Options
- Option A: [for example: static website (HTML and JavaScript) on GitHub Pages]
- Option B: [for example: Python web app (Flask) with a database on a cloud host]
- Option C: [your own idea]

## Decision matrix
Weight: how important the criterion is for YOUR project (1 = low, 5 = high).
Score: how well each option does (1 = poor, 5 = excellent).
Weighted score = weight x score. Add them up for each option.

| Criterion                          | Weight | A score | B score | C score |
|------------------------------------|--------|---------|---------|---------|
| Fits my requirements               | 5      | 3       | 5       | 3       |
| Skills I already have              | 4      | 5       | 3       | 4       |
| Time to build before my deadline   | 4      | 5       | 3       | 4       |
| Free hosting and tools             | 3      | 5       | 3       | 2       |
| Performance and security needs     | 4      | 4       | 4       | 2       |
| Room to grow later                 | 2      | 2       | 4       | 1       |
| **Total (weighted)**               |        | **90**  | **82**  | **63**  |

## Decision record

- **Context:** The project requires a web application, image processing, machine learning, OCR and a database. Development time, existing programming skills and hosting costs are important constraints.

- **Decision:** Option B — PHP web application with MySQL database and Python Flask API for machine learning.

- **Reasons:**
  1. PHP and MySQL support the web application and data management requirements.
  2. Python Flask supports machine learning, image processing and OCR.
  3. Separating the web application from the AI service makes development and maintenance easier.

- **Consequences:** The system can manage user interactions and records through PHP and MySQL, while Flask handles AI processing. However, integrating and deploying two environments requires additional configuration.

- **Risks and next review:** AI processing may be slow, and hosting services may have resource limits or charges. I will review performance, security and deployment requirements after implementing the main system modules.