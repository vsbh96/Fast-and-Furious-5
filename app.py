from flask import Flask, render_template, url_for,session,request,redirect,flash
import sqlite3

app = Flask(__name__)
app.secret_key = "secret_key"
DATABASE = "users.db"

#Registration functionality
@app.route("/registration", methods=["GET", "POST"])
def registration():
    if request.method == "POST":
        name = request.form["fullname"]
        email = request.form["email"]
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (email,name,username, password) VALUES (?, ?, ?, ?)", (email, name, username, password))
        conn.commit()
        cursor.close()
        conn.close()
        session["username"] = username
        return redirect(url_for("home"))
    return render_template('registration.html')

#Signin functionality
@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
        user = cursor.fetchone()
        conn.close()
        if user:
            session['username'] = user[1]
            return redirect(url_for('cuisines_loggedin'))
        else:
            flash('Invalid username or password')
    return render_template('index.html')

# Function to check if user is signed in
def is_user_signed_in():
    return "username" in session

#Logout functionality
@app.route('/logout')
def logout():
    # Clear the session data and redirect to the login page
    session.clear()
    return redirect(url_for('home'))


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/cuisines') 
def cuisines():
    return render_template('newcuisines.html')

@app.route('/cuisines_loggedin') 
def cuisines_loggedin():
    username = session.get('username')
    return render_template('newcuisines_loggedin_user.html', username=username)

@app.route('/contactus_loggedin') 
def contactus_loggedin():
    username = session.get('username')
    return render_template('Contact_Us_loggedin_user.html', username=username)

@app.route('/desserts_loggedin') 
def desserts_loggedin():
    username = session.get('username')
    return render_template('desserts_loggedin_user.html', username=username)

@app.route('/search_loggedin') 
def search_loggedin():
    username = session.get('username')
    return render_template('Search_loggedin_user.html', username=username)



@app.route('/indiancuisines') 
def indiancuisines():
    return render_template('indiancuisines.html')

@app.route('/mexicancuisines') 
def mexicancuisines():
    return render_template('mexicancuisines.html')

@app.route('/italiancuisines') 
def italiancuisines():
    return render_template('italiancuisine.html')

@app.route('/chinesecuisines') 
def chinesecuisines():
    return render_template('chinesecuisines.html')

@app.route('/japanesecuisines') 
def japanesecuisines():
    return render_template('japanesecuisines.html')

@app.route('/thaicuisines') 
def thaicuisines():
    return render_template('thaicuisines.html')

@app.route('/greekcuisines') 
def greekcuisines():
    return render_template('greekcuisines.html')

@app.route('/dessertsmain') 
def dessertsmain():
    return render_template('desserts_main.html')

@app.route('/indiandesserts') 
def indiandesserts():
    return render_template('indiandesserts.html')

@app.route('/italiandesserts') 
def italiandesserts():
    return render_template('italiandessert.html')

@app.route('/thaidesserts') 
def thaidesserts():
    return render_template('thaidesserts.html')

@app.route('/mexicandesserts') 
def mexicandesserts():
    return render_template('mexicandessart.html')

@app.route('/aboutus') 
def aboutus():
    return render_template('About us.html')

@app.route('/contact') 
def contact():
    return render_template('Contact us.html')

@app.route('/search') 
def search():
    return render_template('Search.html')

@app.route('/Spaghetti Carbonara Italian') 
def SpaghettiCarbonaraItalian():
    return render_template('Spaghetti Carbonara Italian.html')

@app.route('/Enchiladas Verdes Mexican') 
def EnchiladasVerdesMexican():
    return render_template('Enchiladas Verdes Mexican.html')

@app.route('/ChickenTikkaMasalaIndian') 
def ChickenTikkaMasalaIndian():
    return render_template('ChickenTikkaMasalaIndian.html')

@app.route('/Pad Thai Thai Cuisine') 
def PadThai():
    return render_template('Thai Cuisine Pad Thai.html')

@app.route('/KungPao Chicken Chinese') 
def KungPaoChickenChinese():
    return render_template('KungPao Chicken Chinese.html')

@app.route('/Teriyaki Salmon Japanese') 
def TeriyakiSalmonJapanese():
    return render_template('Teriyaki Salmon Japanese.html')

@app.route('/GulabJamun IndianDessert') 
def GulabJamunIndianDessert():
    return render_template('GulabJamun IndianDessert.html')

@app.route('/Choclate Italian Dessert') 
def ChoclateItalianDessert():
    return render_template('Choclate Italian Dessert.html')

@app.route('/Kaho Niaow Thai Dessert') 
def KahoNiaowThaiDessert():
    return render_template('Kaho Niaow Thai Dessert.html')

@app.route('/Sopapillas Mexican Dessert') 
def SopapillasMexicanDessert():
    return render_template('Sopapillas Mexican Dessert.html')


def get_db_connection():
    conn = sqlite3.connect('recipes.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_total_recipes():
    conn = get_db_connection()
    total_recipes = conn.execute('SELECT COUNT(*) FROM recipes').fetchone()[0]
    conn.close()
    return total_recipes



@app.route('/index_db')
def index():
    conn = get_db_connection()
    recipes = conn.execute('SELECT * FROM recipes').fetchall()
    cursor = conn.execute('SELECT * FROM recipes;')
    recipes = cursor.fetchall()
    total_recipes = len(recipes)
    conn.close()
    username = session.get('username')    
    return render_template('index_db.html', recipes=recipes, total_recipes=total_recipes,username=username)

#Add recipes
@app.route('/add', methods=('GET', 'POST'))
def add_recipe():
    if request.method == 'POST':
        title = request.form['title']
        cuisine = request.form['cuisine']
        ingredients = request.form['ingredients']
        instructions = request.form['instructions']
        cookingtime = request.form['cookingtime']

        conn = get_db_connection()
        conn.execute('INSERT INTO recipes (title, cuisine, ingredients, instructions, cookingtime) VALUES (?, ?, ?, ?, ?)',
                     (title, cuisine, ingredients, instructions, cookingtime))
        
        conn.commit()
        conn.close()
        flash('The recipe has been added successfully.')

        return redirect(url_for('index'))

    return render_template('add_recipe.html')

#Deleting the added recipes
@app.route('/recipes/<int:recipe_id>', methods=['POST', 'DELETE'])
def delete_recipe(recipe_id):
    if request.method == 'POST' and request.form['_method'] == 'DELETE':
        conn = get_db_connection()
        conn.execute('DELETE FROM recipes WHERE id = ?', (recipe_id,))
        conn.commit()
        conn.close()
        flash('The recipe has been deleted.', 'success')
        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

#Editing the added recipes
@app.route('/edit_recipe/<int:recipe_id>', methods=['GET'])
def edit_recipe(recipe_id):
    conn = get_db_connection()
    recipe = conn.execute('SELECT * FROM recipes WHERE id = ?', (recipe_id,)).fetchone()
    conn.close()

    return render_template('edit_recipe.html', recipe=recipe)

@app.route('/update_recipe/<int:recipe_id>', methods=['POST'])
def update_recipe(recipe_id):
    conn = get_db_connection()

    title = request.form['title']
    cuisine = request.form['cuisine']
    ingredients = request.form['ingredients']
    instructions = request.form['instructions']
    cookingtime = request.form['cookingtime']

    conn.execute('UPDATE recipes SET title = ?, cuisine = ?, ingredients = ?, instructions = ?, cookingtime = ? WHERE id = ?', (title, cuisine, ingredients, instructions, cookingtime, recipe_id))
    conn.commit()
    conn.close()

    flash('Recipe updated successfully!')

    return redirect(url_for('index'))



