from flask import ( Blueprint, render_template, request, redirect ) 

bp = Blueprint('fact', __name__, url_prefix="/facts")

@bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print(request.form)
        # Perform any necessary processing for form submission
        # For example, saving data to a database
        return redirect(('fact.index'))  # Redirect to the same page to avoid resubmission
    return render_template('facts/index.html')

@bp.route('/new')
def new():
    return render_template('facts/new.html')