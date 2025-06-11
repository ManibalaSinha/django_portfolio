

#  Django Portfolio

A dynamic and responsive **personal portfolio website**, built with **Django**, styled with **Bootstrap**, and designed to showcase your skills, projects, blog entries, and more.

---

##  Key Features

* **Home**, **About**, **Projects**, **Blog**, **Contact** pages
* Admin-managed content: add/edit projects and blog posts via Django Admin
* Responsive design using **Bootstrap 5**
* Blog posts with featured images and tags
* Contact form that sends email messages via SMTP

---

##  Project Structure

```
django_portfolio/
├── portfolio/          ← Main Django app
│   ├── migrations/
│   ├── templates/      ← HTML templates
│   ├── static/         ← CSS, JS, images
│   ├── models.py       ← Data models (Project, BlogPost, etc.)
│   ├── views.py        ← Page rendering logic
│   ├── urls.py         ← App-specific routes
│   └── forms.py        ← Contact/Rich-text forms
├── django_portfolio/   ← Project configuration
│   ├── settings.py
│   ├── urls.py         ← URL routes (includes portfolio app)
│   └── wsgi.py
├── requirements.txt
├── manage.py
└── README.md
```

---

##  Setup & Installation

1. **Clone the repo**

   ```bash
   git clone https://github.com/ManibalaSinha/django_portfolio.git
   cd django_portfolio
   ```

2. **Create a virtual environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   Create a `.env` file and add:

   ```
   SECRET_KEY=your-secret-key
   DEBUG=True
   EMAIL_HOST=...
   EMAIL_PORT=...
   EMAIL_HOST_USER=...
   EMAIL_HOST_PASSWORD=...
   ```

5. **Run migrations**

   ```bash
   python manage.py migrate
   ```

6. **Create a superuser**

   ```bash
   python manage.py createsuperuser
   ```

7. **Run the dev server**

   ```bash
   python manage.py runserver
   ```

   Navigate to [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

---

##  Usage

* **Add content** via Django Admin (`/admin`): projects, blog posts, tags
* **Contact form** on the site sends email to admin email defined in `.env`
* **Tag filtering** and pagination for blog posts

---

##  Extend & Customize

* **Styling**: Add themes with Bootstrap or Tailwind CSS
* **Media uploads**: Enhance your portfolio with project and post imagery
* **Advanced blog**: Add comments, rich text editor, search, categories
* **Deploy**: Use Heroku, Vercel, or DigitalOcean for production hosting

---

##  Testing

Add tests in a `tests/` directory:

```bash
pytest  # or python manage.py test
```

---

##  Contributing

Contributions are welcome! To help:

1. Fork the repo
2. Create a new branch (`git checkout -b feature/xyz`)
3. Commit your work (`git commit -m "Add xyz"`)
4. Push to your branch (`git push origin feature/xyz`)
5. Open a Pull Request

---

##  Contact & License

* **Author**: Manibala Sinha
* **Email**: [manibalasinha1@gmail.com](mailto:manibalasinha1@gmail.com)
* **License**: MIT

