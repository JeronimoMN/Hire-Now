from collections import defaultdict

from flask import (Blueprint,
                   render_template,
                   request,
                   session,
                   flash,
                   redirect,
                   url_for,
                   jsonify)

from models import Posts, Cities, db, Applications, Users
from services.email_service import EmailSender
from utils.data_structures import SingledList

company_bp = Blueprint('company_hire', __name__)

@company_bp.route('/home_company')
def home():
    cities = Cities.query.all()
    posts = Posts.query.all()
    vacants = Applications.query.filter_by(status='pending').all()

    #Integración de una Cola --En Proceso
    singled_list = SingledList()
    for vacant in vacants:
        singled_list.add({
            "user_id": vacant.user_id,
            "date": vacant.created_at
        })

    vacants_by_post = defaultdict(int)
    for vacant in vacants:
        vacants_by_post[vacant.post_id] += 1

    return render_template('company/home_empresa.html', cities = cities, posts = posts, vacants = vacants)

#TODO: CRUD for offer jobs

@company_bp.route('/create_vacant', methods=['POST'])
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

        db.session.add(new_post)
        db.session.commit()
        flash('Vacante creada con éxito', 'success')
        return redirect(url_for('company_hire.home'))

    # Si es GET, puede servir para retornar solo datos o una vista parcial
    return '', 204


@company_bp.route('/get_aspirants', methods=['POST'])
def get_aspirants():
    # Obtener el ID de la publicación desde el formulario
    post_id = request.form.get('post_id')

    # Validar que el post pertenece a la empresa actual
    post = Posts.query.filter_by(id=post_id, user_id=session.get('user_id')).first()


    # Consulta para obtener los aspirantes
    aspirants = db.session.query(Users). \
        join(Applications, Users.id == Applications.user_id). \
        filter(Applications.post_id == post_id,
               Applications.status == 'pending'). \
        all()

    # Convertir resultados a formato JSON
    aspirants_data = [{
        'id': user.id,
        'name': user.name,
        'email': user.email,
        # Agrega más campos según necesites
    } for user in aspirants]

    return jsonify(aspirants_data)

@company_bp.route('/delete_vacant/<id>', methods = ['GET', 'POST'])
def delete_vacant(id):
    post = Posts.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('company_hire.home'))

#TODO: Hacer el contador de ofertas en la vista y no en el template


@company_bp.route('/deny_applicant', methods=['POST'])
def deny_applicant():
    applicant_id = request.form.get('applicant_id')  # ID del usuario
    post_id = request.form.get('post_id')          # ID de la oferta

    # Busca la aplicación específica de ese usuario para esa oferta
    application = Applications.query.filter_by(
        user_id=applicant_id,
        post_id=post_id
    ).first()

    print(application)

    user = Users.query.get(applicant_id)
    sendRs = EmailSender()
    sendRs.send_application_email( 'ok', user.email)


    if not application:
        return jsonify({"status": "error", "message": "Solicitud no encontrada"}), 404


    # Actualiza el estado a "deny" (o el campo que uses)
    application.status = "deny"  # Ajusta según tu modelo
    db.session.commit()

    return jsonify({"status": "success", "message": "Solicitud denegada"})