from flask import Flask, render_template, request, redirect
import json
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)


RECIPE_FILE = 'data/recipes.json'
KITCHEN_FILE = 'data/kitchen.json'

# Utility functions
def load_data(file_path):
    if not os.path.exists(file_path):
        return []
    with open(file_path, 'r') as f:
        return json.load(f)

def save_data(file_path, data):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

# ROUTES

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recipes', methods=['GET', 'POST'])
def recipes():
    recipes = load_data(RECIPE_FILE)
    if request.method == 'POST':
        title = request.form['title']
        ingredients = request.form['ingredients']
        method = request.form['method']
        recipes.append({'title': title, 'ingredients': ingredients, 'method': method})
        save_data(RECIPE_FILE, recipes)
        return redirect('/recipes')
    return render_template('recipes.html', recipes=recipes)

@app.route('/recipe/<int:id>')
def recipe_detail(id):
    recipes = load_data(RECIPE_FILE)
    if 0 <= id < len(recipes):
        recipe = recipes[id]
        return render_template('recipe_detail.html', recipe=recipe)
    else:
        return "Recipe not found", 404


@app.route('/add-recipe', methods=['GET', 'POST'])
def add_recipe():
    recipes = load_data(RECIPE_FILE)
    if request.method == 'POST':
        title = request.form['title']
        ingredients = request.form['ingredients']
        method = request.form['method']
        recipes.append({'title': title, 'ingredients': ingredients, 'method': method})
        save_data(RECIPE_FILE, recipes)
        return redirect('/recipes')
    return render_template('add_recipe.html')

@app.route('/delete-recipe/<int:index>')
def delete_recipe(index):
    recipes = load_data(RECIPE_FILE)
    if 0 <= index < len(recipes):
        recipes.pop(index)
        save_data(RECIPE_FILE, recipes)
    return redirect('/recipes')

@app.route('/kitchen', methods=['GET', 'POST'])
def kitchen():
    kitchen = load_data(KITCHEN_FILE)
    if request.method == 'POST':
        item = request.form['item']
        kitchen.append(item)
        save_data(KITCHEN_FILE, kitchen)
        return redirect('/kitchen')
    return render_template('kitchen.html', kitchen=kitchen)

@app.route('/add-item', methods=['GET', 'POST'])
def add_item():
    kitchen = load_data(KITCHEN_FILE)
    if request.method == 'POST':
        item = request.form['item']
        kitchen.append(item)
        save_data(KITCHEN_FILE, kitchen)
        return redirect('/kitchen')
    return render_template('add_item.html')

@app.route('/delete-item/<int:index>')
def delete_item(index):
    kitchen = load_data(KITCHEN_FILE)
    if 0 <= index < len(kitchen):
        kitchen.pop(index)
        save_data(KITCHEN_FILE, kitchen)
    return redirect('/kitchen')

@app.route('/suggest', methods=['GET', 'POST'])
def suggest():
    import openai

    suggestion = None  

    if request.method == 'POST':
        kitchen = load_data(KITCHEN_FILE)
        ingredients = ', '.join(kitchen)

        prompt = (
            f"I have the following ingredients: {ingredients}. "
            "Suggest one meal I can make using all or some of them, and explain how to prepare it. "
            "Keep the instructions simple and beginner-friendly."
        )

        try:
            client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful and creative recipe assistant."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=300
            )

            suggestion = response.choices[0].message.content.strip()
        except Exception as e:
            suggestion = f"Error: {str(e)}"

    return render_template('suggest.html', suggestion=suggestion)




if __name__ == '__main__':
    app.run(debug=True)
