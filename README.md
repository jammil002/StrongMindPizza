# Pizza Management Web Application

## Introduction

This is my submission to the StrongMind team.

## Deployment

The Pizza Management Web Application is deployed and accessible on Heroku. Visit the application using the following link: [https://strongmind-jamesmiller-b3814733338c.herokuapp.com/](https://strongmind-jamesmiller-b3814733338c.herokuapp.com/).

## Live Demo

I created a loom video that quickly goes over each of the points here: [Loom Video Link](https://www.loom.com/share/950154332aca4250acea16b3a2428b80).

## Getting Started

These instructions will guide you through setting up and running the application locally for development and testing purposes.

### Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.x
- Flask

### Installation

Follow these steps to get your development environment running:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/pizza-management-app.git
   cd pizza-management-app
   ```

2. **Set up a virtual environment (Optional):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**

   ```bash
   flask run
   ```

   Access the application at `http://127.0.0.1:5000/`.

### Testing the Application Locally

1. **Flask Debug Mode**:
    - Flask provides a convenient debug mode that automatically reloads the application when changes are made to the source code. To enable debug mode:
        ```bash
        export FLASK_ENV=development
        ```
    - Run the Flask application:
        ```bash
        flask run
        ```
    - With debug mode enabled, any changes made to the source code will trigger an automatic reload of the application, making it easy to see the effects of code modifications in real-time.

2. **Testing Each Portion of the App**:
    - **Home Page**: 
        - Open a web browser and navigate to `http://localhost:5000` (or the appropriate URL where the Flask application is running).
        - Verify that the home page loads successfully and displays the expected content.

    - **Manage Pizzas**:
        - Navigate to `http://localhost:5000/pizza`.
        - Add a new pizza by entering a name and selecting toppings, then click the "Add/Update Pizza" button.
        - Verify that the pizza is added to the list of pizzas.

    - **Delete Pizza**:
        - On the "Manage Pizzas" page (`http://localhost:5000/pizza`), click the "Delete" link next to a pizza.
        - Verify that the pizza is successfully deleted from the list.

    - **Manage Toppings**:
        - Navigate to `http://localhost:5000/toppings`.
        - Add a new topping by entering its name in the form field and submitting the form.
        - Verify that the new topping is added to the list of available toppings.

    - **Delete Topping**:
        - On the "Manage Toppings" page (`http://localhost:5000/toppings`), click the "Delete" link next to a topping.
        - Verify that the topping is successfully deleted from the list.

3. **Error Handling**:
    - To test error handling, you can intentionally navigate to a non-existent page (e.g., `http://localhost:5000/nonexistent-page`) and verify that the custom error page is displayed.

By following these steps, you can thoroughly test each portion of the Flask application locally to ensure that it functions as expected.

