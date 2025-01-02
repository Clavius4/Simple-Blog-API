# Simple Blog API

A simple Django REST Framework API for managing blog posts. This project is designed to be beginner-friendly and provides basic functionality to create, read, update, and delete (CRUD) blog posts.

## Features
- **CRUD Operations**: Perform operations on blog posts, including creating, retrieving, updating, and deleting.
- **Fields**: Each blog post includes the following fields:
  - `title`: The title of the blog post.
  - `content`: The main content of the blog post.
  - `published_date`: The date the blog post was published.
- **Ease of Use**: No authentication required, making it ideal for learning and quick prototyping.
- **Extensible**: Can be used as a foundation for larger projects.

## Requirements
- Python 3.8+
- Django 4.0+
- Django REST Framework 3.12+

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Clavius4/Simple-Blog-API.git
   cd Simple-Blog-API
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```bash
   python manage.py migrate
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

## API Endpoints

| Method | Endpoint           | Description                     |
|--------|--------------------|---------------------------------|
| GET    | `/posts/`          | Retrieve all blog posts         |
| GET    | `/posts/<id>/`     | Retrieve a specific blog post   |
| POST   | `/posts/`          | Create a new blog post          |
| PUT    | `/posts/<id>/`     | Update an existing blog post    |
| DELETE | `/posts/<id>/`     | Delete a blog post              |

## Example Request

### Create a New Blog Post
```bash
POST /posts/
{
  "title": "My First Post",
  "content": "This is the content of my first post.",
  "published_date": "2023-11-21"
}
```

### Sample Response
```json
{
  "id": 1,
  "title": "My First Post",
  "content": "This is the content of my first post.",
  "published_date": "2023-11-21"
}
```

## Contributing
Contributions are welcome! Feel free to submit a pull request or open an issue to suggest improvements or report bugs.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements
This project is powered by Django and Django REST Framework.
