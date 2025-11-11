"""Application Flask principale pour le portfolio de Mike."""

import os  # Standard library

from flask import Flask, render_template, redirect, url_for, request, flash
from flask_mail import Mail, Message
from dotenv import load_dotenv

# Charger les variables d'environnement depuis .env
load_dotenv()

# Initialisation de l'application Flask
app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'defaultsecretkey')

# Configuration Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')

mail = Mail(app)

# ----------------------------
# Routes principales
# ----------------------------
@app.route('/')
def home():
    """Affiche la page d'accueil."""
    return render_template('index.html', title="Home")


@app.route('/about')
def about():
    """Affiche la page 'About'."""
    return render_template('about.html', title="About")


@app.route('/services')
def services():
    """Affiche la page des services."""
    return render_template('services.html', title="Services")


@app.route('/resume')
def resume():
    """Affiche la page du CV."""
    return render_template('resume.html', title="Resume")


@app.route('/portfolio')
def portfolio():
    """Affiche la page de portfolio."""
    return render_template('portfolio.html', title="Portfolio")


@app.route('/portfolio_details')
def portfolio_details():
    """Affiche la page de détails du portfolio."""
    return render_template('portfolio_details.html', title="Portfolio Details")


@app.route('/starter_page')
def starter_page():
    """Affiche la page starter_page."""
    return render_template('starter_page.html', title="Starter Page")


# ----------------------------
# Route contact
# ----------------------------
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """Affiche la page de contact et gère l'envoi de messages."""
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message_body = request.form.get('message')

        # Créer le message
        msg = Message(
            subject=f"Nouveau message: {subject}",
            sender=app.config['MAIL_USERNAME'],
            recipients=[app.config['MAIL_USERNAME']],
            body=f"Nom: {name}\nEmail: {email}\n\nMessage:\n{message_body}"
        )

        try:
            mail.send(msg)
            flash('Votre message a été envoyé avec succès !', 'success')
        except Exception as e:
            flash(f"Erreur lors de l'envoi : {str(e)}", 'danger')

        return redirect(url_for('contact'))

    return render_template('contact.html')


# ----------------------------
# Lancer l'application
# ----------------------------
if __name__ == '__main__':
    app.run(debug=True)
