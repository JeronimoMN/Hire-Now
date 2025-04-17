from flask import (Blueprint,
                   render_template,
                   request,
                   session,
                   flash,
                   redirect,
                   url_for,
                   )

from models import Posts, Cities, db

company_bp = Blueprint('company_hire', __name__)

@company_bp.route('/home_company')
def home():
    cities = Cities.query.all()
    posts = Posts.query.all()

    return render_template('home_empresa.html', cities = cities, posts = posts)

#TODO: CRUD for offer jobs

@company_bp.route('/create_vacant', methods=['GET', 'POST'])
def create_vacant():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        skills = request.form.get('skills')
        city_id = request.form.get('city')

        new_post = Posts(
            title=title,
            content=content,
            skills=skills,
            city=city_id,
            user_id=session.get('user_id')  # Asegúrate de que esté autenticado
        )

        print(new_post)

        db.session.add(new_post)
        db.session.commit()
        flash('Vacante creada con éxito', 'success')
        return redirect(url_for('company_hire.home'))

    # Si es GET, puede servir para retornar solo datos o una vista parcial
    return '', 204

