<table>
<thead><tr><th scope="col"><p><span><strong><span>Endpoint</span></strong></span></p></th><th scope="col"><p><span><strong><span>Role</span></strong></span></p></th><th scope="col"><p><span><strong><span>Method</span></strong></span></p></th><th scope="col"><p><span><strong><span>Purpose</span></strong></span></p></th></tr></thead><tbody><tr><td><p><span><var><span>/api/users</span></var></span></p></td><td><p><span><span>No role required</span></span></p></td><td><p><span><var><span>POST</span></var></span></p></td><td><p><span><span>Creates a new user with name, email , password,...etc</span></span></p></td></tr><tr><td><p><span><var><span>/api/users/users/me/</span></var></span></p><p><span><span>&nbsp;</span></span></p></td><td><p><span><span>Anyone with a valid user token</span></span></p></td><td><p><span><var><span>GET</span></var></span></p></td><td><p><span><span>Displays only the current user</span></span></p></td></tr><tr><td><p><span><var><span>/login</span></var></span></p></td><td><p><span><span>Anyone with a valid username and password</span></span></p></td><td><p><span><var><span>POST</span></var></span></p></td><td><p><span><span>Generates access tokens that can be used in other API calls in this project</span></span></p></td></tr>
<tr><td><p><span><var><span>/logout</span></var></span></p></td><td><p><span><span>Anyone has alredy login</span></span></p></td><td><p><span><var><span>POST</span></var></span></p></td><td><p><span><span>Deleting the token from the database for security reasons</span></span></p></td></tr></tbody></table>


#### This project is under Devlopment

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/DigitalMarket_API.git
    ```

2. Navigate to the project directory:

    ```bash
    cd DigitalMarket_API
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Apply database migrations:

    ```bash
    python manage.py migrate
    ```

5. Run the development server:

    ```bash
    python manage.py runserver
    ```

6. Access the API at `http://localhost:8000/`.

---

Feel free to reach out with any questions, feedback, or suggestions!
