#  My Recipe Book

I absolutely love to cook and **My Recipe Book** is a pantry-themed, AI-powered web app that lets users save, view, and organize recipes — and get intelligent meal suggestions based on what's in their kitchen. Built with Python(Flask), HTML, and CSS, it features a cozy wood-textured UI with animated pantry elements. I use this app to store all of the meals I love to cook, and to figure out what to cook when I'm low on groceries.

Click here to try -->   [![Live Site](https://img.shields.io/badge/live-demo-FF6F61?style=for-the-badge&logo=render&logoColor=white)](https://my-recipe-book-rioq.onrender.com)

---

##  Features

-  Add, view, and delete custom recipes
-  Track ingredients in your virtual kitchen
-  Get AI-powered recipe suggestions based on ingredients (OpenAI API)
-  Pantry-themed UI with a wood-texture background and animated “swinging pantry door”
-  Built with Python, HTML & CSS 

---

## Tech Stack

- Python (Flask)
- HTML + CSS + (Jinja2 templates) + Tailwind CSS ( For Modern UI)
- JSON (as a local datastore)
- OpenAI API (for recipe suggestions)
  

---

## App Walkthrough

https://drive.google.com/file/d/1QoPri3idCMnG9nlKQzDiDrqrSubisWE2/view?usp=sharing

## Note

You’ll need an OpenAI API key to use the meal suggestion feature. Sign up for a free OpenAI account and paste your key in the .env or export it to your terminal session as shown below.

## To Run Locally

1. Clone the repo  

2. Install dependencies
   pip install -r requirements.txt

3. Add OpenAI API key:
    export OPENAI_API_KEY='your-key-here'

4. Run the app
    python app.py
    Open http://127.0.0.1:5000 in your browser.

## Future Enhancements

- Upload recipe images (v2)
- Login/Sign Up (v2)
- Categorize recipes (e.g. breakfast, dinner) (v2)
- Share or print recipes (v2)
- Mobile layout improvements (v2)
- Social element: share recipes with friends or make “cookbooks” from favorites
- Generate shopping list for missing ingredients
- Let users tag recipes by culture (Caribbean, Asian, Mediterranean, etc.)
- Filter AI suggestions by dietary needs (vegetarian, halal, gluten-free)

## License

free to use, remix, and build on.

## Author

Built with love by Riana Battick.
